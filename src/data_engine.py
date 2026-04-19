import pandas as pd
import numpy as np

def generate_poll_data():
    """Generates synthetic poll data for the project."""
    np.random.seed(42)
    rows = 1000
    regions = ['North America', 'Europe', 'Asia-Pacific', 'LATAM', 'Middle East']
    choices = ['Product A (Premium)', 'Product B (Budget)', 'Product C (Eco)', 'Undecided']
    age_groups = ['18-24', '25-34', '35-50', '50+']
    
    df = pd.DataFrame({
        'Respondent_ID': range(1, rows + 1),
        'Region': np.random.choice(regions, rows),
        'Vote': np.random.choice(choices, rows, p=[0.3, 0.4, 0.2, 0.1]),
        'Age_Group': np.random.choice(age_groups, rows),
        'Satisfaction': np.random.randint(1, 6, rows)
    })
    return df