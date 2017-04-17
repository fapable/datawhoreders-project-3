from tkinter import *
import colors as c
import pliesiebureaus as pb
from database import Database as d   
import grafieken as g
import matplotlib.pyplot as plt

tk = Tk()
tk.resizable(width=False, height=False)
tk.title("( ͡° ͜ʖ ͡°)")

width = 1280
height = 720
canvas = Canvas(tk, width=width, height=height)
kaart = PhotoImage(file = "kaart4.gif")
canvas.create_image(905,355,image=kaart)

class Standaard_Kaart:
    def __init__(self, area_color, text_color):
        self.Charlois =  Area(area_color,(841,409,859,428,919,411,915,463,907,465,907,480,945,515,971,549,925,547,877,565,877,579,828,581,774,559,801,549,812,533,801,528,799,509,831,437,817,431,818,413))
        self.charloisTxt = canvas.create_text(850,500,fill = text_color,text="Charlois")
        self.Delfshaven =  Area(area_color,(705,319,689,364,699,388,692,407,742,398,818,413,841,409,829,372,815,369,831,359,829,304))
        self.delfshavnTxt = canvas.create_text(750,360,fill = text_color,text="Delfshaven")
        self.Feijenoord =  Area(area_color,(931,333,917,337,881,383,841,409,859,428,919,411,915,463,907,465,907,480,945,515,969,490,991,490,997,465,967,403,979,395,969,348))
        self.feijenoordTxt = canvas.create_text(950,460,fill = text_color,text="Feijenoord")
        self.Hillegersberg_Schiebroek =  Area(area_color,(828,123,825,237,1013,188,999,126,983,142,955,130,952,115,925,94,921,103,853,60))
        self.hillegersberg_schiebroekTxt = canvas.create_text(915,160,fill = text_color,text="Hillegersberg Schiebroek")
        self.Ijsselmonde =  Area(area_color,(1048,396,993,411,979,395,967,403,997,465,991,490,969,490,945,515,971,549,1016,554,1049,542,1105,511,1111,519,1121,513,1141,404,1083,389))
        self.ijsselmondeTxt = canvas.create_text(1050,475,fill = text_color,text="Ijsselmonde")
        self.Kralingen_Crooswijk =  Area(area_color,(1014,188,1041,303,1025,332,1048,396,993,411,979,395,969,348,931,333,921,307,891,303,887,220))
        self.kralingen_crooswijkTxt = canvas.create_text(960,275,fill = text_color,text="Kralingen Crooswijk")
        self.Noord =  Area(area_color,(887,220,825,237,739,288,757,312,804,308,805,303,859,295,891,303))
        self.noordTxt = canvas.create_text(825,275,fill = text_color,text="Noord")
        self.Overschie =  Area(area_color, (603,129,631,122,637,137,737,73,784,133,815,109,828,123,825,237,739,288,759,314,705,319,678,269,706,233,700,230,669,244,643,215,633,228))
        self.overschieTxt = canvas.create_text(740,190,fill = text_color,text="Overschie")
        self.Prins_Alexander =  Area(area_color,(1041,303,1107,283,1101,233,1129,251,1100,151,1109,148,1115,155,1214,94,1194,77,1210,21,1203,8,1078,51,1120,97,1085,113,1063,89,999,126))
        self.prins_alexanderTxt = canvas.create_text(1060,170,fill = text_color,text="Prins Alexander")
        self.Centrum =  Area(area_color, (841,409,829,372,815,369,831,359,829,307,804,308,805,303,859,295,891,303,921,307,931,333,917,337,881,383))
        self.centrumTxt = canvas.create_text(860,350,fill = text_color,text="Centrum")
        self.button01 = Button(tk, text = "Criminaliteit 2009", command = create_average_crime_result_2009, bg = "white", fg = "black")
        self.button02 = Button(tk, text = "Criminaliteit 2011", command = create_average_crime_result_2011, bg = "white", fg = "black")
        self.button03 = Button(tk, text = "Question 3", command = None, bg = "white", fg = "black")
        self.button04 = Button(tk, text = "Concentratie metrostations", command = create_metro_result, bg = "white", fg = "black")
        self.button05 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button06 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button07 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button08 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button09 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button10 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button11 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button12 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button13 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button14 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button15 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button16 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button17 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button18 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button19 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button20 = Button(tk, text = "", command = None, bg = "white", fg = "black")
        self.button01.grid(row = 0, column = 0)
        self.button02.grid(row = 1, column = 0)
        self.button03.grid(row = 2, column = 0)
        self.button04.grid(row = 3, column = 0)
        self.button05.grid(row = 4, column = 0)
        self.button06.grid(row = 5, column = 0)
        self.button07.grid(row = 6, column = 0)
        self.button08.grid(row = 7, column = 0)
        self.button09.grid(row = 8, column = 0)
        self.button10.grid(row = 9, column = 0)
        self.button11.grid(row = 10, column = 0)
        self.button12.grid(row = 11, column = 0)
        self.button13.grid(row = 12, column = 0)
        self.button14.grid(row = 13, column = 0)
        self.button15.grid(row = 14, column = 0)
        self.button16.grid(row = 15, column = 0)
        self.button17.grid(row = 16, column = 0)
        self.button18.grid(row = 17, column = 0)
        self.button19.grid(row = 18, column = 0)
        self.button20.grid(row = 19, column = 0)



