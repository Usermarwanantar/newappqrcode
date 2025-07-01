import streamlit as st
import os
import qrcode
from io import BytesIO
from PIL import Image
import urllib.parse

# 📁 Dossier public de sauvegarde des fichiers (sous /static/)
UPLOAD_DIR = "static/uploaded"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# 🌍 Lien réel de ton app (⚠️ vérifie bien qu’il est exact)
APP_BASE_URL = "https://newappqrcode-b844r2wqzg8xgytpjuchld.streamlit.app"

# 💻 Interface Streamlit
st.set_page_config(page_title="Uploader + QR", layout="centered")
st.title("📁 Uploader un fichier et générer un QR Code public")

# 📤 Uploader un fichier
uploaded_file = st.file_uploader("Sélectionnez un fichier à partager", type=None)

if uploaded_file:
    # 🔐 Nettoyer le nom de fichier
    safe_filename = urllib.parse.quote(uploaded_file.name)

    # 💾 Sauvegarde du fichier dans le dossier static/uploaded/
    file_path = os.path.join(UPLOAD_DIR, safe_filename)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ Fichier enregistré : {uploaded_file.name}")

    # 🔗 Création du lien public (chemin statique)
    public_link = f"{APP_BASE_URL}/static/uploaded/{safe_filename}"
    st.markdown(f"🔗 [Lien de téléchargement direct]({public_link})")

    # 📷 Génération du QR code
    qr = qrcode.make(public_link)
    buf = BytesIO()
    qr.save(buf)
    buf.seek(0)
    st.image(Image.open(buf), caption="📷 QR Code du lien de téléchargement")

    # 💾 Téléchargement du QR code
    st.download_button(
        label="📥 Télécharger le QR Code",
        data=buf,
        file_name="qr_code.png",
        mime="image/png"
    )
