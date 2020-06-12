destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# index = get_destination_index("Los Angeles, USA")
# print(index)
# print(get_destination_index("Paris, France"))
# print(get_destination_index("Hyderabad, India"))
