import pandas as pd
import glob2

# create an empty list to store dataframes
dfs = []

# find all csv files in the current directory
for csv_file in glob2.glob('*.csv'):
    # read each csv file into a dataframe and append it to the list
    dfs.append(pd.read_csv(csv_file))

# concatenate all dataframes into one
combined_df = pd.concat(dfs)

# save the combined dataframe to a new csv file
combined_df.to_csv('combined.csv', index=False)