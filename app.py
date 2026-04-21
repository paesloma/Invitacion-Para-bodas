import streamlit as st
from st_click_detector import click_detector

# Configuración inicial
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

if 'abierto' not in st.session_state:
    st.session_state.abierto = False

# Datos de la URL
params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")

if not st.session_state.abierto:
    # Diseño del Sobre con ID para el detector de clics
    # Al hacer clic en el id='sobre', st_click_detector lo capturará
    content = f"""
        <style>
            .envelope-container {{
                display: flex; flex-direction: column; align-items: center;
                justify-content: center; height: 80vh; font-family: serif;
            }}
            .envelope {{
                position: relative; width: 500px; height: 320px;
                background: #2c3e50; border-radius: 0 0 15px 15px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.5);
                cursor: pointer; transition: transform 0.3s;
            }}
            .envelope:hover {{ transform: scale(1.02); }}
            .flap {{
                position: absolute; top: 0; left: 0; width: 0; height: 0;
                border-left: 250px solid transparent; border-right: 250px solid transparent;
                border-top: 190px solid #d4af37; z-index: 2;
            }}
            .seal {{
                position: absolute; top: 150px; left: 205px;
                width: 90px; height: 90px; background: #8b0000;
                border-radius: 50%; z-index: 3; display: flex;
                align-items: center; justify-content: center;
                color: #d4af37; font-size: 24px; font-weight: bold;
                box-shadow: 0 5px 10px rgba(0,0,0,0.3);
            }}
            .recipient {{
                position: absolute; bottom: 40px; width: 100%;
                text-align: center; color: #f4f1ea; letter-spacing: 3px; font-size: 14px;
            }}
        </style>
        <div class='envelope-container'>
            <a href='#' id='sobre' style='text-decoration: none;'>
                <div class='envelope'>
                    <div class='flap'></div>
                    <div class='seal'>P&J</div>
                    <div class='recipient'>PARA: {nombre.upper()}</div>
                </div>
            </a>
            <p style='margin-top: 25px; color: #888; font-style: italic;'>Haz clic en el sobre para abrir</p>
        </div>
    """

    # El detector de clics renderiza el HTML y nos avisa si se tocó el ID 'sobre'
    clicked = click_detector(content)

    if clicked == "sobre":
        st.session_state.abierto = True
        st.rerun()

else:
    # --- PANTALLA CONTENIDO ---
    st.balloons()
    st.markdown(f"<h1 style='text-align: center; color: #d4af37;'>¡Bienvenidos, {nombre}!</h1>", unsafe_allow_html=True)
    
    # Aquí puedes colocar el mapa, calendario y RSVP
    if st.button("← Ver sobre"):
        st.session_state.abierto = False
        st.rerun()
