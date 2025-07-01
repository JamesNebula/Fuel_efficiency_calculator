import csv

def read_vehicle_data(filename):

    vehicle_records = []
    
    try:
        with open(filename, 'r') as file:
            
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
            
                record = {
                    'vehicle_id': row['Vehicle_ID'],
                    'date': row['Date'],
                    'odometer_start': int(row['Odometer_Start']),
                    'odometer_end': int(row['Odometer_End']),
                    'fuel_added': float(row['Fuel_Added']),
                    'vehicle_type': row['Vehicle_Type']
                }
                
                vehicle_records.append(record)
           
        print(f"✅ Successfully loaded {len(vehicle_records)} vehicle records")
        
        return vehicle_records
     
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found!")
        return []
    
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []