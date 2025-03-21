import streamlit as st
from crud import CRUD

def project_card(project):
    with st.container():
        st.markdown("""
        <style>
            .project-card {
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                margin: 1rem 0;
                border: 1px solid #e2e8f0;
                transition: transform 0.2s ease-in-out;
                background: white;
            }
            .project-card:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }
            .tech-badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                background: #e0f2fe;
                color: #0369a1;
                font-size: 0.8em;
                margin: 2px;
            }
            .gradient-icon {
                background: linear-gradient(135deg, #6366f1 0%, #3b82f6 100%);
            }
        </style>
        """, unsafe_allow_html=True)

        #st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("""
            <div class="gradient-icon" style="width: 56px; height: 56px; 
                        border-radius: 14px; display: flex; align-items: center; 
                        justify-content: center; color: white; font-size: 28px;">
                🚀
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            tags_html = ' '.join([f'<span class="tech-badge">{tag}</span>' for tag in project.get('tags', [])])
            
            st.markdown(f"""
            <div style="margin-left: 0.8rem;">
                <h3 style="margin: 0; color: #1e293b; font-weight: 600; font-size: 1.4rem;">
                    {project['title']}
                </h3>
                <div style="display: flex; align-items: center; gap: 1rem; margin: 8px 0;">
                    <span style="color: #64748b; font-size: 0.9em;">
                        📅 {project['created_at'].strftime('%d/%m/%Y')}
                    </span>
                    <div style="flex-grow: 1;">{tags_html}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        description = project['description']
        paragraphs = description.split('\n\n')
        preview_content = '\n\n'.join(paragraphs[:2])
        
        st.markdown(f"""
        <div style="color: #475569; line-height: 1.7; margin: 1.2rem 0; 
                    border-left: 3px solid #3b82f6; padding-left: 1rem;">
            {preview_content}
        </div>
        """, unsafe_allow_html=True)
        
        if len(paragraphs) > 2:
            with st.expander("🔍 Detalhes completos do projeto", expanded=False):
                remaining_content = '\n\n'.join(paragraphs[2:])
                st.markdown(f"""
                <div style="color: #475569; line-height: 1.7; padding: 1rem;">
                    {remaining_content}
                </div>
                """, unsafe_allow_html=True)
        
        if project.get('repo_url'):
            st.markdown(f"""
            <a href="{project['repo_url']}" target="_blank" style="
                display: inline-flex; align-items: center; padding: 10px 20px; 
                background: #f8fafc; border-radius: 8px; text-decoration: none; 
                color: #2563eb; margin-top: 1rem; border: 1px solid #e2e8f0;
                transition: all 0.2s ease;">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" 
                     fill="currentColor" class="bi bi-github" viewBox="0 0 16 16" style="margin-right: 10px;">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                <span style="font-weight: 500;">Ver Repositório</span>
            </a>
            """, unsafe_allow_html=True)
        
        if st.session_state.get('authentication_status'):
            with st.expander("⚙️ Administrar projeto", expanded=False):
                col_edit, col_del, _ = st.columns([1, 1, 4])
                with col_edit:
                    st.button(
                        "✏️ Editar",
                        key=f"edit_{project['_id']}",
                        help="Editar projeto",
                        use_container_width=True
                    )
                with col_del:
                    if st.button(
                        "🗑️ Excluir",
                        key=f"del_{project['_id']}",
                        type="primary",
                        use_container_width=True
                    ):
                        CRUD.delete_project(project['_id'])
                        st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

def post_card(post):
    with st.container():
        st.markdown("""
        <style>
            .post-badge {
                display: inline-block;
                padding: 4px 12px;
                border-radius: 20px;
                background: #f0fdf4;
                color: #15803d;
                font-size: 0.8em;
                margin: 2px;
            }
            .post-gradient {
                background: linear-gradient(135deg, #10b981 0%, #3b82f6 100%);
            }
        </style>
        """, unsafe_allow_html=True)

        #st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns([1, 20])
        with col1:
            st.markdown("""
            <div class="post-gradient" style="width: 56px; height: 56px; 
                        border-radius: 14px; display: flex; align-items: center; 
                        justify-content: center; color: white; font-size: 28px;">
                📝
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            tags_html = ' '.join([f'<span class="post-badge">{tag}</span>' for tag in post.get('tags', [])])
            
            st.markdown(f"""
            <div style="margin-left: 0.8rem;">
                <h3 style="margin: 0; color: #1e293b; font-weight: 600; font-size: 1.4rem;">
                    {post['title']}
                </h3>
                <div style="display: flex; align-items: center; gap: 1rem; margin: 8px 0;">
                    <span style="color: #64748b; font-size: 0.9em;">
                        📅 {post['created_at'].strftime('%d/%m/%Y')}
                    </span>
                    <div style="flex-grow: 1;">{tags_html}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        content = post['content']
        paragraphs = content.split('\n\n')
        preview_content = '\n\n'.join(paragraphs[:2])
        
        st.markdown(f"""
        <div style="color: #475569; line-height: 1.7; margin: 1.2rem 0; 
                    border-left: 3px solid #10b981; padding-left: 1rem;">
            {preview_content}
        </div>
        """, unsafe_allow_html=True)
        
        if len(paragraphs) > 2:
            with st.expander("📖 Continue lendo...", expanded=False):
                remaining_content = '\n\n'.join(paragraphs[2:])
                st.markdown(f"""
                <div style="color: #475569; line-height: 1.7; padding: 1rem;">
                    {remaining_content}
                </div>
                """, unsafe_allow_html=True)
        
        if st.session_state.get('authentication_status'):
            with st.expander("⚙️ Administrar postagem", expanded=False):
                col_edit, col_del, _ = st.columns([1, 1, 4])
                with col_edit:
                    st.button(
                        "✏️ Editar",
                        key=f"edit_post_{post['_id']}",
                        help="Editar postagem",
                        use_container_width=True
                    )
                with col_del:
                    if st.button(
                        "🗑️ Excluir",
                        key=f"del_post_{post['_id']}",
                        type="primary",
                        use_container_width=True
                    ):
                        CRUD.delete_post(post['_id'])
                        st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

# CSS Global adicional
st.markdown("""
<style>
    [data-testid="stExpander"] .st-emotion-cache-1q7spjk {
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        margin: 1rem 0;
    }
    [data-testid="stExpander"] .st-emotion-cache-1q7spjk:hover {
        border-color: #94a3b8;
    }
    [data-testid="stExpander"] .st-emotion-cache-1h9usl1 {
        color: #3b82f6;
        font-weight: 500;
    }
    .stButton button {
        transition: all 0.2s ease;
        border: 1px solid #e2e8f0 !important;
    }
    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .st-emotion-cache-1aehpvj {
        gap: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)