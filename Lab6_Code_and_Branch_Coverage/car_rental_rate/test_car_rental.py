import pytest
from car_rental_rate import process_rental_fleet, check_fleet_telematics

# Starter test case
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

# Complete 100% Code and Branch coverage test suite
def test_branch_validation():
    with pytest.raises(ValueError, match="Invalid rental list or admin fee"):
        process_rental_fleet("invalid_type", 10.0)

    with pytest.raises(ValueError, match="Invalid rental list or admin fee"):
        process_rental_fleet([], -1.0)

def test_branch_confirmation_and_days_filter():
    rentals = [
        {"is_confirmed": False, "vehicle_type": "economy", "days": 3},
        {"is_confirmed": True, "vehicle_type": "luxury", "days": 0},
        {"is_confirmed": True, "vehicle_type": "suv", "days": -2}
    ]
    result = process_rental_fleet(rentals, 15.0)
    assert result["total_revenue"] == 0.0
    assert result["status"] == "EMPTY_BATCH"

def test_branch_vehicle_type_economy_default():
    rentals = [
        {
            "is_confirmed": True,
            "days": 1
        }
    ]
    result = process_rental_fleet(rentals, 5.0)
    assert result["total_revenue"] == 45.0
    assert result["status"] == "STANDARD"

def test_branch_luxury_underage_and_long_trip():
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "luxury",
            "driver_age": 20,
            "days": 2,
            "trip_segments": [350, 50]
        }
    ]
    result = process_rental_fleet(rentals, 10.0)
    assert result["total_revenue"] == 600.0
    assert result["status"] == "STANDARD"

def test_branch_suv_young_driver_and_mileage_paths():
    rentals = [
        {
            "is_confirmed": True,
            "vehicle_type": "suv",
            "driver_age": 23,
            "days": 1,
            "trip_segments": [-50, 100, 400]
        }
    ]
    result = process_rental_fleet(rentals, 20.0)
    assert result["total_revenue"] == 290.0
    assert result["status"] == "STANDARD"

def test_branch_high_risk_audit():
    rentals = [
        {"is_confirmed": True, "days": -1},
        {"is_confirmed": True, "days": 0},
        {"is_confirmed": True, "days": 1, "trip_segments": [-1, -2, 500]}
    ]
    result = process_rental_fleet(rentals, 0.0)
    assert result["status"] == "HIGH_RISK_AUDIT"

def test_branch_telematics_all_conditions():
    assert check_fleet_telematics([]) == "NO_DATA"
    assert check_fleet_telematics([[120, 130]]) == "GROUND_VEHICLE"
    assert check_fleet_telematics([[110, 80, 110, 70]]) == "SAFE"
    assert check_fleet_telematics([[50, 60], [70, 80]]) == "SAFE"
