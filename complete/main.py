import os
from sample_data import *
from read_data import *
from analyze_vehicle_eff import *
from find_eff_insights import *
from generate_report import *
from save_to_file import *

def main():
    
    print("🚗 Vehicle Fuel Efficiency Calculator")
    print("=" * 40)
    
    data_file = "vehicle_data.csv"
    
    if not os.path.exists(data_file):
        
        print("📝 Creating sample data file...")
        create_sample_data_file(data_file)
    
    print("📖 Loading vehicle data...")

    vehicle_records = read_vehicle_data(data_file)
   
    if not vehicle_records:
        print("❌ No data to analyze. Exiting.")
        return
    
    print("🔍 Analyzing fuel efficiency...")
    
    vehicle_stats = analyze_vehicle_efficiency(vehicle_records)
    
    print("💡 Generating insights...")
    
    insights = find_efficiency_insights(vehicle_stats)
    
    generate_report(vehicle_stats, insights)
    
    save_analysis_to_file(vehicle_stats, insights)
    
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main()