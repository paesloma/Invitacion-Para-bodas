import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="P&J - Boda", page_icon="💍", layout="wide")

if 'abierto' not in st.session_state:
    st.session_state.abierto = False

params = st.query_params
invitado = params.get("invitado", "Invitado Especial").replace("_", " ")

if not st.session_state.abierto:
    # Diseño de alta gama con sombras ambientales y texturas
    html_luxury = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Great+Vibes&display=swap');

        .viewport {{
            display: flex; justify-content: center; align-items: center;
            height: 100vh; background: #0a0a0a; overflow: hidden;
        }}

        /* EL SOBRE */
        .envelope {{
            position: relative; width: 600px; height: 400px;
            background: #1c2a38; /* Azul Noche Profundo */
            /* Textura de papel lino */
            background-image: url("https://www.transparenttextures.com/patterns/linen-paper.png");
            border-radius: 0 0 8px 8px;
            box-shadow: 0 50px 100px rgba(0,0,0,0.8);
            cursor: pointer;
        }}

        /* SOLAPA DORADA CON RELIEVE */
        .flap {{
            position: absolute; top: 0; left: 0; width: 0; height: 0;
            border-left: 300px solid transparent;
            border-right: 300px solid transparent;
            border-top: 240px solid #c5a059;
            /* Degradado de metal real */
            border-image: linear-gradient(145deg, #e6c673 0%, #c5a059 45%, #8a6d29 100%) 1;
            z-index: 3; transform-origin: top;
            transition: all 0.9s cubic-bezier(0.4, 0, 0.2, 1);
            filter: drop-shadow(0 5px 10px rgba(0,0,0,0.4));
        }}

        /* SELLO DE CERA PREMIUM */
        .wax-seal {{
            position: absolute; top: 180px; left: 50%;
            transform: translateX(-50%);
            width: 110px; height: 110px;
            background: radial-gradient(circle at 30% 30%, #a52a2a, #800000 70%, #4d0000);
            border-radius: 50%; z-index: 4;
            display: flex; align-items: center; justify-content: center;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.5), 0 10px 20px rgba(0,0,0,0.6);
            border: 2px solid #5e0000;
            transition: 0.5s;
        }}

        .seal-text {{
            color: #d4af37; font-family: 'Great Vibes', cursive;
            font-size: 40px; text-shadow: 2px 2px 3px rgba(0,0,0,0.4);
            user-select: none;
        }}

        /* DETALLES FINALES */
        .recipient {{
            position: absolute; bottom: 60px; width: 100%; text-align: center;
            color: rgba(212, 175, 55, 0.8); font-family: 'Cinzel', serif;
            letter-spacing: 5px; font-size: 14px; text-transform: uppercase;
        }}

        /* ANIMACIÓN DE APERTURA */
        .envelope.open .flap {{ transform: rotateX(180deg); z-index: 1; }}
        .envelope.open .wax-seal {{ opacity: 0; transform: translateX(-50%) scale(1.5); }}

    </style>

    <div class="viewport" onclick="openMe()">
        <div class="envelope" id="env">
            <div class="flap"></div>
            <div class="wax-seal">
                <span class="seal-text">P&J</span>
            </div>
            <div class="recipient">Para: {invitado}</div>
        </div>
    </div>

    <script>
        function openMe() {{
            document.getElementById('env').classList.add('open');
            setTimeout(() => {{
                window.parent.postMessage({{type: 'streamlit:setComponentValue', value: true}}, '*');
            }}, 1000);
        }}
    </script>
    """
    components.html(html_luxury, height=800)

    # Botón elegante para invitados que no tienen JS habilitado
    if st.button("ABRIR INVITACIÓN", type="primary", use_container_width=True):
        st.session_state.abierto = True
        st.rerun()

else:
    # --- PANTALLA DE LA INVITACIÓN ---
    st.balloons()
    
    st.markdown(f"""
        <div style='text-align: center; padding: 50px; border: 2px solid #d4af37; background: #fff; border-radius: 15px;'>
            <h1 style='font-family: Cinzel; color: #1c2a38; font-size: 50px;'>¡Bienvenidos!</h1>
            <p style='font-family: Great Vibes; font-size: 35px; color: #d4af37;'>{invitado}</p>
            <hr style='border-top: 1px solid #d4af37; width: 50%; margin: auto;'>
            <br>
            <p style='font-family: Cinzel; letter-spacing: 2px;'>Estamos emocionados de compartir nuestro día con ustedes.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Aquí puedes agregar el mapa dinámico de Cuenca y el RSVP
    if st.button("← Cerrar"):
        st.session_state.abierto = False
        st.rerun()
