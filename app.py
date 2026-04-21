import streamlit as st
import streamlit.components.v1 as components

# Configuración de página
st.set_page_config(page_title="Boda Pablo y Joy", page_icon="💍", layout="centered")

# 1. CAPTURAR DATOS DE LA URL
# Ejemplo: ?invitado=Ana_y_Luis&pases=2
params = st.query_params
nombre_invitado = params.get("invitado", "Invitado Especial").replace("_", " ")
cupos = params.get("pases", "2")

# 2. ESTILO CSS PARA EL SOBRE (Animación)
# Aquí inyectamos el diseño del sobre y la lógica de apertura
envelope_html = f"""
<style>
    :root {{
        --bg-color: #f4f1ea;
        --envelope-color: #2c3e50;
        --paper-color: #ffffff;
        --gold: #d4af37;
    }}
    .body-envelope {{
        display: flex; justify-content: center; align-items: center; height: 400px;
        font-family: 'Georgia', serif; background: transparent;
    }}
    .envelope-wrapper {{ position: relative; cursor: pointer; transition: 0.5s; }}
    .envelope {{
        position: relative; width: 300px; height: 200px;
        background: var(--envelope-color); border-bottom-left-radius: 5px; border-bottom-right-radius: 5px;
    }}
    .envelope:before {{
        content: ""; position: absolute; z-index: 2; top: 0;
        border-top: 110px solid var(--gold); border-left: 150px solid transparent; border-right: 150px solid transparent;
        transform-origin: top; transition: all 0.5s ease-in-out;
    }}
    .envelope.open:before {{ transform: rotateX(180deg); z-index: 0; }}
    .letter {{
        position: absolute; bottom: 10px; left: 10px; width: 280px; height: 180px;
        background: var(--paper-color); padding: 20px; text-align: center;
        transition: all 0.5s ease-in-out; z-index: 1; border: 1px solid #eee;
    }}
    .envelope.open .letter {{ transform: translateY(-120px); height: 250px; z-index: 3; }}
    .text-invite {{ font-size: 14px; color: #333; }}
</style>

<div class="body-envelope">
    <div class="envelope-wrapper" onclick="document.querySelector('.envelope').classList.toggle('open')">
        <div class="envelope">
            <div class="letter">
                <p class="text-invite">PARA:</p>
                <h3 style="color:var(--gold);">{nombre_invitado}</h3>
                <p class="text-invite">Tenemos {cupos} lugares reservados para ustedes.</p>
                <p style="font-size: 10px;">(Haz clic para cerrar/abrir)</p>
            </div>
        </div>
    </div>
</div>
"""

# 3. INTERFAZ DE STREAMLIT
st.markdown(f"<h1 style='text-align: center;'>👰🤵 Pablo & Joy</h1>", unsafe_allow_html=True)

# Mostrar el sobre interactivo
components.html(envelope_html, height=450)

# El resto del contenido solo se ve si el usuario hace scroll
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.header("📍 Ubicación")
    st.write("Iglesia de San Blas, Cuenca")
    st.button("Ver en Google Maps")

with col2:
    st.header("⏳ Cuenta Regresiva")
    st.subheader("Julio 2026")

st.divider()

# Formulario de Confirmación (RSVP)
st.header("Confirmar Asistencia")
with st.form("rsvp_form"):
    st.write(f"Hola {nombre_invitado}, confirma tu asistencia:")
    asistencia = st.radio("¿Asistirás?", ["Sí, allí estaré", "Lo siento, no puedo"])
    comida = st.selectbox("Restricciones alimentarias", ["Ninguna", "Vegetariano", "Sin gluten"])
    
    submitted = st.form_submit_button("Enviar Confirmación")
    if submitted:
        if asistencia == "Sí, allí estaré":
            st.balloons()
            st.success(f"¡Gracias {nombre_invitado}! Te esperamos con ansias.")
        else:
            st.warning("Te extrañaremos en nuestro gran día.")
