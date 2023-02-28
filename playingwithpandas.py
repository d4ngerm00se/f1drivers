import pandas as pd

drivers = pd.read_csv('C:/Users/danaa/Desktop/driverdeets.csv')

# Filter the DataFrame to only include drivers who finished in first position
fourth_place_drivers = drivers[drivers['Pos'] == "4"]


# Group the DataFrame by team and count the number of drivers in each team
fourth_count_drivers = fourth_place_drivers.groupby('Driver')['Pos'].count()

top_three_drivers = fourth_count_drivers.sort_values(ascending=False)[:3]

# Print the names of the top three drivers and the number of times they finished in fourth position
for driver, count in top_three_drivers.items():
    print(f"{driver} finished in fourth position {count} times.")