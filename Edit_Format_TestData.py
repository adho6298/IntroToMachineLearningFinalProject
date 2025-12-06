"""
This program formats the test data files for the NASA Turbofan Jet Engine Data Set.
It reads test data files and adds proper column headers (without RUL since that's in a separate file).

The RUL values for test data are stored separately in RUL_FD00x.csv files.
"""


import pandas as pd
import os

# Define column names for the dataset (same as training, but RUL will not be added)
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

# Process each test file
for i in range(1, 5):
    input_file = os.path.join(cmaps_dir, f'test_FD00{i}.csv')
    rul_file = os.path.join(cmaps_dir, f'RUL_FD00{i}.csv')
    output_file = os.path.join(script_dir, f'Test{i}.csv')
    
    print(f'Processing {input_file}...')
    
    # Read the test CSV file without headers (space-separated with multiple spaces)
    # Use sep='\s+' to handle multiple spaces between values
    df = pd.read_csv(input_file, sep=r'\s+', header=None, engine='python')
    
    # Remove any columns that are completely NaN (can happen with trailing spaces)
    df = df.dropna(axis=1, how='all')
    
    # Assign column names to the dataframe
    df.columns = column_names[:len(df.columns)]
    
    # Read the RUL values (one value per engine, representing the RUL at the last cycle)
    rul_values = pd.read_csv(rul_file, header=None, names=['RUL_at_last_cycle'])
    
    # Calculate RUL for each row in the test data
    rul_list = []
    
    # Group by engine number
    for engine_id in df['engine'].unique():
        # Get all rows for this engine
        engine_data = df[df['engine'] == engine_id]
        
        # Get the RUL value for this engine's last cycle (engine_id is 1-indexed in the file)
        rul_at_last = rul_values.iloc[int(engine_id) - 1]['RUL_at_last_cycle']
        
        # Count how many cycles this engine has in the test data
        num_cycles = len(engine_data)
        
        # Calculate RUL for each cycle: start from (rul_at_last + num_cycles - 1) and count down
        for idx, row in enumerate(engine_data.itertuples()):
            # RUL decreases as we go forward in time (from first cycle to last)
            rul = rul_at_last + (num_cycles - 1 - idx)
            rul_list.append(rul)
    
    # Add the RUL column to the dataframe
    df['RUL'] = rul_list
    
    # Save to the output file with proper comma separation for CSV
    df.to_csv(output_file, index=False)
    
    print(f'Created {output_file} with {len(df)} rows')
    print(f'  Engines in test set: {df["engine"].nunique()}')
    print()

print('All test files processed successfully!')
print('\nRUL values have been calculated and added to each test file using the RUL_FD00x.csv files.')
