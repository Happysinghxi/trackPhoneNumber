import phonenumbers
from phonenumbers import geocoder
#from test import number


import folium
key="37ba221a1c734494ad960488c46772fd"
number=input("enter a phone_number with country code:")

check_number=phonenumbers.parse(number)
number_location=geocoder.description_for_number(check_number,"en")
print(number_location)

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider,"en"))

from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(key)


query=str(number_location)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

map_location=folium.Map(location=[lat,lng ],zoom_starts=9)
folium.Marker([lat,lng],popup=number_location ).add_to(map_location)
map_location.save("myloction.html")