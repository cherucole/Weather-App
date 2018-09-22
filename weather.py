#works from idle python program. python 3.7 idle
import urllib.request,json

#to run program just run module in idle and then call the weather search function i.e weather_search()
def weather_search():
    city= input("Enter city Name: ")
    url='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' + city
    json_obj = urllib.request.urlopen(url)
    data = json.load(json_obj)
#this returns the whole object from url
    print (data)

#looping through the object(dictionary) to fetch only what is in the weather dictionary. Dictionary is whats inside curly braces {}
    for item in data["weather"]:
        print (item)

#looping through the list to return only main. Lists are inside square braces[]

        print (item['main'])
        print (item['description'])
