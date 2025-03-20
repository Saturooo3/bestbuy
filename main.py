from store import Store
from products import Product


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]


def display_menu() -> None:
    """
    prints the help menu
    """
    print("\n\tStore Menu\n\t----------")
    print("1. List all products in the store\n2. Show total amount in store\n3. Make an order\n4. Quit")


def display_products(best_buy, products: list) -> None:
    """
    gets a list and prints the list
    """
    print("______")
    [print(f"{index+1}. {product.show()}") for index, product in enumerate(products)]
    print("______")


def display_total_amount(best_buy, products) -> None:
    """
    gets the store object and returns the total quantity of the items in the store.
    """
    print(f"\nTotal of {best_buy.get_total_quantity()} items in store.\n")


def get_choice_for_order(products) -> list[tuple]:
    """
    gets a list of products, asks for product and amount, that want to be ordered
    and creates tuples of name and amount of the chosen product returns the choice in a list
    """
    order: list[tuple] = []

    while True:
        try:
            product_choice = input("\nWhich product do you want? ")
            order_amount = input("What amount do you want? ")

            if product_choice == "" or order_amount == "":
                break

            elif int(order_amount) <= 0:
                print("Enter an amount over zero!")
                continue

            else:
                order.append((products[int(product_choice) - 1], int(order_amount)))
                print("Product added to list!")

        except ValueError:
            print("Error adding product!")
        except IndexError:
            print("Choose an offered product from the store!")
    return order


def get_order(best_buy, products) -> None:
    """
    gets store abject and list of products and prints the total price of the order
    """
    display_products(best_buy, products)
    print("When you want to finish order, enter empty text.")
    order = get_choice_for_order(products)
    total_price = best_buy.order(order)
    if total_price > 0:
        print(f"\n********\nOrder made! Total payment: ${total_price}")

dict_for_choice = {1: display_products,
                   2: display_total_amount,
                   3: get_order,
                   }


def main():
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    while True:
        display_menu()
        try:
            choice = int(input("Please choose a number: "))
            if choice < 1 or choice > 4:
                continue
            elif choice == 4:
                exit()
            else:
                dict_for_choice[choice](best_buy, products)
        except ValueError as e:
            print("Error with your choice! Try again!")



if __name__ == "__main__":
    main()