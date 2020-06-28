import tkinter as tk
from tkinter import ttk
from utils.dbutils import DbUtils
from utils.pathutils import PathUtils
import constants

#Get value
def ddvalue(event):
        global SpeciesId
        SpeciesId = db.get_species_id(Species.get())[0]
        scientific_name = db.get_scientific_name(SpeciesId)
        CommonName.insert(0,scientific_name[0])

def getvalues():
        observation_values = {
        'species_id' : SpeciesId ,
        'country'    : Country.get(),
        'state'      : State.get(),
        'place'      : Place.get()
    }
        db.create_observation(values=observation_values)

app = tk.Tk()
app.geometry('350x390')

frame = tk.LabelFrame(app,text="FORM",width=330,height=370,bg="DodgerBlue4",fg="White").place(x=10,y=10)

Specieslable = tk.Label(frame,text = "Select Species",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=50)
project_root = PathUtils.get_project_root()
db_path = PathUtils.append_path(project_root,constants.DB_NAME)
db = DbUtils()
db.db_open(db_path)
db.create_tables()
test_list = db.get_species()
Species = ttk.Combobox(frame,values=[x[1] for x in test_list])
Species.place(x=150,y=50,height=25,width=150)
Species.bind("<<ComboboxSelected>>", ddvalue)

CommonNamelable = tk.Label(frame,text = "Common Name",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=85)
CommonName = tk.Entry(frame)
CommonName.place(x=150,y=85,height=25,width=150)

Countrylable = tk.Label(frame,text = "Country",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=120)
Country = tk.Entry(frame)
Country.place(x=150,y=120,height=25,width=150)

Statelable = tk.Label(frame,text = "State",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=155)
State = tk.Entry(frame)
State.place(x=150,y=155,height=25,width=150)

Placelable = tk.Label(frame,text = "Place",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=190)
Place = tk.Entry(frame)
Place.place(x=150,y=190,height=25,width=150)

Latitudelable = tk.Label(frame, text = "Latitude",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=225)
Latitude = tk.Entry(frame)
Latitude.place(x=150,y=225,height=25,width=150)

Longitudelable = tk.Label(frame, text = "Longitude",justify="left",bg="DodgerBlue4",fg="White",font="Arial 12 bold").place(x=30,y=260)
Longitude = tk.Entry(frame)
Longitude.place(x=150,y=260,height=25,width=150)

button = tk.Button(frame,text="Submit",font="Helbetica 12 bold",command=getvalues).place(x=150,y=320)
app.mainloop()