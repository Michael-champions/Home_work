# Creative Feature Added: User can type a country name to get its min, max, and average life expectancy across years.
# Also detects the largest drop in life expectancy between consecutive years for a country.

from collections import defaultdict

filename = "life-expectancy.csv"
data = []

# Load dataset
with open(filename) as file:
    next(file)  # Skip header
    for line in file:
        parts = line.strip().split(",")
        country = parts[0]
        code = parts[1]
        year = int(parts[2])
        life_exp = float(parts[3])
        data.append((country, code, year, life_exp))

print("\n📊 === LIFE EXPECTANCY DATA ANALYSIS ===")

# --- Overall lowest and highest life expectancy ---
min_life = min(data, key=lambda x: x[3])
max_life = max(data, key=lambda x: x[3])

print("\n🌍 Overall Life Expectancy Statistics:")
print(f"🔽 Lowest life expectancy:  {min_life[3]:.2f} years in {min_life[0]} ({min_life[2]})")
print(f"🔼 Highest life expectancy: {max_life[3]:.2f} years in {max_life[0]} ({max_life[2]})")

# --- Year-based analysis with validation ---
while True:
    year_input = input("\n📅 Enter a year to analyze: ")
    if year_input.isdigit() and 1800 <= int(year_input) <= 2023:
        year_input = int(year_input)
        break
    else:
        print("❌ Invalid input. Please enter a year between 1800 and 2023.")

year_data = [x for x in data if x[2] == year_input]

if year_data:
    avg_life = sum([x[3] for x in year_data]) / len(year_data)
    min_year_life = min(year_data, key=lambda x: x[3])
    max_year_life = max(year_data, key=lambda x: x[3])

    print(f"\n📆 Life Expectancy in {year_input}:")
    print(f"📈 Average life expectancy:  {avg_life:.2f} years")
    print(f"🔽 Minimum: {min_year_life[3]:.2f} years ({min_year_life[0]})")
    print(f"🔼 Maximum: {max_year_life[3]:.2f} years ({max_year_life[0]})")
else:
    print(f"⚠️ No data found for the year {year_input}.")

# --- Country-based analysis ---
country_query = input("\n🌐 Enter a country name to analyze (optional): ").strip()

if country_query:
    country_data = [entry for entry in data if entry[0].lower() == country_query.lower()]

    if country_data:
        min_country_life = min(country_data, key=lambda x: x[3])
        max_country_life = max(country_data, key=lambda x: x[3])
        avg_country_life = sum([x[3] for x in country_data]) / len(country_data)

        print(f"\n📍 Life Expectancy in {country_query.title()}:")
        print(f"🔽 Minimum life expectancy: {min_country_life[3]:.2f} years in {min_country_life[2]}")
        print(f"🔼 Maximum life expectancy: {max_country_life[3]:.2f} years in {max_country_life[2]}")
        print(f"📈 Average life expectancy: {avg_country_life:.2f} years")
    else:
        print(f"⚠️ No data found for country: {country_query}")

# --- Largest life expectancy drop between years ---
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

print(f"\n📉 Largest Drop in Life Expectancy:")
print(f"{drop_country}: dropped by {largest_drop:.2f} years from {year_before} to {year_after}")

print("\n✅ Analysis Complete. Thank you for using the Life Expectancy Analyzer!")
