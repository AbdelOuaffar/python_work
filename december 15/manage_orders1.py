import sys
from datetime import datetime as date
import ord


class Orders:
    def __init__(self, order_id, order_date, product_id,  quantity_ordered):
        self.order_id = order_id
        self.order_date = self.parse_order_date(order_date)
        self.product_id = product_id
        self.quantity_ordered = quantity_ordered

    def parse_order_date(self, date1):
        self.order_date = date.strptime(date1, '%y/%m/%d')
        return date1


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


def orders_two_dates(date1, date2, order):
    start_date = date.strptime(date1, '%y/%m/%d')
    end_date = date.strptime(date2, '%y/%m/%d')
    order_start_end = []
    for element in order:
            order_date1 = date.strptime(element.order_date, '%y/%m/%d')
            if start_date <= order_date1 <= end_date:
                order_start_end += [element]

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


def search(key_search, orders, order, products):

        while key_search != 0:

            if key_search == 1:
                category = ord.parse_by_category(products)
                for element in category:
                    print(element)
            elif key_search == 2:
                product_id = input("enter product id :E1,E2,E3,E4,E5,K1,K2,K3,K4,K5,O1,O2,H1:")
                keys = orders.keys()
                if product_id not in keys:
                        print("no orders for this product")

                else:

                    for key in orders:
                        product_name = ord.product_id_product_name(products, product_id)
                        if product_id == key:
                            print(product_name)
                            [print(item) for item in orders[key]]

            elif key_search == 3:
                product_name = input("enter product name  :")
                ord.search_product_by_name(product_name, products)

            elif key_search == 4:

                start_date = input("enter start search date (yy/mm/dd) :")
                end_date = input("enter end search date as(yy/mm/dd) :")
                if start_date <= end_date:
                    result = orders_two_dates(start_date, end_date, order)
                    print("Dates"+"\t"+"Product_Id"+"\t"+"Order_Id"+"\t "+"Quantity_Ordered")
                    [print(element.order_date + "\t  " + element.product_id+"\t   " + element.order_id + "\t        "
                                              + element.quantity_ordered) for element in result]

                else:
                    result = orders_two_dates(end_date, start_date, order)
                    print("Dates"+"\t  "+"Product_Id"+"\t   "+"Order_Id"+"\t "+"Quantity_Ordered")
                    [print(element.order_date + "\t  " + element.product_id + "\t  " + element.order_id + "\t     "
                                              + element.quantity_ordered) for element in result]

            key_search = int(input("  enter   0: quit \n"
                                   "          1: to list product by category\n"
                                   "          2:list all orders for a given product\n "
                                   "          3:search product by name \n "
                                   "          4:to see orders between a specific date range :\n"))


def main():
    try:
        if len(sys.argv) != 3:
            print("exactly three argument needed in this program : manage_orders1.py orders.txt products.txt")
            return
        file1 = sys.argv[1]
        file2 = sys.argv[2]
        # list of class Orders  objects
        order = orders_file(file1)
        # making a dictionary using order(list of class objects)product_id is the key
        orders = order_file_dictionary(order)
        products = ord.parse_product_file(file2)
        # dictionary from orders.txt(order_id is the key)
        orders1 = parse_orders_file()

        key_search = int(input("enter 1:to list product by category\n"
                               "      2:list all orders for a given product\n "
                               "      3:search product by name \n "
                               "      4:to see orders between a specific date range :\n"))
        search(key_search, orders, order, products)

    except NameError:
        print("argument entry errors", file=sys.stderr)


if __name__ == "__main__":
    main()


