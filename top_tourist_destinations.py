#top_tourist_destinations

import pandas as pd

# Data on top tourist destinations (estimated number of international tourists per year)
data = {
    'Country': ['France', 'Spain', 'United States', 'China', 'Italy', 'Turkey', 'Mexico', 'Thailand', 'Germany', 'United Kingdom'],
    'Tourists (Millions)': [89.4, 83.7, 79.3, 65.7, 64.5, 51.2, 45.0, 39.8, 38.8, 36.3]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Display the top tourist destinations sorted by the number of tourists
def display_top_destinations(df):
    print("Top Tourist Destinations by Number of International Tourists:")
    print(df.sort_values(by='Tourists (Millions)', ascending=False))

# Main function
def main():
    print("Welcome to the Top Tourist Destinations Analysis")
    display_top_destinations(df)

    # Save the data to a CSV file
    df.to_csv('top_tourist_destinations.csv', index=False)
    print("Data saved to 'top_tourist_destinations.csv'.")

# Run the main function
if __name__ == "__main__":
    main()
