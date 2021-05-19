# Dictionary Comprehension template
# a partir de uma lista
# new_dict = {new_key:new_value for item in list}
# a partir de um dicionario
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# Conditional Dictionary Comprehension template
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}

#Dictionary Comprehension
import random
names = ["Alex", "Beth", "Caroline", "Eleanor"]
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)


# Dictionary Comprehension 1 FROM A LIST
# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called result that takes each word in the given
# sentence and calculates the number of letters in each word.
# Try Googling to find out how to convert a sentence into a list of words.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?".split()

result = {word: len(word) for word in sentence}

print(result)


# Dictionary Comprehension 2 FROM A DICTIONARY
# Instructions
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
# degrees Celsius and converts it into degrees Fahrenheit.
# To convert temp_c into temp_f:
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# new_dict = {new_key:new_value for (key,value) in dict.items()}
weather_f = {day: (temp * 9/5) + 32 for (day, temp) in weather_c.items()}


print(weather_f)
