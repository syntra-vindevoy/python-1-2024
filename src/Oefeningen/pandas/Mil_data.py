import pandas as pd


def main():
    # Load the CSV file
    mil_data = pd.read_csv("../../resources/SIPRI-Milex-data-1948-2023.csv", sep=",")

    mil_data_cleaned = mil_data.dropna()
    # Step 1: Drop rows where 'Country' is NaN or empty
    mil_data_cleaned = mil_data.dropna(subset=['Country'], how='any')

    # Step 2: Drop rows where ALL fields contain "..." (rows entirely filled with "...")
    mil_data_cleaned = mil_data_cleaned[~(mil_data_cleaned.eq("...").all(axis=1))]

    # Step 3: Optionally remove rows where ANY field contains "..." (if desired)
   # mil_data_cleaned = mil_data_cleaned[~(mil_data_cleaned.isin(["..."]).any(axis=1))]


    data=mil_data_cleaned[["Country", "2023"]]
    data.value_counts().plot(kind='pie', title='Milex exports by country 2023', autopct='%1.1f%%')

    # Optionally save the cleaned data to a new CSV file
    # mil_data_cleaned.to_csv("../../resources/cleaned_data.csv", index=False)


if __name__ == '__main__':
    main()
