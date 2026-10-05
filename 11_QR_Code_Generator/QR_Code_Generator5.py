from urllib.parse import urlencode

import qrcode


def main():
    print("Email QR Code Generator")
    email = input("Enter the email address: ").strip()
    subject = input("Enter the subject: ").strip()
    message = input("Enter the message: ").strip()

    if not email or "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        print("Error: Enter a valid email address.")
        return

    # urlencode safely encodes spaces and special characters in the fields.
    email_details = urlencode({"subject": subject, "body": message})
    payload = f"mailto:{email}?{email_details}"

    qr = qrcode.make(payload)
    qr.save("email_qr.png")
    print("QR code saved as email_qr.png")


if __name__ == "__main__":
    main()