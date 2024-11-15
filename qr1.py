# Install Required Libraries:
# pip install qrcode[pil]

# Import Libraries:
import qrcode
from PIL import Image

# 1. Basic QR Code Generation:
def generate_basic_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('https://www.example.com')
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('example_qr.png')
    print("Basic QR code generated and saved as 'example_qr.png'.")

# 2. Customization: Change Size and Color
def generate_custom_qr():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data('https://www.example.com')
    qr.make(fit=True)
    img = qr.make_image(fill='blue', back_color='yellow')
    img.save('custom_qr.png')
    print("Custom QR code with different colors generated and saved as 'custom_qr.png'.")

# 3. Advanced Features: Add Logos or Custom Images
def generate_qr_with_logo():
    base = Image.open('custom_qr.png')  # Ensure 'custom_qr.png' exists
    logo = Image.open('logo.png')  # Ensure 'logo.png' exists in the same directory
    logo = logo.resize((50, 50))
    base.paste(logo, (80, 80), logo)
    base.save('qr_with_logo.png')
    print("QR code with a logo generated and saved as 'qr_with_logo.png'.")

# Example Usage:
if __name__ == "__main__":
    # Uncomment the function you want to run
    generate_basic_qr()  # Generate a basic QR code
    generate_custom_qr()  # Generate a custom QR code with different colors
    generate_qr_with_logo()  # Generate a QR code with a logo
