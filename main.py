import csv
import pandas as pd
import sys
import datetime
import eel
import pos_system


# JSからアクセス可能に
@eel.expose
# 以下、jsで呼び出したい処理
def main():
    pos_system.main()
@eel.expose
def receive_order(code, count):
    pos_system.order.receive_order(code, count)

eel.init("web")
eel.start("index.html")