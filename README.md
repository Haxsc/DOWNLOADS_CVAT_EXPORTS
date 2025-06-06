
📦 CVAT Dataset Downloader via Requests API
===========================================

Este script em Python permite baixar automaticamente todos os datasets exportados no CVAT Online (https://app.cvat.ai), usando a API da aba Requests — exatamente como você vê na interface web após exportar tarefas.

✅ Funcionalidades
------------------

- 🔐 Login automático na conta CVAT
- 🔎 Busca todas as exportações da aba "Requests"
- 🧠 Filtra apenas aquelas com status `finished`
- ⬇️ Baixa diretamente os arquivos `.zip` exportados
- 💾 Nomeia os arquivos como `task_<ID>.zip`
- 🧼 Evita baixar arquivos já existentes

🚀 Como usar
------------

1. Clone o repositório:

`git clone https://github.com/Haxsc/DOWNLOADS_CVAT_EXPORTS.git
cd DOWNLOADS_CVAT_EXPORTS
`

2. Instale os requisitos:

    pip install requests

3. Configure suas credenciais:

    Edite o script `download_tasks.py`:

        EMAIL = 'seu_usuario_cvat'
        SENHA = 'sua_senha_cvat'

4. Execute o script:

    python download_tasks.py

    Os arquivos serão salvos no mesmo diretório do script.

📁 Exemplo de saída
-------------------

    [✓] Login feito com sucesso!
    ✓ Task 895758 exportada em YOLO 1.1 (2025-06-06T19:12:04Z)
    ✓ Task 897531 exportada em YOLO 1.1 (2025-06-06T16:11:42Z)

    [↓] Iniciando download de 2 arquivos...

      → Baixando task 895758...
        ✓ Salvo como: ./task_895758.zip

      → Baixando task 897531...
        ✓ Salvo como: ./task_89753.zip

    [✔] Download concluído. Total de arquivos baixados: 2

⚠️ Observações
--------------

- O script não gera novas exportações — ele baixa apenas aquelas com status `finished`.
- Exportações expiram em cerca de 24 horas. Reexporte na interface do CVAT se necessário.
- Suas credenciais são usadas apenas localmente, por isso, não compartilhe o script com elas salvas.

📃 Licença
----------

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).

🙋‍♂️ Autor
---------

Feito por [Gustavo H.] com ❤️ para automação de tarefas no CVAT.

