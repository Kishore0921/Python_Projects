from datetime import datetime

import qrcode


def escape_ical_value(value):
    """Escape special characters in an iCalendar text value."""
    return (
        value.replace("\\", "\\\\")
        .replace("\r\n", "\n")
        .replace("\r", "\n")
        .replace("\n", "\\n")
        .replace(",", "\\,")
        .replace(";", "\\;")
    )


def main():
    print("Event QR Code Generator")
    event_name = input("Enter the event name: ").strip()
    start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
    start_time = input("Enter the start time (HH:MM): ").strip()
    end_date = input("Enter the end date (YYYY-MM-DD): ").strip()
    end_time = input("Enter the end time (HH:MM): ").strip()
    location = input("Enter the event location: ").strip()

    if not all((event_name, start_date, start_time, end_date, end_time, location)):
        print("Error: All event fields are required.")
        return

    try:
        start = datetime.strptime(f"{start_date} {start_time}", "%Y-%m-%d %H:%M")
        end = datetime.strptime(f"{end_date} {end_time}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Error: Enter dates as YYYY-MM-DD and times as HH:MM.")
        return

    if end <= start:
        print("Error: End date and time must be after the start date and time.")
        return

    # Use floating local times and CRLF line endings as expected by iCalendar.
    payload = "\r\n".join(
        [
            "BEGIN:VCALENDAR",
            "VERSION:2.0",
            "BEGIN:VEVENT",
            f"SUMMARY:{escape_ical_value(event_name)}",
            f"DTSTART:{start.strftime('%Y%m%dT%H%M%S')}",
            f"DTEND:{end.strftime('%Y%m%dT%H%M%S')}",
            f"LOCATION:{escape_ical_value(location)}",
            "END:VEVENT",
            "END:VCALENDAR",
        ]
    )

    qr = qrcode.make(payload)
    qr.save("event_qr.png")
    print("QR code saved as event_qr.png")


if __name__ == "__main__":
    main()