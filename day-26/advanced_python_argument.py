

# advanced python argument

def my_function(a, b, c):
    # Do this with a
    # Then do this with b
    # Finally do this with c
    return a, b, c

# 3개의 argument(인수) 를 가지고 있는 my_function
my_function(a=1, b=2, c=3)

# Unlimited Arguments
# 아스테리스크
# def add(*args): # Parameter(매개변수)
#     for i in args:
#         print(i)

def add(*args): # 아스테리스크를 이용한 해당 가변 인수는 가변 위치 인수라고도 불린다
    print(args)
    return sum(args)

ans = add(1,2,3,4,5)
print(ans)




# 2개의 아스테리스크
def calculate(**kwargs): # 2개의 아스테리스크를 이용하여 가변 위치 인수를 만들어줌
    print(kwargs)

calculate(name="name", age=12)


class Car:

    def __init__(self, **keg):
        # self.make = keg["make"]
        self.make = keg.get("make") or "a"
        # self.model = keg["model"]
        self.model = keg.get("model") or "b"


# car = Car(make="Nissan", model="GT-8")
car = Car(make="Nissan")
print(car.make)
print(car.model)

