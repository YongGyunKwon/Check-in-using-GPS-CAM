import app
import googlemaps
import math
import requests

gmaps_key = "AIzaSyAJ-WSc3L6hD7wxm43Rw3N5cSSCinXnJO4"
gmaps = googlemaps.Client(key = gmaps_key)
a = gmaps.geocode('패스파인더_부산대',language = 'ko')
x=(a[0]['geometry']['location']['lat'])
y=(a[0]['geometry']['location']['lng'])
loc = [x,y]
print(loc)

url = 'https://chenkin-app.firebaseio.com/location.json'
data = list(requests.get(url).json().values())
my_loc = [data[0]['latitude'], data[0]['longitude']] # 현재 위치 값
print(my_loc)
lat = (loc[0]-my_loc[0])*88.8
lng = (loc[1]-my_loc[1])*111.18
dist = math.sqrt((lat*lat)+(lng*lng))
print(dist)

if dist<0.600 :
    app.hello_world()
