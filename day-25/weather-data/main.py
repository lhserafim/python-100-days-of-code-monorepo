import csv
import pandas

# DataFrame is the role table
# Series are the columns

# using csv library
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # print(temperatures)


# using pandas
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

# calculating the average
print(data["temp"].mean())

# getting the max value
print(data["temp"].max())

# I can use the table headings as a attribute. Panda has converted it
# CaseSensitive attribute!!
print(data.Day)
print(data.temp)
print(data.condition)

# Get data in row
print("Get data in a row")
print(data[data.Day == "Monday"])

print(data[data.temp == data.temp.max()])

# Get a value from in a row
print("Get a value from in a row")
monday = data[data.Day == "Monday"]
print(monday.condition)

monday_temp = int(monday.temp)
print(monday_temp)

# create a dataframe from scratch
data_dict_ex = {
    "students": ["Luiz", "Henrique", "Sanches", "Serafim"],
    "scores": [89, 24, 88, 66]
}
data = pandas.DataFrame(data_dict_ex)
print(data)
data.to_csv("new_data.csv")