import csv
#Create a read_vehicle_data(filename) function that takes filename as a param. The function will read the vehicle data. It will also convert string numbers to actual numbers. It also handles any errors if issue with file.
def read_vehicle_data(filename):
    #create vehicle_records array
    vehicle_records = []
    # create a try except block
    try:
        # open filename as file eg with open(filename, 'r') as file:
        with open(filename, 'r') as file:
            # nstead of accessing data by numerical index (like row[0], row[1]), DictReader allows you to access data by column name (e.g., row['column_name']), we do this like: csv_reader = csv.DictReader(file)
            csv_reader = csv.DictReader(file)
            # loop over each row in csv_reader
            for row in csv_reader:
                # Convert string numbers to actual numbers. we do this with a dictionary called record and set the keys and values as needed. 
                record = {
                    'vehicle_id': row['Vehicle_ID'],
                    'date': row['Date'],
                    'odometer_start': int(row['Odometer_Start']),
                    'odometer_end': int(row['Odometer_End']),
                    'fuel_added': float(row['Fuel_Added']),
                    'vehicle_type': row['Vehicle_Type']
                }
                # append record dict to vehicle records array
                vehicle_records.append(record)
        # explain what just happened print(f"✅ Successfully loaded {len(vehicle_records)} vehicle records")       
        print(f"✅ Successfully loaded {len(vehicle_records)} vehicle records")
        # and return vehicle_records
        return vehicle_records
    # except FileNotFoundError:   
    except FileNotFoundError:
        # print filename not found ie print(f"❌ Error: File '{filename}' not found!") and return an empty array 
        print(f"❌ Error: File '{filename}' not found!")
        return []
    # except Exception as e for any other issues
    except Exception as e:
        # print print(f"❌ Error reading file: {e}") and return empty array
        print(f"❌ Error reading file: {e}")
        return []