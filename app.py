# --- INSTALL REQUIREMENTS ---
# pip install streamlit qrcode[pil] pillow

import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# --- YOUR URLS ---
# Add as many URLs as you want
urls = {
    "NIHSS App": "https://your-streamlit-app-url.com",
    "Another App": "https://another-app-url.com",
    "GitHub Repo": "https://github.com/yourusername/your-repo"
}

st.title("📱 Scan QR Codes to Open Apps / Sites")

for name, url in urls.items():
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert to PIL Image (optional, if you want to manipulate or show in Streamlit)
    pil_img = img.convert("RGB")
    
    # Display in Streamlit
    st.markdown(f"**{name}**")
    st.image(pil_img, caption=f"Scan to open {name}", use_column_width=False)

    # Save PNG locally
    filename = f"{name.replace(' ', '_')}_QR.png"
    pil_img.save(filename)
