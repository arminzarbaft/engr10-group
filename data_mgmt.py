import pandas as pd

# Define the CSV file path
file_path = "sample_data/vehicle_dynamics_data_20251104.csv"

# Define the expected columns
columns = [
    "Time",
    "Speed",
    "Acceleration",
    "EngineRPM",
    "FuelConsumption",
    "Distance",
    "TestID",
    "VehicleType",
    "ProfileType"
]

# Read the CSV into a DataFrame
df = pd.read_csv(file_path, names=columns, header=0)  # header=0 if the CSV already has headers

# Display the first few rows
print(df.head().to_string(col_space=12, justify='left'))
