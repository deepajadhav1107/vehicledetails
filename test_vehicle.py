from vehicle import vehicle_info

def test_vehicle_info():
    expected_output = (
        "Vehicle Number: KA01AB1234\n"
        "Owner Name: Suraj\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2020"
    )
    result = vehicle_info("KA01AB1234", "Suraj", "Car", 2020)
    assert result == expected_output, f"Test failed: {result}"  # Added error message for debugging
