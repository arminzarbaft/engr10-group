import pandas as pd
import numpy as np

# -----------------------------
# Basic statistics
# -----------------------------
def compute_basic_stats(df: pd.DataFrame):
    
    stats = df.describe().T  # mean, std, min, max, etc.
    return stats


# -----------------------------
# Acceleration characteristics
# -----------------------------
def compute_acceleration_characteristics(df: pd.DataFrame):
    
    
    result = {}

    if "Acceleration" in df.columns:
        acc = df["Acceleration"]

        result["max_acceleration"] = acc.max()
        result["min_acceleration"] = acc.min()
        result["mean_acceleration"] = acc.mean()
        result["time_spent_accelerating"] = (acc > 0).sum()
        result["time_spent_braking"] = (acc < 0).sum()

    return result

def compute_engine_rpm(df: pd.DataFrame):
    
    result = {}
    
    rpm = df["EngineRPM"]
    
    result["max_rpm"] = rpm.max()
    result["min_rpm"] = rpm.min()
    result["mean_rpm"] = rpm.mean()
    
    return result

# -----------------------------
# Fuel Efficiency
# -----------------------------
def compute_fuel_efficiency(df: pd.DataFrame):
    result = {}

    if "FuelConsumption" in df.columns and "Distance" in df.columns:

        total_fuel = df["FuelConsumption"].sum()
        total_distance = df["Distance"].iloc[-1] - df["Distance"].iloc[0]
        
        result["total_distance"] = total_distance

        if total_fuel > 0:
            result["fuel_consumption_rate"] = total_distance / total_fuel
        else:
            result["fuel_consumption_rate"] = None
            
        

    return result


# -----------------------------
# Braking performance
# -----------------------------
def compute_braking_performance(df: pd.DataFrame):

    
    result = {}

    if "Acceleration" in df.columns and "Speed" in df.columns:
        braking_events = df[df["Acceleration"] < -3.0]  # threshold
        result["num_hard_brakes"] = len(braking_events)

        if not braking_events.empty:
            result["max_braking_force"] = braking_events["Acceleration"].min()
            result["mean"] = braking_events["Acceleration"].mean()
            
            result["count"] = braking_events["Acceleration"].count()

    return result


# -----------------------------
# Basic motion analysis
# -----------------------------
def compute_motion_analysis(df: pd.DataFrame):
    
    result = {}

    if "Speed" in df.columns:
        speed = df["Speed"]
        time = df["Time"]
        result["max_speed"] = speed.max()
        result["mean_speed"] = speed.mean()
        result["distance_estimate"] = np.trapz(speed, x=time)  # integration

    return result
