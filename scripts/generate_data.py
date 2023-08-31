import pandas as pd
import random

# Set a random seed for reproducibility
random.seed(42)

# Generate more random data
num_samples = 1000  # Number of samples to generate
data = []

for _ in range(num_samples):
    age = random.randint(18, 65)
    income = random.randint(20000, 100000)
    target = random.choice([0, 1])
    data.append([age, income, target])

# Create a DataFrame from the generated data
columns = ['age', 'income', 'target']
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to a CSV file
df.to_csv('./data/generated_data.csv', index=False)
