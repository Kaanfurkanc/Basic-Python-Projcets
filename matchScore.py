teamName = input("Enter team name : ")
matchNumber = int(input("Enter match number : "))
total_point = 0
teamFile = teamName + ".txt"
while matchNumber > 0:
    status = int(input("Enter 1 for the win\nEnter 2 for draw in match\nEnter 3 for defeat \n"))
    if status == 1:
        total_point += 3
    elif status == 2:
        total_point += 1
    elif status == 3:
        total_point += 0
    matchNumber -= 1

with open(teamFile,"w",encoding="utf-8") as file:
    file.write("Total point of ")
    file.write(teamName)
    file.write(" = ")
    file.write(str(total_point))

with open(teamFile,"r+",encoding="utf-8") as file:
    print(file.read())