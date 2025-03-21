# BlogStreamlit 🚀

[![Licença CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Feito com Streamlit](https://img.shields.io/badge/Feito%20com-Streamlit-FF4B4B)](https://streamlit.io)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)

Um blog moderno com autenticação de usuários, chatbot integrado e painel administrativo, desenvolvido com Streamlit e Python.

![Captura de Tela](images/demo.png) <!-- Adicione suas imagens na pasta /images -->

---

## 📦 Recursos Principais
- 🔐 **Autenticação segura** de usuários
- 🤖 **Chatbot** com histórico de conversas
- ✍️ **CRUD** para posts e comentários
- 🛠️ **Painel administrativo** para gerenciamento
- 🎨 **Design responsivo** com componentes personalizados
- 🗄️ **Banco de dados integrado** para armazenamento eficiente

---

## ⚙️ Instalação

Clone o repositório e instale as dependências:

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/blogstreamlit.git
cd blogstreamlit

# Instale as dependências
pip install -r requirements.txt
```

### 🚀 Como Executar

```bash
streamlit run main.py
```

---

## 📁 Estrutura do Projeto

```bash
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
```

---

## 📄 Licença

Este projeto está licenciado sob a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). Você pode:

✅ Compartilhar e adaptar o código
✅ Usar para fins comerciais
❗ Condição: Deve dar os devidos créditos ao autor original.

---

## 👥 Contribuição

Contribuições são bem-vindas! Para contribuir, siga estes passos:

1. Faça um **Fork** do projeto
2. Crie sua **Branch** (`git checkout -b feature/nova-feature`)
3. Faça **Commit** das mudanças (`git commit -m 'Adiciona nova feature'`)
4. **Push** para a Branch (`git push origin feature/nova-feature`)
5. Abra um **Pull Request**

---

## 🛠️ Guia de Desenvolvimento

### 📏 Padrões de Código

- Seguir a **PEP8** para formatação de código
- Utilizar **Docstrings Google Style** para documentação

### ✅ Testes

Execute os testes com **pytest**:

```bash
pytest tests/
```

### 🌍 Ambiente Recomendado

- **Python 3.9+**
- **Virtualenv** para isolamento do ambiente

---

## ❓ Perguntas Frequentes (FAQ)

🔹 **Como personalizar o chatbot?**  
Modifique o arquivo `chatbot.py` e adicione novas intenções no dicionário `intents`.

🔹 **Posso usar outro banco de dados?**  
Sim! Basta modificar `database.py` para se conectar ao banco desejado.

🔹 **O projeto roda em Docker?**  
Ainda não, mas contribuições para adicionar suporte a Docker são bem-vindas!

---

## 📚 Citação

Se você usar este projeto em seu trabalho, por favor cite:

```bibtex
@misc{blogstreamlit,
  author = {Seu Nome},
  title = {BlogStreamlit},
  year = {2024},
  publisher = {GitHub},
  journal = {Repositório GitHub},
  howpublished = {\url{https://github.com/seu-usuario/blogstreamlit}}
}
```

---

## 📜 Criando o Arquivo de Licença

Crie um arquivo `LICENSE` com o texto completo da [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.txt).

---

## 📑 Documentação Adicional

### `requirements.txt`

```txt
streamlit
sqlalchemy
passlib
python-dotenv
```

### `.gitignore`

```txt
__pycache__/
*.pyc
.env
venv/
*.sqlite
```

### 📘 Desenvolvimento Avançado (Opcional)

Crie um arquivo `docs/DEVELOPMENT.md` com detalhes sobre o desenvolvimento interno do projeto.

---

🚀 **Vamos construir algo incrível!**
