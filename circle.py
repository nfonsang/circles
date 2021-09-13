# Developer A
## Create a function that computes the area of a circle
def circle_area(radius):
    pi = 3.14
    area = pi*(radius)**2
    return area

print("Testing the area function:")

print("The area of a circle with radius=10 is: ", circle_area(10))
print("The area of a circle with radius=15 is: ", circle_area(15))

# Develope a test function for the circle_area function
def test():
    assert circle_area(20)==1256
print(test()) 

# Developer B
## Create a function that computes the circumference of a circle 
