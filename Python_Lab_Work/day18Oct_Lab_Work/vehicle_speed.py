# Write a program to calculate speed of a vehicle
#     whose distance and time has been given using a function.

def speed(distance, time):
    return distance / time


d = float(input("Enter distance (in km): "))
t = float(input("Enter time (in hours): "))

print("Speed of vehicle:", speed(d, t), "km/h")
