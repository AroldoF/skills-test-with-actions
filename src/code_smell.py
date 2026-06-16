def process_order(order):
    if not order:
        print("Pedido inválido")
        return

    total = 0

    for item in order["items"]:
        total += item["price"] * item["quantity"]

    if order["customer_type"] == "premium":
        total = total * 0.9

    print(f"Cliente: {order['customer_name']}")
    print(f"Total: R$ {total}")

    # Simula persistência
    with open("orders.txt", "a") as f:
        f.write(f"{order['customer_name']} - {total}\n")

    # Simula envio de email
    print(f"Enviando email para {order['email']}...")