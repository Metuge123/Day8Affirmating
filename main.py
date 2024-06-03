name = input("What is your name? ")
print("Hello" +  name)
date = input("What is the date of today? ")
print("Today" + date)
print("Hello" + name + "Today" + date)
if name == "Dave" or name == "dave":
  print("Hello Dave")
  DOW = input("What is the day of the week? ")
  if DOW == "Monday" or DOW == "monday":
    print("It is going to be a great Monday", name)
    if DOW == "Tuesday" or DOW == "tuesday":
      print("What a wonderfull Tuesday it is", name)
      if DOW == "Wednesday" or DOW == "wednesday":
        print("Happy Hump Day", name)
        if DOW == "Thursday" or DOW == "thursday":
          print(name, "Your week is almost over!")
          if DOW == "Friday" or DOW == "friday":
            print(name, "It's Friday")

elif name == "David" or name == "david":
  DOW = input("What is the day of the week")
  if DOW == "monday" or DOW == "Monday":
    print("It is going to be a great Monday", name)
    if DOW == "tuesday" or DOW == "Tuesday":
      print("You look great in that color", name)
      if DOW == "wednesday" or DOW == "Wednesday":
        print("You look chipper today", name)
        if DOW == "thursday" or DOW == "Thursday":
          print(name, "you are doing a great job!")
          if DOW == "friday" or DOW == "Friday":
            print(name, "it's Friday")

else:
  print("I do not know your name, but I hope you have a graet day!")
