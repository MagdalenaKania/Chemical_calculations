import math
def srednia(liczby):
    srednia = sum(liczby)/len(liczby)
    return srednia

def odchylenie(liczby):
    srednia = sum(liczby)/len(liczby)
    suma = 0
    for i in liczby:
        suma += (i-srednia)**2
    odchylenie = math.sqrt(suma/(len(liczby)-1))
    return odchylenie

def regresja(x,y):
    X = []
    Y = []
    XY = []
    X2 = []
    Y2 = []
    wynik = []

    for i in range(len(x)):
        X.append(x[i])
        Y.append(y[i])
        XY.append(x[i]*y[i])
        X2.append(x[i]**2)
        Y2.append(y[i]**2)
    n = len(x)
    delta = n*sum(X2)-sum(X)**2
    a = (n*sum(XY)-sum(X)*sum(Y))/delta
    b = (sum(X2)*sum(Y)-sum(X)*sum(XY))/delta
    Da = math.sqrt((float(n)/(float(n)-2))*(sum(Y2)-a*sum(XY)-b*sum(Y))/delta)
    Db = math.sqrt(Da*sum(X2)/n)
    wynik.append(a)
    wynik.append(b)
    wynik.append(Da)
    wynik.append(Db)
    return wynik
