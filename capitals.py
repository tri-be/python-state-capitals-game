import random
# an array of state dictionaries
states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

test = [
{
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}
]

score = {
    "points": 0,
}

print("############################################# ")
print("--------------------------------------------- ")
print("Welcome to the States Capital Guessing Game!")
print("Can you guess the capitals of all 50 states?")

# set initial points to 0
points = 0
play = True
while play == True:
    # shuffle the order of the states to make it harder for player to guess the capitals
    random.shuffle(states)
    for i in states:
        print("--------------------------------------------- ")
        print("--------------------------------------------- ")
        print(f'State: {i["name"]}')
        letters = i["capital"][0:3]
        hint = input("Would you like a hint? Y/N ")
        if hint == "Y" or hint == "y":
            print(f"The first 3 letters of the capital are: {letters}")
            print('--------------------------------------------------')
            print('--------------------------------------------------')
        else:
            pass
        guess = input("Capital: ")
        if guess == i["capital"]:
            points += 1
            if "correct" not in i:
                i["correct"] = 1
            else:
                i["correct"] += 1
            print('---------------------------------------------------------------------------------')
            print('---------------------------------------------------------------------------------')
            print(f'Correct! Number of times you have answered this capital correctly: {i["correct"]}')
            print(f'You now have {points} points.')
        else:
            if "wrong" not in i:
                i["wrong"] = 1
            else:
                i["wrong"] += 1
            print('---------------------------------------------------------------------------------')
            print('---------------------------------------------------------------------------------')
            print(f'Wrong. Number of times you have answered this capital incorrectly: {i["wrong"]}')
            print(f'You have {points} points.')

    start = input("Play Again? Y/N ")

    if start == "Y" or start == "y":
        play = True
    else:
        play = False
        print('---------------------------------------')
        print('---------------------------------------')
        print(f"Your final score is {points} points.")
        for i in states:
            if "correct" in i:
                pass
            else:
                print('------------------------------------------------------------')
                print(f'You were unable to answer with the capital of {i["name"]}')
                print(f'The capital of {i["name"]} is {i["capital"]}')
        print('---------------------------------------')
        print('#######################################')
        print("Thank you for playing!")
                









