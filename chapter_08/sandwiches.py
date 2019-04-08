def make_sandwich(*toppings) -> None:
    print("Making a sandwich with toppings:")
    for topping in toppings:
        print("- {}".format(topping))
    print()


make_sandwich("cheese")
make_sandwich()
make_sandwich("cheese", "cucumber", "tomato", "beacon")
