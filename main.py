class Employee:
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("destructor created, Employee deleted")

obj = Employee()
del obj