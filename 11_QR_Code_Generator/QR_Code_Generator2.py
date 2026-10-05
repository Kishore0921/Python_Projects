from urllib.parse import urlsplit

import qrcode


def main():
    print("URL QR Code Generator")
    url = input("Enter a website URL: ").strip()

    if not url:
        print("Error: URL cannot be empty.")
        return

    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.netloc:
        print("Error: Enter a valid URL beginning with http:// or https://.")
        return

    qr = qrcode.make(url)
    qr.save("url_qr.png")
    print("QR code saved as url_qr.png")


if __name__ == "__main__":
    main()