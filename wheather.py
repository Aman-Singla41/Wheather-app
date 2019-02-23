import tkinter as tk
import urllib.request
import json




data=""
Data=""

def get():
    URL = "https://api.openweathermap.org/data/2.5/forecast?q="+entry.get()+"&appid=5fa70590378b2cf06fca2de89f8c616f"
    global data
    response=urllib.request.urlopen(URL)
       
    data = json.loads(response.read())
    current()
    newWindow()

    
def newWindow():
    root=tk.Tk()
    root.geometry("250x300")
    canvas=tk.Canvas(root,width=200,height=400)
        
    canvas.grid()
    canvas.create_text(110,110,text=Data,font="times 10 bold")
    button3=tk.Button(root,text=">>",command=nex)
    canvas.create_window(50,220,height=20,width=50,window=button3)
    button4=tk.Button(root,text=">>>",command=prev)
    canvas.create_window(120,220,height=20,width=50,window=button4)
    root.mainloop()

def current():
    global Data
    Data=("City :"+ str(data['city']['name']))+"\n"+("Country :"+ str(data['city']['country']))+"\n"+"\n"+("Date: "+str(data['list'][0]['dt_txt'].split()[0]))+"\n"+("Temperature :"+ str(round(data['list'][0]['main']['temp']-273.15,2))+" C")+"\n"+("Max Temp :"+ str(round(data['list'][0]['main']['temp_max']-273.15,2))+" C")+"\n"+("Min Temp :"+ str(round(data['list'][0]['main']['temp_min']-273.15,2))+" C")+"\n"+("Pressure :"+ str(data['list'][0]['main']['pressure'])+" hpa")+"\n"+("Humidity :"+ str(data['list'][0]['main']['humidity'])+" %")+"\n"+("Wind speed :"+ str(data['list'][0]['wind']['speed'])+" m\s")+"\n"+("wind direction :"+ str(data['list'][0]['wind']['deg'])+" degrees")
          


       
def nex():
    global Data
    Data=("City :"+ str(data['city']['name']))+"\n"+("Country :"+ str(data['city']['country']))+"\n"+"\n"+("Date: "+str(data['list'][9]['dt_txt'].split()[0]))+"\n"+("Temperature :"+ str(round(data['list'][1]['main']['temp']-273.15,2))+" C")+"\n"+("Max Temp :"+ str(round(data['list'][1]['main']['temp_max']-273.15,2))+" C")+"\n"+("Min Temp :"+ str(round(data['list'][1]['main']['temp_min']-273.15,2))+" C")+"\n"+("Pressure :"+ str(data['list'][1]['main']['pressure'])+" hpa")+"\n"+("Humidity :"+ str(data['list'][1]['main']['humidity'])+" %")+"\n"+("Wind speed :"+ str(data['list'][1]['wind']['speed'])+" m\s")+"\n"+("wind direction :"+ str(data['list'][1]['wind']['deg'])+" degrees")
    newWindow()
def prev():
    global Data
    Data=("City :"+ str(data['city']['name']))+"\n"+("Country :"+ str(data['city']['country']))+"\n"+"\n"+("Date: "+str(data['list'][17]['dt_txt'].split()[0]))+"\n"+("Temperature :"+ str(round(data['list'][2]['main']['temp']-273.15,2))+" C")+"\n"+("Max Temp :"+ str(round(data['list'][2]['main']['temp_max']-273.15,2))+" C")+"\n"+("Min Temp :"+ str(round(data['list'][2]['main']['temp_min']-273.15))+" C")+"\n"+("Pressure :"+ str(data['list'][2]['main']['pressure'])+" hpa")+"\n"+("Humidity :"+ str(data['list'][2]['main']['humidity'])+" %")+"\n"+("Wind speed :"+ str(data['list'][2]['wind']['speed'])+" m\s")+"\n"+("wind direction :"+ str(data['list'][2]['wind']['deg'])+" degrees")+"\n"
    newWindow()

obj=tk.Tk()
obj.geometry("470x270")

canvas = tk.Canvas(obj, width = 100, height = 50)

canvas.grid()
entry=tk.Entry(obj,width=20)
canvas.create_text(60,10,font='times 10 bold',text="Enter the City")
entry.place(x=20,y=20)

button=tk.Button(text="search",command=get)
canvas.create_window(50,55,height=20,width=50,window=button)

button1=tk.Button(text="cancel",command=obj.quit)
canvas.create_window(120,55,height=20,width=50,window=button1)


obj.mainloop()

    
