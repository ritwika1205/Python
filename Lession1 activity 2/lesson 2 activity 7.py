class employee:
    def __init__(self):
        print("enplyee created")
    def __del__(self):
        print("employee created, employee deleted")
obj=employee()
del obj