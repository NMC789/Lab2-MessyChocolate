s = int(input("How many seconds?: "))

hours = s//3600
remainder1 = s%3600

minutes = remainder1//60

seconds = remainder1%60


print(str(s)+ " seconds = " + str(hours) + " hour, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
