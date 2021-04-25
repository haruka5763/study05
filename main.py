import csv
import pandas as pd
import sys
import datetime
import eel
import pos_system
from pos_system import Order

# Orderクラスのインスタンス化（グローバル領域）
INPUT_CSV = "./item_master.csv"
csv = INPUT_CSV
item_master=pos_system.read_item_master_csv(csv)
order = Order(item_master)


# ==========main呼び出し==========
@eel.expose
def main():
    pos_system.main()
# ==========注文登録==========
@eel.expose
def receive_order(code, count):
    order.receive_order(code, count)
# ==========注文キャンセル==========
@eel.expose
def clear_order():
    order.clear_order()
# ==========合計金額==========
@eel.expose
def order_detail():
    print("total_fnc実行")
    total = order.order_detail()
    print(f"合計金額は{total}円です")
    return int(total)
# ==========おつり計算==========
@eel.expose
def bill(receive_money, total_price):
    return_money = order.bill(receive_money, total_price)
    print(f"おつりは{return_money}円です")
    return int(return_money)
# ==========レシート作成==========
@eel.expose
def make_receipt(text):
    order.make_receipt(text)




eel.init("web")
eel.start("index.html")