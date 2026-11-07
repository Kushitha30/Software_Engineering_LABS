def sanitize_license_plate(plate):
    """
    Sanitize license plate string by stripping delimiters (-, ' ', _, #)
    and converting to uppercase. Handles None and non-string inputs safely.
    """
    if plate is None or not isinstance(plate, str):
        return ""
    plate = plate.strip()
    for ch in ['-', ' ', '_', '#']:
        plate = plate.replace(ch, '')
    return plate.upper()

def parse_trip_mileage(mileage_csv):
    """
    Parse a comma-separated string of trip mileages into a list of floats.
    Safely ignores empty parts, invalid numbers, and handles None or non-string inputs.
    """
    if mileage_csv is None or not isinstance(mileage_csv, str):
        return []
    parts = mileage_csv.split(',')
    res = []
    for m in parts:
        m = m.strip()
        if not m:
            continue
        try:
            val = float(m)
            if val < 0:
                continue
            res.append(val)
        except ValueError:
            continue
    return res

def format_rental_invoice(record):
    """
    Format a rental invoice from 'Driver:Days:Category' string.
    Validates input type, required delimiters, valid integer days (>= 0),
    and non-empty fields. Returns a formatted invoice string or an error message.
    """
    if record is None or not isinstance(record, str):
        return "Invalid record: Expected non-null string format 'Driver:Days:Category'"
    parts = record.split(':')
    if len(parts) < 3:
        return "Invalid record format: Expected 'Driver:Days:Category'"
    driver = parts[0].strip()
    if not driver:
        return "Invalid record: Driver name cannot be empty"
    try:
        days = int(parts[1].strip())
    except (ValueError, TypeError):
        return f"Invalid record: Days must be a valid integer, got '{parts[1]}'"
    if days < 0:
        return "Invalid record: Days cannot be negative"
    category = parts[2].strip()
    if not category:
        return "Invalid record: Category cannot be empty"
    daily_rate = 50.0 if category.lower() == "suv" else 30.0
    total = days * daily_rate
    return f"Driver {driver} booked {category} for {days} days: Total ${total:.2f}"

def main():
    print("==== Running sanitize_license_plate ====")
    raw_plate = input("Enter license plate with delimiters (-, _, #): ")
    clean_plate = sanitize_license_plate(raw_plate)
    print("Sanitized Plate:", clean_plate)

    print("\n==== Running parse_trip_mileage ====")
    csv_input = input("Enter CSV of mileages (e.g. 100.5, 45.2, 80.0): ")
    mileage_list = parse_trip_mileage(csv_input)
    print("Parsed Mileage List:", mileage_list)

    print("\n==== Running format_rental_invoice ====")
    record_input = input("Enter rental record (Driver:Days:Category): ")
    invoice = format_rental_invoice(record_input)
    print("Rental Invoice:", invoice)

if __name__ == "__main__":
    main()
