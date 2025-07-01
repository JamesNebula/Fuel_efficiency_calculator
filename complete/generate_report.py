# Now we generate our report which starts with creating a generate_report() function that takes a vehicle_stats dictionary from our analyze_fuel_efficiency function and insights dictionary from our find_efficicncy insights function.
# This function will generate a formatted report of our analysis
def generate_report(vehicle_stats, insights):
    # first we print the below as a nice way to present our report in the terminal.
    print("\n" + "="*60)
    print("🚗 VEHICLE FUEL EFFICIENCY ANALYSIS REPORT")
    print("="*60)
    
    # We then display the Individual vehicle performance findings
    print("\n📊 INDIVIDUAL VEHICLE PERFORMANCE:")
    print("-" * 50)
    # here we loop over vehicle_id, stats in vehicle_stats.items()
    for vehicle_id, stats in vehicle_stats.items():
        # and print out all of our results as below
        print(f"\n🚙 {vehicle_id} ({stats['vehicle_type']})")
        print(f"   Overall MPG: {stats['overall_mpg']} mpg")
        print(f"   Average MPG: {stats['average_mpg']} mpg")
        print(f"   Total Distance: {stats['total_distance']} miles")
        print(f"   Total Fuel: {stats['total_fuel']} gallons")
        print(f"   Number of Trips: {stats['trip_count']}")
    
    # This is where we display our Efficiency insights 
    # we check if insights:
    if insights:
        # then print the below as a nice way to present in the terminal
        print("\n🎯 KEY INSIGHTS:")
        print("-" * 50)
        # firstly we find our most_eff and least_eff with most_eff = insights['most_efficient_vehicle']. we are just accessing our value from key 'most_efficient_vehicle' in the insights dictionary do the same for least_eff. least_eff = insights['least_efficient_vehicle']
        most_eff = insights['most_efficient_vehicle']
        least_eff = insights['most_efficient_vehicle']
        # show the results by printing out nicely as below.
        print(f"🏆 Most Efficient: {most_eff[0]} ({most_eff[1]['overall_mpg']} mpg)")
        print(f"⚠️  Least Efficient: {least_eff[0]} ({least_eff[1]['overall_mpg']} mpg)")
        
        # find the efficiency difference with the sum of most_eff[1]['overall_mpg'] - least_eff[1]['overall_mpg'] and store it in a variable called efficiency_difference
        efficiency_difference = most_eff[1]['overall_mpg'] - least_eff[1]['overall_mpg']
        # show the efficieny difference in the terminal like so: print(f"📈 Efficiency Gap: {efficiency_difference} mpg")
        print(f"📈 Efficiency Gap: {efficiency_difference} mpg")
        
        # Vehicle type analysis
        # show what we are doing with this print statement: print(f"\n🚗 VEHICLE TYPE ANALYSIS:")
        print(f"\n🚗 VEHICLE TYPE ANALYSIS:")
        # then loop over vtype, data in insights['vehicle_type_averages'].items():
        for vtype, data in insights['vehicle_type_averages'].items():
            # and print(f"   {vtype}: {data['average_mpg']} mpg (avg)") 
            print(f"   {vtype}: {data['average_mpg']} mpg (avg)")
    
    # We then show our Recommendations to our company, employer, customer
    print("\n💡 RECOMMENDATIONS:")
    print("-" * 50)
    # again check if there even is any insights: if insights:
    if insights:
        # get the insights['least_efficient_vehicle'] and store it in a least_eff variable 
        least_eff = insights['least_efficient_vehicle']
        # We then check the least efficient vehicle and assume its due for maintenance
        # check if least_eff[1]['overall_mpg'] < 10:
        if least_eff[1]['overall_mpg'] < 10:
            # then print(f"🔧 {least_eff[0]} needs immediate maintenance check")
            print(f"🔧 {least_eff[0]} needs immediate maintenance check")
            
        # we then get the sum of most_eff[1]['overall_mpg'] - least_eff[1]['overall_mpg'] to find the efficiency gap and store it in a variable named efficiency_gap
        efficiency_gap = most_eff[1]['overall_mpg'] - least_eff[1]['overall_mpg']
        # if the efficiency gap is greater than 5: if efficiency_gap > 5:
        if efficiency_gap > 5:
            print("📚 Consider driver training for fuel-efficient driving")
            print("🔍 Investigate maintenance schedules for underperforming vehicles")
            
    # then print("\n" + "="*60) to show the end of report
    print("\n" + "="*60)