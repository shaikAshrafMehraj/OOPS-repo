class employee:

    # these are the special methods / dunder methods or constructor
    def __init__(self):
        print("**Starting executing the attributes")
        self.id = 123
        self.salary = "$50,000"
        self.designation = "SDE"
        print("**attributes have been initiated")

    def travel(self,destination):
        print("**This travel function was called manually")
        print(f"Employee is now travelling to {destination}")

sam = employee()

# print(sam.id)
# print(sam.salary)
# print(sam.designation)

# sam.travel("hyd")

print(type(sam))