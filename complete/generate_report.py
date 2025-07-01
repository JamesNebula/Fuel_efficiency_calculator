def generate_report(vehicle_stats, insights):
    
    print("\n" + "="*60)
    print("🚗 VEHICLE FUEL EFFICIENCY ANALYSIS REPORT")
    print("="*60)
    
    print("\n📊 INDIVIDUAL VEHICLE PERFORMANCE:")
    print("-" * 50)
    
    for vehicle_id, stats in vehicle_stats.items():
        
        print(f"\n🚙 {vehicle_id} ({stats['vehicle_type']})")
        print(f"   Overall MPG: {stats['overall_mpg']} mpg")
        print(f"   Average MPG: {stats['average_mpg']} mpg")
        print(f"   Total Distance: {stats['total_distance']} miles")
        print(f"   Total Fuel: {stats['total_fuel']} gallons")
        print(f"   Number of Trips: {stats['trip_count']}")
    
    if insights:
        
        print("\n🎯 KEY INSIGHTS:")
        print("-" * 50)
        
        most_eff = insights['most_efficient_vehicle']
        least_eff = insights['most_efficient_vehicle']
        
        print(f"🏆 Most Efficient: {most_eff[0]} ({most_eff[1]['overall_mpg']} mpg)")
        print(f"⚠️  Least Efficient: {least_eff[0]} ({least_eff[1]['overall_mpg']} mpg)")
        
        efficiency_difference = most_eff[1]['overall_mpg'] - least_eff[1]['overall_mpg']
        
        print(f"📈 Efficiency Gap: {efficiency_difference} mpg")
        
        print(f"\n🚗 VEHICLE TYPE ANALYSIS:")
        
        for vtype, data in insights['vehicle_type_averages'].items():
            print(f"   {vtype}: {data['average_mpg']} mpg (avg)")
    
    
    print("\n💡 RECOMMENDATIONS:")
    print("-" * 50)
    
    if insights: 
        least_eff = insights['least_efficient_vehicle']
        if least_eff[1]['overall_mpg'] < 10:
            print(f"🔧 {least_eff[0]} needs immediate maintenance check")

        efficiency_gap = most_eff[1]['overall_mpg'] - least_eff[1]['overall_mpg']
        
        if efficiency_gap > 5:
            print("📚 Consider driver training for fuel-efficient driving")
            print("🔍 Investigate maintenance schedules for underperforming vehicles")
            
    print("\n" + "="*60)