weather = input("is the weather rainy or sunny?")
mood = input("are you happy or tired?")

if weather == "sunny" and mood == "happy" :
    print("Go for a hike!")
elif weather == "rainy" or weather == "sunny" and mood == "tired":
    print("relax indoors")
elif weather == "rainy" and mood == "happy":
    print("relax indoors")
else: print("relax indoors")