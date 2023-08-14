class Vehicle:
    def __init__(model, name):
        model.name = name

    def get_name(model):
        print("Vehicle name is %s" % model.name)
 
    def get_color(model):
        color = input()
        print("Vehicle color is %s" % color) 

Information = Vehicle("Hossein")
Information.get_name()
Information.get_color()