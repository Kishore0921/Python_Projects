import qrcode


def escape_wifi_value(value):
    """Escape special characters in a Wi-Fi QR value."""
    for character in ("\\", ";", ",", ":"):
        value = value.replace(character, "\\" + character)
    return value


def main():
    print("Wi-Fi QR Code Generator")
    ssid = input("Enter the Wi-Fi network name (SSID): ").strip()

    if not ssid:
        print("Error: Wi-Fi network name cannot be empty.")
        return

    password = input("Enter the Wi-Fi password (leave blank for None): ").strip()
    security_choice = input("Enter security type (WPA, WEP, or None): ").strip().upper()

    if security_choice not in ("WPA", "WEP", "NONE"):
        print("Error: Security type must be WPA, WEP, or None.")
        return
    if security_choice != "NONE" and not password:
        print("Error: A password is required for WPA or WEP.")
        return

    security = "nopass" if security_choice == "NONE" else security_choice
    payload = (
        f"WIFI:T:{security};S:{escape_wifi_value(ssid)};"
        f"P:{escape_wifi_value(password)};;"
    )

    qr = qrcode.make(payload)
    qr.save("wifi_qr.png")
    print("QR code saved as wifi_qr.png")


if __name__ == "__main__":
    main()