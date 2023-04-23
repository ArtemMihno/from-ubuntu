import requests
import json
import datetime


# h = str(datetime.datetime.now().time())
# print(h)
# h = "03:26:43.497421"
# print(type(h))
# print(h)
# hour = ""
# for c in h:
#     if c == ":":
#         break
    
#     hour += c
# if hour[0] == "0":
#     hour.remove("0")
# print(hour)




def get_the_weather_by_coordinates_now(days : int, latitude, longitude: float)-> str:
    api_key = "1da3061de68747ed9eb201205231304"
    responce = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={latitude},{longitude}&days={days}&hour={0}").text
    data = json.loads(responce)
    otvet = ""
    
    name_of_city = data["location"]["name"]
    country = data["location"]["country"]
    temperature = data["current"]["temp_c"]

    otvet = f"Город: {name_of_city}({country})\nТемпература:{temperature}(C)\n*************\n"

    
    forecastday = data["forecast"]["forecastday"]
    for i in range(0,days):
        otvet +=(forecastday[i]["date"] + "\n" + str(forecastday[i]["day"]["maxtemp_c"]) + " : " + str(forecastday[i]["day"]["mintemp_c"]) + "\n" + "*************" + "\n")


    return otvet
        

    # with open("pogoda1.json", "w") as file:
    #     json.dump(data, file, ensure_ascii=False, indent= 4)

# print(get_the_weather_by_coordinates_now(1,53.935334,))



