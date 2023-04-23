from geopy.geocoders import Nominatim
import fake_useragent

ua = fake_useragent.UserAgent().random

# print(ua)

location = Nominatim(user_agent=ua)

coordinates = "53.8000000 , 27.566"

loca = location.reverse(coordinates)

print(loca.raw)

city = location.geocode(loca.raw["address"]["city"])
print(city)