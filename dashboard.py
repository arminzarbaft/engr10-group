import streamlit as st
import data_mgmt 
import visualization as viz
import analysis

df = data_mgmt.df #gets the dataframe and data that was read in data_mgmt.py

st.set_page_config(
    layout='wide', 
    page_title="Vehicle Dynamics Dashboard" # Optional: Set a title for the browser tab
)

st.title("Vehicle Dynamics Data Dashboard")


vehicle = st.sidebar.selectbox(
    "Vehicle Type", df["VehicleType"].unique()
)

profile = st.sidebar.selectbox(
    "Profile Type", df["ProfileType"].unique()
)


st.dataframe(df)

filtered = df[
    (df["VehicleType"] == vehicle)
]

menus = ("Data", "Data Visualization", "Data Analysis")

menu = st.selectbox(
    "What do you want to see?", menus
)


if menu == menus[0]:
    st.subheader("Filtered Data")
    st.dataframe(filtered)

elif menu == menus[1]:
    plots = ('Time Series Plots', 'A-V Curve', 'Fuel Efficiency Map')
    plot = st.radio("What visualization do you want to see?", plots)
    
    if plot == plots[0]:
        tplot = viz.time_plots(vehicle)
        
        st.pyplot(tplot, width="content")
        
    elif plot == plots[1]:
        avplot = viz.v_a_plot(vehicle)
        
        st.pyplot(avplot, width="content")
        
    elif plot == plots[2]:
        fuelplot = viz.plot_fuel_efficiency_map(vehicle)
        
        st.pyplot(fuelplot)
    
elif menu == menus[2]:
        
    maxacc = analysis.compute_acceleration_characteristics(filtered)["max_acceleration"]
    minacc = analysis.compute_acceleration_characteristics(filtered)["min_acceleration"]
    meanacc = analysis.compute_acceleration_characteristics(filtered)["mean_acceleration"]
    
    maxrpm = analysis.compute_engine_rpm(filtered)["max_rpm"]
    meanrpm = analysis.compute_engine_rpm(filtered)["mean_rpm"]
    
    maxspeed = analysis.compute_motion_analysis(filtered)["max_speed"]
    
    total_dist = analysis.compute_fuel_efficiency(filtered)["total_distance"]
    
    efficiency = analysis.compute_fuel_efficiency(filtered)["fuel_consumption_rate"]
    
    max_decel = analysis.compute_braking_performance(filtered)["max_braking_force"]
    mean_decel = analysis.compute_braking_performance(filtered)["mean"]
    
    hard_brakes = analysis.compute_braking_performance(filtered)["count"]
    
    stats = analysis.compute_basic_stats(filtered)
    
    st.markdown(
        f"""
        
        # Performance Analysis
        
        This report summarizes the key performance indicators for the **{vehicle.capitalize()}** vehicle during the **{profile.capitalize()}** driving cycle.
        
        ---
        
        ## Motion and Acceleration Characteristics
        
        The analysis of the longitudinal dynamics reveals the vehicle's limits and typical operational range:
        
        - **Maximum Attainable Speed:** {maxspeed:.2f} $m/s$.
        - **Peak Acceleration Capacity:** {maxacc:.3f} $m/s^2$. This defines the upper bound of the performance envelope.
        - **Maximum Braking Capacity:** {abs(minacc):.3f} $m/s^2$. (This is the magnitude of the minimum, or most negative, acceleration).
        - **Mean Acceleration:** {meanacc:.3f} $m/s^2$. A near-zero value indicates the test cycle was approximately balanced between acceleration and deceleration phases.
        
        ## Engine Performance Profile
        
        The engine's operational data indicates how the vehicle was driven across the cycle:
        
        - **Maximum Engine Speed:** {maxrpm:.0f} $rpm$.
        - **Average Engine Speed:** {meanrpm:.0f} $rpm$.
        
        ## Fuel Efficiency Summary
        
        Overall efficiency metrics provide a direct comparison against the vehicle's fuel consumption:
        
        - **Total Distance Traveled:** {total_dist:.0f} $m$.
        - **Overall Efficiency Metric:** {efficiency:.3f} **$m/ml$** (Distance per unit Fuel Consumed). This metric serves as a key performance indicator (KPI) for comparing the three different vehicle types and driving profiles.
        
        ## Braking Performance Summary
        
        This section quantifies the braking capabilities and driver behavior during the test cycle based on the vehicle's deceleration profile.
        
        ---

        ### Key Deceleration Metrics

        | Metric | Value | Interpretation |
        | :--- | :--- | :--- |
        | **Maximum Deceleration** | {abs(max_decel):.3f} $m/s^2$ | This is the maximum braking force exerted by the vehicle during the test. A higher value indicates superior braking capacity. |
        | **Average Deceleration** | {abs(mean_decel):.3f} $m/s^2$ | The average deceleration experienced during all periods where the vehicle was slowing down. This reflects the typical braking intensity of the driving profile. |

        ### Hard Braking Events

        - **Total Hard Braking Events:** **{hard_brakes}** time steps.
        
        This metric counts the number of data points where deceleration exceeded **3.0 $m/s^2$**. A high count suggests aggressive driving or unexpected obstacles in the test profile.
        
        ### Basic Statistics:
        
        | Parameter | Mean | Standard Deviation |
        | :--- | :--- | :--- |
        | **Speed** | {stats["mean"]["Speed"]:.3f}$ m/s$ |   {stats["std"]["Speed"]:.3f} $ m/s$
        | **Acceleration** |  {stats["mean"]["Acceleration"]:.3f} $ m/s^2$  | {stats["std"]["Acceleration"]:.3f} $ m/s^2$ |
        | **EngineRPM** | {stats["mean"]["EngineRPM"]:.0f} $ rpm$  | {stats["std"]["EngineRPM"]:.0f} $ rpm$ | 
        | **Fuel Consumption** | {stats["mean"]["FuelConsumption"]:.3f} $ m/ml$ | {stats["std"]["FuelConsumption"]:.3f} $ m/ml$ |
        
            
        """
    )
    
    