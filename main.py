# Data Types in Python
from pyscript import display, document

#String
name = 'Athena Luisa C. Alfaro'
#Integer
_age = 15
#Floar
height = 152.4
#Boolean
student_type = False
#List
countries = ['France', 'Greece', 'Austria', 'Switzerland']
#Dictionary
facts = {'color':'pink', 'car_brand':"Toyota", 'shoe_size':'7','best_friend':'Rafa'}
#set
fruits = set(['Strawberry', 'Blueberry', 'Apple'])
#tuple
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

display(type(name),
target='result')
display(type(_age),
target='result')
display(type(height),
target='result')
display(type(is_it_suspended),
target='result')
display(type(Sections),
target='result')
display(type(math_teachers),
target='result')
display(type(science_teachers),
target='result')
display(type(sample_dictionary),
target='result')

document.getElementById('result').innerHTML = f'Hello! My name is <i>{name} {middle_name}</i>. I am {_age} years old and I am {height}cm tall .I am a new student{student_type}. I would like to go to {countries}, My favorite color is {color}, my car is a {car_brand}, my shoe size is {shoe_size} And my bestfriend is {best_friend}. My favorite fruits are {fruits} and I read on {days_of_week}