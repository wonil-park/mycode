#!/usr/bin/env python3
intro = "can we guess your car with 4 random questions?"
print(intro.title())

def main(): 
    questions = ["choose a pet", "pick a fast food to eat in the car", "pick a song to blast in the car", "Pick A '90s Movie"]
    choices = {"choose a pet": ["A 'lil pig", "A fluffy puppy", "A floofy kitten", "A nice goat", "A happy rat", "A chill lizard"], "pick a fast food to eat in the car": ["Taco Bell", "McDonald's", "Subway", "Arby's"], "pick a song to blast in the car": ["Beyonce - Daddy Lessons", "Fall Out Boy - Sugar, We're Goin Down", "Rae Sremmurd - Black Beatles", "Taylor Swift - Bad Blood", "Tim McGraw - I like, I Love It"], "Pick A '90s Movie":["Titanic", "The Little Rascals", "Terminator 2: Judgement Day", "My Best Friend's Wedding", "Jurassic Park", "Friday"]}
    cars = ["Jeep Wrangler", "Toyota Camry", "Chevy Impala", "BMW M4", "VW Golf"]
    point = 0

    while len(questions) > 0:
        q = questions.pop()
        print(q.title())

        current_q = choices[q]
        
        for choice in current_q:
            print(current_q.index(choice)+1, choice.title())
        a = input("Please choose an answer: ")
        
        try:
            if int(a) <= len(current_q) and int(a) > 0:
                point += int(a)
                print()
            else:
                questions.append(q)
        except:
            print("Invalid input. Please select an answer")
            questions.append(q)

    msg = "Your car is: "
    if point >= 18:
        msg += cars[0]
    elif point >= 14:
        msg += cars[1]
    elif point >= 10:
        msg += cars[2]
    elif point >= 6:
        msg += cars[3]
    else:
        msg += cars[-1]

    print(msg)

main()
