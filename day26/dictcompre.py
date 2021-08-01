
import random

import pandas

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freedie']
students_score = {student:random.randint(1,100) for student in names}
print(students_score)

passed_students = {student:score for (student,score) in students_score.items()
                   if score>60}
print(passed_students)

#new challenge

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
letter_list = sentence.split()
word_count = {word:len(word) for word in letter_list }
print(word_count)



# new challenge
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
# Write your code 👇 below:
weather_f = {day:temp_c*9/5+32 for (day,temp_c) in weather_c.items()}
print(weather_f)

pi_multiplier = {
    "Circle_1": 90,
    "Circle_2": 12,
    "Circle_3": 98,
    "Circle_4": 33,
    "Circle_5": 11
}
print(pi_multiplier)
pi_circle = {circlenum:size*3.141562 for (circlenum,size) in pi_multiplier.items()}
print(pi_circle)


student_dict = {
    "student": ["angela","asher", "anvil", "seth"],
    "score": [11,23,24, 99]
}
#Looping through dictionary
for key,value in student_dict.items():
    print(key)
    print(value)

dfStudent_dict = pandas.DataFrame(student_dict)
print(dfStudent_dict)

#loop through a data frame
for key,value in dfStudent_dict.items():
    print(key)
    print(value)

#loop thorough a rows of data frame
for (index,row) in dfStudent_dict.iterrows():
    print(row.student)
    print(row.score)
