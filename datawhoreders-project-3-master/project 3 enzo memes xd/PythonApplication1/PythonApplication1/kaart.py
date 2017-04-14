from tkinter import *
import colors as c
import pliesiebureaus as pb
from database import Database as d
import matplotlib    
        
        

tk = Tk()
tk.resizable(width=False, height=False)
tk.title("( ͡° ͜ʖ ͡°)")

width = 1280
height = 720
canvas = Canvas(tk, width=width, height=height)
kaart = PhotoImage(file = "kaart4.gif")
pimg = PhotoImage(file = "wouten.gif")
canvas.create_image(905,355,image=kaart)

class Kaart:
    def __init__(self):
        self.charlois =  Area("blue",(841,409,859,428,919,411,915,463,907,465,907,480,945,515,971,549,925,547,877,565,877,579,828,581,774,559,801,549,812,533,801,528,799,509,831,437,817,431,818,413))
        self.charloisTxt = canvas.create_text(850,500,fill = "white",text="Charlois")
        self.delfshaven =  Area("blue",(705,319,689,364,699,388,692,407,742,398,818,413,841,409,829,372,815,369,831,359,829,304))
        self.delfshavnTxt = canvas.create_text(750,360,text="Delfshaven")
        self.feijenoord =  Area("blue",(931,333,917,337,881,383,841,409,859,428,919,411,915,463,907,465,907,480,945,515,969,490,991,490,997,465,967,403,979,395,969,348))
        self.feijenoordTxt = canvas.create_text(950,460,text="Feijenoord")
        self.hillegersberg_schiebroek =  Area("blue",(828,123,825,237,1013,188,999,126,983,142,955,130,952,115,925,94,921,103,853,60))
        self.hillegersberg_schiebroekTxt = canvas.create_text(915,160,text="Hillegersberg Schiebroek")
        self.ijsselmonde =  Area("blue",(1048,396,993,411,979,395,967,403,997,465,991,490,969,490,945,515,971,549,1016,554,1049,542,1105,511,1111,519,1121,513,1141,404,1083,389))
        self.ijsselmondeTxt = canvas.create_text(1050,475,text="Ijsselmonde")
        self.kralingen_crooswijk =  Area("blue",(1014,188,1041,303,1025,332,1048,396,993,411,979,395,969,348,931,333,921,307,891,303,887,220))
        self.kralingen_crooswijkTxt = canvas.create_text(960,275,text="Kralingen Crooswijk")
        self.noord =  Area("blue",(887,220,825,237,739,288,757,312,804,308,805,303,859,295,891,303))
        self.noordTxt = canvas.create_text(825,275,text="Noord")
        self.overschie =  Area("blue",(603,129,631,122,637,137,737,73,784,133,815,109,828,123,825,237,739,288,759,314,705,319,678,269,706,233,700,230,669,244,643,215,633,228))
        self.overschieTxt = canvas.create_text(740,190,text="Overschie")
        self.prins_alexander =  Area("blue",(1041,303,1107,283,1101,233,1129,251,1100,151,1109,148,1115,155,1214,94,1194,77,1210,21,1203,8,1078,51,1120,97,1085,113,1063,89,999,126))
        self.prins_alexanderTxt = canvas.create_text(1060,170,text="Prins Alexander")
        self.centrum =  Area("blue", (841,409,829,372,815,369,831,359,829,307,804,308,805,303,859,295,891,303,921,307,931,333,917,337,881,383))
        self.centrumTxt = canvas.create_text(860,350,text="Centrum")

def callback():
    print("click!")

button1 = Button(tk, text ="Question 1", command = callback, bg = "white", fg = "black")
button2 = Button(tk, text ="Question 2", command = callback, bg = "white", fg = "black")
button3 = Button(tk, text ="Question 3", command = callback, bg = "white", fg = "black")


def politiebureau():
    for item in d.politie_coordinaten():
        canvas.create_image(item[0], item[1], image = pimg)

class Area:
    def __init__(self,color,location):
        self.color = color 
        self.shape = canvas.create_polygon(location, fill=self.color, outline='black', width = 2)

map = Kaart()

#1080p
#overschie = polygon(c.red0(),(904,194,947,183,955,205,1106,109,1176,199,1222,163,1242,185,1237,355,1109,432,1138,471,1057,479,1017,403,1059,350,1050,345,1003,366,964,322,949,342))
#hillegersberg = polygon("blue",(1242,185,1237,355,1520,282,1499,189,1475,213,1432,195,1428,172,1387,141,1382,154,1280,90))
#prins_alexander = polygon("blue",(1562,454,1661,425,1651,350,1693,337,1650,227,1663,222,1673,233,1821,141,1791,116,1815,31,1804,12,1617,76,1680,145,1627,169,1595,134,1499,189))
#kralingen = polygon("blue",(1521,282,1562,454,1538,498,1572,594,1489,616,1469,593,1453,522,1397,500,1382,461,1337,454,1331,330))
#oord = polygon("blue",(1331,330,1237,355,1109,432,1136,468,1206,462,1208,455,1288,443,1337,454))
#delftshaven = polygon("blue",(1057,479,1034,546,1048,582,1038,610,1113,596,1227,620,1262,614,1244,558,1223,553,1247,539,1243,456))
#centrum = polygon("blue",(1262,614,1244,558,1223,553,1247,539,1243,461,1206,462,1208,455,1288,443,1337,454,1382,461,1397,500,1375,506,1322,574))
#feijenoord = polygon("blue",(1397,500,1375,506,1322,574,1262,614,1288,642,1378,617,1372,694,1361,698,1361,720,1417,772,1454,735,1487,735,1496,698,1450,605,1469,593,1453,522))
#ijsselmonde = polygon("blue",(1572,594,1489,616,1469,593,1450,605,1496,698,1487,735,1454,735,1417,772,1457,824,1524,831,1574,813,1657,766,1666,779,1682,769,1712,606,1625,584))
#charlois = polygon("blue",(1262,614,1288,642,1378,617,1372,694,1361,698,1361,720,1417,772,1457,824,1388,820,1315,848,1315,869,1242,871,1161,839,1201,824,1218,800,1201,792,1199,763,1246,656,1225,646,1227,620))

#pb.politiebureau()

if d.get_crime_data("average", "'2009'", "'Charlois'") > 10:
   canvas.itemconfig(map.charlois.shape, fill="black")

def mainLoop():
    politiebureau()
    canvas.grid()
    button1.grid(row = 0, column = 0)
    button2.grid(row = 1, column = 0)
    button3.grid(row = 2, column = 0)
    canvas.grid(row=0, column=1,rowspan = 3)
    tk.mainloop() 
    d.test()

mainLoop()