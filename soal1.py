#Tugas Jumlahkan dan tampilkan Hasilnya Gunakan variabel input

# Data for each month
data = {
    "January": {"kelahiran": 80, "kematian": 10, "usia_produktif": 5},
    "February": {"kelahiran": 15, "kematian": 8, "usia_produktif": 7}
}

# Function to calculate total population
def calculate_population(births, deaths, productive_age):
    total_population = (births - deaths) + productive_age
    return total_population

# Function to determine population condition
def population_condition(births, productive_age):
    if births > productive_age:
        return "Data Meningkat"  # Population increases
    else:
        return "Data Sejahtera"  # Population well-being

# Process data for each month
for month, values in data.items():
    births = values["kelahiran"]
    deaths = values["kematian"]
    productive_age = values["usia_produktif"]
    
    total_population = calculate_population(births, deaths, productive_age)
    condition = population_condition(births, productive_age)
    
    print(f"Bulan: {month}")
    print(f"Total Penduduk: {total_population}")
    print(f"Keterangan: {condition}")
    print("-" * 30)
