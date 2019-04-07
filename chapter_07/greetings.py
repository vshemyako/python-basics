def greet_user(name: str = "Stranger") -> None:
    """Prints greeting message to standard output"""
    message_template = "Hello, {}!"
    greeting_message = message_template.format(name)
    print(greeting_message)


greet_user("Johnnie Walker")


def offer_food(name: str, food: str) -> None:
    greet_user(name)
    food_offer_template = "Here's your tasty {}! Enjoy!"
    food_offer_message = food_offer_template.format(food)
    print(food_offer_message)


offer_food("Clare", "Potatoes")

# basic usage of keyword arguments
offer_food(food="Tomato Soup", name="Jan")
