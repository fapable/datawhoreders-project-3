from tkinter import *



def politiebureau():
    import kaart as k
    pimg = PhotoImage(file = "wouten.gif")
    k.canvas.create_image(895, 305, image = pimg) #Doelwater (Hoofdbureau), pimg = politieimage
    k.canvas.create_image(900, 260, image = pimg) #Zaagmolenstraat
    k.canvas.create_image(925, 292, image = pimg) #Bureau Boezemsingel
    k.canvas.create_image(897, 230, image = pimg) #Noord
    k.canvas.create_image(960, 297, image = pimg) #Taborstraat
    k.canvas.create_image(926, 390, image = pimg) #Maashaven