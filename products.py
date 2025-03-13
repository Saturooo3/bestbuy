class Product:
    def __init__(self, name, price, quantity):
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
        return self.quantity


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def set_quantity(self, quantity):
        self.quantity = quantity
        print(f"Total amount of {self.name} is stocked to {self.quantity}.")
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self) -> bool:
        return self.active


    def show(self):
        return f"{self.name}, {self.price}, {self.quantity}"


    def buy(self,  quantity) -> float:
        try:
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()

            elif self.quantity < 0:
                raise Exception(f"Quantity of {self.name} larger then exists")

        except Exception as e:
            print(e)

        total_price: float  = self.price * quantity
        return total_price











