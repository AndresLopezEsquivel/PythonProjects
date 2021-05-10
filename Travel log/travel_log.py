travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, number_visits, cities_visited):

  travel_log.append({"country" : "", "visits" : 0, "cities" : []})

  index = len(travel_log) - 1

  travel_log[index]["country"] = country_name

  travel_log[index]["visits"] = number_visits

  travel_log[index]["cities"] = cities_visited

  print(f"You've visited {country_name} {number_visits} times.")

  print(f"You've been to {cities_visited[0]} and {cities_visited[1]}")

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)



