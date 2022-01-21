from restaurantData import *

print(15*"\n"+"Welcome to RR – the restaurant recommender!")
choice = input("What kind of restaurant do you want to go to?\nWrite two letters for an overview\n")[0:2]
print(f"Looking for: {choice}")

## check if input matches available types of restaurants
matches = []
for type in types:
    if type[0] == choice[0]:
        if type[1] == choice[1]:
            matches.append(type)

## print out the restaurant infos for the restaurants of matching type    
if matches:
    for match in matches:
        print("found: " + match, end=" • ")
    print(2*"\n")
    print("These are places matching your desires:\n")
    print("Name\t\t\tRating\t\tAddress" + "\n" + 60*"—")
    for restaurant in restaurant_data:
        if restaurant[0][0:2] == choice:
            tablen = 24-len(restaurant[1])       
            print(restaurant[1] + tablen * " " + restaurant[3] + "\t\t" + restaurant[4], end="")
            print()
    print("\n" + 60 * "—" + 2*"\n")
else:
    print("\nNothing found"+5*"\n")

