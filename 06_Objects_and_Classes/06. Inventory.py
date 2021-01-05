class Inventory:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.left_capacity = self.__capacity
        self.items = []

    def add_item(self, item):
        if self.left_capacity > 0:
            self.items.append(item)
            self.left_capacity -= 1
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return f"{self.__capacity}"

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.left_capacity}"