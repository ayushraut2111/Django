from django.shortcuts import render
import requests, json
def index(request):
    if request.method=='POST':
        city=request.POST["city"]
        # print(city)
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

        URL = BASE_URL + "q=" + city + "&appid=" + "1b3a3a907f567fe52ae4799136331b48"
        response = requests.get(URL)
        dt = response.json()
        # print(dt)
        data={
            'city':city,
            'country':str(dt['sys']['country']),
            'coordinate':str(dt['coord']['lon'])+ " "+str(dt['coord']['lat']),
            'temp':str(dt['main']['temp'])+' k',
            'pressure':str(dt['main']['pressure']),
            'humidity':str(dt['main']['humidity'])
        }
        # print(data)

    else:
        data={}
    return render(request,"index.html",data)
