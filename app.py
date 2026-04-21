import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

if 'abierto' not in st.session_state:
    st.session_state.abierto = False

# Captura de parámetros
params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")

# 2. LÓGICA DE PANTALLAS
if not st.session_state.abierto:
    # Este bloque de HTML contiene el diseño, la animación y el disparador
    envelope_html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
        
        .container {{
            display: flex; flex-direction: column; align-items: center;
            justify-content: center; height: 100vh; cursor: pointer;
            font-family: 'serif';
        }}
        
        .envelope {{
            position: relative; width: 450px; height: 300px;
            background: #2c3e50; border-radius: 0 0 15px 15px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            transition: transform 0.3s;
        }}

        /* Solapa */
        .flap {{
            position: absolute; top: 0; left: 0; width: 0; height: 0;
            border-left: 225px solid transparent;
            border-right: 225px solid transparent;
            border-top: 180px solid #d4af37;
            transform-origin: top;
            transition: transform 0.6s ease-in-out;
            z-index: 3;
        }}

        /* Sello */
        .seal {{
            position: absolute; top: 140px; left: 180px;
            width: 90px; height: 90px; background: #8b0000;
            border-radius: 50%; z-index: 4;
            display: flex; align-items: center; justify-content: center;
            color: #d4af37; font-family: 'Playfair Display', serif;
            font-size: 24px; box-shadow: 0 5px 10px rgba(0,0,0,0.3);
            transition: opacity 0.4s;
        }}

        .recipient {{
            position: absolute; bottom: 40px; width: 100%;
            text-align: center; color: #f4f1ea;
            letter-spacing: 3px; font-size: 12px; z-index: 2;
        }}

        /* Animación de apertura al hacer clic */
        .opened .flap {{ transform: rotateX(180deg); z-index: 1; }}
        .opened .seal {{ opacity: 0; }}
        
    </style>

    <div class="container" id="env_container" onclick="openEnvelope()">
        <div class="envelope" id="envelope">
            <div class="flap"></div>
            <div class="seal">P&J</div>
            <div class="recipient">PARA: {nombre.upper()}</div>
        </div>
        <p style="margin-top: 20px; color: #888; font-style: italic;">Haz clic en el sobre para abrir</p>
    </div>

    <script>
        function openEnvelope() {{
            const env = document.getElementById('envelope');
            env.classList.add('opened');
            
            // Esperamos a que la animación termine para avisar a Streamlit
            setTimeout(() => {{
                window.parent.postMessage({{type: 'streamlit:setComponentValue', value: true}}, '*');
            }}, 700);
        }}
    </script>
    """

    # Usamos el componente para detectar el clic desde JS
    # 'evento_clic' recibirá el valor 'true' desde el script de arriba
    evento_clic = components.html(envelope_html, height=550)
    
    # Truco para capturar el mensaje de JS en Streamlit
    if st.button("ENTRAR A LA INVITACIÓN"):
        st.session_state.abierto = True
        st.rerun()

else:
    # --- PANTALLA CONTENIDO ---
    st.balloons()
    st.markdown(f"<h1 style='text-align: center;'>¡Bienvenidos, {nombre}!</h1>", unsafe_allow_html=True)
    
    # Aquí puedes añadir el resto de tu contenido (Mapa, RSVP, etc.)
    if st.button("← Ver sobre de nuevo"):
        st.session_state.abierto = False
        st.rerun()
