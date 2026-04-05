import streamlit as st
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import base64

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img = get_base64("Foto1.jpeg")

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
# --- CONFIG ---
st.set_page_config(page_title="Flor & Lucas 💍", layout="centered")

# --- GOOGLE SHEETS ---
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope
)

client = gspread.authorize(creds)

# ✅ HOJA CORRECTA (IMPORTANTE)
sheet = client.open_by_key(
    "1SnktIvny6sN1hfr2QfgRLZfEkiPaPQPEv6b31ko_Ucg"
).worksheet("Respuestas de la invitacion")

# --- CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Poppins:wght@300;400&display=swap');

.stApp { background-color: #FDECEC; }

#MainMenu, header, footer { visibility: hidden; }

html, body {
    font-family: 'Poppins', sans-serif;
    color: #5F5F5F;
}

h1, h2 {
    font-family: 'Playfair Display', serif;
    text-align: center;
    color: #E8A0A0;
}

.divider {
    height: 1px;
    background: #E8A0A0;
    opacity: 0.3;
    margin: 40px 0;
}

.center { text-align: center; }

.stButton button {
    background-color: #E8A0A0;
    color: white;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
#st.image("Foto.jpg", use_column_width=True)
# --- PORTADA ---
st.markdown("<h1>Flor & Lucas</h1>", unsafe_allow_html=True)
st.markdown('<p class="center">¡Nos casamos! 💍</p>', unsafe_allow_html=True)
st.markdown('<p class="center">03 de Octubre 2026</p>', unsafe_allow_html=True)

# --- CONTADOR ---
fecha_evento = datetime(2026, 10, 3)
dias = (fecha_evento - datetime.now()).days
st.markdown(f'<p class="center"><b>Faltan {dias} días 💕</b></p>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- HISTORIA ---
st.markdown("<h2>Te Invitamos a nuestra Boda</h2>", unsafe_allow_html=True)
st.markdown(
    '<p class="center">Compartimos 15 años juntos y queremos celebrarlo con ustedes ❤️</p>',
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- EVENTO ---
st.markdown("<h2>Detalles del evento</h2>", unsafe_allow_html=True)
st.markdown('<p class="center">📍 Los Cipreses 2</p>', unsafe_allow_html=True)
st.markdown('<p class="center">🕒 17:45 hs</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="center"><a href="https://maps.app.goo.gl/3oauB4HkXW6wqN7U7" target="_blank">📍 Ver ubicación</a></p>',
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- CBU ---
st.markdown("<h2>Regalo</h2>", unsafe_allow_html=True)

st.markdown("""
<p class="center">
Si querés hacernos un regalo 💕<br><br>
Podés ayudarnos con nuestra luna de miel ✈️
</p>
""", unsafe_allow_html=True)

CBU = "0720176588000026340436"
ALIAS = "CAMI.GABI.MACA"

st.markdown(f'<p class="center"><b>CBU:</b> {CBU}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="center"><b>Alias:</b> {ALIAS}</p>', unsafe_allow_html=True)

st.code(CBU, language=None)
st.caption("👆 Tocá para copiar el CBU")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- RSVP ---
st.markdown("<h2>Confirmar asistencia</h2>", unsafe_allow_html=True)

nombre = st.text_input("Nombre y apellido")
asistencia = st.selectbox("¿Asistís?", ["Sí", "No"])

col1, col2 = st.columns(2)
with col1:
    adultos = st.number_input("Adultos", min_value=0, step=1)
with col2:
    ninos = st.number_input("Niñes (Menores de 8 años)", min_value=0, step=1)

restriccion = st.text_input("¿Restricción alimentaria? (opcional)")
coche = st.selectbox("¿Venís en auto?", ["Sí", "No"])

# --- DATA ACTUAL ---
data = sheet.get_all_records()
df = pd.DataFrame(data)

def ya_existe(nombre):
    if df.empty:
        return False
    return nombre.lower().strip() in df["Nombre"].astype(str).str.lower().str.strip().values


if st.button("Confirmar asistencia"):

    if not nombre:
        st.error("Por favor ingresá tu nombre")

    elif ya_existe(nombre):
        st.warning("⚠️ Este nombre ya confirmó asistencia")

    else:
        sheet.append_row([
            nombre,
            asistencia,
            adultos,
            ninos,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            restriccion,
            coche
        ])

        st.success("💖 ¡Gracias por confirmar! Te esperamos")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(
    '<p class="center" style="opacity:0.6;">Con amor, Flor & Lucas 💖</p>',
    unsafe_allow_html=True
)
#st.image("Foto1.jpeg", use_column_width=True)
