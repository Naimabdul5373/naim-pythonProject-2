favorite_movies =[]

for i in range(5):
    movie = input("enter your favorite movie:")
    favorite_movies.append(movie)
    
    print("\n here is your favorite movies:")
    
    
    
    for movie in favorite_movies:
        print(f"{movie}")
        