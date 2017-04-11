from tkinter import *



def politiebureau():
    import kaart as k
    pliesie = PhotoImage(file = "wouten.gif")
    k.canvas.create_image(895, 305, image = pliesie) #Doelwater (Hoofdbureau)
    k.canvas.create_image(900, 260, image = pliesie) #Zaagmolenstraat
    k.canvas.create_image(925, 292, image = pliesie) #Bureau Boezemsingel
    k.canvas.create_image(897, 230, image = pliesie) #Noord
    k.canvas.create_image(960, 297, image = pliesie) #Taborstraat
    k.canvas.create_image(926, 390, image = pliesie) #Maashaven