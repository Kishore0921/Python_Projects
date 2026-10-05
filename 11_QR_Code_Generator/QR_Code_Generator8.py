import qrcode


def main():
    print("Location QR Code Generator")
    latitude_text = input("Enter the latitude (-90 to 90): ").strip()
    longitude_text = input("Enter the longitude (-180 to 180): ").strip()

    try:
        latitude = float(latitude_text)
        longitude = float(longitude_text)
    except ValueError:
        print("Error: Latitude and longitude must be numbers.")
        return

    if not -90 <= latitude <= 90:
        print("Error: Latitude must be between -90 and 90.")
        return
    if not -180 <= longitude <= 180:
        print("Error: Longitude must be between -180 and 180.")
        return

    coordinates = f"{latitude:g},{longitude:g}"
    payload = f"https://www.google.com/maps?q={coordinates}"
    qr = qrcode.make(payload)
    qr.save("location_qr.png")
    print("QR code saved as location_qr.png")


if __name__ == "__main__":
    main()