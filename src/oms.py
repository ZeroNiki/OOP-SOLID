class Order:
    def __init__(self, order_id, customer_name, items, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount
        self.status = "pending"

    def __str__(self):
        return f"Order {self.order_id} for {self.customer_name} - Total: {self.total_amount} - Status: {self.status}"


class OrderManager:
    def __init__(self):
        self.orders = {}

    def add_order(self, order):
        self.orders[order.order_id] = order

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def update_order_status(self, order_id, new_status):
        if order_id in self.orders:
            self.orders[order_id].status = new_status

    def remove_order(self, order_id):
        return self.orders.pop(order_id, None)

    def list_orders(self):
        return [str(order) for order in self.orders.values()]
