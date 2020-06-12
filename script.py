destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# index = get_destination_index("Los Angeles, USA")
# print(index)
# print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India"))

def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# test_destination_index = get_traveler_location(test_traveler)
# print(test_destination_index)

# first methos : List of emty lists:
# attractions = [[], [], [], [], []]

# second method: Foor loop
# attractions = []
# for destination in destinations:
#   attractions.append([])

# third method using List comprehentions:
attractions = [ [] for destination in destinations ]
#print(attractions)
