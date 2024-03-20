import qrcode

# The URL to your resume
resume_url = 'https://austin-brock.github.io/contact.html'

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(resume_url)
qr.make(fit=True)

# Create an Image object from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save('resume_qr.png')

print("QR code generated and saved as resume_qr.png")
