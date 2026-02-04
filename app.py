"""
# QR Code Generator for URLs

A Python and Streamlit app to generate QR codes for multiple URLs quickly.  
Perfect for sharing web apps, dashboards, or any online resources with colleagues or mobile devices.

## Features

- Generate QR codes from a list of URLs
- Display QR codes in a Streamlit dashboard for easy scanning
- Clickable links to open URLs directly in browser
- Save QR codes locally as PNG files
- Customizable QR code size and colors
- Supports multiple apps / websites at once

## Usage

1. Update the `urls` dictionary below with your desired URLs (already included).
2. Run the Streamlit app locally:

    pip install -r requirements.txt
    streamlit run app.py

3. Or deploy to Streamlit Cloud — dependencies will install automatically from requirements.txt.
4. Scan the QR codes displayed on the dashboard or click the links to open the URLs.
5. PNG files of each QR code will also be saved locally for printing or sharing.

## Acknowledgements

Developed by **Dr. Dawid Krynicki**

## License

MIT License
"""

# ----------------- ACTUAL CODE -----------------
import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import os

# --- YOUR URLS ---
urls = {
    "Medsuite": "https://medsuite.streamlit.app/",
    "Adult Refeeding Syndrome": "https://adult-refeeding-syndrome.streamlit.app/",
    "CHADS-BLED Web": "https://chads-bled-web.streamlit.app/",
    "NIHSS Stroke Severity Scoring": "https://nihss-stroke-severity-scoring.streamlit.app/",
    "Check-in SafeCheck": "https://check-in-safecheck.streamlit.app/"
}

st.set_page_config(page_title="QR Code Generator", page_icon="📱", layout="centered")
st.title("📱 QR Code Generator Dashboard")
st.markdown("Scan the QR codes or click the links below to open the corresponding apps or websites.")

# Create folder for saved QR codes
save_folder = "qr_codes"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Generate and display QR codes
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
    pil_img = img.convert("RGB")

    # Save PNG locally
    filename = os.path.join(save_folder, f"{name.replace(' ', '_')}_QR.png")
    pil_img.save(filename)

    # Convert to BytesIO for Streamlit display
    buf = BytesIO()
    pil_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Display in Streamlit
    st.markdown(f"### {name}")
    st.image(byte_im, caption=f"Scan to open {name}", use_column_width=False)
    st.markdown(f"[🔗 Click to open {name}]({url})")
