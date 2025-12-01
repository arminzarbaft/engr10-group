import pandas as pd
import matplotlib.pyplot as plt
import data_mgmt

df = data_mgmt.df.copy().iloc[::20]
raw = data_mgmt.df.copy()

    
def time_plots(type):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(25, 25))
    
    fig.suptitle(f'Time Series Analysis for {type} Vechicle', fontsize=16)
    
    specified_df = df[df["VehicleType"] == type]
    
    time = specified_df['Time']
    
    parameters = ["Speed","Acceleration","EngineRPM","FuelConsumption","Distance"]
    
    fig.delaxes(axes[1, 2])
    
    for i in range(len(parameters)):
        
        param = specified_df[parameters[i]]

        all_axes = axes.flatten()
        
        ax = all_axes[i]
        
        ax.plot(time, param, linewidth=0.7)
        ax.set_ylabel(parameters[i])
        ax.set_xlabel("Time")
        ax.set_title(f'{parameters[i]}-Time Graph')
        
    plt.subplots_adjust(hspace=0.5)    
    return fig

def v_a_plot(type): 
    
    spdf = raw[raw["VehicleType"] == type]
    
    fig, ax = plt.subplots(figsize=(10, 8))
    speed_bins = 100 
    accel_bins = 100 
    
    density = ax.hist2d(
        spdf['Speed'], 
        spdf['Acceleration'],
        bins=[speed_bins, accel_bins], 
        cmap='magma', 

        cmin=1
    )

    cbar = fig.colorbar(density[3], ax=ax)
            
    ax.set_ylim(-6, 6) 
    ax.set_xlim(0, spdf['Speed'].max() * 1.05) 
    ax.axhline(0, color='white', linestyle='--', linewidth=0.8)

    ax.set_title(f'Acceleration-Speed Density Map ({type})')
    ax.set_xlabel('Speed ($\mathrm{m}/\mathrm{s}$)')
    ax.set_ylabel('Acceleration ($\mathrm{m}/\mathrm{s}^2$)')
    ax.legend()
    ax.grid(False)
    plt.tight_layout()
    
    return fig
    
def plot_fuel_efficiency_map(type):
    spdf = df[df["VehicleType"] == type].copy()
    spdf["Efficiency_metric"] = spdf["Distance"] / spdf["FuelConsumption"]
    
    fig, ax = plt.subplots()
    
    scatter = ax.scatter(spdf["Speed"], spdf["Efficiency_metric"], c=spdf["EngineRPM"], cmap='plasma', s=5, alpha=0.8)
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Engine RPM')
    
    ax.set_title(f'Fuel Efficiency Map (Efficiency vs. Speed) for {type}')
    ax.set_xlabel('Speed ($\mathrm{m}/\mathrm{s}$)')
    ax.set_ylabel('Efficiency Metric ($\mathrm{Distance}/\mathrm{Fuel}$)')  
    ax.grid(True, linestyle='--', alpha=0.6)

    return fig


