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
def bill(receive_money, total_price):
    pos_system.order.bill(receive_money, total_price)

@eel.expose
def order_detail():
    pos_system.order.order_detail()

@eel.expose
def make_receipt(text):
    pos_system.order.make_receipt(text)




eel.init("web")
eel.start("index.html")