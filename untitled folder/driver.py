from meow import FancyFoodOrder  
def create_object_list():
    object_list = []

    try:
        num_items = int(input("How many items will you order today? "))
        if num_items < 1:
            raise ValueError("Number of items must be at least 1.")

        for i in range(1, num_items + 1):
            print(f"Item #{i}-")
            food_name = input("Enter food: ")
            amount = float(input("Enter amount of pounds: "))

            while amount <= 0:
                print("Amount of pounds must be greater than 0.")
                amount = float(input("Enter amount of pounds: "))

            item = FancyFoodOrder(food_name, amount)
            object_list.append(item)

    except ValueError as ve:
        print(f"{ve} Please try again.")

    return object_list

def display_object_list(object_list):
    for item in object_list:
        print(item)

def calculate_total_cost(object_list):
    total_cost = 0.0
    for item in object_list:
        total_cost += item.calculate_cost()
    return total_cost

def main():
    items_list = create_object_list()
    display_object_list(items_list)
    total_cost = calculate_total_cost(items_list)
    print(f"\nTotal cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
