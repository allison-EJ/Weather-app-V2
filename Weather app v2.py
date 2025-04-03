from tkinter import *
from tkinter import messagebox as mb
import requests
from datetime import datetime

def get_weather():
    city_name = city_input.get()
    if not city_name:
        mb.showerror("Error", "Please enter a city name")
        return

    # Make a request to a weather API
    API_KEY = "4632117b6b689b06ff17b78aa889073c"
    API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"

    try:
        response = requests.get(API_URL)
        data = response.json()

        # Extract relevant information from the API response
        temperature = data['main']['temp']
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        cloudiness = data['clouds']['all']
        description = data['weather'][0]['description']

        # Update the entry fields with the retrieved information
        temp_field.delete(0, END)
        temp_field.insert(0, str(temperature))

        pressure_field.delete(0, END)
        pressure_field.insert(0, str(pressure))

        humid_field.delete(0, END)
        humid_field.insert(0, str(humidity))

        wind_field.delete(0, END)
        wind_field.insert(0, str(wind_speed))

        cloud_field.delete(0, END)
        cloud_field.insert(0, str(cloudiness))

        desc_field.delete(0, END)
        desc_field.insert(0, description)


    except Exception as e:
        mb.showerror("Error", f"An error occurred: {str(e)}")

def get_forecast():
    # Implement the logic to get weather forecast data
    pass

def reset():
    city_input.delete(0, END)
    temp_field.delete(0, END)
    pressure_field.delete(0, END)
    humid_field.delete(0, END)
    wind_field.delete(0, END)
    cloud_field.delete(0, END)
    desc_field.delete(0, END)

root = Tk()
root.title("Emily's Weather Application")
root.configure(bg='Black')
root.geometry("700x450")

title = Label(root, text='Weather Detection and Forecast', fg='Red', bg='Orange', font=("bold", 15))
label1 = Label(root, text='Enter the city name : ', font=("bold", 12), bg="Pink")
city_input = Entry(root, width=24, fg='Black', font=12, relief=GROOVE)
time_label = Label(root, text='', bg='Brown', font=('bold', 14), fg='yellow')
btn_submit = Button(root, text='Get Weather', width=10, font=12, bg='lime green', command=get_weather)
btn_forecast = Button(root, text='Weather Forecast', width=14, font=12, bg='White', command=get_forecast)
btn_reset = Button(root, text="Reset", font=12, bg="lime green", command=reset)

label2 = Label(root, text="Temperature :", font=('bold', 12), bg=("Light Blue"))
label3 = Label(root, text="Pressure :", font=('bold', 12), bg='Light Blue')
label4 = Label(root, text="Humidity :", font=('bold', 12), bg='Light Blue')
label5 = Label(root, text="Wind :", font=('bold', 12), bg='Light Blue')
label6 = Label(root, text="Cloudiness :", font=('bold', 12), bg=("Light Blue"))
label7 = Label(root, text="Description :", font=('bold', 12), bg='Light Blue')

temp_field = Entry(root, width=24, font=11)
pressure_field = Entry(root, width=24, font=11)
humid_field = Entry(root, width=24, font=11)
wind_field = Entry(root, width=24, font=11)
cloud_field = Entry(root, width=24, font=11)
desc_field = Entry(root, width=24, font=11)

# Layout setup using grid
title.grid(row=0, column=0, columnspan=3, pady=10)
label1.grid(row=1, column=0, padx=10, pady=5)
city_input.grid(row=1, column=1, padx=10, pady=5)
btn_submit.grid(row=1, column=2, pady=5)
btn_forecast.grid(row=2, column=0, pady=5)
btn_reset.grid(row=2, column=1, pady=5)

label2.grid(row=3, column=0, padx=10, pady=5)
temp_field.grid(row=3, column=1, padx=10, pady=5)
label3.grid(row=4, column=0, padx=10, pady=5)
pressure_field.grid(row=4, column=1, padx=10, pady=5)
label4.grid(row=5, column=0, padx=10, pady=5)
humid_field.grid(row=5, column=1, padx=10, pady=5)
label5.grid(row=6, column=0, padx=10, pady=5)
wind_field.grid(row=6, column=1, padx=10, pady=5)
label6.grid(row=7, column=0, padx=10, pady=5)
cloud_field.grid(row=7, column=1, padx=10, pady=5)
label7.grid(row=8, column=0, padx=10, pady=5)
desc_field.grid(row=8, column=1, padx=10, pady=5)


root.mainloop()