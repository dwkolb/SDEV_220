#Author: Derek W. Kolb
#Version 1.  11/10/2023
#File Name: kolb_m03_caseStudy.py
# Description:This Python script defines two classes, Vehicle and Automobile, to create an Automobile 
# Information System. The Vehicle class serves as the superclass with a primary attribute for the type 
# of vehicle, while the Automobile class inherits from Vehicle and extends its attributes to include 
# details like year, make, model, doors, and roof type.
# The main() function prompts the user to input information about a specific vehicle, instantiates an 
# Automobile object with the provided data, and then displays the collected information in a clear and 
# readable format.


class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        
class Automobile(Vehicle):
    def __init__(self,vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
def main(): 

    #create an instance of the Automobile class
    car = Automobile(
        input("Enter type of vehicle (i.e. car, truck, plane, boat, or even a broomstick): "),
        input('Enter the year: '),
        input('Enter the make: '),
        input('Enter the model: '),
        input('Enter the number of doors (2 or 4): '),
        input('Enter the type of roof (i.e solid, sunroof, convertible): ')
    )
    
    #Output the data
    print('Vehicle Type: ', car.vehicle_type)
    print('Year: ', car.year)
    print('Make: ', car.make)
    print('Model: ', car.model)
    print('Number of doors: ', car.doors)
    print('Type of roof: ', car.roof)

if __name__ == "__main__":
    main()