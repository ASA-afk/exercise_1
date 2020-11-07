## Aufgabe 3.a.i  ##
x=str(input("Uhrzeit der Stunden kleiner als 24: "))
y=str(input("Uhrzeit der Minuten kleiner als 60: "))
z=str(input("Eingabe der Minuten die man bereits fliegt: "))

endMin=(int(y)-int(z))%60
endStd=(((int(x)*60)+int(y)-int(z))//60)%24
print("{:02d}:{:02d}".format(endStd,endMin))


## Aufgabe 3.a.ii  ##
boardingMin=(endMin-30)%60
boardingStd=(((int(x)*60)+int(y)-int(z)-30)//60)%24
print("{:02d}:{:02d}".format(boardingStd,boardingMin))