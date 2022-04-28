import requests
from twilio.rest import Client
api_key = "15a3f4fc1fb50cf92c0743550836b96d"
end_point = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC9c152f2281a80455d3adbc6dc1c19ab3"
auth_token = "a67ba6a0658458c81a2fc0d736075624"
weather_params = {
    "lat":11.3756199,
    "lon":77.848344,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
response=requests.get(end_point,params=weather_params)
response.raise_for_status()
weather_data=response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
will_rain = True
for hour_data in weather_slice:
    cond_code=(hour_data["weather"][0]["id"])
    if int(cond_code)<700:
        will_rain = True

#print(weather_data["hourly"][0]["weather"][0]["id"])
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today so please bring an umbrella",
        from_='+19802383793',
        to='+91 93448 84610'
    )
    print(message.status)