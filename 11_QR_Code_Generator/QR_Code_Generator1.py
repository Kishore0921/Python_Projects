import qrcode


def main():
    print("Text QR Code Generator")
    text = input("Enter the text for your QR code: ").strip()

    if not text:
        print("Error: Text cannot be empty.")
        return

    qr = qrcode.make(text)
    qr.save("text_qr.png")
    print("QR code saved as text_qr.png")


if __name__ == "__main__":
    main()