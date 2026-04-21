import streamlit as st
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN E INICIALIZACIÓN
st.set_page_config(page_title="Boda Pablo y Joy", page_icon="💍", layout="centered")

# Inicializamos el estado del sobre si no existe
if 'sobre_abierto' not in st.session_state:
    st.session_state.sobre_abierto = False

# Captura de parámetros para personalización
params = st.query_params
nombre = params.get("invitado", "Invitado Especial").replace("_", " ")
pases = params.get("pases", "2")

# 2. LÓGICA DE VISUALIZACIÓN
if not st.session_state.sobre_abierto:
    # --- APARTADO A: EL SOBRE (INICIO) ---
    
    # HTML con un botón invisible que activa el callback de Streamlit
    # Usamos un truco: el clic en el sobre recarga la página con un parámetro
    envelope_html = f"""
    <style>
        .envelope-container {{
            display: flex; flex-direction: column; align-items: center;
            justify-content: center; height: 80vh; cursor: pointer;
        }}
        .envelope {{
            width: 500px; height: 300px; background: #2c3e50;
            position: relative; border-radius: 0 0 10px 10px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3);
        }}
        .envelope:before {{
            content: ""; position: absolute; top: 0;
            border-top: 170px solid #d4af37;
            border-left: 250px solid transparent; border-right: 250px solid transparent;
        }}
        .label {{
            position: absolute; top: 180px; width: 100%; text-align: center;
            color: white; font-family: sans-serif; letter-spacing: 2px;
        }}
    </style>
    <div class="envelope-container" id="open-btn">
        <div class="envelope">
            <div class="label">PARA: {nombre.upper()}</div>
        </div>
        <p style="margin-top: 20px; color: #888; font-family: serif;">Haz clic para abrir la invitación</p>
    </div>
    """
    
    components.html(envelope_html, height=500)
    
    # Botón de Streamlit para "entrar" formalmente
    if st.button("ABRIR INVITACIÓN"):
        st.session_state.sobre_abierto = True
        st.rerun()

else:
    # --- APARTADO B: CONTENIDO DETALLADO ---
    
    # Botón para regresar (opcional)
    if st.button("← Ver sobre de nuevo"):
        st.session_state.sobre_abierto = False
        st.rerun()

    st.markdown(f"<h1 style='text-align: center; color: #d4af37;'>¡Bienvenidos, {nombre}!</h1>", unsafe_allow_html=True)
    
    # Aquí va toda la info que ya planeamos
    col1, col2, col3 = st.columns(3)
    col1.metric("Fecha", "25 Julio")
    col2.metric("Lugar", "Cuenca")
    col3.metric("Pases", pases)

    st.divider()
    
    # Sección de confirmación mejorada
    st.subheader("Confirma tu asistencia aquí")
    with st.form("rsvp"):
        asistencia = st.radio("¿Nos acompañas?", ["Sí, confirmo", "No puedo asistir"])
        mensaje = st.text_area("Mensaje para Pablo y Joy")
        if st.form_submit_button("Enviar RSVP"):
            st.balloons()
            st.success("¡Tu respuesta ha sido guardada!")
