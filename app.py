import streamlit as st
import qrcode
from PIL import Image

# --- YOUR URLS ---
# Add your URLs here. Key = label, Value = URL
urls = {
    "NIHSS App": "https://your-streamlit-app-url.com",
    "Another App": "https://another-app-url.com",
    "GitHub Repo": "https://github.com/yourusername/your-repo"
}

st.set_page_config(page_title="QR Code Generator", page_icon="📱", layout="centered")
st.title("📱 QR Code Generator Dashboard")
st.markdown("Scan the QR codes below to open the corresponding apps or websites.")

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
    
    # Convert to PIL Image
    pil_img = img.convert("RGB")
    
    # Display in Streamlit
    st.markdown(f"**{name}**")
    st.image(pil_img, caption=f"Scan to open {name}", use_column_width=False)
    
    # Save locally as PNG
    filename = f"{name.replace(' ', '_')}_QR.png"
    pil_img.save(filename)
