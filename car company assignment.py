class vehicle:

    def model(self):
        self.Mercedes_model_year={'E':1953,'S':1954,'G':1979,'C':1993,'A':1997}
        self.Bentley_model_year={'Mark V':1939,'Mark VI':1946,'Brooklands':1992,'Flying Spur':2005,'Bentayga':2015}
        self.Porsche_model_year={'911':1964,'Boxster':1996,'Cayenne':2002,'Panamera':2010,'Macan':2014}
class car(vehicle):
    def fuel(self):
        self.Mercede_fuel='Gasoline'
        self.Bentley_fuel='Bio-fuel'
        self.Porsche_fuel='Premium unleaded fuel'
    def mileage(self):
        self.Mercedes_mileage='16.9 Kmpl-23 Kmpl'
        self.Bentley_mileage='12.9 Kmpl'
        self.Porsche_mileage='18 mpg and 25 mpg'
class e_car(car):
    def battery_capacity(self):
        self.Mercedes_battery='107.8 kwh'
        self.Bentley_battery='18.0 kwh'
        self.Porsche_battery='93.4 kwh'
    def charging_capacity(self):
        self.Mercedes_charging='11 kW'
        self.Bentley_charging='8000 mah or 3.7 V'
        self.Porsche_charging='50 kW'
    

a=e_car()
car_name=['Mercedes','Bentley','Porsche']
choice=int(input('''
                   Press 1 for Mercedes:
                   Press 2 for Bentley:
                   Press 3 for Porsche:'''))
if choice==1:
    a.model()
    print("Details about MERCEDES : MODEL,YEAR,FUEL,MILEAGE,BATTERY CAPACITY, CHARGING CAPACITY")
    print("Mercedes with their repective year are:")
    for i in a.Mercedes_model_year:
        print(i,":",a.Mercedes_model_year[i])
    a.fuel()
    print("Fuel : ",a.Mercede_fuel)
    a.mileage()
    print("Mileage : ",a.Mercedes_mileage)
    a.battery_capacity()
    print("battery_capacity : ",a.Mercedes_battery)
    a.charging_capacity()
    print("charging_capacity : ",a.Mercedes_charging)

elif choice==2:
    a.model()
    print("Details about Bentley : MODEL,YEAR,FUEL,MILEAGE,BATTERY CAPACITY, CHARGING CAPACITY")
    print("Bentley with their repective year are:")
    for i in a.Bentley_model_year:
        print(i,":",a.Bentley_model_year[i])
    a.fuel()
    print("Fuel : ",a.Bentley_fuel)
    a.mileage()
    print("Mileage : ",a.Bentley_mileage)
    a.battery_capacity()
    print("battery_capacity : ",a.Bentley_battery)
    a.charging_capacity()
    print("charging_capacity : ",a.Bentley_charging)

elif choice==3:
    a.model()
    print("Details about Porsche : MODEL,YEAR,FUEL,MILEAGE,BATTERY CAPACITY, CHARGING CAPACITY")
    print("Porsche with their repective year are:")
    for i in a.Porsche_model_year:
        print(i,":",a.Porsche_model_year[i])
    a.fuel()
    print("Fuel : ",a.Porsche_fuel)
    a.mileage()
    print("Mileage : ",a.Porsche_mileage)
    a.battery_capacity()
    print("battery_capacity : ",a.Porsche_battery)
    a.charging_capacity()
    print("charging_capacity : ",a.Porsche_charging)
    
else:
    print("Choose 1 or 2 or 3 for details ")
print("THANKYOU")

