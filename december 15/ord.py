class Product:
    def __init__(self, category, product_id, product_name, price, quantity_on_hand):
        self.category = category
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity_on_hand = quantity_on_hand


def parse_product_file(file2):
    file = open(file2)
    products_from_class = []
    file.readline()
    for line in file:
        newline = line.split(",")
        products_from_class.append(Product(newline[0], newline[1], newline[2], newline[3], newline[4]))
    file.close()
    return products_from_class


def parse_by_category(products):

    file_by_category = []
    search_category = ["Kitchen", "Electronic", "Office", "Home decors"]
    for category in search_category:
        for product in products:
            if product.category.upper() == category.upper():
                file_by_category += [[product.category, product.product_id, product.product_name, product.price,
                                      product.quantity_on_hand]]
    return file_by_category


def search_product_by_name(product_name, products):

    for product in products:
        if product.product_name.upper() == product_name.upper():
            print(product.product_name, product.category, product.price, product.quantity_on_hand)
            return


def product_id_product_name(products, product_id):
    product = products
    for element in product:
        if element.product_id == product_id:
            return element.product_name
