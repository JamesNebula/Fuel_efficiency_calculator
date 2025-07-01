from calc_fuel import *

# now its time to create the analyze_vehicle_efficiency(vehicle_records) function that takes a list: vehicle_records (from read_vehicle_data) as an arg. The function will return a dictionary called vehicle_stats which contains our analysis results.
def analyze_vehicle_efficiency(vehicle_records):
    # start with a condition that checks if there is even any records: if not vehicle_records: and return an empty dict 
    if not vehicle_records:
        return {}
    # Group data by vehicle
    # create a dict for vehicle stats ie vehicle_stats = {}
    vehicle_stats = {}
    #loop over each record in vehicle_records
    for record in vehicle_records:
        # get record['vehicle_id'] and set it to a variable called vehicle_id
        vehicle_id = record['vehicle_id']
        # calculate the fuel efficiency of the record by calling calculate_fuel_efficiency function and passing in record as an arg. set it to a variable named mpg
        mpg = calculate_fuel_efficiency(record)
        # setup a conditional that checks if vehicle_id is not in vehicle_stats
        if vehicle_id not in vehicle_stats:
            #set vehicle_stats[vehicle_id] to a dictionary that stores 'vehicle_type': record['vehicle_type], 'total_distance': 0, 'total_fuel': 0, 'trip_count': 0, 'mpg_readings': []
            vehicle_stats[vehicle_id] = {
                'vehicle_type': record['vehicle_type'],
                'total_distance': 0,
                'total_fuel': 0,
                'trip_count': 0,
                'mpg_readings': []
            }
        
        # Accumulate data for this vehicle
        # calculate distance by subtracting record['odometer_end'] - record['odometer_start'] and set it to a variable named distance
        distance = record['odometer_end'] - record['odometer_start']
        # calculate total distance by vehicle_stats[vehicle_id]['total_distance'] += distance
        vehicle_stats[vehicle_id]['total_distance'] += distance
        # calculate total fuel with vehicle_stats[vehicle_id]['total_fuel'] += record['fuel_added'] 
        vehicle_stats[vehicle_id]['total_fuel'] += record['fuel_added']
        #calculate trip count with vehicle_stats[vehicle_id]['trip_count'] += 1
        vehicle_stats[vehicle_id]['trip_count'] += 1
        # calculate mpg readings with vehicle_stats[vehicle_id]['mpg_readings'].append(mpg)
        vehicle_stats[vehicle_id]['mpg_readings'].append(mpg)
    
    # Calculate overall efficiency for each vehicle
    # start by looping over for vehicle_id, stats in vehicle_stats.items():
    for vehicle_id, stats in vehicle_stats.items():
        # create conditional to make sure there is fuel with if stats['total_fuel'] > 0: 
        if stats['total_fuel'] > 0:
            # set stats['overall_mpg'] to the sum of round(stats['total_distance'] / stats['total_fuel'], 2)
            stats['overall_mpg'] = round(stats['total_distance'] / stats['total_fuel'], 2)
            #set stats['average_mpg'] to the sum of round(sum(stats['mpg_readings']) / len(stats['mpg_readings']), 2)
            stats['average_mpg'] = round(sum(stats['mpg_readings']) / len(stats['mpg_readings']), 2)
        # create else condition    
        else:
            # in regards to our if statement if there IS actually no fuel we set stats['overall_mpg'] = 0 and stats['average_mpg'] = 0
            stats['overall_mpg'] = 0
            stats['average_mpg'] = 0
    # then we return our completed vehicle stats dictionary
    return vehicle_stats