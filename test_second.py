x = 60
for x in range(10,181,10):
    print("Time Limit: " + str(x))
    s_h = x/2
    print("Second Half")
    print(s_h)
    cardio = s_h*0.8
    if cardio > 50:
        print("Heavy Bag")
        print(40)
        print("Bike")
        print(cardio-40)
    else:
        print("Heavy Bag")
        print(cardio)


    print("Alt Lifts")
    print(s_h*0.1)
    print("Stretch")
    print(s_h*0.1)
    print("\n\n")
