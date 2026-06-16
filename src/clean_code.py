def calculate_total(items):
    return sum(item["price"] * item["quantity"] for item in items)


def apply_discount(total, customer_type):
    return total * 0.9 if customer_type == "premium" else total


def process_order(order):
    total = calculate_total(order["items"])
    total = apply_discount(total, order["customer_type"])

    return {
        "customer": order["customer_name"],
        "total": total,
    }