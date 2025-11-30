import pandas as pd
from analysis import *

# Define the CSV file path
file_path = "sample_data/vehicle_dynamics_data_20251104.csv"

# Define the expected columns
# columns = [
#     "Time",
#     "Speed",
#     "Acceleration",
#     "EngineRPM",
#     "FuelConsumption",
#     "Distance",
#     "TestID",
#     "VehicleType",
#     "ProfileType"
# ]

# Read the CSV into a DataFrame
df = pd.read_csv(file_path)  # header=0 if the CSV already has headers

# Run analyses
basic_stats = compute_basic_stats(df)
accel_stats = compute_acceleration_characteristics(df)
fuel_stats = compute_fuel_efficiency(df)
braking_stats = compute_braking_performance(df)
motion_stats = compute_motion_analysis(df)


# -----------------------------
# Pretty print functions
# -----------------------------



def print_acceleration_stats(stats):
    print("=== ACCELERATION CHARACTERISTICS ===")
    print(f"Max Acceleration: {stats['max_acceleration']:.2f} m/s²")
    print(f"Min Acceleration: {stats['min_acceleration']:.2f} m/s²")
    print(f"Mean Acceleration: {stats['mean_acceleration']:.2f} m/s²")
    print(f"Time Accelerating: {stats['time_spent_accelerating']} samples")
    print(f"Time Braking: {stats['time_spent_braking']} samples\n")


def print_fuel_stats(stats):
    print("=== FUEL EFFICIENCY ===")
    if stats['fuel_consumption_rate'] is not None:
        print(f"Fuel Consumption Rate: {stats['fuel_consumption_rate']:.2f} gallons/mile")
    else:
        print("Fuel Consumption Rate: N/A")
    print()


def print_braking_stats(stats):
    print("=== BRAKING PERFORMANCE ===")
    print(f"Number of Hard Brakes: {stats['num_hard_brakes']}")
    if 'max_braking_force' in stats:
        print(f"Max Braking Force: {stats['max_braking_force']:.2f} m/s²")
    print()


def print_motion_stats(stats):
    print("=== MOTION ANALYSIS ===")
    print(f"Max Speed: {stats['max_speed']:.2f} m/s")
    print(f"Mean Speed: {stats['mean_speed']:.2f} m/s")
    print(f"Estimated Distance: {stats['distance_estimate']:.2f} m")
    print()


# -----------------------------
# Print everything nicely
# -----------------------------
print("=== BASIC STATS ===") 
print(basic_stats)
print()
print_acceleration_stats(accel_stats)
print_fuel_stats(fuel_stats)
print_braking_stats(braking_stats)
print_motion_stats(motion_stats)
