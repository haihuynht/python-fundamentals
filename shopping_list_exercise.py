#Shopping List Exercise

shopping_list = []

for i in range(5):
    item = (input("Please enter a grocery item:"))
    shopping_list.append(item)
    print(item,"this has been added to your grocery list.")

for grocery in shopping_list:
    print(grocery)

print("Total Items:", len(shopping_list))
