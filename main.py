from package.imdbrequest import ImdbRequest

def main():
    movies = ImdbRequest.get_movies(search="Inception 2010")

    print(movies[1].id)

main()
