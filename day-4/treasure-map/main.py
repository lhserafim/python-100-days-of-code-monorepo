# 🚨 Don't change the code below 👇
# I'm using emojis
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#split position = position.split(",")
position_y = int(position[0])
position_x = int(position[1])

# O -1 é para evitar que saia do index da lista, uma vez que a lista começa com 0
map[position_x - 1][position_y - 1] = "✖️"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")