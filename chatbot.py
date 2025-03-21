import os
import re
import requests
from pymongo import TEXT
from database import projects_col, posts_col

class PortfolioChatbot:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1/chat/completions"
        self._ensure_indexes()

    def _ensure_indexes(self):
        """Cria índices com pesos diferenciados"""
        try:
            # Índice com peso maior para títulos
            if "portfolio_search" not in projects_col.index_information():
                projects_col.create_index(
                    [
                        ("title", TEXT),
                        ("description", TEXT)
                    ],
                    weights={"title": 10, "description": 5},
                    default_language="portuguese",
                    name="portfolio_search"
                )

            if "portfolio_search" not in posts_col.index_information():
                posts_col.create_index(
                    [
                        ("title", TEXT),
                        ("content", TEXT)
                    ],
                    weights={"title": 10, "content": 5},
                    default_language="portuguese",
                    name="portfolio_search"
                )
                
        except Exception as e:
            print(f"Erro nos índices: {str(e)}")

    def _get_context(self, query):
        """Busca aprimorada com normalização de texto"""
        try:
            # Normalização da query
            clean_query = re.sub(r'[^\w\s]', '', query).lower().strip()
            search_terms = [f'"{term}"' for term in clean_query.split() if term]
            
            # Busca combinando operadores OR
            search_query = " ".join(search_terms) if len(search_terms) > 1 else f'"{clean_query}"'
            
            # Busca com projeção otimizada
            projects = list(projects_col.find(
                {"$text": {"$search": search_query}},
                {"score": {"$meta": "textScore"}, "title": 1, "description": 1}
            ).sort([("score", {"$meta": "textScore"})]).limit(3))

            posts = list(posts_col.find(
                {"$text": {"$search": search_query}},
                {"score": {"$meta": "textScore"}, "title": 1, "content": 1}
            ).sort([("score", {"$meta": "textScore"})]).limit(3))

            # Construção de contexto enriquecido
            context = []
            
            if projects:
                context.append("### 📂 Projetos Relevantes\n")
                for proj in projects:
                    desc = proj.get('description', 'Descrição não disponível')
                    context.append(f"**{proj.get('title', 'Sem título')}**\n{desc[:250]}...")

            if posts:
                context.append("\n### 📝 Artigos Relacionados\n")
                for post in posts:
                    content = post.get('content', 'Conteúdo não disponível')
                    context.append(f"**{post.get('title', 'Sem título')}**\n{content[:300]}...")

            return "\n".join(context) if context else "Nenhum dado relevante encontrado no banco de dados."

        except Exception as e:
            print(f"Erro de contexto: {str(e)}")
            return ""

    def generate_response(self, prompt):
        """Sistema de prompts aprimorado"""
        context = self._get_context(prompt)
        
        system_prompt = f"""
          Você é o assistente técnico do site pessoal de Alan José, 
          você vai responder os visitantes que buscam informações sobre as postagens e projetos no banco de dados.

Diretrizes:
1. Analise cuidadosamente o contexto abaixo e responda com base nas informações disponíveis quando possível.
2. Responda usando MARKDOWN com formatação simples
3. Seja técnico mas didático
4. Caso não encontre informações procure algo relacionado no banco de dados, Se necessário, peça mais informações ao usuário
5. Se necessário, peça mais informações ao usuário
6. Não se esqueça de ser educado e cordial, mas objetivo
7. Não forneça links externos


Contexto disponível:
{context if context else 'Nenhum dado encontrado'}"""

        try:
            response = requests.post(
                self.base_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "mistralai/mistral-7b-instruct:free",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.5,
                    "max_tokens": 1000
                },
                timeout=20
            )

            return response.json()['choices'][0]['message']['content']

        except Exception as e:
            print(f"Erro na API: {str(e)}")
            return "Estou com dificuldades técnicas. Por favor tente mais tarde."

if __name__ == "__main__":
    bot = PortfolioChatbot()
    print("Chatbot Técnico - Escreva sua pergunta:")
    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() in ["sair", "exit"]:
            break
        print("\nAssistente:", bot.generate_response(user_input))