import math

altitude = int(input("altitude:"))
a1 = -0.0065
a3 = 0.0010
a4 = 0.0028
a6 = -0.0028
a7 = -0.0020
R = 287.00
c1 = - 9.80665 / (a1 * R)
c3 = - 9.80665 / (a3 * R)
c4 = - 9.80665 / (a4 * R)
c6 = - 9.80665 / (a6 * R)
c7 = - 9.80665 / (a7 * R)
T0 = 288.15
h0 = 0
p0 = 101325
T = T0
h = h0
p = p0
po = p
rho0 = p0 / (R * T0)
rho = rho0
"""this for loop increases the altitude 1m at a time and calculates
the new temperature at each step until it reaches the inputed
altitude. i in this loop is the current height, and we subtract h
because it is still the old h, which gives dh (which is 1 in this case). Then we update h to
be the new height."""
for i in range(altitude + 1):
    if i <= 11000:
        To = T #keep track of previous T so that we can use it to find pressure
        T += a1 * (i - h)
#use the old pressure to calculate a new pressure, then update the old pressure to
# the new pressure to use it in the next calculation
        p = po * (T / To)**c1
        po = p
        rho = p / (R * T)
        h = i
    elif i <= 20000:
        T = T
        p = po * math.exp((-9.80665/(R*T))*(i-h))
        po = p
        rho = p / (R * T)
        h = i
    elif i <= 32000:
        To = T
        T += a3 * (i -h)
        p = po * (T / To)**c3
        po = p
        rho = p / (R * T)
        h = i
    elif i <= 47000:
        To = T
        T += a4 * (i -h)
        p = po * (T / To)**c4
        po = p
        rho = p / (R * T)
        h = i
    elif i <= 51000:
        T = T
        p = po * math.exp((-9.80665/(R*T))*(i-h))
        po = p
        rho = p / (R * T)
        h = i
    elif i <= 71000:
        To = T
        T += a6 * (i -h)
        p = po * (T / To)**c6
        po = p
        rho = p / (R * T)
        h = i
    elif i <= 84852:
        To = T
        T += a7 * (i -h)
        p = po * (T / To)**c7
        po = p
        rho = p / (R * T)
        h = i

print(rho)


