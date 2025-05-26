class Product:
    """This class represents a product and contains relevant properties and methods"""
    count = 0

    def __init__(self, name, price, quantity):
        """Initialize Object"""
        if name != "":
            self.name = name
        else:
            raise Exception("Error: String is empty.")

        if price >= 0 and (type(price) == float or type(price) == int):
            self.price = float(price)
        else:
            raise Exception("Error: Invalid price.")

        if quantity >= 0 and type(quantity) == int:
            self.quantity = quantity
        else:
            raise Exception("Error: Invalid Quantity.")
        Product.count += 1
        self.id = Product.count
        self.active = True


    def get_quantity(self, quantity) -> int:
        """Getter function for quantity"""
        return self.quantity


    def set_quantity(self, quantity):
        """Setter function for quantity"""
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False


    def is_active(self) -> bool:
        """Getter function for active"""
        return self.active


    def activate(self):
        """Sets active to True"""
        self.active = True


    def deactivate(self):
        """Sets active to False"""
        self.active = False


    def show(self) -> str:
        """Returns a string with name, price and quantity"""
        return f"{self.id}: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """Buys certain quantity of the product.
        -> Returns total price(float)
        -> Updates quantity
        -> Raises an Exception when quantity is not of type int
        """

        if type(quantity) is not int:
            raise Exception("Error: Quantity needs to be of type int.")
        else:
            self.quantity -= quantity
            return quantity * self.price
