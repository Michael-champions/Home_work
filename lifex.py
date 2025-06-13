# Life Expectancy Analysis Program
# This program reads a CSV file containing life expectancy data, calculates overall minimum and maximum life expectancies,
# and allows users to query life expectancy data for a specific year or country.
filename = "life-expectancy.csv"

# Initialize variables
overall_min_life = float('inf')
overall_max_life = float('-inf')
min_country = ""
min_year = 0
max_country = ""
max_year = 0

data = []

# Load and process file

with open(filename) as file:
    next(file)  # Skip header
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_exp = float(parts[3])

        data.append((country, code, year, life_exp))

        if life_exp < overall_min_life:
            overall_min_life = life_exp
            min_country = country
            min_year = year

        if life_exp > overall_max_life:
            overall_max_life = life_exp
            max_country = country
            max_year = year

# Print overall results
print(f"\nThe overall max life expectancy is: {overall_max_life:.3f} from {max_country} in {max_year}")
print(f"The overall min life expectancy is: {overall_min_life:.2f} from {min_country} in {min_year}")

# Ask for year of interest
year_of_interest = int(input("\nEnter the year of interest: "))

year_life_exp = []
for entry in data:
    if entry[2] == year_of_interest:
        year_life_exp.append(entry)

if year_life_exp:
    total = sum([item[3] for item in year_life_exp])
    avg = total / len(year_life_exp)

    max_entry = max(year_life_exp, key=lambda x: x[3])
    min_entry = min(year_life_exp, key=lambda x: x[3])

    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {avg:.2f}")
    print(f"The max life expectancy was in {max_entry[0]} with {max_entry[3]:.2f}")
    print(f"The min life expectancy was in {min_entry[0]} with {min_entry[3]:.3f}")
else:
    print(f"No data found for year {year_of_interest}")