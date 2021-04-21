import csv
import pandas as pd
import sys
import datetime
import eel
import pos_system


INPUT_CSV = "./item_master.csv"


# JSからアクセス可能に
@eel.expose
# 以下、jsで呼び出したい処理
def main():
    pos_system.main()

@eel.expose
def receive_order(code, count):
    pos_system.order.receive_order(code, count)

@eel.expose
def order_detail():
    print("total_fnc実行")
    total = pos_system.order.order_detail()
    print(f"合計金額は{total}円です")
    return int(total)

@eel.expose
def bill(receive_money, total_price):
    return_money = pos_system.order.bill(receive_money, total_price)
    print(f"おつりは{return_money}円です")
    return int(return_money)

@eel.expose
def make_receipt(text):
    pos_system.order.make_receipt(text)




eel.init("web")
eel.start("index.html")