import qrcode


def escape_vcard(value):
    """Escape special characters used in vCard text values."""
    return (
        value.replace("\\", "\\\\")
        .replace("\r\n", "\\n")
        .replace("\n", "\\n")
        .replace(",", "\\,")
        .replace(";", "\\;")
    )


def main():
    print("Contact QR Code Generator")
    name = input("Enter the contact name: ").strip()
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    address = input("Enter the address (optional): ").strip()

    if not name or not phone or not email:
        print("Error: Name, phone number, and email address are required.")
        return

    # Build a simple vCard 3.0 contact payload.
    contact_data = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:;{escape_vcard(name)};;;",
        f"FN:{escape_vcard(name)}",
        f"TEL;TYPE=CELL:{escape_vcard(phone)}",
        f"EMAIL:{escape_vcard(email)}",
    ]
    if address:
        contact_data.append(f"ADR;TYPE=HOME:;;{escape_vcard(address)};;;;")
    contact_data.append("END:VCARD")
    payload = "\r\n".join(contact_data)

    qr = qrcode.make(payload)
    qr.save("contact_qr.png")
    print("QR code saved as contact_qr.png")


if __name__ == "__main__":
    main()