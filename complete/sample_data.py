import csv

# Sample data - ideally, this would come from vehicle sensors, fuel cards or manually inputted.

SAMPLE_DATA = [
    ["Vehicle_ID", "Date", "Odometer_Start", "Odometer_End", "Fuel_Added", "Vehicle_Type"],
    ["TRUCK001", "2024-01-15", "45230", "45580", "85.5", "Delivery Truck"],
    ["VAN002", "2024-01-15", "23450", "23720", "42.3", "Service Van"],
    ["TRUCK001", "2024-01-16", "45580", "45920", "78.9", "Delivery Truck"],
    ["CAR003", "2024-01-16", "67890", "68145", "28.4", "Company Car"],
    ["VAN002", "2024-01-17", "23720", "24050", "48.2", "Service Van"],
    ["TRUCK001", "2024-01-17", "45920", "46280", "82.1", "Delivery Truck"],
]

# create sample data file function, takes a filename="vehicle_data.csv" as param, the function will create a csv file with vehicle data. 
def create_sample_data_file(filename="vehicle_data.csv"):
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(SAMPLE_DATA)
    
    print(f"✅ Sample data file '{filename}' created successfully!")