from calc_fuel import *

def analyze_vehicle_efficiency(vehicle_records):
    
    if not vehicle_records:
        return {}
    
    vehicle_stats = {}
    
    for record in vehicle_records:
    
        vehicle_id = record['vehicle_id']
        
        mpg = calculate_fuel_efficiency(record)
        
        if vehicle_id not in vehicle_stats:
        
            vehicle_stats[vehicle_id] = {
                'vehicle_type': record['vehicle_type'],
                'total_distance': 0,
                'total_fuel': 0,
                'trip_count': 0,
                'mpg_readings': []
            }
        
        distance = record['odometer_end'] - record['odometer_start']
        vehicle_stats[vehicle_id]['total_distance'] += distance
        vehicle_stats[vehicle_id]['total_fuel'] += record['fuel_added']
        vehicle_stats[vehicle_id]['trip_count'] += 1
        vehicle_stats[vehicle_id]['mpg_readings'].append(mpg)
    
    for vehicle_id, stats in vehicle_stats.items():
        
        if stats['total_fuel'] > 0:
            stats['overall_mpg'] = round(stats['total_distance'] / stats['total_fuel'], 2)
            stats['average_mpg'] = round(sum(stats['mpg_readings']) / len(stats['mpg_readings']), 2)    
        else:
            stats['overall_mpg'] = 0
            stats['average_mpg'] = 0

    return vehicle_stats