import qrcode


def main():
    print("Phone QR Code Generator")
    phone = input("Enter the phone number: ").strip()

    if not phone:
        print("Error: Phone number cannot be empty.")
        return

    qr = qrcode.make(f"tel:{phone}")
    qr.save("phone_qr.png")
    print("QR code saved as phone_qr.png")


if __name__ == "__main__":
    main()