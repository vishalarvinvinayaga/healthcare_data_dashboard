import pandas as pd
import numpy as np
import random

# Simulate synthetic data
num_records = 1000
np.random.seed(42)

user_ids = np.random.randint(1000, 1050, num_records)
access_times = pd.date_range('2024-01-01', periods=num_records, freq='H')
actions = np.random.choice(['Access', 'Breach'], size=num_records, p=[0.95, 0.05])
sensitivity_levels = np.random.choice(['Low', 'Medium', 'High'], size=num_records)
locations = np.random.choice(['USA', 'Europe', 'Asia'], size=num_records)

# Create a DataFrame
data = pd.DataFrame({
    'User ID': user_ids,
    'Access Time': access_times,
    'Action Type': actions,
    'Data Sensitivity': sensitivity_levels,
    'Location': locations
})

# Save the generated data to a CSV file in the /data directory
data.to_csv('data/simulated_data.csv', index=False)
print("Synthetic data generated and saved to data/simulated_data.csv")
