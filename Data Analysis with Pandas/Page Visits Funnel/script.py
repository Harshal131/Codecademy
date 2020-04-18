import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

pd.merge(visits,cart,how='left')
cart[cart.cart_time.isnull()]
pd.merge(cart,checkout,how='left')

all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())

checkout_no_purchase = all_data[all_data.purchase_time.isnull()].count() / all_data[~all_data.checkout_time.isnull()].count()
print(checkout_no_purchase)

