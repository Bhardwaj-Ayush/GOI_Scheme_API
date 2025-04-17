import pandas as pd

# Load the cleaned dataset
schemes_df = pd.read_csv("./Cleaned_GOI_Schemes.csv")

def recommend_schemes(user):
    age = user.get("age")
    gender = user.get("gender", "All")
    caste = user.get("caste", "All").upper()
    income = user.get("income", 0)
    occupation = user.get("occupation", "").strip().title()

    def is_eligible(row):
        if pd.notna(row['min_age']) and age < row['min_age']:
            return False
        if pd.notna(row['max_age']) and age > row['max_age']:
            return False

        if row['cleaned_gender'] != "All" and row['cleaned_gender'] != gender:
            return False

        caste_values = [c.strip().upper() for c in str(row['cleaned_caste']).split(',')]
        if caste not in caste_values and "ALL" not in caste_values:
            return False

        if income > row['cleaned_income']:
            return False

        if row['cleaned_occupation'] and occupation.lower() != row['cleaned_occupation'].lower():
            return False

        return True

    eligible_schemes = schemes_df[schemes_df.apply(is_eligible, axis=1)]
    return eligible_schemes['scheme_name'].dropna().unique().tolist()
