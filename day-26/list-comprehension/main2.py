import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries
for (key, value) in student_dict.items():
    print(value)


students_data_frame = pandas.DataFrame(student_dict)
print(students_data_frame)
print("")
print("")
print("")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
for (index, row) in students_data_frame.iterrows():
    print(row.student)
    print(row.score)
    if row.student == "Angela":
        print("Score da Angela:", row.score)
