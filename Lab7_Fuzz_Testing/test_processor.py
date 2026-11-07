from hypothesis import given, strategies as st
from processor import sanitize_license_plate, parse_trip_mileage, format_rental_invoice

@given(st.text() | st.none())
def test_sanitize_license_plate_no_crash(s):
    # To-Do: Using try and except complete this function.
    try:
        sanitize_license_plate(s)
    except Exception as e:
        assert False, f"sanitize_license_plate crashed with: {e}"

@given(st.text() | st.none())
def test_parse_trip_mileage_safe(s):
    # To-Do: Using try and except complete this function.
    try:
        parse_trip_mileage(s)
    except Exception as e:
        assert False, f"parse_trip_mileage crashed with: {e}"

@given(st.text() | st.none())
def test_format_rental_invoice_safe(s):
    # To-Do: Using try and except complete this function.
    try:
        format_rental_invoice(s)
    except Exception as e:
        assert False, f"format_rental_invoice crashed with: {e}"
