## Aufgabe 3.b  ##
x=str(input("Ankunftszeit in Südkorea der Stunde: "))
y=str(input("Ankunftszeit in Südkorea der Minuten: "))

deutschlandZeitMin=(int(y)-(7*60))%60
deutschlandZeitStd=(((int(x)*60)+int(y)-(7*60))//60)%24
print("{:02d}:{:02d}".format(deutschlandZeitStd,deutschlandZeitMin))
