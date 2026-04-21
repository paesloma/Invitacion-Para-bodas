import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN E INICIALIZACIÓN
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

# Inicializamos el estado del sobre si no existe
if 'sobre_abierto' not in st.session_state:
    st.session_state.sobre_abierto = False

# Captura de parámetros (Personalización)
params = st.query_params
nombre_invitado = params.get("invitado", "Invitado Especial").replace("_", " ")
pases = params.get("pases", "2")

# 2. LÓGICA DE VISUALIZACIÓN
if not st.session_state.sobre_abierto:
    # --- APARTADO A: EL SOBRE CON SELLO (INICIO) ---

    # CSS e HTML para el SOBRE GRANDE CON SELLO DE CERA P&J
    # Se utilizaron gradientes y sombras para texturas realistas
    envelope_html = f"""
    <style>
        .main-container {{
            display: flex; flex-direction: column; justify-content: center;
            align-items: center; height: 90vh; font-family: 'Playfair Display', serif;
        }}
        
        .envelope-wrapper {{
            position: relative; width: 600px; height: 400px;
            background-color: #2c3e50; /* Azul noche elegante */
            background-image: linear-gradient(135deg, #2c3e50 25%, #34495e 100%);
            border-bottom-left-radius: 15px; border-bottom-right-radius: 15px;
            cursor: pointer; box-shadow: 0 30px 60px rgba(0,0,0,0.4);
            transition: transform 0.3s ease;
        }}
        
        .envelope-wrapper:hover {{ transform: translateY(-5px); }}

        /* Solapa superior dorada */
        .envelope-wrapper:before {{
            content: ""; position: absolute; top: 0; z-index: 2;
            border-top: 220px solid #d4af37; /* Dorado */
            border-left: 300px solid transparent; border-right: 300px solid transparent;
            transform-origin: top; transition: all 0.6s ease-in-out;
            border-radius: 10px 10px 0 0;
        }}

        /* SELLO DE CERA P&J (CSS Puro) */
        .wax-seal {{
            position: absolute; top: 180px; left: 250px; width: 100px; height: 100px;
            background: radial-gradient(circle, #b22222 0%, #8b0000 100%); /* Rojo cera */
            border-radius: 50%; z-index: 10;
            box-shadow: inset 0 0 15px rgba(0,0,0,0.5), 0 5px 15px rgba(0,0,0,0.3);
            display: flex; align-items: center; justify-content: center;
            color: #d4af37; font-family: 'Georgia', serif; font-size: 32px;
            font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
            border: 2px solid #a52a2a;
        }}
        
        .seal-initials {{ letter-spacing: -2px; transform: rotate(-5deg); }}

        /* Texto de destinatario en el sobre */
        .recipient-label {{
            position: absolute; bottom: 30px; width: 100%; text-align: center;
            color: #f4f1ea; font-family: sans-serif; font-size: 14px;
            letter-spacing: 3px; text-transform: uppercase; z-index: 1;
        }}
    </style>

    <div class="main-container">
        <div class="envelope-wrapper">
            <div class="wax-seal">
                <span class="seal-initials">P&J</span>
            </div>
            <div class="recipient-label">PARA: {nombre_invitado}</div>
        </div>
        <p style="margin-top: 30px; color: #888; font-style: italic;">Haz clic en el sello para abrir</p>
    </div>
    """

    components.html(envelope_html, height=700)

    # Botón de Streamlit para "entrar" formalmente (Actúa como el trigger)
    # Al hacer clic, se recarga la página mostrando el contenido
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("ABRIR INVITACIÓN", use_container_width=True):
        st.session_state.sobre_abierto = True
        st.rerun()

else:
    # --- APARTADO B: CONTENIDO DETALLADO ---
    
    # Botón opcional para regresar
    if st.button("← Ver sobre", type="secondary"):
        st.session_state.sobre_abierto = False
        st.rerun()

    # Título principal con diseño elegante
    st.markdown(f"""
        <h1 style='text-align: center; color: #d4af37; font-family: Playfair Display, serif; font-size: 48px; margin-bottom: 0;'>
            ¡Bienvenidos!
        </h1>
        <h3 style='text-align: center; color: #2c3e50; font-family: sans-serif; font-weight: normal; margin-top: 0;'>
            {nombre_invitado}
        </h3>
        <p style='text-align: center; color: #888; font-style: italic;'>
            Tenemos {pases} pases reservados para ustedes.
        </p>
    """, unsafe_allow_html=True)

    st.divider()
    
    # Resumen de detalles
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<p style='text-align:center; color:#d4af37;'>📅 FECHA</p>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>25 Julio</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>2026</p>", unsafe_allow_html=True)
    with col2:
        st.markdown("<p style='text-align:center; color:#d4af37;'>📍 LUGAR</p>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Cuenca</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>Ecuador</p>", unsafe_allow_html=True)
    with col3:
        st.markdown("<p style='text-align:center; color:#d4af37;'>📋 PÁGINA</p>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;'>Detalles</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;'>(Scroll down)</p>", unsafe_allow_html=True)

    st.divider()
    
    # Aquí puedes añadir el mapa y el formulario RSVP que diseñamos antes...
    st.info("Aquí continuaría el resto del contenido de la invitación (Mapa, Formulario, etc.)")
