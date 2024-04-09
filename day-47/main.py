from price_search import PriceSearch
from data_manage import DataManage
from notification_manage import NotificationManage

data_manage = DataManage()
notification_manage = NotificationManage()

# Get csv products
for index, row in data_manage.data.iterrows():
    price_search = PriceSearch(row["product"])

    old_price = float(row["price"])
    new_price = price_search.get_price()

    if new_price and old_price > new_price:
        notification_manage.create_message(price_search.url)

if len(notification_manage.message) > notification_manage.message_initial_len:
    notification_manage.send_email()
