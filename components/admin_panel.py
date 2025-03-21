import streamlit as st
from datetime import datetime
from crud import CRUD

def project_management():
    with st.form("Novo Projeto", clear_on_submit=True):
        st.text_input("Título*", key="project_title")
        st.text_area("Descrição*", height=150, key="project_desc")
        st.text_input("URL Repositório", key="project_url")
        st.text_input("Tags (separar por vírgulas)", key="project_tags")
        
        if st.form_submit_button("💾 Salvar Projeto"):
            CRUD.create_project({
                'title': st.session_state.project_title,
                'description': st.session_state.project_desc,
                'repo_url': st.session_state.project_url,
                'tags': [t.strip() for t in st.session_state.project_tags.split(',')],
                'created_at': datetime.now()
            })
            st.rerun()

def post_management():
    with st.form("Novo Post", clear_on_submit=True):
        st.text_input("Título*", key="post_title")
        st.text_area("Conteúdo*", height=300, key="post_content")
        st.text_input("Tags (separar por vírgulas)", key="post_tags")
        
        if st.form_submit_button("💾 Publicar Post"):
            CRUD.create_post({
                'title': st.session_state.post_title,
                'content': st.session_state.post_content,
                'tags': [t.strip() for t in st.session_state.post_tags.split(',')],
                'created_at': datetime.now()
            })
            st.rerun()