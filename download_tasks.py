import requests
import os

# === CONFIGURAÇÕES ===
EMAIL = ''
SENHA = ''
BASE_URL = 'https://app.cvat.ai/api'
EXPORT_FORMAT = ''
OUTPUT_DIR = '.'

# === LOGIN ===
session = requests.Session()
resp = session.post(f'{BASE_URL}/auth/login', json={'username': EMAIL, 'password': SENHA})
resp.raise_for_status()
print('[✓] Login feito com sucesso!')

# === LISTAR REQUESTS FINALIZADAS ===
page = 1
finalizados = []

while True:
    resp = session.get(f'{BASE_URL}/requests?page={page}')
    resp.raise_for_status()
    data = resp.json()

    requests_list = data.get('results', [])
    if not requests_list:
        break

    for req in requests_list:
        if req['status'] == 'finished':
            op = req.get('operation', {})
            if op.get('target') == 'task':
                task_id = op.get('task_id')
                format_name = op.get('format')
                created_at = req.get('created_date')
                result_url = req.get('result_url')

                print(f'✓ Task {task_id} exportada em {format_name} ({created_at})')
                finalizados.append((task_id, result_url))

    if not data.get('next'):
        break
    page += 1

# === RESUMO FINAL ===
print(f'\n[✔] Total de exportações finalizadas encontradas: {len(finalizados)}')

# === BAIXAR TODAS AS EXPORTAÇÕES FINALIZADAS ===
print(f'\n[↓] Iniciando download de {len(finalizados)} arquivos...\n')

baixados = 0

for task_id, url in finalizados:
    filename = os.path.join(OUTPUT_DIR, f'task_{task_id}.zip')

    # Pular se já existe
    if os.path.exists(filename):
        print(f'  • Já existe: {filename} — ignorado.')
        continue

    print(f'  → Baixando task {task_id}...')

    r = session.get(url)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r.content)
        print(f'    ✓ Salvo como: {filename}')
        baixados += 1
    else:
        print(f'    ✗ Erro ao baixar task {task_id} (HTTP {r.status_code})')

print(f'\n[✔] Download concluído. Total de arquivos baixados: {baixados}')
