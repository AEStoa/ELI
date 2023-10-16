import sys
sys.stdout.flush()
import pandas as pd
file_path = 'FakeingredientC02e.csv'
df = pd.read_csv(file_path) #reads database file

user_input = input("Enter a category: ") #user input (recipe)

result = df[df['Category'] == user_input]['Value'].values

if len(result) > 0:
    print(f"The corresponding value for category '{user_input}' is: {result[0]}")
else:
    print(f"No matching category found for '{user_input}'")


#print (df)

