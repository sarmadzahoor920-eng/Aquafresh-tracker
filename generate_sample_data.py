import csv
import random
from datetime import date, timedelta

random.seed(42)

customers =["Ahmed Khan", "Ali Ahmed"," Hamza Riaz", "Bilal Raza", "Shayan Tahir","Usman ali","Moiz Ahmed","Zain Abbas", "Zeeshan Ali","Sarmad Zahoor","Waleed Qasim"]
areas =["G-10", "F-8","I-8","E-11","DHA Phase 2", "Bahria Town"]
statuses =["delivered", "delivered", "delivered", "pending","cancelled"]
PRICE_PER_BOTTLE =250

with open("orders.csv", "w",newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id","customer","area","bottles","amount_pkr","status","order_date"])
    for i, name in enumerate(customers, start=1):
        bottles = random.randint(1,6)
        order_date = date(2026,11,1) + timedelta(days=random.randint(0,13))
        writer.writerow( [f"AF-{1000+i}", name, random.choice(areas), bottles, bottles* PRICE_PER_BOTTLE, random.choice(statuses),order_date] )
