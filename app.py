"""
📱 QR Code Generator Pro Dashboard

Features:
- Dynamic QR generator at the top
- Predefined app QR codes from JSON
- Grid layout for neat display
- Download buttons for all QR codes
"""

import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import os
import json

# --- PAGE CONFIG ---
st.set_page_config(page_title="QR Code Generator Pro", page_icon="📱", layout="wide")
st.title("📱 QR Code Generator Pro Dashboard")

# --- HELPER FUNCTION ---
def generate_qr_image(url: str) -> Image.Image:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img

# --- DYNAMIC QR GENERATOR ---
st.header("🔹 Generate a QR Code for Any URL")
user_url = st.text_input("Enter a URL here:")

if user_url:
    pil_user = generate_qr_image(user_url)
    buf = BytesIO()
    pil_user.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption=f"QR Code for {user_url}", use_column_width=False)
    st.markdown(f"[🔗 Click to open URL]({user_url})")
    st.download_button(
        label="💾 Download QR Code",
        data=byte_im,
        file_name="dynamic_QR.png",
        mime="image/png"
    )

st.divider()
st.markdown("### Predefined App QR Codes")

# --- CREATE FOLDER FOR SAVED QR CODES ---
save_folder = "qr_codes"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# --- LOAD PREDEFINED APPS FROM JSON ---
with open("apps_config.json") as f:
    apps = json.load(f)

# --- DISPLAY IN GRID ---
cols_per_row = 3  # Adjust number of columns per row
cols = st.columns(cols_per_row)
for i, (name, url) in enumerate(apps.items()):
    pil_img = generate_qr_image(url)
    
    # Save PNG locally
    filename = os.path.join(save_folder, f"{name.replace(' ', '_')}_QR.png")
    pil_img.save(filename)

    # Convert to BytesIO for display
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Determine column
    col = cols[i % cols_per_row]

    with col:
        st.markdown(f"**{name}**")
        st.image(byte_im, caption=f"Scan to open {name}", use_column_width=True)
        st.markdown(f"[🔗 Open {name}]({url})")
        st.download_button(
            label="💾 Download QR Code",
            data=byte_im,
            file_name=f"{name.replace(' ', '_')}_QR.png",
            mime="image/png"
        )

    # Start a new row after every cols_per_row
    if (i + 1) % cols_per_row == 0:
        cols = st.columns(cols_per_row)
