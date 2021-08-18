#nested dictionary in adictionary
#list-nested inside dictionary 
travel_log ={
    "france":{"cities_visited":["paris","lille","dijon"],"total_visits":10},
    "germany":{"cities_know":["berlin","hamburg","stuttg"],"total_places":15}
}
print(travel_log )

#nesting dictionary in a list
travel_log =[
   {
      "country":"france",
      "cities_visited":["paris","lille","dijon"],
      "total_visits":10
   },
   {
    "country":"germany",
    "cities_know":["berlin","hamburg","stuttg"],
    "total_places":15
    }
]
print(travel_log )

