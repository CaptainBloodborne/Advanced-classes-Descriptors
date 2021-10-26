class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set__(self, instance, value: int):
        if not 0 <= value <= 100:
            raise ValueError("ValueError: Price must be between 0 and 100.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name: str):
        self.name = name


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set__(self, instance, value: str):
        if instance.__dict__.get(self.name):
            raise ValueError(f"ValueError: {self.name.capitalize()} can not be changed.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner: type, name: str):
        self.name = name


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author: str, name: str, price: int):
        self.author = author
        self.name = name
        self.price = price
