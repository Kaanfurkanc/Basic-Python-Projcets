import datetime

start_time = datetime.datetime.now()
text = "lorem ipsum dolor sit amet consectetur adipiscing elit"
print("\nText : ",text)

str = input("Write the text !\n")
if (str == text):
    finish_time = datetime.datetime.now()
    time = finish_time - start_time
    seconds = round(time.total_seconds(),2)
    print("\nYou wrote the text in", seconds,"seconds . ")
else:
    print("Wrong input !")