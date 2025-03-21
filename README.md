# BlogStreamlit 🚀

[![Licença CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Um blog moderno com autenticação de usuários, chatbot integrado e painel administrativo, desenvolvido com Streamlit e Python.

![Captura de Tela](images/demo.png) <!-- Adicione suas imagens na pasta /images -->

## 📦 Recursos Principais
- Autenticação segura de usuários
- Chatbot com histórico de conversas
- CRUD para posts e comentários
- Painel administrativo
- Design responsivo com componentes personalizados
- Banco de dados integrado

## ⚙️ Instalação
```bash
git clone https://github.com/seu-usuario/blogstreamlit.git
cd blogstreamlit
pip install -r requirements.txt
🚀 Como Executar
bash
Copy
streamlit run main.py
� Estrutura do Projeto
Copy
blogstreamlit/
├── auth.py          # Autenticação de usuários
├── chatbot.py       # Lógica do chatbot
├── crud.py          # Operações de banco de dados
├── database.py      # Configuração do banco de dados
├── main.py          # Ponto de entrada principal
├── components/
│   ├── admin_panel.py  # Painel administrativo
│   ├── cards.py        # Componentes de layout
│   ├── header.py       # Cabeçalho da aplicação
│   └── styles.py       # Estilos CSS personalizados
└── images/          # Assets visuais
📄 Licença
Este projeto está licenciado sob Creative Commons Attribution 4.0 International License. Você pode:

Compartilhar e adaptar o código

Usar para fins comerciais

Condição: Deve dar os devidos créditos ao autor original.

👥 Contribuição
Contribuições são bem-vindas! Siga estes passos:

Faça um Fork do projeto

Crie sua Branch (git checkout -b feature/nova-feature)

Faça Commit das mudanças (git commit -m 'Adiciona nova feature')

Push para a Branch (git push origin feature/nova-feature)

Abra um Pull Request

🙌 Créditos
Desenvolvido por Seu Nome

Copy

# Licença (LICENSE)
Crie um arquivo `LICENSE` com o texto completo da [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.txt)

# Documentação Adicional

1. **requirements.txt**
```txt
streamlit
sqlalchemy
passlib
python-dotenv
.gitignore

gitignore
Copy
__pycache__/
*.pyc
.env
venv/
*.sqlite
docs/DEVELOPMENT.md (opcional)

markdown
Copy
## Guia de Desenvolvimento

### Padrões de Código
- PEP8
- Docstrings Google Style

### Testes
```bash
pytest tests/
Ambiente
Recomendado:

Python 3.9+

Virtualenv

Copy

# Sugestões Extras:

1. **Badges Personalizadas** (no README):
```markdown
[![Feito com Streamlit](https://img.shields.io/badge/Feito%20com-Streamlit-FF4B4B)](https://streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
Seção de FAQ:

markdown
Copy
## ❓ Perguntas Frequentes

**Como personalizar o chatbot?**
Modifique o arquivo `chatbot.py` e adicione novas intenções no dicionário `intents`
Exemplo de Citação:

markdown
Copy
## 📚 Citação
Se usar este projeto em seu trabalho, cite:
bibtex
Copy
@misc{blogstreamlit,
  author = {Seu Nome},
  title = {BlogStreamlit},
  year = {2024},
  publisher = {GitHub},
  journal = {Repositório GitHub},
  howpublished = {\url{https://github.com/seu-usuario/blogstreamlit}}
}
