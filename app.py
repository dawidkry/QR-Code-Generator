"""
# QR Code Generator for URLs

A Python and Streamlit app to generate QR codes for multiple URLs quickly.  
Perfect for sharing web apps, dashboards, or any online resources with colleagues or mobile devices.

## Features

- Generate QR codes from a list of predefined URLs
- Display QR codes in a Streamlit dashboard for easy scanning
- Clickable links to open URLs directly in browser
- Save PNG codes locally for predefined URLs
- Dynamically create a QR code for any URL without saving
- Download QR codes for copying/pasting
- Customizable QR code size and colors
"""

import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import os

# --- PREDEFINED URLS ---
urls = {
    "Medsuite": "https://medsuite.streamlit.app/",
    "Adult Refeeding Syndrome": "https://adult-refeeding-syndrome.streamlit.app/",
    "CHADS-BLED Web": "https://chads-bled-web.streamlit.app/",
    "NIHSS Stroke Severity Scoring": "https://nihss-stroke-severity-scoring.streamlit.app/",
    "Check-in SafeCheck": "https://check-in-safecheck.streamlit.app/"
}

st.set_page_config(page_title="QR Code Generator", page_icon="📱", layout="centered")
st.title("📱 QR Code Generator Dashboard")

# --- DYNAMIC QR CODE GENERATOR AT THE TOP ---
st.header("🔹 Generate a QR Code for Any URL")
user_url = st.text_input("Enter a URL here:")

def generate_qr_image(url: str) -> Image.Image:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img

if user_url:
    pil_user = generate_qr_image(user_url)
    
    # Display in Streamlit
    buf = BytesIO()
    pil_user.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.image(byte_im, caption=f"QR Code for {user_url}", use_column_width=False)
    st.markdown(f"[🔗 Click to open URL]({user_url})")
    
    # Download button
    st.download_button(
        label="💾 Download QR Code",
        data=byte_im,
        file_name="dynamic_QR.png",
        mime="image/png"
    )

st.divider()
st.markdown("### Predefined Apps QR Codes")
st.markdown("Scan the QR codes below or click the links to open the corresponding apps or websites.")

# --- CREATE FOLDER FOR SAVED QR CODES ---
save_folder = "qr_codes"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# --- GENERATE AND DISPLAY PREDEFINED QR CODES ---
for name, url in urls.items():
    pil_img = generate_qr_image(url)

    # Save PNG locally
    filename = os.path.join(save_folder, f"{name.replace(' ', '_')}_QR.png")
    pil_img.save(filename)

    # Convert to BytesIO for Streamlit display
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.markdown(f"### {name}")
    st.image(byte_im, caption=f"Scan to open {name}", use_column_width=False)
    st.markdown(f"[🔗 Click to open {name}]({url})")
    
    # Download button for predefined QR codes
    st.download_button(
        label="💾 Download QR Code",
        data=byte_im,
        file_name=f"{name.replace(' ', '_')}_QR.png",
        mime="image/png"
    )
