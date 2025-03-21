import streamlit as st

st.set_page_config(
    page_title="Alan José",
    page_icon="🐦‍⬛",
    layout="wide",
    initial_sidebar_state="collapsed"
)

from auth import setup_auth
from components.styles import load_css
from components.header import profile_header
from components.cards import project_card, post_card
from components.admin_panel import project_management, post_management
from chatbot import PortfolioChatbot
from database import projects_col, posts_col

# Carregar CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Header do perfil
profile_header()

# Sistema de Autenticação
authenticator = setup_auth()

# Gerenciamento de Login
with st.sidebar:
    try:
        if not st.session_state.get('authentication_status'):
            name, auth_status, username = authenticator.login(
                '🔐 Acesso Admin',
                location='sidebar'
            )
            st.session_state.update({
                'authentication_status': auth_status,
                'name': name
            })
        else:
            authenticator.logout("🚪 Sair", "sidebar")
            st.success(f"👋 Bem-vindo, {st.session_state.name}!")
    except Exception as e:
        st.error(f"Erro no login: {str(e)}")

# Função para gerenciar o chat
def handle_chat():
    # Inicializar histórico se necessário
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    # Container do chat
    with st.container():
        st.markdown("""
        <div class="chat-container">
            <div class="chat-messages">
        """, unsafe_allow_html=True)
        
        # Mostrar histórico de mensagens
        messages_container = st.container()
        with messages_container:
            for message in st.session_state.chat_history:
                avatar = "👤" if message["role"] == "user" else "🤖"
                message_class = "user-message" if message["role"] == "user" else "bot-message"
                
                st.markdown(f"""
                <div class="message {message_class}">
                    {message["content"]}
                    <div class="message-avatar">{avatar}</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)  # Fecha chat-messages
        
        # Área de input
        st.markdown("""
        <div class="chat-input-container">
            <div class="chat-input-wrapper">
        """, unsafe_allow_html=True)
        
        # Input com gerenciamento correto de estado
        prompt = st.text_input(
            "Digite sua mensagem...",
            key="chat_input",
            label_visibility="collapsed",
            on_change=lambda: st.session_state.update({'new_message': True})
        )
        
        # Botão de enviar
        col1, col2 = st.columns([6, 1])
        with col2:
            send_button = st.button("Enviar", use_container_width=True)
        
        st.markdown("""
            </div>
        </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Processar nova mensagem
        if send_button or st.session_state.get('new_message'):
            if prompt:
                # Adicionar mensagem do usuário
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": prompt
                })
                
                # Gerar resposta do bot
                with st.spinner("Gerando resposta..."):
                    chatbot = PortfolioChatbot()
                    response = chatbot.generate_response(prompt)
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": response
                    })
                
                # Resetar estados
                st.session_state.new_message = False
                
                # Forçar atualização do componente
                st.rerun()

# Conteúdo Principal
if not st.session_state.get('authentication_status'):
    tab1, tab2, tab3 = st.tabs(["📦 Projetos Recentes", "📝 Artigos Técnicos", "💬 Chatbot"])
    
    with tab1:
        cols = st.columns(2)
        for idx, project in enumerate(projects_col.find().sort("created_at", -1).limit(4)):
            with cols[idx % 2]:
                project_card(project)
    
    with tab2:
        cols = st.columns(2)
        for idx, post in enumerate(posts_col.find().sort("created_at", -1).limit(4)):
            with cols[idx % 2]:
                post_card(post)

    with tab3:
        handle_chat()

else:
    with st.sidebar:
        st.markdown("""
        <div style="background: #f8fafc; padding: 1.5rem; border-radius: 16px; margin-bottom: 2rem;">
            <h3 style="color: #2563eb; margin: 0 0 1rem 0;">⚙️ Painel Admin</h3>
        """, unsafe_allow_html=True)
        
        menu = st.radio("Navegação", ["📦 Projetos", "📝 Posts"], label_visibility="collapsed")
        
        if menu == "📦 Projetos":
            project_management()
        elif menu == "📝 Posts":
            post_management()
        
        st.markdown("</div>", unsafe_allow_html=True)

    if menu == "📦 Projetos":
        st.header("📦 Gestão de Projetos")
        search_term = st.text_input("🔍 Buscar projetos...", key="project_search")
        cols = st.columns(2)
        for idx, project in enumerate(projects_col.find({"$text": {"$search": search_term}} if search_term else {})):
            with cols[idx % 2]:
                project_card(project)

    elif menu == "📝 Posts":
        st.header("📝 Gestão de Posts")
        search_term = st.text_input("🔍 Buscar posts...", key="post_search")
        cols = st.columns(2)
        for idx, post in enumerate(posts_col.find({"$text": {"$search": search_term}} if search_term else {})):
            with cols[idx % 2]:
                post_card(post)

# Mensagem de erro
if st.session_state.get('authentication_status') is False:
    st.error("🔒 Credenciais inválidas. Acesso restrito ao administrador.")
