import pytest
from car_rental_rate import process_rental_fleet, check_fleet_telematics


# ==========================================
# Initial Starter Test
# ==========================================
def test_single_economy_rental():
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "economy",
            "driver_age": 30,
            "days": 2,
            "trip_segments": [100]
        }
    ]
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 110.0
    assert result["status"] == "STANDARD"


# ==========================================
# Input Validation & Exceptions
# ==========================================
def test_invalid_rentals_input():
    with pytest.raises(ValueError, match="Invalid rental list or admin fee"):
        process_rental_fleet("not-a-list", 10.0)

    with pytest.raises(ValueError, match="Invalid rental list or admin fee"):
        process_rental_fleet([], -5.0)


# ==========================================
# Confirmation & Skipping
# ==========================================
def test_unconfirmed_and_invalid_days_rental():
    rentals = [
        {
            "is_confirmed": False,
            "vehicle_type": "economy",
            "driver_age": 30,
            "days": 3
        },
        {
            "is_confirmed": True,
            "vehicle_type": "economy",
            "driver_age": 30,
            "days": 0  # days <= 0 increments risk_flags and skips
        }
    ]
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "EMPTY_BATCH"


# ==========================================
# Vehicle Types & Young Driver Surcharges
# ==========================================
def test_luxury_young_driver():
    # Luxury daily rate: 120.0, driver_age < 25 adds 50.0 * days
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "luxury",
            "driver_age": 22,
            "days": 2,
            "trip_segments": [50]  # <= 300: 50 * 0.20 = 10.0
        }
    ]
    # Contract = (120 * 2) + 15 + 10 + (50 * 2) = 240 + 15 + 10 + 100 = 365.0
    result = process_rental_fleet(rentals, 15.0)
    assert result["total_revenue"] == 365.0
    assert result["status"] == "STANDARD"


def test_suv_young_driver():
    # SUV daily rate: 70.0, driver_age < 25 (non-luxury) adds 20.0 * days
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "suv",
            "driver_age": 24,
            "days": 1,
            "trip_segments": []
        }
    ]
    # Contract = (70 * 1) + 10 + 0 + (20 * 1) = 100.0
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 100.0
    assert result["status"] == "STANDARD"


# ==========================================
# Trip Segments & Risk Rules
# ==========================================
def test_trip_segments_negative_and_long_trips():
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "economy",
            "driver_age": 28,  # >= 21 and >= 25
            "days": 1,
            "trip_segments": [-10, 400]  # -10 continues, 400 > 300 adds miles * 0.40
        }
    ]
    # Contract = (40 * 1) + 5 + (400 * 0.40 = 160) = 205.0
    result = process_rental_fleet(rentals, 5.0)
    assert result["total_revenue"] == 205.0
    assert result["status"] == "STANDARD"


def test_underage_driver_long_trip_break():
    # driver_age < 21 with segment > 300 triggers penalty 250.0 and break
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "economy",
            "driver_age": 19,
            "days": 1,
            "trip_segments": [350, 100]  # second segment never reached due to break
        }
    ]
    # Contract = (40 * 1) + 10 + 250 + (20 * 1) = 320.0
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 320.0
    assert result["status"] == "STANDARD"


def test_high_risk_audit_status():
    # Need risk_flags > 4
    rentals = [
        {"is_confirmed": True, "vehicle_type": "economy", "days": -1},  # risk +1
        {"is_confirmed": True, "vehicle_type": "economy", "days": 0},   # risk +1
        {
            "is_confirmed": True,
            "vehicle_type": "economy",
            "days": 1,
            "driver_age": 30,
            "trip_segments": [-5, -10, 400]  # risk +1, risk +1, risk +1 => total 5
        }
    ]
    result = process_rental_fleet(rentals, 10.0)
    assert result["status"] == "HIGH_RISK_AUDIT"


# ==========================================
# Fleet Telematics Tests
# ==========================================
def test_fleet_telematics():
    # Empty / falsy matrix
    assert check_fleet_telematics([]) == "NO_DATA"
    assert check_fleet_telematics(None) == "NO_DATA"

    # Consecutive speeding >= 2
    assert check_fleet_telematics([[80, 105, 110]]) == "GROUND_VEHICLE"

    # Reset streak on normal speed
    assert check_fleet_telematics([[120, 90, 110]]) == "SAFE"

    # All safe speeds
    assert check_fleet_telematics([[60, 70, 80], [90, 85]]) == "SAFE"
