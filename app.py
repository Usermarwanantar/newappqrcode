import streamlit as st
import os
import qrcode
from io import BytesIO
from PIL import Image

# 📁 Dossier public où enregistrer les fichiers
UPLOAD_DIR = "static/uploaded"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 🌍 URL de base de ton application Streamlit Cloud
# 🛠️ À modifier après déploiement (ex: https://monapp.streamlit.app)
APP_BASE_URL = "https://newappqrcode-b844r2wqzg8xgytpjuchld.streamlit.app"

st.set_page_config(page_title="Uploader + QR", layout="centered")
st.title("📁 Uploader un fichier et générer un QR Code")

uploaded_file = st.file_uploader("📤 Choisissez un fichier", type=None)

if uploaded_file:
    # 1. Sauvegarder le fichier dans 'static/uploaded'
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ Fichier sauvegardé : {uploaded_file.name}")

    # 2. Créer le lien public
    public_link = f"{APP_BASE_URL}/{UPLOAD_DIR}/{uploaded_file.name}"
    st.markdown(f"🔗 [Lien public de téléchargement]({public_link})")

    # 3. Générer le QR Code
    qr = qrcode.make(public_link)
    buf = BytesIO()
    qr.save(buf)
    buf.seek(0)
    st.image(Image.open(buf), caption="📷 QR Code du lien")

    # 4. Bouton de téléchargement du QR
    st.download_button(
        label="📥 Télécharger le QR Code",
        data=buf,
        file_name="qr_code.png",
        mime="image/png"
    )
