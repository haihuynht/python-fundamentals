#temperature_exercise
#Hai Huynh
#03-09-2026

#temperatures given in the exercise
temperatures = [72, 85, 91, 68, 77, 95, 82]

#placing both total and count variables as this exercise requires a count and sum (total)
total = 0
count = 0

#for temp in temperatures is listing the temp as the loop and temperature is the list
for temp in temperatures:
    #putting in conditional if/else/elif
    if temp > 80:
        #counting temperatures greater than 80, don't forget to add 1 since Python counts 0 first.
        count += 1
        #total temperatures being added together (if you see temp above, we're adding all temp)
        total += temp

#print outside of the loop
print("Temperatures above 80:", count, "Sum of the temperatures:", total)