def str_to_code(object, attr):
    return getattr(object, attr)

class crime_result:
    def __init__(self, main_screen, jaar, soort):
        for wijk in d.get_areas("criminaliteit", jaar):
            a = wijk[0]
            result = d.get_crime_data(soort, jaar, ("'" + a + "'"))
            canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = c.rgb_to_hex(result, (255, 0 ,0), 20, True))

class metro_result:
    def __init__(self, main_screen):
        for wijk in d.get_areas("metro", None):
            a = wijk[0]
            info = d.get_metro_info(("'" + a + "'"))[0]
            if info[1] != None:
                result = info[1]/info[0]
                canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = c.rgb_to_hex(result, (0, 255, 0), 2, False))
            else:
                canvas.itemconfig(str_to_code(main_screen, str(a)).shape, fill = str_to_code(main_screen, str(a)).color)

def create_average_crime_result_2009():
    remove_extra_images()
    crime_result(map, "'2009'", "average")
    politiebureau()
    g.crime_graph_2009()

def create_average_crime_result_2011():
    remove_extra_images()
    crime_result(map, "'2011'", "average")
    politiebureau()
    g.crime_graph_2011()

def create_metro_result():
    remove_extra_images()
    metro_result(map)
    metro_stations()

def metro_stations():
    global mimg
    mimg = PhotoImage(file = "metro.gif")
    global mlimg
    mlimg = PhotoImage(file = "Metro_legenda.gif")
    for item in d.metro_coordinaten():
        canvas.create_image(item[0], item[1], image = mimg)
    canvas.create_image((width - (mlimg.width()/2)), (height - (mlimg.height()/2)), image = mlimg)

def politiebureau():
    global pimg 
    pimg = PhotoImage(file = "wouten.gif")
    global climg
    climg = PhotoImage(file = "Politiebureau_legenda.gif")
    for item in d.politie_coordinaten():
        canvas.create_image(item[0], item[1], image = pimg)
    canvas.create_image((width - (climg.width()/2)), (height - (climg.height()/2)), image = climg)

def remove_extra_images():
    plt.close()
    try:
        pimg.__del__()
        climg.__del__()
    except(NameError):
        pass
    try:
        mimg.__del__()
        mlimg.__del__()
    except(NameError):
        pass
        
class Area:
    def __init__(self,color,location):
        self.color = color 
        self.shape = canvas.create_polygon(location, fill=self.color, outline='black', width = 2)

map = Standaard_Kaart(c.grey(), "white")
def mainLoop():
    canvas.grid()
    canvas.grid(row=0, column=6,rowspan = 800)
    tk.mainloop() 

mainLoop()