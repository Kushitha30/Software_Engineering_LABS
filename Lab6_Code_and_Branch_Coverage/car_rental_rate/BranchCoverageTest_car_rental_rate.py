import pytest
from car_rental_rate import process_rental_fleet, check_fleet_telematics


# ============================================================================
# Branch Coverage Suite for car_rental_rate.py
# Achieves 100% Branch Coverage by systematically evaluating every decision
# outcome (True / False / elif branches) across all functions.
# ============================================================================

def test_branch_validation():
    """Branch: rentals not list (True) vs base_admin_fee < 0 (True)."""
    with pytest.raises(ValueError, match="Invalid rental list or admin fee"):
        process_rental_fleet("invalid_type", 10.0)

    with pytest.raises(ValueError, match="Invalid rental list or admin fee"):
        process_rental_fleet([], -1.0)


def test_branch_confirmation_and_days_filter():
    """Branch: is_confirmed (False -> continue, True -> proceed).
       Branch: days <= 0 (True -> risk_flags++ & continue, False -> proceed).
       Branch: total_revenue == 0.0 (True -> EMPTY_BATCH)."""
    rentals = [
        {"is_confirmed": False, "vehicle_type": "economy", "days": 3},
        {"is_confirmed": True, "vehicle_type": "luxury", "days": 0},
        {"is_confirmed": True, "vehicle_type": "suv", "days": -2}
    ]
    result = process_rental_fleet(rentals, 15.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "EMPTY_BATCH"


def test_branch_vehicle_type_economy_default():
    """Branch: vehicle_type == 'luxury' (False), == 'suv' (False) -> else 40.0.
       Branch: driver_age < 25 (False).
       Branch: trip_segments empty."""
    rentals = [
        {
            "is_confirmed": True,
            # vehicle_type omitted -> default 'economy'
            # driver_age omitted -> default 25
            "days": 1
        }
    ]
    result = process_rental_fleet(rentals, 5.0)
    assert result["total_revenue"] == 45.0
    assert result["status"] == "STANDARD"


def test_branch_luxury_underage_and_long_trip():
    """Branch: vehicle_type == 'luxury' (True -> 120.0).
       Branch: driver_age < 25 (True) with luxury (50 * days).
       Branch: miles > 300 (True) with driver_age < 21 (True -> break)."""
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "luxury",
            "driver_age": 20,
            "days": 2,
            "trip_segments": [350, 50]  # Breaks after 350
        }
    ]
    # (120 * 2) + 10 + 250 + (50 * 2) = 240 + 10 + 250 + 100 = 600.0
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 600.0
    assert result["status"] == "STANDARD"


def test_branch_suv_young_driver_and_mileage_paths():
    """Branch: vehicle_type == 'suv' (True -> 70.0).
       Branch: driver_age < 25 (True) with non-luxury (20 * days).
       Branch: miles < 0 (True -> risk_flags++ & continue).
       Branch: miles <= 300 (True -> miles * 0.20).
       Branch: miles > 300 with driver_age >= 21 (True -> miles * 0.40)."""
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "suv",
            "driver_age": 23,
            "days": 1,
            "trip_segments": [-50, 100, 400]
        }
    ]
    # (70 * 1) + 20 + (100 * 0.20 = 20) + (400 * 0.40 = 160) + (20 * 1) = 290.0
    result = process_rental_fleet(rentals, 20.0)
    assert result["total_revenue"] == 290.0
    assert result["status"] == "STANDARD"


def test_branch_high_risk_audit():
    """Branch: risk_flags > 4 (True -> HIGH_RISK_AUDIT)."""
    rentals = [
        {"is_confirmed": True, "days": -1},  # +1
        {"is_confirmed": True, "days": 0},   # +1
        {"is_confirmed": True, "days": 1, "trip_segments": [-1, -2, 500]}  # +1, +1, +1 => 5
    ]
    result = process_rental_fleet(rentals, 0.0)
    assert result["status"] == "HIGH_RISK_AUDIT"


def test_branch_telematics_all_conditions():
    """Branch: telematics_matrix falsy (True -> NO_DATA).
       Branch: speed > 100 (True), streak >= 2 (True -> GROUND_VEHICLE).
       Branch: speed <= 100 (True -> reset streak = 0).
       Branch: loop completes without consecutive violations -> SAFE."""
    assert check_fleet_telematics([]) == "NO_DATA"
    assert check_fleet_telematics([[120, 130]]) == "GROUND_VEHICLE"
    assert check_fleet_telematics([[110, 80, 110, 70]]) == "SAFE"
    assert check_fleet_telematics([[50, 60], [70, 80]]) == "SAFE"
