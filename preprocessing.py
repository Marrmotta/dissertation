!pip install -U ipykernel 

import pandas as pd
import numpy as np

# Load the data csv and 'Raw' sheet, skipping the first two rows
raw_df = pd.read_csv(r'C:\Users\norst\Desktop\Diss_Data\Dissertation+Experiment+1A_November+12,+2023_01.24.csv')
#raw_df = pd.read_csv(r'C:\Users\norst\Desktop\Diss_Data\Dissertation+Experiment+1B_November+12,+2023_01.44.csv')
#raw_df = pd.read_csv(r'C:\Users\norst\Desktop\Diss_Data\Dissertation+Experiment+2A_November+12,+2023_01.53.csv')
#raw_df = pd.read_csv(r'C:\Users\norst\Desktop\Diss_Data\Dissertation+Experiment+2B_November+12,+2023_01.53.csv')

raw_df.head()

# Dropping the specified columns from the dataset
columns_to_drop = [
    "StartDate", "EndDate", "Status", "IPAddress", "Progress", "Duration (in seconds)", 
    "Finished", "RecordedDate", "ResponseId", "RecipientLastName", "RecipientFirstName",
    "RecipientEmail", "ExternalReference", "LocationLatitude", "LocationLongitude", "UserLanguage"]

# Ensuring that all specified columns are in the dataset
columns_to_drop = [col for col in columns_to_drop if col in raw_df.columns]

# Dropping the columns
data_cleaned = raw_df.drop(columns=columns_to_drop)

# Displaying the first few rows of the cleaned dataset
data_cleaned.head()
print(data_cleaned.dtypes)
