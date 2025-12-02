def vehicle_info(vehicle_number, owner_name, vehicle_type, year_of_manufacture):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {year_of_manufacture}"
    )
    return result

def main():
    # Sample input values (you can modify these)
    vehicle_number = "KA09AB1234"
    owner_name = "John Doe"
    vehicle_type = "Sedan"
    year_of_manufacture = 2018
    
    # Call vehicle_info and print the result
    print(vehicle_info(vehicle_number, owner_name, vehicle_type, year_of_manufacture))

if __name__ == "__main__":
    main()
