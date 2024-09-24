from .lib import Library, Book
from .tms import Task, TaskManager
from .calc import Calculator
from .oms import Order, OrderManager


def lib():
    library = Library()
    book1 = Book("1984", "George Orwell", 1949, "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0987654321")

    library.add_book(book1)
    library.add_book(book2)

    print(library.list_books())
    print(library.find_book("George"))
    library.remove_book("1234567890")
    print(library.list_books())


def tms():
    task_manager = TaskManager()
    task1 = Task("Finish homework", "Math exercises", due_date="2024-09-30")
    task2 = Task("Clean the house", "Living room and kitchen",
                 status="in_progress")

    task_manager.add_task(task1)
    task_manager.add_task(task2)

    print(task_manager.list_tasks())
    task_manager.update_task_status("Finish homework", "completed")
    print(task_manager.list_tasks())
    print(task_manager.filter_tasks_by_status("completed"))


def calc():
    calculator = Calculator()
    print(calculator.calculate("+", 5, 3))
    print(calculator.calculate("-", 5, 3))
    print(calculator.calculate("-", 0, 3))
    print(calculator.calculate("*", 5, 3))
    print(calculator.calculate("/", 5, 3))
    print(calculator.calculate("/", 5, 0))


def oms():
    order_manager = OrderManager()
    order1 = Order(1, "Alice", ["Book", "Pen"], 25.50)
    order2 = Order(2, "Bob", ["Notebook", "Pencil"], 15.75)

    order_manager.add_order(order1)
    order_manager.add_order(order2)

    print(order_manager.list_orders())
    order_manager.update_order_status(1, "shipped")
    print(order_manager.list_orders())
    order_manager.remove_order(2)
    print(order_manager.list_orders())
