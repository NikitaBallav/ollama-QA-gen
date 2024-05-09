import pandas as pd

# Load the original CSV file into a pandas DataFrame
df = pd.read_csv('combined.csv')

# Split the DataFrame into two separate DataFrames
df1 = df[['intent', 'Question']]
df2 = df[['intent', 'Answer']]

# Save the first DataFrame to a new CSV file
df1.to_csv('Question.csv', index=False)

# Save the second DataFrame to a new CSV file
df2.to_csv('Answer.csv', index=False)