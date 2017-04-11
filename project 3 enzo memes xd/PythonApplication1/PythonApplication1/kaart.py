from tkinter import *
import colors as c



tk = Tk()
tk.resizable(width=False, height=False)
tk.title("( ͡° ͜ʖ ͡°)")

width = 1920
height = 1080
canvas = Canvas(tk, width=width, height=height)
kaart = PhotoImage(file = "gsh.gif")
pliesie = PhotoImage(file = "wouten.gif")
wirhabenstroom = PhotoImage(file = "stroom.gif")
canvas.create_image(1000,500,image=kaart)

class polygon:
    def __init__(self,color,list):
        self.color = color 
        self.shape = canvas.create_polygon(list, fill=self.color, outline='black', width = 2)

overschie = polygon(c.red(),(904,194,947,183,955,205,1106,109,1176,199,1222,163,1242,185,1237,355,1109,432,1138,471,1057,479,1017,403,1059,350,1050,345,1003,366,964,322,949,342))
hillegersberg = polygon("blue",(1242,185,1237,355,1520,282,1499,189,1475,213,1432,195,1428,172,1387,141,1382,154,1280,90))
prins_alexander = polygon("blue",(1562,454,1661,425,1651,350,1693,337,1650,227,1663,222,1673,233,1821,141,1791,116,1815,31,1804,12,1617,76,1680,145,1627,169,1595,134,1499,189))
kralingen = polygon("blue",(1521,282,1562,454,1538,498,1572,594,1489,616,1469,593,1453,522,1397,500,1382,461,1337,454,1331,330))
noord = polygon("blue",(1331,330,1237,355,1109,432,1136,468,1206,462,1208,455,1288,443,1337,454))
delftshaven = polygon("blue",(1057,479,1034,546,1048,582,1038,610,1113,596,1227,620,1262,614,1244,558,1223,553,1247,539,1243,456))
centrum = polygon("blue",(1262,614,1244,558,1223,553,1247,539,1243,461,1206,462,1208,455,1288,443,1337,454,1382,461,1397,500,1375,506,1322,574))
feijenoord = polygon("blue",(1397,500,1375,506,1322,574,1262,614,1288,642,1378,617,1372,694,1361,698,1361,720,1417,772,1454,735,1487,735,1496,698,1450,605,1469,593,1453,522))
ijsselmonde = polygon("blue",(1572,594,1489,616,1469,593,1450,605,1496,698,1487,735,1454,735,1417,772,1457,824,1524,831,1574,813,1657,766,1666,779,1682,769,1712,606,1625,584))
charlois = polygon("blue",(1262,614,1288,642,1378,617,1372,694,1361,698,1361,720,1417,772,1457,824,1388,820,1315,848,1315,869,1242,871,1161,839,1201,824,1218,800,1201,792,1199,763,1246,656,1225,646,1227,620))

canvas.create_image(1000,500, image = pliesie)
canvas.create_image(1100,500, image = wirhabenstroom)
canvas.grid()

tk.mainloop()
