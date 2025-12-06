"""
This program is part of the feature engineering pipeline. 
It reads training data files for the NASA Turbofan Jet Engine Data Set,
and reformats them by naming the columns, and by adding a column for 
remaining useful life (RUL) based on the cycle number of the engine,
and saves the modified data to new CSV files.

This is helpful because it will give us directly a target variable (RUL) for 
training machine learning models, instead of having to calculate it later 
during training. 
"""


import pandas as pd
import os

# Define column names for the dataset
column_names = [
    'engine',          # Engine No.
    'cycle',           # Time, In Cycles
    'op_set1',        # Operation Setting 1
    'op_set2',        # Operation Setting 2
    'op_set3',        # Operation Setting 3
    'Fan Inlet Temperature',         # Fan Inlet Temperature (◦R)
    'LPC Outlet Temperature',         # LPC Outlet Temperature (◦R)
    'HPC Outlet Temperature',         # HPC Outlet Temperature (◦R)
    'LPT Outlet Temperature',         # LPT Outlet Temperature (◦R)
    'Fan Inlet Pressure',         # Fan Inlet Pressure (psia)
    'Bypass-Duct Pressure',         # Bypass-Duct Pressure (psia)
    'HPC Outlet Pressure',         # HPC Outlet Pressure (psia)
    'Physical Fan Speed',         # Physical Fan Speed (rpm)
    'Physical Core Speed',         # Physical Core Speed (rpm)
    'Engine Pressure Ratio',        # Engine Pressure Ratio(P50/P2)
    'HPC Outlet Static Pressure',        # HPC Outlet Static Pressure (psia)
    'Ratio of Fuel Flow to Ps30',        # Ratio of Fuel Flow to Ps30 (pps/psia)
    'Corrected Fan Speed',        # Corrected Fan Speed (rpm)
    'Corrected Core Speed',        # Corrected Core Speed (rpm)
    'Bypass Ratio',        # Bypass Ratio
    'Burner Fuel-Air Ratio',        # Burner Fuel-Air Ratio
    'Bleed Enthalpy',        # Bleed Enthalpy
    'Required Fan Speed',        # Required Fan Speed
    'Required Fan Conversion Speed',        # Required Fan Conversion Speed
    'High-Pressure Turbines Cool Air Flow',        # High-Pressure Turbines Cool Air Flow
    'Low-Pressure Turbines Cool Air Flow'         # Low-Pressure Turbines Cool Air Flow
]

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
cmaps_dir = os.path.join(script_dir, 'CMaps')

# Process each training file
for i in range(1, 5):
    input_file = os.path.join(cmaps_dir, f'train_FD00{i}.csv')
    output_file = os.path.join(script_dir, f'Train{i}.csv')
    
    print(f'Processing {input_file}...')
    
    # Read the CSV file without headers (space-separated with multiple spaces)
    # Use sep='\s+' to handle multiple spaces between values
    df = pd.read_csv(input_file, sep=r'\s+', header=None, engine='python')
    
    # Remove any columns that are completely NaN (can happen with trailing spaces)
    df = df.dropna(axis=1, how='all')
    
    # Assign column names to the dataframe
    df.columns = column_names[:len(df.columns)]
    
    # Column 0 is engine number, column 1 is cycle number
    engine_col = 'engine'
    cycle_col = 'cycle'
    
    # Calculate remaining cycles for each engine
    remaining_cycles = []
    
    # Group by engine number
    for engine_id in df[engine_col].unique():
        # Get all rows for this engine
        engine_data = df[df[engine_col] == engine_id]
        
        # Get the maximum cycle number for this engine
        max_cycle = engine_data[cycle_col].max()
        
        # Calculate remaining cycles: max_cycle - current_cycle
        for idx, row in engine_data.iterrows():
            current_cycle = row[cycle_col]
            remaining = max_cycle - current_cycle
            remaining_cycles.append(remaining)
    
    # Add the remaining cycles column to the dataframe
    df['RUL'] = remaining_cycles
    
    # Save to the output file with proper comma separation for CSV
    df.to_csv(output_file, index=False)
    
    print(f'Created {output_file} with {len(df)} rows')
    print(f'  Engines processed: {df[engine_col].nunique()}')
    print()

print('All files processed successfully!')
