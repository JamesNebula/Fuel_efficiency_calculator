from datetime import datetime
# lastly we need to save all our work to a file. We do this by creating a save_analysis_to_file function that takes our vehicle_stats dictionary from analyze_fuel_efficiency function, our insights dict from find_efficiency_insights function and a filename="fuel_analysis_report.txt" which is our filename from create_sample_data_file function
def save_analysis_to_file(vehicle_stats, insights, filename="fuel_analysis_report.txt"):
    # first we try:
    try:
        # we open our file and store it as a variable named file ie with open(filename, 'w') as file:
        with open(filename, 'w') as file:
            # we make it look nice with 
            file.write("VEHICLE FUEL EFFICIENCY ANALYSIS REPORT\n")
            file.write("="*50 + "\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # we then need to Write individual vehicle stats
            # start by looping over vehicle_id, stats in vehicle_stats.items()
            for vehicle_id, stats in vehicle_stats.items():
                # we write in our information like so:
                file.write(f"Vehicle: {vehicle_id}\n")
                file.write(f"Type: {stats['vehicle_type']}\n")
                file.write(f"Overall MPG: {stats['overall_mpg']}\n")
                file.write(f"Total Distance: {stats['total_distance']} miles\n")
                file.write(f"Total Fuel: {stats['total_fuel']} gallons\n")
                file.write("-" * 30 + "\n")
            
            # Write insights
            # check if there even is any insights ie if insights:
            if insights:
                # then plug in our insights 
                file.write(f"\nMost Efficient Vehicle: {insights['most_efficient_vehicle'][0]}\n")
                file.write(f"Least Efficient Vehicle: {insights['least_efficient_vehicle'][0]}\n")
                
        # show that our analysis has been saved 
        print(f"✅ Analysis saved to '{filename}'")
        
    # then finish our try: except block with except Exception as e:    
    except Exception as e:
        print(f"❌ Error saving file: {e}")