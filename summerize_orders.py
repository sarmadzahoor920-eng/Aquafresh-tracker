import csv
import sys
from collections import Counter



def load_orders(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    path =sys.argv[1] if len(sys.argv) > 1 else "orders.csv"
    try:
        orders = load_orders(path)
    except FileNotFoundError:
        print(f"File not found :{path}")
        sys.exit(1)

    status_counts = Counter(o["status"] for o in orders)
    revenue = sum(int(o["amount_pkr"]) for o in orders if o["status"] == "delivered")
    bottles = sum(int(o["bottles"])for o in orders if o["status"] == "delivered")


    print("=== AquaFresh Delivery Summary ===")
    print(f"Total orders: {len(orders)}")
    for status, count in  status_counts.items():
        print(f" {status}: {count}")
    print(f"Bottles delivered: {bottles}")
    print(f"Revenue (delivered): PKR {revenue}")


if __name__ == "__main__":
    main()
