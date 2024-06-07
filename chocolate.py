weight = float(input("What is your weight, in pound?: "))
height = float(input("What is your height, in inches?: "))
age = float(input("What is your age?: "))
bmr_woman = 655.1+(4.35*weight)+(4.7*height)-(4.7*age)
bmr_man = 66+(6.2*weight)+(12.7*height)-(6.76*age)

final_num_w = str(bmr_woman/214)
final_num_m = str(bmr_man/214)

print("Necessary chocolate bars for a woman to sustain weight: " + final_num_w)
print("Necessary chocolate bars for a man to sustain weight: " + final_num_m) 
