import qrcode


def main():
    print("SMS QR Code Generator")
    phone = input("Enter the phone number: ").strip()
    message = input("Enter the SMS message: ").strip()

    if not phone or not message:
        print("Error: Both phone number and message are required.")
        return

    payload = f"SMSTO:{phone}:{message}"
    qr = qrcode.make(payload)
    qr.save("sms_qr.png")
    print("QR code saved as sms_qr.png")


if __name__ == "__main__":
    main()