import math
import statistics

plik1 = open("Dane_a.txt", "r")
plik2 = open("Dane_b.txt", "r")
plik3 = open("Dane_c.txt", "r")
wyniki1 = open("Wyniki_1.txt", "w")
wyniki2 = open("Wyniki_2.txt", "w")

dane1 = plik1.readlines()
dane1 = dane1[1]
dane1 = dane1.split()
c0k = float(dane1[0])
c0z = float(dane1[1])
cHCl = float(dane1[2])
cNaOH = float(dane1[3])
fk = float(dane1[4])
fz = float(dane1[5])
Vk = float(dane1[8])
Vz = float(dane1[9])
T = float(dane1[10])

dane2 = plik2.readlines()
dane2.remove(dane2[0])
pH = []
VNaOH = []
for wartosci in dane2:
    wartosci = wartosci.split()
    pH.append(float(wartosci[1]))
    VNaOH.append(float(wartosci[0]))

cz = []
ck = []
for i in range(len(pH)):
    if pH[i]<=3.5:
        c = (VNaOH[i]*cNaOH)/(Vk+VNaOH[i])+10**(-pH[i])
        cz.append(c)
    else:
        c = (VNaOH[i]*cNaOH)/(Vk+VNaOH[i])
        cz.append(c)
for i in range(len(cz)):
    c = (Vk*c0k*fk)/(Vk+VNaOH[i])-cz[i]
    ck.append(c)
p = []
q = []
for i in range(len(cz)):
    p1 = math.log(cz[i]/ck[i], 10)
    p.append(p1)
    q1 = (0.509*math.sqrt(cz[i]))/(1+math.sqrt(cz[i]))
    q.append(q1)
pKk = []
for i in range(len(p)):
    pKk1 = pH[i]-(p[i]-q[i])
    pKk.append(pKk1)
pq = []
for i in range(len(p)):
    pq1 = p[i]-q[i]
    pq.append(pq1)
sredni_pKk = statistics.srednia(pKk)
odchylenie_pKk = statistics.odchylenie(pKk)

wyniki1.write("%-10s %-10s \n" %("p-q", "pH"))
for i in range(len(pH)):
    wyniki1.write("%-10.3f %-10.3f \n" %(pq[i], pH[i]))

regresja = statistics.regresja(pq, pH)
pKk_wykres = regresja[1]
odchylenie_pKk_wykres = regresja[3]


dane3 = plik3.readlines()
dane3.remove(dane3[0])
pH = []
VHCl = []
for wartosci in dane3:
    wartosci = wartosci.split()
    pH.append(float(wartosci[1]))
    VHCl.append(float(wartosci[0]))

cz = []
ck = []
for i in range(len(pH)):
    if pH[i]>=10.5:
        c = (VHCl[i]*cHCl)/(Vz+VHCl[i])+10**(-(14-pH[i]))
        ck.append(c)
    else:
        c = (VHCl[i]*cHCl)/(Vz+VHCl[i])
        ck.append(c)
for i in range(len(ck)):
    c = (fz*Vz*c0z)/(Vz+VHCl[i])-ck[i]
    cz.append(c)

p = []
q = []
for i in range(len(cz)):
    p1 = math.log(cz[i]/ck[i], 10)
    p.append(p1)
    q1 = (0.509*math.sqrt(ck[i]))/(1+math.sqrt(ck[i]))
    q.append(q1)

pKz = []
for i in range(len(p)):
    pKz1 = pH[i]-(p[i]+q[i])
    pKz.append(pKz1)
pq = []
for i in range(len(p)):
    pq1 = p[i]+q[i]
    pq.append(pq1)

sredni_pKz = statistics.srednia(pKz)
odchylenie_pKz = statistics.odchylenie(pKz)

wyniki2.write("%-10s %-10s \n" %("p+q", "pH"))
for i in range(len(pH)):
    wyniki2.write("%-10.3f %-10.3f \n" %(pq[i], pH[i]))

regresja = statistics.regresja(pq, pH)
pKz_wykres = regresja[1]
odchylenie_pKz_wykres = regresja[3]

print "Wartosc pKk wyznaczona numerycznie wynosi: %.3f. Niepewnosc pomiaru wynosi: %.3f" %(sredni_pKk, odchylenie_pKk)
print "Wartosc pKk wyznaczona z wykresu wynosi: %.3f. Niepewnosc pomiaru wynosi: %.3f" %(pKk_wykres, odchylenie_pKk_wykres)
print "Wartosc pKz wyznaczona numerycznie wynosi: %.3f. Niepewnosc pomiaru wynosi: %.3f" %(sredni_pKz, odchylenie_pKz)
print "Wartosc pKz wyznaczona z wykresu wynosi: %.3f. Niepewnosc pomiaru wynosi: %.3f" %(pKz_wykres, odchylenie_pKz_wykres)

plik1.close()
plik2.close()
plik3.close()
wyniki1.close()
wyniki2.close()
