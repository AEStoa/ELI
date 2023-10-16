import sys
sys.stdout.flush()
import pandas as pd
file_path = 'FakeingredientC02e.csv'
df = pd.read_csv(file_path) #reads database file

user_category = input("Enter a category: ") #user input (recipe)
user_number = float(input("Enter a number: "))  # Convert input to float for numeric operations

# Find the corresponding value for the user category from the database
filtered_df = df[df['Category'] == user_category]

if not filtered_df.empty:
    database_value = filtered_df['Value'].iloc[0]  # Get the first matching value from the DataFrame
    result = database_value * user_number
    print(f"The calculated result for category '{user_category}' multiplied by {user_number} is: {result}")
else:
    print(f"No matching category found for '{user_category}'")


