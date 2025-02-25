#Module 8 Homework for Demian_Packett
#making a function that accepts a list of sandwich ingredients

def make_sandwich(bread, *toppings):
    """Print a list of sandwiches with toppings and bread type that have been requested."""
    print(f"\nMaking a sandwich on {bread} with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
make_sandwich('sour dough', 'ham', 'cheese', 'lettuce', 'spicy mayo')
make_sandwich('wheat', 'roast beef','mushrooms', 'green peppers', 'onions', 'swiss cheese', 'mustard')