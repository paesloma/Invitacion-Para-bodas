import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

if 'abierto' not in st.session_state:
    st.session_state.abierto = False

params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")

# 2. ESTILOS CSS (Diseño del Sobre + Botón Invisible)
st.markdown(f"""
<style>
    /* Contenedor relativo para encimar elementos */
    .envelope-container {{
        position: relative;
        width: 100%;
        max-width: 500px;
        height: 380px;
        margin: auto;
    }}

    /* Diseño del Sobre */
    .envelope-design {{
        position: absolute;
        width: 100%;
        height: 350px;
        background: linear-gradient(135deg, #2c3e50 25%, #34495e 100%);
        border-radius: 0 0 15px 15px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-end;
        padding-bottom: 30px;
        z-index: 1;
    }}

    .envelope-design:before {{
        content: "";
        position: absolute;
        top: 0;
        border-top: 180px solid #d4af37;
        border-left: 250px solid transparent;
        border-right: 250px solid transparent;
        z-index: 2;
    }}

    .wax-seal {{
        position: absolute;
        top: 140px;
        width: 90px;
        height: 90px;
        background: radial-gradient(circle, #b22222 0%, #8b0000 100%);
        border-radius: 50%;
        z-index: 3;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #d4af37;
        font-family: serif;
        font-size: 28px;
        font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.4);
        border: 2px solid #a52a2a;
    }}

    .recipient {{
        color: #f4f1ea;
        font-family: sans-serif;
        letter-spacing: 3px;
        font-size: 14px;
        z-index: 2;
        text-transform: uppercase;
    }}

    /* EL TRUCO: Volver el botón de Streamlit invisible y que cubra todo */
    .stButton > button {{
        position: absolute;
        width: 500px;
        height: 350px;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        background: transparent !important;
        border: none !important;
        color: transparent !important;
        z-index: 10; /* Siempre encima de todo */
        cursor: pointer;
    }}
    
    /* Eliminar efectos de hover de Streamlit */
    .stButton > button:hover, .stButton > button:active, .stButton > button:focus {{
        background: transparent !important;
        color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}
</style>
""", unsafe_allow_html=True)

# 3. LÓGICA DE PANTALLAS
if not st.session_state.abierto:
    # Dibujamos el sobre visual (HTML)
    st.markdown(f"""
    <div class="envelope-container">
        <div class="envelope-design">
            <div class="wax-seal">P&J</div>
            <div class="recipient">PARA: {nombre}</div>
        </div>
    </div>
    <p style="text-align: center; color: #888; font-family: serif; font-style: italic;">Haz clic en el sobre para abrir</p>
    """, unsafe_allow_html=True)
    
    # Colocamos el botón invisible encima
    if st.button(" ", key="abrir_sobre"):
        st.session_state.abierto = True
        st.rerun()

else:
    # Pantalla de destino (Invitación abierta)
    st.balloons()
    st.markdown(f"<h1 style='text-align: center; color: #d4af37;'>¡Bienvenidos, {nombre}!</h1>", unsafe_allow_html=True)
    
    if st.button("← Ver sobre"):
        st.session_state.abierto = False
        st.rerun()
