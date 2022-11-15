"""Restaurant rating lister."""
def readratings(filename):
    with open(filename) as file:

        ratings = {}
        new_restautant = input("give me a new restaurant: ")
        new_rating = int(input("give me a rating between 1 and 5: "))
        
        while new_rating < 1 or new_rating > 5:
            new_rating = int(input("give me a rating between 1 and 5: "))

            # if new_rating not in range(5):
                # new_rating = int(input("give me a rating between 1 and 5: "))
            # if new_rating in range(5):
            #     break
            # break
        ratings[new_restautant] = new_rating

        for line in file:
            line = line.rstrip().split(":")
            restaurant = line[0]
            rate = line[1]
            # resturant, rate = line.rstrip().split(":")
            ratings[resturant] = rate

        sorted_rating = sorted(ratings)

        for restaurant in sorted_rating:
            print(f'{restaurant} in rated {ratings[restaurant]}')
        
readratings("scores.txt")

    # put your code here
