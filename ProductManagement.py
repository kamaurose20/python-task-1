# Product Management Class

class Product:
    def __init__(self):
        self.product_name = ""
        self.product_code = ""
        self.price = 0
        self.quantity = 0
        self.stock_value = 0

    def setProductDetails(self, product_name, product_code, price, quantity):
        self.product_name = product_name
        self.product_code = product_code
        self.price = price
        self.quantity = quantity

    def calculateStockValue(self):
        self.stock_value = self.price * self.quantity

    def displayProductDetails(self):
        print("Product Name:", self.product_name)
        print("Product Code:", self.product_code)
        print("Price: KSh", self.price)
        print("Quantity:", self.quantity)
        print("Stock Value: KSh", self.stock_value)


# Main Program
product = Product()

product.setProductDetails(
    "Laptop",
    "LP101",
    50000,
    10
)

product.calculateStockValue()
product.displayProductDetails()