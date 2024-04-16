import pandas as pd

# Example DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['x', 'y', 'z', 'x', 'y'],
    'C': [10, 11, 12, 13, 14]
}
df = pd.DataFrame(data)

# Dictionary of values to match
values_to_match = {
    'A': [1, 2, 3],  # Only rows with A in [1, 2, 3]
    'B': ['x', 'y']  # and B in ['x', 'y'] will be selected
}

# Using .isin() and boolean indexing
mask = pd.concat([df[col].isin(values) for col, values in values_to_match.items()], axis=1).all(axis=1)
filtered_df = df[mask]

print(filtered_df)