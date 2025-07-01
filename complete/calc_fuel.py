def calculate_fuel_efficiency(record):
   
    distance = record['odometer_end'] - record['odometer_start']
    
    if record['fuel_added'] == 0:
        return 0

    mpg = distance / record['fuel_added']

    return round(mpg, 2)