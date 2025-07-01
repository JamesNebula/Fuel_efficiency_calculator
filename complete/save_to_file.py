from datetime import datetime

def save_analysis_to_file(vehicle_stats, insights, filename="fuel_analysis_report.txt"):
    
    try:
        with open(filename, 'w') as file:
            
            file.write("VEHICLE FUEL EFFICIENCY ANALYSIS REPORT\n")
            file.write("="*50 + "\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
   
            for vehicle_id, stats in vehicle_stats.items():
                
                file.write(f"Vehicle: {vehicle_id}\n")
                file.write(f"Type: {stats['vehicle_type']}\n")
                file.write(f"Overall MPG: {stats['overall_mpg']}\n")
                file.write(f"Total Distance: {stats['total_distance']} miles\n")
                file.write(f"Total Fuel: {stats['total_fuel']} gallons\n")
                file.write("-" * 30 + "\n")
            
            if insights:
            
                file.write(f"\nMost Efficient Vehicle: {insights['most_efficient_vehicle'][0]}\n")
                file.write(f"Least Efficient Vehicle: {insights['least_efficient_vehicle'][0]}\n")
                
        print(f"✅ Analysis saved to '{filename}'")
         
    except Exception as e:
        print(f"❌ Error saving file: {e}")