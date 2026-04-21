import streamlit as st

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

# Inicialización de estado
if 'abierto' not in st.session_state:
    st.session_state.abierto = False

# Datos de URL
params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")

# 2. CSS PARA EL SOBRE-BOTÓN
# Este CSS convierte el botón estándar de Streamlit en tu sobre elegante
st.markdown(f"""
<style>
    /* Ocultamos el estilo por defecto del botón de Streamlit */
    div.stButton > button {{
        background: none;
        border: none;
        padding: 0;
        width: 100%;
        height: auto;
    }}
    
    div.stButton > button:hover {{
        background: none;
        border: none;
        box-shadow: none;
    }}

    /* Contenedor del Sobre */
    .envelope {{
        position: relative; width: 100%; max-width: 500px; height: 350px;
        background: linear-gradient(135deg, #2c3e50 25%, #34495e 100%);
        margin: auto; border-radius: 0 0 15px 15px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        display: flex; flex-direction: column; align-items: center; justify-content: flex-end;
        padding-bottom: 30px;
    }}

    /* Solapa Dorada */
    .envelope:before {{
        content: ""; position: absolute; top: 0;
        border-top: 180px solid #d4af37;
        border-left: 250px solid transparent; border-right: 250px solid transparent;
        z-index: 1;
    }}

    /* Sello de Cera */
    .wax-seal {{
        position: absolute; top: 140px; width: 90px; height: 90px;
        background: radial-gradient(circle, #b22222 0%, #8b0000 100%);
        border-radius: 50%; z-index: 2;
        display: flex; align-items: center; justify-content: center;
        color: #d4af37; font-family: serif; font-size: 28px; font-weight: bold;
        box-shadow: 0 5px 15px rgba(0,0,0,0.4);
        border: 2px solid #a52a2a;
    }}

    .recipient {{
        color: #f4f1ea; font-family: sans-serif; letter-spacing: 3px; font-size: 14px;
        z-index: 1; text-transform: uppercase;
    }}
</style>
""", unsafe_allow_html=True)

# 3. LÓGICA DE PANTALLAS
if not st.session_state.abierto:
    # Mostramos el sobre. Al ser un botón de Streamlit, 'click' dispara la lógica de Python
    # El contenido del label es el HTML de nuestro sobre
    sobre_html = f'''
        <div class="envelope">
            <div class="wax-seal">P&J</div>
            <div class="recipient">PARA: {nombre}</div>
        </div>
        <p style="text-align: center; color: #888; margin-top: 20px;">Haz clic en el sobre para abrir</p>
    '''
    
    # Creamos el botón que ocupa todo el sobre
    if st.button(sobre_html, key="boton_sobre"):
        st.session_state.abierto = True
        st.rerun()

else:
    # --- PANTALLA CONTENIDO ---
    st.balloons()
    st.markdown(f"<h1 style='text-align: center;'>¡Bienvenidos, {nombre}!</h1>", unsafe_allow_html=True)
    
    if st.button("Regresar"):
        st.session_state.abierto = False
        st.rerun()
