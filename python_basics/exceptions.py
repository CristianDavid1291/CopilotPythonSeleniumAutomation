ItemsInCar = 5

if ItemsInCar < 10:
    raise Exception("There are less than 10 items in the car")

#try and except

try:
    ItemsInCar = 5
    if ItemsInCar < 10:
        raise Exception("There are less than 10 items in the car")
except Exception as e:
    print(f"An exception occurred: {e}")
# finally block 
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
    
