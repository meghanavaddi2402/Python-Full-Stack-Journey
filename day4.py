'''
Senario to understand (*args and **kwargs)

#Employee details
def employees(*names,**settings):
    """Employee details with settings"""
    names = map(str,input("Employee names: ").split(','))
    for employee in names:
        print(employee)
    for key,value in settings.items():
        print("Key is: ",key)
        print("value is: ",value)
employees("x","y","z",dept="backend",experince="3 years",resume=True)

module - A Module is a simple python file(reusable,organized code)
- Using 'import' keyword we can access a module

'''      
#Employee details
def employees(*names,**settings):
    """Employee details with settings"""
    #names = map(str,input("Employee names: ").split(','))
    for employee in names:
        print(employee)
    for key,value in settings.items():
        print("Key is: ",key)
        print("value is: ",value)
#employees("x","y","z",dept="backend",experince="3 years",resume=True)
details = {"name":'meghana',"age":21,"location":"Vizag"}
print(__name__) #Dunder methods - Magic methods
