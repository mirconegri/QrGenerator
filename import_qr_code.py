import qrcode

# Ask the user to enter the text or URL to encode
data = input("Enter the text or URL to generate the QR code: ")

# Generate the QR code image
qr_image = qrcode.make(data)

# Save the generated QR code to a file
qr_image.save("qrcode.png")

# Notify the user that the operation was successful
print("QR code successfully generated and saved as 'qrcode.png'.")
