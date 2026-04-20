import streamlit as st
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import base64
import time

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
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

/* GENERAL */
html, body {
    font-family: 'Poppins', sans-serif;
    color: #5F5F5F;
}

.stApp {
    background-color: #FDECEC;
}

/* TITULO */
.title {
    font-family: 'Great Vibes', cursive;
    text-align: center;
    font-size: 60px;
    animation: fadeInTitle 2s ease;
}

@keyframes fadeInTitle {
    from { opacity: 0; transform: translateY(-20px);}
    to { opacity: 1; transform: translateY(0);}
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
    transition: all 0.3s ease;
}

.button-premium:hover {
    transform: scale(1.05);
    background-color:#d98c8c;
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

/* PETALOS */
.petal {
    position: fixed;
    top: -10px;
    width: 12px;
    height: 12px;
    background: #f7b5b5;
    border-radius: 50%;
    opacity: 0.7;
    animation: fall linear infinite;
}

@keyframes fall {
    to {
        transform: translateY(110vh) rotate(360deg);
    }
}

/* MOBILE */
@media (max-width: 768px) {

    .title {
        font-size: 40px !important;
    }

    .center {
        font-size: 20px !important;
    }

    h2 {
        font-size: 24px !important;
    }

    .card {
        padding: 15px;
        margin: 20px 0;
    }

    .button-premium {
        font-size: 16px;
        padding: 10px 18px;
    }
}

/* OCULTAR MENU */
#MainMenu, header, footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# --- PETALOS ---
petals_html = ""
for i in range(20):
    petals_html += f"""
    <div class="petal" style="
        left:{i*5}%;
        animation-duration:{5 + i%5}s;
        animation-delay:{i*0.3}s;
    "></div>
    """
st.markdown(petals_html, unsafe_allow_html=True)

# --- PORTADA ---
st.markdown('<h1 class="title">Flor & Lucas</h1>', unsafe_allow_html=True)
st.markdown('<p class="center fade-in" style="font-size:32px;">¡Nos casamos! 💍</p>', unsafe_allow_html=True)
st.markdown('<p class="center fade-in">03 de Octubre 2026</p>', unsafe_allow_html=True)

# --- CONTADOR ---
fecha_evento = datetime(2026, 10, 3)
dias = (fecha_evento - datetime.now()).days

st.markdown(f'<p class="center fade-in"><b>Faltan {dias} días 💕</b></p>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- HISTORIA ---
st.markdown('<h2 class="fade-in">Te Invitamos a nuestra Boda</h2>', unsafe_allow_html=True)
st.markdown(
    '<p class="center fade-in">Compartimos 15 años juntos y queremos celebrarlo con ustedes ❤️</p>',
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("""
<style>
.card {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    border-radius: 20px;
    padding: 30px;
    margin: 30px 0;

    border: 1px solid rgba(255, 255, 255, 0.2);
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);

    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-3px);
}
</style>
""", unsafe_allow_html=True)

# --- EVENTO ---
st.markdown('<h2 class="fade-in">Detalles del evento</h2>', unsafe_allow_html=True)

st.markdown("""
<div class="card fade-in">

<div style='text-align:center;'>

<div style='font-size:30px; margin-bottom:15px;'>
👗 <b>Dress Code</b> 👗
</div>

<div style='font-size:24px; margin-bottom:20px;'>
Elegante 
</div>

<div style='color:#d16d6d; font-size:22px;'>

<span style="font-style:italic; font-size:24px;">
<span style="color:#E8A0A0;">❤</span> 
<b>"On Wednesdays we wear pink"</b>
</span>

<br><br>

<span style="font-size:20px;">
Y como nos casamos un 3 de octubre…<br>
¡sumale un toque de rosa en tu look! 😉
</span>

</div>

</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<p class="center fade-in" style="font-size:28px; font-weight:600;">📍 Los Cipreses 2</p>', unsafe_allow_html=True)
st.markdown('<p class="center fade-in" style="font-size:24px;">🕒 17:45 hs</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="center fade-in"><a href="https://maps.app.goo.gl/TnEYrN58aaj6j29v5" target="_blank">📍 Ver ubicación</a></p>',
    unsafe_allow_html=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- REGALO ---
CBU = "0720176588000026340436"
ALIAS = "CAMI.GABI.MACA"

st.markdown(f"""
<div class="card fade-in" style="text-align:center;">

<p style="font-size:24px;">
Si querés hacernos un regalo 💕<br><br>
Podés ayudarnos con nuestra luna de miel ✈️
</p>

<p style="font-size:22px;">
<b>CBU:</b> {CBU}
</p>

<p style="font-size:22px;">
<b>Alias:</b> {ALIAS}
</p>

<button onclick="navigator.clipboard.writeText('{CBU}')"
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

<script>
const btn = document.querySelector("button");
btn.addEventListener("click", function() {{
    const msg = document.getElementById("copiado");
    msg.style.opacity = 1;
    setTimeout(() => {{
        msg.style.opacity = 0;
    }}, 1500);
}});
</script>

</div>
""", unsafe_allow_html=True)
# --- PLAYLIST ---
st.markdown("""
<div class="center fade-in">
    <p style="font-size:26px;">🎶 Agregá una canción a la fiesta</p>
    <a href="https://music.youtube.com/playlist?list=PLmptaA43xE8G1tBG9apqVDBuNOFJu_3DA&jct=QRyJxei3lhU_dmo4Zvdnbw" target="_blank">
        <button class="button-premium">🎧 Agregar canción</button>
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# --- RSVP ---
st.markdown('<h2 class="fade-in">Confirmar asistencia</h2>', unsafe_allow_html=True)

nombre = st.text_input("Nombre y apellido")
asistencia = st.selectbox("¿Asistís?", ["Sí", "No"])

col1, col2 = st.columns(2)
with col1:
    adultos = st.number_input("Adultos", min_value=0, step=1)
with col2:
    ninos = st.number_input("Niñes (Menores de 8 años)", min_value=0, step=1)

restriccion = st.text_input("¿Restricción alimentaria? (opcional)")
coche = st.selectbox("¿Venís en auto?", ["Sí", "No"])

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
