def add(*args): #unlimited input arguments
    sum = 0
    for n in args:
        sum = sum + n
    print (sum)

def calculate(n, **kwargs):#unlimited keyword arguments
    print(kwargs)
    #for key,value in kwargs.items():
    #    print(key)
    #print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiple"]
    print(n)


add(12,1,2,3,3)
calculate(2, add=3, multiple = 5)

#class and kwargs

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.make = kwargs.get("model")
        self.make = kwargs["make"]
        self.model = kwargs["model"]


        #self.model = kwargs["model"]

my_car = Car(make = "Honda", model = "Civic")
print(my_car.model)
print(my_car.make)
