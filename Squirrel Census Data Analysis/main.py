# Data extracted from the 2018 Central Park Squirrel Census
# Check the website: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw

import pandas

SQUIRREL_CENSUS_DATA_CSV_PATH = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrels_census_data = pandas.read_csv(SQUIRREL_CENSUS_DATA_CSV_PATH)

squirrels_colors_count = {"Fur Color": ["Gray", "Cinnamon", "Black"], "Count": []}

gray_squirrels_count = len(squirrels_census_data[squirrels_census_data["Primary Fur Color"] == "Gray"])

cinnamon_squirrels_count = len(squirrels_census_data[squirrels_census_data["Primary Fur Color"] == "Cinnamon"])

black_squirrels_count = len(squirrels_census_data[squirrels_census_data["Primary Fur Color"] == "Black"])

squirrels_colors_count["Count"].append(gray_squirrels_count)

squirrels_colors_count["Count"].append(cinnamon_squirrels_count)

squirrels_colors_count["Count"].append(black_squirrels_count)

squirrels_colors_count_data = pandas.DataFrame(squirrels_colors_count)

print(squirrels_colors_count_data)
