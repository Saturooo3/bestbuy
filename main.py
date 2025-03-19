from store import Store
from products import Product


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]


# best_buy = Store([bose, mac])
# price = best_buy.order([(bose, 5), (mac, 30), (bose, 10)])
# print(f"Order cost: {price} dollars.")
#
# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))


def start(best_buy):
    print("\n\tStore Menu\n\t----------")
    print("1. List all products in the store\n2. Show total amount in store\n3. Make an order\n4. Quit")


def display_products(best_buy, products):
    print("______")
    [print(f"{index+1}. {product.show()}") for index, product in enumerate(products)]
    print("______")


def display_total_amount(best_buy):
    print(f"\nTotal of {best_buy.get_total_quantity()} items in store.\n")


def get_order(best_buy, products):
    display_products(best_buy, products)
    print("When you want to finish order, enter empty text.")

    order: list[tuple]  = []

    while True:
        product_choice = input("Which product do you want? ")
        order_amount = input("What amount do you want? ")

        if product_choice == "" or order_amount == "":
            break

        else:
            print("Product added to list!\n")
            order.append((products[int(product_choice) - 1], int(order_amount)))

    total_price = best_buy.order(order)
    print("********")
    print(f"Order made! Total payment: ${total_price}")

dict_for_choice = {1: display_products,
                   2: display_total_amount,
                   3: get_order,
                   4: exit
                   }


def main():
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    while True:
        start(best_buy)
        try:
            choice = int(input("Please choose a number: "))
            if 1 <= choice <= 3:
                dict_for_choice[choice](best_buy, products)
            elif choice == 4:
                dict_for_choice[choice]()
            else:
                print("Enter a number between 1 and 4!")
                continue
        except ValueError:
            print("Enter a number between 1 and 4!")
            continue



if __name__ == "__main__":
    main()