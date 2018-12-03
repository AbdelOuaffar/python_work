import sys
from datetime import datetime as date
import pandas as pd


class Product:
    def __init__(self, category, product_id, product_name, price, quantity_on_hand):
        self.category = category
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity_on_hand = quantity_on_hand


class Orders:
    def __init__(self, order_id, order_date, product_id,  quantity_ordered):
        self.order_id = order_id
        self.order_date = self.parse_order_date(order_date)
        self.product_id = product_id
        self.quantity_ordered = quantity_ordered

    def parse_order_date(self, order_date):
        self.order_date = date.strptime(order_date, '%y/%m/%d')
        return order_date


def parse_product_file(file2):
    file = open(file2)
    products_from_class = []
    file.readline()
    for line in file:
        newline = line.split(",")
        products_from_class.append(Product(newline[0], newline[1], newline[2], newline[3], newline[4]))
    file.close()
    return products_from_class


def orders_file(file1):
    file = open(file1)
    file.readline()
    orders1 = []

    parse_line = [line.split(",") for line in file.readlines()]
    for element in parse_line:
        orders1 += [Orders(element[0], element[1], element[2], element[3])]
    return orders1


def order_file_dictionary(order_file):
    orders = {}
    for order in order_file:

        if order.product_id in orders:
            orders[order.product_id].append([order.order_id, order.order_date, order.quantity_ordered])
        else:
            orders[order.product_id] = [[order.order_id, order.order_date, order.quantity_ordered]]

    return orders


def parse_orders(file1):
    orders = {}
    file = open(file1)
    file.readline()
    for line in file:
        order = line.split(",")
        orders[order[0]] = [(order[1]), order[2], float(order[3])]
    file.close()

    return orders


def orders_two_dates(date1, date2, orders1):
    start_date = date.strptime(date1, '%y/%m/%d')
    end_date = date.strptime(date2, '%y/%m/%d')

    order_start_end = []
    for key in orders1:
        for element in orders1[key]:
            order_date = date.strptime(element[1], '%y/%m/%d')
            if start_date <= order_date <= end_date:
                order_start_end += [(key, element)]

    return order_start_end


def parse_orders_file():

    retrieve_orders = {}
    file = open("orders.txt")
    file.readline()
    for line in file:
            newline = line.split(",")
            retrieve_orders[newline[2]] = [newline[0], newline[1], newline[3]]
            for line1 in file:
                newline = line1.split(",")
                if newline[2] in retrieve_orders:
                    retrieve_orders[newline[2]].append([newline[0], newline[1], newline[3]])
                else:
                    retrieve_orders[newline[2]] = [newline[0], newline[1], newline[3]]
    file.close()
    return retrieve_orders


def parse_by_category(products):

    file_by_category = []

    search_category = ["kitchen", "Electronic"]
    for category in search_category:
        for product in products:
            if product.category == category:
                file_by_category += [[product.category, product.product_id, product.product_name, product.price
                                         , product.quantity_on_hand]]
    return file_by_category


def search_product_by_name(product_name, products):

    for product in products:
        if product.product_name == product_name:
            print(product.product_name, product.category, product.price, product.quantity_on_hand)
            return


def search(key_search,orders1, orders, products):

        while key_search != 0:
            if key_search == 1:
                category = parse_by_category(products)
                for element in category:
                    print(element)
            elif key_search == 2:
                product_id = input("enter product id :E1,K1,E2,K2, O1:")
                for key in orders:
                    if key == product_id:
                        print(orders[key])

            elif key_search == 3:
                product_name = input("enter product name  :")
                search_product_by_name(product_name, products)

            elif key_search == 4:

                start_date = input("enter start search date (yy/mm/dd) :")
                end_date = input("enter end search date as(yy/mm/dd) :")
                if start_date <= end_date:
                    result = orders_two_dates(start_date, end_date, orders1)
                    for element in result:
                        print(element)
                else:
                    result = orders_two_dates(end_date, start_date, orders)
                    for element in result:
                        print(element)

            key_search = int(input("  enter   0: quit \n"
                                   "          1: to list product by category\n"
                                   "          2:list all orders for a given product\n "
                                   "          3:search product by name \n "
                                   "          4:to see orders between a specific date range :\n"))


def main():
    if len(sys.argv) != 3:
        print('Need only 3 argument for this program')
        return
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    order = orders_file(file1)
    orders = order_file_dictionary(order)
    products = parse_product_file(file2)
    orders1 = parse_orders_file()
    key_search = int(input("enter 1:to list product by category\n"
                           "      2:list all orders for a given product\n "
                           "      3:search product by name \n "
                           "      4:to see orders between a specific date range :\n"))

    search(key_search, orders, orders1, products)


if __name__ == "__main__":
    main()


