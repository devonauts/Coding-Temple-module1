# a = input("Whats your name?")
# b = input("Age?")
# c = input("favorite color?")

# print(a,b,c)


excelent = "Excelent"
good = "Good"
needs_improvement = "Needs improvement"

score = 0

score = int(input("What was your score?"))

if score >= 90 :
 print(excelent)
elif score < 90 and score >70 :
 print(good)
else :
 print(needs_improvement)