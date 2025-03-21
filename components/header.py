import streamlit as st
import requests
import re

def profile_header():
    # Função para buscar dados do GitHub
    def get_github_stats(username):
        if not isinstance(username, str) or not username.strip():
            return {'error': 'Username inválido'}

        headers = {'User-Agent': 'Python GitHub Stats Fetcher'}

        try:
            response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
            response.raise_for_status()  # Lança uma exceção para códigos de status HTTP 4xx/5xx
            repos = response.json()

            return {
                'repos': len(repos),
                'stars': sum(repo['stargazers_count'] for repo in repos)
            }
        except requests.exceptions.RequestException as e:
            return {'error': f'Erro ao buscar dados do GitHub: {str(e)}'}
        except ValueError as e:
            return {'error': f'Erro ao decodificar JSON: {str(e)}'}

    # Seção Principal
    with st.container():
        col1, col2 = st.columns([1, 2], gap="medium")
        
        with col1:
            st.image(
                "images/profile.jpeg",
                width=400,
                caption="Desenvolvedor Backend e Analista de Dados"
            )
            
            st.markdown("""
            ### 🌐 Conecte-se
            [![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github)](https://github.com/Mogutaa)
            [![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?logo=linkedin)](https://www.linkedin.com/in/alan-jose-filho/)
            """)

        with col2:
            st.title("Alan José", anchor=False)
            st.markdown("""
            #### **Desenvolvedor Backend e Analista de Dados**  
            ##### *Python | Análise de Dados | Entusiasta de IA*
            """)
            
            github_stats = get_github_stats("Mogutaa")
            
            col1, col2 = st.columns(2)
            col1.metric("Repositórios", github_stats['repos'])
            col2.metric("Estrelas", github_stats['stars'])

            st.markdown("---")
            with st.expander("🛠 Habilidades Técnicas", expanded=True):
                st.markdown("""
                - **Linguagens**: Python, SQL, Go
                - **Ferramentas**: Git, VS Code, Jupyter
                - **Análise de Dados**: Pandas, Excel, Power BI
                - **Machine Learning**: Scikit-learn, TensorFlow
                - **Web**: Streamlit, Flask, Django
                - **Bancos de Dados**: MySQL, SQLite, MongoDB
                """)


if __name__ == "__main__":
    profile_header()