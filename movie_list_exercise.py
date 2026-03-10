#Movie List Exercise

movies_list = []

for i in range(5):
    movies = input("Please enter your favorite movie:")
    movies_list.append(movies)
    print("This movie has been added to your list.")

for i in range(len(movies_list)):
    print(i + 1, movies_list[i])