from products import Product


class Store:
    def __init__(self, product_list:list):
        self.product_list = product_list


    def add_product(self, product):
        self.product_list.append(product)


    def remove_product(self, product):
        self.product_list.remove(product)


    def get_total_quantity(self) -> int:
        return sum([product.quantity for product in self.product_list])


    def get_all_products(self) -> list[Product]:
        return [product for product in self.product_list if product.quantity > 0]


    def order(self, shopping_list: list[tuple]) -> float:
        total_price = 0

        for product, quantity in shopping_list:
            price = product.buy(quantity)
            total_price += price

        return total_price