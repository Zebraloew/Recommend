from restaurantData import types
from restaurantData import restaurant_data

print(15*"\n"+"Welcome to RR – the restaurant recommender!")
#print(types)
#print(types[0][0]) # "g"
choice = input("What kind of restaurant do you want to go to?\nWrite two letters for an overview\n")[0:2]
print(f"Looking for: {choice}")
matches = []
for type in types:
    if type[0] == choice[0]:
        #print(f"Found something: {type}")
        if type[1] == choice[1]:
            print(f"This fits totally: {type}")
            matches.append(type)
            #print(matches)
    else: 
        #print("still looking.")
        pass
if matches:
    