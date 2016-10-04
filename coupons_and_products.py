"""
Given a class Product and a class Coupon write a function that takes in a list of
products and coupons and returns the minimum cost of buying all the products.
Each product and coupon have a category associated with them and coupons of a
category can only be applied to the product of the same category.

RetailMeNot question
"""


class Product:

    def __init__(self, price, category):
        self.price = price
        self.category = category

    def __repr__(self):
        return str(self.category) + ": " + str(self.price)


class Coupon:

    def __init__(self, discount, category):
        self.discount = discount
        self.category = category

    def __repr__(self):
        return str(self.category) + ": " + str(self.discount)


def get_min_price(products, coupons):
    pmap = {}
    cmap = {}

    if not products:
        return 0

    if not coupons:
        return sum(product.price for product in products)

    p_copy = sorted(products, key=lambda p: p.price, reverse=True)
    c_copy = sorted(coupons, key=lambda c: c.discount, reverse=True)

    for product in p_copy:
        if product.category in pmap:
            pmap[product.category].append(product)
        else:
            pmap[product.category] = [product]

    for coupon in c_copy:
        if coupon.category in cmap:
            cmap[coupon.category].append(coupon)
        else:
            cmap[coupon.category] = [coupon]

    cost = 0
    for category in pmap:
        plist = pmap[category]
        clist = []

        if category in cmap:
            clist = cmap[category]

        for product in plist:
            if clist:
                cost += product.price * (1 - clist.pop(0).discount)
            else:
                cost += product.price

    return cost


if __name__ == "__main__":
    products = [Product(100, "a"), Product(20, "b"), Product(35, "a")]
    coupons = [Coupon(0.2, "a"), Coupon(0.7, "a"), Coupon(0.4, "c")]
    print(get_min_price(products, coupons))
