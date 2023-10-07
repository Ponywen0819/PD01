import math

class Book:
    name: str
    price: int
    discount: list

    def __init__(self, name, num, price, discount):
        self.name = name
        self.price = int(price)
        self.num = int(num)
        self.discount = [int(data) for data in discount]


def get_book_info(name, price):
    infos = input().split(",")
    return Book(name=name, price=price, num=infos[0], discount=infos[1:])


def get_books_info():
    res = []
    name = ["A", "B", "C"]
    price = [380, 1200, 180]
    for i in range(3):
        res.append(get_book_info(name[i], price[i]))
    return res


def calc_price(books: list):
    res = []
    for book in books:
        discount = 100
        if book.num > 30:
            discount = book.discount[2]
        elif book.num > 20:
            discount = book.discount[1]
        elif book.num > 10:
            discount = book.discount[0]

        total = book.price * book.num * discount / 100

        res.append((book, math.ceil(total)))
    return res

def sort(infos: list):
    infos.sort(key=lambda e: e[1], reverse=True)
    return infos
def print_infos(infos:list):
    for info in infos:
        print(f"{info[0].name},{info[1]:.0f}")

def print_total(infos: list):
    total = 0
    for info in infos:
        total += info[1]
    print(f"{total}")

def main():
    books = get_books_info()
    infos = calc_price(books)
    infos = sort(infos)
    print_infos(infos)
    print_total(infos)

main()