
def find_efficiency_insights(vehicle_stats):
    
    if not vehicle_stats:
        return {}
    
    vehicles_by_efficiency = sorted(
        vehicle_stats.items(),
        key=lambda x: x[1]['overall_mpg'],
        reverse=True
    )
    
    most_efficient = vehicles_by_efficiency[0]
    least_efficient = vehicles_by_efficiency[-1]
    
    type_stats = {}
    
    for vehicle_id, stats in vehicle_stats.items():
        
        vtype = stats['vehicle_type']
    
        if vtype not in type_stats:
            type_stats[vtype] = {'mpg_values': [], 'count': 0}
        
        type_stats[vtype]['mpg_values'].append(stats['overall_mpg'])
        type_stats[vtype]['count'] += 1
    
    for vtype, data in type_stats.items():
        data['average_mpg'] = round(sum(data['mpg_values']) / len(data['mpg_values']), 2)
    
    insights = {
        'most_efficient_vehicle': most_efficient,
        'least_efficient_vehicle': least_efficient,
        'vehicle_type_averages': type_stats,
        'total_vehicles_analyzed': len(vehicle_stats)
    }
    
    return insights