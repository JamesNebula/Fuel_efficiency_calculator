import os
from sample_data import *
from read_data import *
from analyze_vehicle_eff import *
from find_eff_insights import *
from generate_report import *
from save_to_file import *

def main():
    # print something to show the start of the program ie print("🚗 Vehicle Fuel Efficiency Calculator")
    print("🚗 Vehicle Fuel Efficiency Calculator")
    print("=" * 40)
    
    # Step 1: Setup data file ie data_file = "vehicle_data.csv"
    data_file = "vehicle_data.csv"
    
    # Create sample data if file doesn't exist ie if not os.path.exists(data_file):
    if not os.path.exists(data_file):
        # explain what you are doing ie print("📝 Creating sample data file...")
        print("📝 Creating sample data file...")
        # call create_sample_data_file function and pass in data_file
        create_sample_data_file(data_file)
    
    # Step 2: Load data
    # Explain what you are doing i.e print("📖 Loading vehicle data...")
    print("📖 Loading vehicle data...")
    # call read_vehicle_data function with data_file as arg and set it to a variable called vehicle_records
    vehicle_records = read_vehicle_data(data_file)
    # If there are no vehicle records(if not vehicle_records). print("❌ No data to analyze. Exiting.") and return 
    if not vehicle_records:
        print("❌ No data to analyze. Exiting.")
        return
    
    # Step 3: Analyze data
    # explain what you are doing ie print("🔍 Analyzing fuel efficiency...")
    print("🔍 Analyzing fuel efficiency...")
    # call function analyze_fuel_efficiency(vehicle_records) and set it to a variabe named vehicle_stats
    vehicle_stats = analyze_vehicle_efficiency(vehicle_records)
    
    # Step 4: Generate insights
    # Explain what you are doing ie print("💡 Generating insights...")
    print("💡 Generating insights...")
    # call find_efficiency_insights(vehicle_stats) function and set it to a variable named insights. We are storing the result of finding the efficiency insights into this variable.
    insights = find_efficiency_insights(vehicle_stats)
    
    # Step 5: Display results
    # call generate_report(vehicle_stats, insights) function. no need to store this in a variable as it just displays our results
    generate_report(vehicle_stats, insights)
    
    # Step 6: Save results
    # save our results to a file by calling save_analysis_to_file(vehicle_stats, insights) function
    save_analysis_to_file(vehicle_stats, insights)
    # show the analysis is complete with print("\n✅ Analysis complete!")
    print("\n✅ Analysis complete!")

# This is a Python idiom that prevents code from running when the file is imported
if __name__ == "__main__":
    main()