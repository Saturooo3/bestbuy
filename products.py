class Product:
    """
    A class representing a Product

    Attributes:
        name, price, quantity
    """
    def __init__(self, name:str, price: int, quantity:int):
        """
        Initializes a Product object.

        :param name: name of product
        :param price: price of product
        :param quantity: quantity of product
        """
        try:
            self.name: str = name
            if not isinstance(self.name, str):
                raise Exception("No valid name")

            self.price: float = price
            if self.price < 0:
                raise Exception("No prices below zero.")

            self.quantity: int = quantity
            if self.quantity < 0:
                raise Exception("No quantity below zero")
            self.active = True

        except Exception as e:
            print(e)
            self.active = False


    def get_quantity(self) -> int:
        """
        returns quantity of object
        """
        return self.quantity


    def activate(self):
        """
        activates product
        """
        self.active = True


    def deactivate(self):
        """
        deactivates product
        """
        self.active = False


    def set_quantity(self, quantity: int):
        """
        sets quantity of product

        :param quantity: quantity of product
        """
        self.quantity = quantity
        print(f"Total amount of {self.name} is stocked to {self.quantity}.")
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        return the variable active to show if product is active or not
        """
        return self.active


    def show(self):
        """
        prints name, price and available quantity of product
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self,  quantity: int) -> float:
        """
        return total price of the order if the ordered quantity is available,
        if not returns zero

        :param quantity: quantity of product, that is ordered
        """
        if self.quantity >= quantity:
            self.quantity -= quantity
            total_price: float = self.price * quantity
            if self.quantity == 0:
                self.deactivate()
            return total_price
        else:
            print(f"Error while making order. Quantity of {self.name} larger then exists")
            return 0