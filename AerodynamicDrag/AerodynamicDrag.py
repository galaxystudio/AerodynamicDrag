import math

x = float(input("Please input the original x:"))
y = float(input("Please input the original y:"))

vx = float(input("Please input the original velocity x:"))
vy = float(input("Please input the original velocity y:"))
v = math.sqrt(vx * vx + vy * vy)
ax = 0
ay = 0

t = float(input("Please input the time:"))
t_interval = float(input("Please input the time intervel:"))

aera = float(input("Please input the sphere's area:"))
mess = float(input("Please input the sphere's mess:"))

C = 0.05
density = 1.293
g = 9.8

k = 0.5 * C * density * aera / mess
n = int(t / t_interval + 1)
t_present = 0

f = open("data.csv","w")
f.write("time,x,y,vx,vy,ax,ay\n")
f.close()

for i in range(0, n):
    f = open("data.csv","a")
    f.write("%f,%f,%f,%f,%f,%f,%f\n" % (t_present, x, y, vx, vy, ax, ay))
    f.close()

    ax = - k * v * vx
    ay = - k * v * vy - g

    vx = vx + ax * t_interval
    vy = vy + ay * t_interval

    x = x + vx * t_interval
    y = y + vy * t_interval

    t_present = t_present + t_interval

