# Lab 7: Fuzzing for Input Validation Bugs

## Overview
This repository contains the completed deliverables for **Lab 7: Fuzzing for Input Validation Bugs** using the **Hypothesis** property-based testing library in Python.

---

## Deliverables Summary

| Deliverable | Description | Location |
|---|---|---|
| **1. PDF Document with Screenshots** | Professional report containing all 4 required step screenshots, failure analysis, and hardening summary | [`Lab_7_Fuzzing_Report.pdf`](Lab_7_Fuzzing_Report.pdf) |
| **2. Fixed Application Python Script** | Hardened version of `processor.py` handling all null, malformed, and edge-case inputs defensively | [`processor.py`](processor.py) |
| **3. Updated Test Script** | Complete property-based fuzz tests using `@given(st.text() \| st.none())` and `try-except` | [`test_processor.py`](test_processor.py) |
| **Step Screenshots** | Individual terminal execution captures | [`screenshots/`](screenshots/) |

---

## Lab Execution Steps

### Step 1: Installing Dependencies
```bash
pip install hypothesis pytest
```

### Step 2: Run Buggy Application
Executed the original `processor.py` with standard inputs:
```bash
python processor.py
```
Output:
```text
==== Running sanitize_license_plate ====
Enter license plate with delimiters (-, _, #): KA-01-AB-1234
Sanitized Plate: KA01AB1234

==== Running parse_trip_mileage ====
Enter CSV of mileages (e.g. 100.5, 45.2, 80.0): 100.5, 45.2, 80.0
Parsed Mileage List: [100.5, 45.2, 80.0]

==== Running format_rental_invoice ====
Enter rental record (Driver:Days:Category): John:3:SUV
Rental Invoice: Driver John booked SUV for 3 days: Total $150.00
```
Screenshot: [`screenshots/step2_buggy_processor_output.png`](screenshots/step2_buggy_processor_output.png)

### Step 3: Complete Property-Based Fuzz Tests in `test_processor.py`
Implemented property-based fuzz tests verifying no crashes occur when functions receive arbitrary Unicode text or `None`:
```python
from hypothesis import given, strategies as st
from processor import sanitize_license_plate, parse_trip_mileage, format_rental_invoice

@given(st.text() | st.none())
def test_sanitize_license_plate_no_crash(s):
    try:
        sanitize_license_plate(s)
    except Exception as e:
        assert False, f"sanitize_license_plate crashed with: {e}"

@given(st.text() | st.none())
def test_parse_trip_mileage_safe(s):
    try:
        parse_trip_mileage(s)
    except Exception as e:
        assert False, f"parse_trip_mileage crashed with: {e}"

@given(st.text() | st.none())
def test_format_rental_invoice_safe(s):
    try:
        format_rental_invoice(s)
    except Exception as e:
        assert False, f"format_rental_invoice crashed with: {e}"
```

### Step 4: Run Fuzz Tests (Exposing Vulnerabilities)
```bash
pytest test_processor.py
```
**Bugs Discovered by Hypothesis:**
1. `sanitize_license_plate`: `AttributeError: 'NoneType' object has no attribute 'strip'` on `None`.
2. `parse_trip_mileage`: `AttributeError` on `None`, and `ValueError: could not convert string to float: ''` on empty / non-numeric tokens.
3. `format_rental_invoice`: `AttributeError` on `None`, `IndexError: list index out of range` on strings with fewer than 2 colons, and `ValueError` on non-integer day values.

Screenshot: [`screenshots/step4_test_cases_failing.png`](screenshots/step4_test_cases_failing.png)

### Step 5: Harden & Fix Buggy Application (`processor.py`)
Applied defensive programming principles:
- **Null & Type Guards:** Explicit checks `if s is None or not isinstance(s, str)` returning safe default values (`""`, `[]`, or descriptive error strings).
- **Delimiter & Token Validation:** Checks token count `len(parts) >= 3` before index access.
- **Safe Type Conversion:** Wrapped numeric parsing (`float`, `int`) in `try-except` blocks, safely discarding invalid tokens and verifying non-negative quantities.

Executed the fixed application:
```bash
python processor.py
```
Screenshot: [`screenshots/step5_fixed_processor_output.png`](screenshots/step5_fixed_processor_output.png)

### Step 6: Re-Run Fuzz Tests Against Hardened Code
```bash
pytest test_processor.py
```
Output:
```text
============================= test session starts =============================
platform win32 -- Python 3.13.9, pytest-9.2.0, pluggy-1.7.0
rootdir: K:\SE\L6_L7_02_car_rental_rate\Lab 7
plugins: anyio-4.13.0, hypothesis-6.170.15
collected 3 items

test_processor.py::test_sanitize_license_plate_no_crash PASSED           [ 33%]
test_processor.py::test_parse_trip_mileage_safe PASSED                   [ 66%]
test_processor.py::test_format_rental_invoice_safe PASSED                [100%]

============================== 3 passed in 3.48s ==============================
```
Screenshot: [`screenshots/step6_test_cases_passing.png`](screenshots/step6_test_cases_passing.png)

---

## Deliverables Files
All required deliverables are compiled in this directory:
- `Lab_7_Fuzzing_Report.pdf`
- `processor.py`
- `test_processor.py`
- `screenshots/`
