import streamlit as st
import requests
import re

def profile_header():


    # Função para buscar dados do GitHub
    def get_github_stats(username):
        try:
            repos = requests.get(f"https://api.github.com/users/{username}/repos").json()
            return {
                'repos': len(repos),
                'stars': sum(repo['stargazers_count'] for repo in repos)
            }
        except:
            return {'repos': 8, 'stars': 15}

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
            ##### *Python | Análise de Dados | Soluções Tech*
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
