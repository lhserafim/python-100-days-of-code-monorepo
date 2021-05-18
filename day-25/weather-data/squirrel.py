import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data["Primary Fur Color"])

gray_s_count = len(data[data["Primary Fur Color"] == "Gray"])
red_s_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_s_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_s_count)
print(red_s_count)
print(black_s_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_s_count, red_s_count, black_s_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("new_data.csv")