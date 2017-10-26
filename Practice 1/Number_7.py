"""
7.С начала суток прошло H часов, M минут, S секунд (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
По данным числам H, M, S определите угол (в градусах), на который повернулаcь часовая стрелка с начала суток и выведите его в виде действительного числа.
"""
import math
import angles

def second_arrow(second):
    return second * math.pi / 30

def minute_arrow(minute, second):
    return (minute * math.pi / 30) + (second_arrow(second) / 60)

def hour_arrow(hour, minute, second):
    return ((hour * math.pi) / 12) + (minute_arrow(minute, second) / 24)

hour = float(input("Hour = "))
minute = float(input("Minute = "))
second = float(input("Second = "))

# angle = (hour * (360/12)) + (minute * (360/60)) + (second * (360/3600)

# ang = hour + minute/60 + second/3600
angle = hour_arrow(hour, minute, second) * angles.r2d(math.pi)
print("Angle = ", angle)