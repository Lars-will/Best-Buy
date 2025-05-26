from products import Product
from store import Store


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)


def start(store):
    """Displays menu, checks, and returns user input.
     if input is invalid, it returns 0
     """

    str_menu ="""1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit"""
    print("Welcome to the Best Buy store! Please make you selection: ")
    print(str_menu)
    int_selection = 0
    try:
        int_input = int(input(">> "))
        if 0 < int_input <= 4:
            int_selection = int_input
    except:
        pass
    return int_selection


def print_products():
    """Prints the products in the store"""
    lst_products = best_buy.get_all_products()
    for product in lst_products:
        print(product.show())


def collect_orders():
    """
    Collects the orders and adds them to shopping list.
    The function checks for valid input and if the shop has enough stock.
    Limitation: It is assumed for now that an item will be only added once per order.
    i.e. duplicates in the order list might lead to unexpected errors.
    """
    list_order = []
    print("If you are finished with your order, press Enter.")
    while True:
        bool_valid_id = False

        str_prod_id = input("Which product do you want to order? ")
        try:
            if str_prod_id == "":
                break
            int_prod_id = int(str_prod_id)
            bool_id_exists = False
            for product in best_buy.products:
                if product.id == int_prod_id:
                    bool_id_exists = True
            if not bool_id_exists:
                raise Exception
            bool_valid_id = True
        except:
            print("Please enter a valid product ID")

        bool_quantity_ok = True
        if bool_valid_id:
            str_quantity = input("How many would you like to order? ")
            try:
                if str_quantity == "":
                    break
                int_quantity = int(str_quantity)
                for product in best_buy.products:
                    if product.id == int_prod_id:
                        if product.quantity < int_quantity:
                            raise Exception
            except:
                bool_quantity_ok = False
                print("Please enter a valid quantity.")
        if bool_valid_id and bool_quantity_ok:
            for product in best_buy.products:
                if int_prod_id == product.id:
                    list_order.append((product, int_quantity))
    return list_order


def place_order():
    """
    Collects shopping list from user, validates input
    and calls the Store.order method
    """
    float_price = 0
    print("If you are finished with our order, press Enter.")
    list_orders = collect_orders()
    if len(list_orders) > 0:
        float_price = best_buy.order(list_orders)
    return float_price


def main():
    """Main program loop"""
    while True:
        int_selection = start(best_buy)
        print()
        if int_selection == 0:
            print("Error. Invalid input. Please enter a valid menu option.")
        elif int_selection == 1:
            print_products()
            print()
        elif int_selection == 2:
            print(f"Total of {best_buy.get_total_quantity()} products in store")
            print()
        elif int_selection == 3:
            print_products()
            print()
            float_total_price = place_order()
            print(f"Your order has been placed. Total Price: {float_total_price}")
            print()
        elif int_selection == 4:
            break


if __name__ == "__main__":
    main()


