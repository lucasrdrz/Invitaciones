import streamlit as st
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import base64
import streamlit.components.v1 as components

# --- FUNCION IMAGEN ---
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("Foto1.jpeg")

st.set_page_config(page_title="Flor & Lucas 💍", layout="centered")

# --- BACKGROUND ---
st.markdown(f"""
<style>
.stApp {{
    background-image: 
        linear-gradient(rgba(253, 236, 236, 0.85), rgba(253, 236, 236, 0.85)),
        url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
}}
</style>
""", unsafe_allow_html=True)

# --- GOOGLE SHEETS ---
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1SnktIvny6sN1hfr2QfgRLZfEkiPaPQPEv6b31ko_Ucg"
).worksheet("Respuestas de la invitacion")

# --- CSS PRO ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;400&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Parisienne&display=swap');

/* GENERAL */
html, body {
    font-family: 'Poppins', sans-serif;
    color: #5F5F5F;
}

/* TITULO */
.title {
    font-family: 'Parisienne', cursive;
    text-align: center;
    font-size: 70px;
    letter-spacing: 2px;
    color: #E8A0A0;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.15);
}

/* SUBTITULOS */
h2 {
    font-family: 'Playfair Display', serif;
    text-align: center;
    color: #E8A0A0;
}

/* DIVIDER */
.divider {
    height: 1px;
    background: #E8A0A0;
    opacity: 0.3;
    margin: 40px 0;
}

/* CENTRO */
.center {
    text-align: center;
}

/* TARJETAS */
.card {
    background: rgba(255,255,255,0.7);
    backdrop-filter: blur(10px);
    padding: 25px;
    border-radius: 20px;
    margin: 30px 0;
    box-shadow: 0 8px 25px rgba(0,0,0,0.05);
}

/* BOTON */
.button-premium {
    background-color:#E8A0A0;
    color:white;
    border:none;
    padding:12px 24px;
    font-size:20px;
    border-radius:12px;
    cursor:pointer;
}

/* ANIMACION */
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 1s ease forwards;
}

@keyframes fadeInUp {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* OCULTAR MENU */
#MainMenu, header, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# --- TITULO ---
st.markdown('<h1 class="title">Flor & Lucas</h1>', unsafe_allow_html=True)
st.markdown('<p class="center fade-in" style="font-size:32px;">¡Nos casamos! 💍</p>', unsafe_allow_html=True)
st.markdown('<p class="center fade-in">03 de Octubre 2026</p>', unsafe_allow_html=True)

# --- CONTADOR ---
fecha_evento = datetime(2026, 10, 3)
dias = (fecha_evento - datetime.now()).days
st.markdown(f'<p class="center fade-in"><b>Faltan {dias} días 💕</b></p>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- EVENTO ---
# --- EVENTO ---
st.markdown('<h2 class="fade-in">Detalles del evento</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card fade-in">

    <div style='text-align:center;'>

        <div style='font-size:28px; margin-bottom:10px;'>
            👗 <b>Dress Code</b> 👗
        </div>

        <div style='font-size:26px; margin-bottom:15px;'>
            Elegante
        </div>

        <div style='
            text-align:center;
            color:#d16d6d;
            font-size:22px;
        '>

            <span style="font-style:italic;">
                <span style="color:#E8A0A0;">❤</span>
                <b>"On Wednesdays we wear pink"</b>
            </span>

            <br><br>

            <span style="font-style:normal;">
                Y como nos casamos un 3 de octubre…<br>
                ¡sumale un toque de rosa en tu look!
            </span>

        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# --- REGALO ---
CBU = "0720176588000026340436"
ALIAS = "CAMI.GABI.MACA"

st.markdown(f"""
<div class="card fade-in" style="text-align:center;">
<p style="font-size:24px;">Si querés hacernos un regalo 💕</p>
<p><b>CBU:</b> {CBU}</p>
<p><b>Alias:</b> {ALIAS}</p>
</div>
""", unsafe_allow_html=True)

# BOTON FUNCIONAL
components.html(f"""
<div style="text-align:center;">

<button onclick="copiarCBU()"
style="
    margin-top:15px;
    background-color:#E8A0A0;
    color:white;
    border:none;
    padding:12px 20px;
    font-size:18px;
    border-radius:10px;
    cursor:pointer;
">
📋 Copiar CBU
</button>

<p id="copiado" style="opacity:0; margin-top:10px;">
✅ Copiado!
</p>

</div>

<script>
function copiarCBU() {{
    navigator.clipboard.writeText("{CBU}");
    const msg = document.getElementById("copiado");
    msg.style.opacity = 1;
    setTimeout(() => {{
        msg.style.opacity = 0;
    }}, 1500);
}}
</script>
""", height=150)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- RSVP ---
st.markdown('<h2>Confirmar asistencia</h2>', unsafe_allow_html=True)

nombre = st.text_input("Nombre y apellido")
asistencia = st.selectbox("¿Asistís?", ["Sí", "No"])

if st.button("Confirmar asistencia"):
    if nombre:
        sheet.append_row([nombre, asistencia])
        st.success("Confirmado 💖")
    else:
        st.error("Ingresá tu nombre")

# --- FOOTER ---
st.markdown('<p class="center">Con amor, Flor & Lucas 💖</p>', unsafe_allow_html=True)
