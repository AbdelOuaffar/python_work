import sys
from datetime import datetime as date


class Product:
    def __init__(self, category, product_id, product_name, price, quantity_on_hand):
        self.Category = category
        self.product_Id = product_id
        self.product_Name = product_name
        self.Price = price
        self.Quantity_on_hand = quantity_on_hand
    def parse_order_date(self,order_date):
        self.order_date = date.strptime(self.order_date, '%y/%m/%d')

class Orders(Product):
    def __init__(self, order_id, order_date, product_id,  quantity_ordered):
        self.__init__ = Product.__init__()
        self.order_id = order_id
        self.order_date = self.Product.parse_order_date(order_date)
        self.product_id = product_id
        self.quantity_ordered = quantity_ordered
def parse_product_file():
    products = []
    file = open("productList.txt", 'r')
    header = file.readline()
    for line in file:
        product = line.split(',')
        products.append(Product(product[0], product[1], product[2], product[3], product[4]))
    file.close()
    return products
def parse_orders():
    orders = {}
    file = open("orders.txt", 'r')
    header = file.readline()
    for line in file:
        order = line.split(",")
        orders[order[0]] = [(order[1]), order[2], int(order[3])]
    file.close()

    return orders


def parse_by_category():
    product_file = parse_product_file()
    category = []
    for catg in ["Electronic", "kitchen"]:
        for product in product_file:
            if product.Category == catg:
                category += [[product.Category, product.product_Id, product.product_Name, product.Price,
                      product.Quantity_on_hand]]

    return category
def __str__(group):
  for category in group:
        print(category[0], category[1], category[2], category[3], category[4])
def same_product_orders(orders,product_id):
    for key in orders:
        if orders[key][1] == product_id:
            print(key, orders[key])
def search_product_by_name(product_name):
    products = parse_product_file()
    for product in products:
        if product.product_Name == product_name:
            print(product.product_Name, product.Category, product.Price, product.Quantity_on_hand)
            return

       # elif product.product_Name != product_name:
            #print("we do not carry")
           # return
def orders_two_dates(date1, date2):
    start_date = date.strptime(date1, '%y/%m/%d')
    end_date = date.strptime(date2, '%y/%m/%d')
    orders = parse_orders()
    order_start_end = []
    for key in orders:
        order_date = date.strptime(orders[key][0], '%y/%m/%d')
        if start_date <= order_date <= end_date:
            order_start_end += [(key, orders[key])]

    return order_start_end

def main():
    search_key = int(input("enter 1:(to list product by category) or 2:(list all orders for a given product) or 3:(search product by name) or 4:(to see orders between a specific date range) :"))
    while search_key != 0:
        if search_key == 1:
            group = parse_by_category()
            __str__(group)
        elif search_key == 2:
            orders = parse_orders()
            product_id = input("enter product id :")
            same_product_orders(orders, product_id)
        elif search_key == 3:
            product_name = input("enter product name  :")
            search_product_by_name(product_name)

        elif search_key == 4:
            start_date = input("enter start search date (yy/mm/dd) :")
            end_date = input("enter end search date as(yy/mm/dd) :")
            if start_date <= end_date:
                result = orders_two_dates(start_date, end_date)
                print(f"orders between {start_date}  and  {end_date} :{result}")
            else:
                result=orders_two_dates(end_date, start_date)
                print(f"orders between {end_date}  and  {start_date} :{result}")
        search_key = int(input("enter 0 to quit or 1 to 4 :"))
main()

