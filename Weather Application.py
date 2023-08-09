
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

def ZipLookUp():
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=25&API_KEY=A6AC43B3-34D7-439D-86FE-00E3CA37F0E8")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#990066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        MyLabel = Label(root, text=city + " ,Air Quality " + str(quality) + " ," + category, font=("Helvetica", 20),
                        background=weather_color)
        MyLabel.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error"

def close_app():
    root.destroy()

root = Tk()
root.title("Weather Application")
root.geometry("300x150")

title_label = Label(root, text="Weather Application", font=("Helvetica", 16))
title_label.place(relx=0.5, y=10, anchor="center")

zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S)
subBut = Button(root, text="Enter", command=ZipLookUp)
subBut.grid(row=0, column=1, sticky=W+E+N+S)

exit_button = Button(root, text="Exit", command=close_app)
exit_button.grid(row=2, column=0, columnspan=2, sticky=W+E+N+S)

root.mainloop()
