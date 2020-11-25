import json
import urllib
import urllib.request
import argparse


def min_max_day (city,country):
    api_key = "c34fa0019d8e4461a92ce998d5ee1e11"
    url="https://api.weatherbit.io/v2.0/forecast/daily?"
    final_url = url + "city=" + city + "&country=" + country + "&key=" + api_key
    final_url = final_url.replace (" ", "%20")
    json_obj = urllib.request.urlopen((final_url))
    js = json.load (json_obj)

    #days = 16
    #the forecast for tomorrow

    #print (js["data"][0]["weather"]["description"])

    for items in js["data"]:
        print (items["datetime"])
        print (items["weather"]["description"])
        print("min_temp:",items["min_temp"])
        print("max_temp:",items["max_temp"])
        print ("------")

#min_max_day("Venice", "Italy")

#parser = argparse.ArgumentParser(description="Previsioni meteo per i prossimi 16 gg")
#parser.add_argument("city", type=str, help=" Input consentiti: Venice, Padua, Milan")
#parser.add_argument("country", type=str, help="Input consentiti: Italy", choices=["Italy"])
#parser.add_argument("-v", "--verbose", help="Restituisci output verboso", action ="store_true")
#args = parser.parse_args()



#if args.verbose:
    #print(f"Nei prossimi giorni la temperatura a '{args.city}' è : {info_meteo}")
#else:
    #print (info_meteo)

#questo è un programma meteorologico
