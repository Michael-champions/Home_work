# Creative Feature Added: User can type a country name to get its min, max, and average life expectancy across years.
filename = "life-expectancy.csv"

data = []

with open(filename) as file:
    next(file) 
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_exp = float(parts[3])
        data.append((country, code, year, life_exp))

# Country-based analysis
country_query = input("\nEnter a country name to analyze (optional): ").strip()

if country_query:
    country_data = [entry for entry in data if entry[0].lower() == country_query.lower()]

    if country_data:
        min_country_life = min(country_data, key=lambda x: x[3])
        max_country_life = max(country_data, key=lambda x: x[3])
        avg_country_life = sum([x[3] for x in country_data]) / len(country_data)

        print(f"\nFor {country_query.title()}:")
        print(f"Minimum life expectancy: {min_country_life[3]:.2f} in {min_country_life[2]}")
        print(f"Maximum life expectancy: {max_country_life[3]:.2f} in {max_country_life[2]}")
        print(f"Average life expectancy: {avg_country_life:.2f}")
    else:
        print(f"No data found for country: {country_query}")

# 🔽 Extra Feature: Detect the country with the largest life expectancy drop between consecutive years
from collections import defaultdict

country_data_dict = defaultdict(list)

for country, code, year, life_exp in data:
    country_data_dict[country].append((year, life_exp))

largest_drop = 0
drop_country = ""
year_before = 0
year_after = 0

for country, entries in country_data_dict.items():
    sorted_entries = sorted(entries)
    for i in range(1, len(sorted_entries)):
        prev_year, prev_life = sorted_entries[i - 1]
        curr_year, curr_life = sorted_entries[i]
        drop = prev_life - curr_life
        if drop > largest_drop:
            largest_drop = drop
            drop_country = country
            year_before = prev_year
            year_after = curr_year

print(f"\n🔍 Largest drop in life expectancy was in {drop_country}:")
print(f"From {year_before} to {year_after}, life expectancy dropped by {largest_drop:.2f} years.")