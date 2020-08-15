# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base

# Base Class
class Vehicle():
    def __init__(self):
        pass

# Inherits from Vehicle


class FlightVehicle(Vehicle):
    def __init__(self):
        pass

# Inherits everything from The main class Vehicle and FlightVehicle


class Starship(FlightVehicle):
    def __init__(self):
        pass

# Inherits everything from The main class Vehicle and FlightVehicle


class Airplane(FlightVehicle):
    def __init__(self):
        pass

# Inherits everything from the main class Vehicle


class GroundVehicle(Vehicle):
    def __init__(self):
        pass

# Takes everything from GroundVehicle to Vehicle


class Car(GroundVehicle):
    def __init__(self):
        pass

# Takes everything from GroundVehicle to Vehicle


class Motorcycle(GroundVehicle):
    def __init__(self):
        pass
