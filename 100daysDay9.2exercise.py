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
def add_new_country(country_name,visit_count,country_cities):
    new_country = { }
    new_country["country"]= country_name
    new_country["visits"] = visit_count
    new_country["cities"] = country_cities
    #print(new_country)
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



