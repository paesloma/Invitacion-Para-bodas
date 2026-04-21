import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Boda P&J", page_icon="💍", layout="centered")

# Inicialización del estado del sobre
if 'abierto' not in st.session_state:
    st.session_state.abierto = False

# Captura de parámetros para personalización (Ej: ?invitado=Ana_y_Luis)
params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")

# 2. LÓGICA DE PANTALLAS
if not st.session_state.abierto:
    # --- PANTALLA A: EL SOBRE CERRADO (Fotorrealista) ---

    # Este bloque de HTML/CSS recrea la estética de tu referencia.
    # Incluye texturas, gradientes metálicos y el sello de cera detallado.
    envelope_html = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@1,400;1,700&display=swap');
        
        .main-container {{
            display: flex; flex-direction: column; align-items: center;
            justify-content: center; height: 100vh; cursor: pointer;
            background-color: #111; /* Fondo oscuro para resaltar el sobre */
        }}
        
        /* CUERPO DEL SOBRE: Azul marino con textura de papel */
        .envelope {{
            position: relative; width: 550px; height: 380px;
            background-color: #2c3e50;
            background-image: 
                linear-gradient(30deg, #2c3e50 12%, transparent 12.5%, transparent 87%, #2c3e50 87.5%, #2c3e50),
                linear-gradient(150deg, #2c3e50 12%, transparent 12.5%, transparent 87%, #2c3e50 87.5%, #2c3e50),
                linear-gradient(30deg, #2c3e50 12%, transparent 12.5%, transparent 87%, #2c3e50 87.5%, #2c3e50),
                linear-gradient(150deg, #2c3e50 12%, transparent 12.5%, transparent 87%, #2c3e50 87.5%, #2c3e50),
                linear-gradient(60deg, #34495e 25%, transparent 25.5%, transparent 75%, #34495e 75.5%, #34495e),
                linear-gradient(60deg, #34495e 25%, transparent 25.5%, transparent 75%, #34495e 75.5%, #34495e);
            background-size: 80px 140px; background-position: 0 0, 0 0, 40px 70px, 40px 70px, 0 0, 40px 70px;
            border-radius: 0 0 15px 15px;
            box-shadow: 0 25px 50px rgba(0,0,0,0.5);
            transition: transform 0.3s ease;
        }}
        .envelope:hover {{ transform: translateY(-5px); }}

        /* SOLAPA DORADA METÁLICA con degradado fotorrealista */
        .flap {{
            position: absolute; top: 0; left: 0; width: 0; height: 0;
            border-left: 275px solid transparent;
            border-right: 275px solid transparent;
            /* Degradado complejo para simular metal dorado cepillado */
            border-top: 220px solid #d4af37;
            border-image: linear-gradient(to bottom, #f7e082 0%, #d4af37 40%, #b8902d 60%, #eacb5f 100%) 1;
            transform-origin: top;
            transition: transform 0.7s ease-in-out;
            z-index: 3;
            border-radius: 10px 10px 0 0;
        }}

        /* SELLO DE CERA ROJO con P&J caligráficas (SVG inyectado) */
        .seal {{
            position: absolute; top: 160px; left: 215px;
            width: 120px; height: 120px;
            /* Rojo cera con degradado radial para relieve */
            background: radial-gradient(circle, #b22222 0%, #8b0000 70%, #660000 100%);
            border-radius: 50%; z-index: 4;
            display: flex; align-items: center; justify-content: center;
            box-shadow: inset 0 0 20px rgba(0,0,0,0.6), 0 10px 20px rgba(0,0,0,0.4);
            border: 3px solid #a52a2a;
            transition: opacity 0.5s ease, transform 0.5s ease;
        }}

        /* Efectos de apertura al hacer clic */
        .opened .flap {{ transform: rotateX(180deg); z-index: 1; }}
        .opened .seal {{ opacity: 0; transform: translateY(-20px) scale(1.2); }}

        /* Texto de destinatario elegante */
        .recipient {{
            position: absolute; bottom: 40px; width: 100%;
            text-align: center; color: #f4f1ea;
            font-family: 'Playfair Display', serif;
            font-style: italic; letter-spacing: 2px; font-size: 16px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
            z-index: 2;
        }}
        
        .instruction {{
            margin-top: 30px; color: #aaa; font-family: serif; font-style: italic;
        }}
    </style>

    <div class="main-container" onclick="openEnvelope()">
        <div class="envelope" id="envelope">
            <div class="flap"></div>
            <div class="seal">
                <svg viewBox="0 0 100 100" width="80" height="80">
                    <defs>
                        <linearGradient id="goldGradient" x1="0%" y1="0%" x2="0%" y2="100%">
                            <stop offset="0%" style="stop-color:#f7e082;stop-opacity:1" />
                            <stop offset="50%" style="stop-color:#d4af37;stop-opacity:1" />
                            <stop offset="100%" style="stop-color:#b8902d;stop-opacity:1" />
                        </linearGradient>
                    </defs>
                    <text x="50%" y="65%" text-anchor="middle" font-family="'Playfair Display', serif" font-weight="700" font-style="italic" font-size="50" fill="url(#goldGradient)" style="filter: drop-shadow(1px 1px 1px rgba(0,0,0,0.5));">
                        P&J
                    </text>
                </svg>
            </div>
            <div class="recipient">PARA: {nombre.upper()}</div>
        </div>
        <p class="instruction">Haz clic en el sello para abrir</p>
    </div>

    <script>
        function openEnvelope() {{
            document.getElementById('envelope').classList.add('opened');
            // Esperamos a que la animación termine para avisar a Streamlit
            setTimeout(() => {{
                window.parent.postMessage({{type: 'streamlit:setComponentValue', value: true}}, '*');
            }}, 800);
        }}
    </script>
    """

    # Renderizamos el sobre interactivo. 'height=750' asegura que la solapa dorada no se corte al abrirse.
    components.html(envelope_html, height=750)

    # Botón de respaldo (invisible o secundario) por seguridad
    st.write("---")
    if st.button("ENTRAR A LA INVITACIÓN", type="secondary", use_container_width=True):
        st.session_state.abierto = True
        st.rerun()

else:
    # --- PANTALLA B: CONTENIDO DETALLADO (Invitación Abierta) ---
    st.balloons()
    
    # Restaura el fondo claro para el contenido
    st.markdown(f"""
        <h1 style='text-align: center; color: #d4af37; font-family:serif; font-size: 50px; margin-bottom:0;'>
            ¡Bienvenidos!
        </h1>
        <h2 style='text-align: center; color: #2c3e50; margin-top:0;'>
            {nombre}
        </h2>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Resumen de detalles (Este apartado ya es totalmente funcional)
    col1, col2, col3 = st.columns(3)
    col1.metric("Fecha", "25 Julio")
    col2.metric("Lugar", "Cuenca")
    col3.metric("Pases", "2")

    st.divider()
    
    # Formulario RSVP (Guardado de datos, etc.)
    st.subheader("Confirmar Asistencia")
    with st.form("rsvp"):
        st.radio("¿Nos acompañas?", ["Sí, confirmo", "Lo siento, no puedo"])
        st.text_area("Mensaje para Pablo y Joy")
        st.form_submit_button("Enviar RSVP")

    if st.button("← Ver sobre de nuevo"):
        st.session_state.abierto = False
        st.rerun()
