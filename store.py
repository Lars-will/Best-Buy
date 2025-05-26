class Store:
    """This class represents a store and manages the products within it"""

    def __init__(self, products):
        """Initializes the object."""
        self.products = products


    def add_product(self, product):
        """
        Adds product to the product list.
        Assumption: product is of type Product.
        """
        self.products.append(product)


    def remove_product(self, product):
        """
        Removes product to the product list.
        Assumptions: product is of type Product and product exists in the products list.
        """
        self.products.remove(product)


    def get_total_quantity(self):
        """Returns total number of products in the store"""
        int_count = 0
        for product in self.products:
            int_count += product.quantity
        return int_count


    def get_all_products(self) -> list:
        """Returns a list of all active products in the store"""
        lst_active_products = []
        for product in self.products:
            if product.active:
                lst_active_products.append(product)
        return lst_active_products


    def order(self, shopping_list):
        """
        Buys the products and returns the total price of the order.
        Assumption: product exists in the store
        """
        float_total_price = 0
        for Product, quantity in shopping_list:
            for product in self.products:
                if Product.name == product.name:
                    float_total_price += product.buy(quantity)
        return float_total_price
