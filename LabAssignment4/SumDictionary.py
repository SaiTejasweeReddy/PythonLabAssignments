def avg(my_list): #defining a function to perform average operation
    for i in my_list: #a loop to iterate all the dictionaries in the list
        #using pop function to refer to the labels
        n1 = i.pop('LastGPA')
        n2 = i.pop('CurrentGPA')
        i['LastGPA+CurrentGPA'] = (n1 + n2)/2 #average of two numbers
    return my_list
#giving the desired input of a list containing dictionaries
my_dict=[
    {'course': 'python', 'LastGPA' : 90, 'CurrentGPA' : 80},
    {'course': 'python', 'LastGPA' : 95, 'CurrentGPA': 85},
    {'course': 'python', 'LastGPA' : 100, 'CurrentGPA': 100}
]
print(avg(my_dict)) #printing a list of dictionaries with sum of elements