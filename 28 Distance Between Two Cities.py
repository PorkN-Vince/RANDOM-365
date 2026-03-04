from geopy.distance import geodesic
delhi = (28.6139, 77.2090)
mumbai = (19.0760, 72.8777)

distance = geodesic(delhi, mumbai)

print("Distance Details")
print("-" * 30)
print(f"From   : Delhi")
print(f"To     : Mumbai")
print(f"KM     :  {distance.kilometers:.2f}")
print(f"Miles  :  {distance.miles:.2f}")