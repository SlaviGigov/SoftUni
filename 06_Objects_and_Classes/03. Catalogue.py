class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [el for el in self.products if el.startswith(first_letter)]

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += "\n".join(sorted(self.products))
        return result
