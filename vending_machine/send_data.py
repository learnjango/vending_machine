from prices.models import Product

products = [
    {'name': 'Sandwich 1', 'price': 500, 'quantity': 1, 'category': 'sandwiches'},
    {'name': 'Sandwich 2', 'price': 500, 'quantity': 2, 'category': 'sandwiches'},
    {'name': 'Sandwich 3', 'price': 500, 'quantity': 5, 'category': 'sandwiches'},
    {'name': 'Sandwich 4', 'price': 500, 'quantity': 7, 'category': 'sandwiches'},
    {'name': 'Sandwich 5', 'price': 500, 'quantity': 3, 'category': 'sandwiches'},
    {'name': 'Sandwich 6', 'price': 500, 'quantity': 2, 'category': 'sandwiches'},
    {'name': 'Sandwich 7', 'price': 500, 'quantity': 5, 'category': 'sandwiches'},
    {'name': 'Sandwich 8', 'price': 500, 'quantity': 7, 'category': 'sandwiches'},
    {'name': 'Sandwich 9', 'price': 500, 'quantity': 3, 'category': 'sandwiches'},
]

for product_data in products:
    product = Product(**product_data)
    product.save()