import qrcode
import os 
import pyfiglet


print()
def display_center(text):
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Calculate left padding to center the text
    left_padding = (terminal_width - len(text)) // 3
    
    # Display text with padding
    print(" " * left_padding + text)

def main():
    text = " >>> YMQ <<<"
    banner = pyfiglet.figlet_format(text, font="big", width=160)
    display_center(banner)
    display_center("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
    print()
    display_center("||  Made by Eng Youssef Mohamed  ||")
    display_center("-----------------------------------")
    display_center("-----------------------------------")
    display_center("||   github.com/Youssef530245    ||")
    print()
    display_center("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print() 
    print()
if __name__ == "__main__":
    main()

#__________________________________________________________________

# Function to create a QR code
print()
def create_qr_code(data, filename):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Controls the error correction used for the QR Code
        box_size=10,  # Controls how many pixels each “box” of the QR code is
        border=4,  # Controls how many boxes thick the border should be
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)
print()
# Get the data to be encoded in the QR code from the user
data = input("Enter the text to be displayed when scanned: ")
print()
# Get the filename to save the QR code image from the user
filename = input("Enter the filename to save the QR code (e.g., qrcode.png): ")

# Create the QR code
create_qr_code(data, filename)
print()
print(f"QR Code generated and saved as {filename}")
print()
