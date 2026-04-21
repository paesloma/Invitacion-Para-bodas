import streamlit as st
from st_click_detector import click_detector
import time

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

if 'abierto' not in st.session_state:
    st.session_state.abierto = False

# Datos de la URL
params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")

if not st.session_state.abierto:
    # 2. DISEÑO DEL SOBRE CON ANIMACIONES CSS
    content = f"""
        <style>
            .envelope-container {{
                display: flex; flex-direction: column; align-items: center;
                justify-content: center; height: 80vh; font-family: 'Playfair Display', serif;
            }}
            
            /* Contenedor del sobre */
            .envelope {{
                position: relative; width: 450px; height: 300px;
                background: #2c3e50; border-radius: 0 0 15px 15px;
                box-shadow: 0 20px 50px rgba(0,0,0,0.5);
                cursor: pointer;
            }}

            /* La solapa dorada */
            .flap {{
                position: absolute; top: 0; left: 0; width: 0; height: 0;
                border-left: 225px solid transparent;
                border-right: 225px solid transparent;
                border-top: 180px solid #d4af37;
                transform-origin: top;
                transition: transform 0.6s ease-in-out;
                z-index: 3;
            }}

            /* El sello de cera */
            .seal {{
                position: absolute; top: 140px; left: 180px;
                width: 90px; height: 90px; background: #8b0000;
                border-radius: 50%; z-index: 4;
                display: flex; align-items: center; justify-content: center;
                color: #d4af37; font-size: 24px; font-weight: bold;
                box-shadow: 0 5px 10px rgba(0,0,0,0.3);
                transition: opacity 0.4s ease-in-out, transform 0.4s ease-in-out;
            }}

            /* Animación al hacer clic */
            /* Usamos la pseudo-clase :active para que la animación ocurra al tocarlo */
            .envelope:active .flap {{
                transform: rotateX(180deg);
                z-index: 1;
            }}
            
            .envelope:active .seal {{
                opacity: 0;
                transform: scale(1.5);
            }}

            .recipient {{
                position: absolute; bottom: 40px; width: 100%;
                text-align: center; color: #f4f1ea;
                letter-spacing: 3px; font-size: 13px; z-index: 2;
                font-family: sans-serif;
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
            <p style='margin-top: 25px; color: #888; font-style: italic; font-size: 14px;'>
                Haz clic y mantén presionado el sello para abrir
            </p>
        </div>
    """

    clicked = click_detector(content)

    if clicked == "sobre":
        # Damos un pequeño tiempo para que la animación de CSS se aprecie
        time.sleep(0.6) 
        st.session_state.abierto = True
        st.rerun()

else:
    # --- PANTALLA CONTENIDO (INVITACIÓN ABIERTA) ---
    st.balloons()
    
    st.markdown(f"""
        <h1 style='text-align: center; color: #d4af37; font-family: serif;'>¡Bienvenidos!</h1>
        <h3 style='text-align: center;'>{nombre}</h3>
        <p style='text-align: center; color: #666;'>Estamos felices de compartir este día con ustedes.</p>
    """, unsafe_allow_html=True)

    st.divider()
    
    # Aquí puedes continuar con los detalles de Cuenca, mapas, etc.
    if st.button("← Regresar al sobre"):
        st.session_state.abierto = False
        st.rerun()
