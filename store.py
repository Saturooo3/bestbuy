from products import Product


class Store:
    """
    A class representing a Store

    Attributes:
        list of products(name, price, quantity)
    """

    def __init__(self, product_list:list):
        """
        Initializes Store object.

        :param product_list: list of products with tuples as elements
        """
        self.product_list = product_list
        print(self.product_list)


    def add_product(self, product):
        """
        adds new product to list of products
        """
        self.product_list.append(product)


    def remove_product(self, product):
        """
        removes product from list of products
        """
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        """
        returns total quantity of offered products
        """
        return sum([product.get_quantity() for product in self.product_list])


    def get_all_products(self) -> list[Product]:
        """
        return list of offered products, that are available
        """
        return [product for product in self.product_list if product.quantity > 0]


    def order(self, shopping_list: list[tuple]) -> float:
        """
        gets a shopping list made of a tuples in a list and returns
        total price of order
        """
        total_price: float = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
