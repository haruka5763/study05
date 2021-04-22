import csv
import pandas as pd
import sys
import datetime
import eel


#==========定数==========
# レシート保存パス
RECEIPT = "./receipt"
# 商品マスタCSV
INPUT_CSV = "./item_master.csv"


### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price

#==========CSVから商品マスタ情報の登録==========
def read_item_master_csv(csv):

    try:
        csv_input = pd.read_csv(csv, encoding="utf-8_sig")
        df = pd.DataFrame(csv_input)
        loopcount =len(df['item_code'])
        for i in range(loopcount):
            item_master = []
            for item_code,item_name,price in zip(
                list(df['item_code']), list(df['item_name']), list(df['price'])
                ):
                item_master.append((item_code,item_name,price))
        return item_master

    except Exception as e:
        print("csvが読み込めませんでした")
        print(e)
        sys.exit()



### オーダークラス
class Order:
    def __init__(self,item_master):
        # 注文内容
        self.item_order_list=[]
        self.item_count_list=[]
        # メニュー一覧
        self.item_master=item_master
        self.datetime_receipt=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    #==========レシート作成==========
    def make_receipt(self, text):
        with open(RECEIPT+"/"+f"{self.datetime_receipt}.txt","a",encoding="utf-8_sig") as f:
            f.write(text+"\n")
            eel.receipt_js(text+"\n")
    #==========商品登録==========
    def receive_order(self, code, count):
        if int(code) != 0:
            order_code =  code
            order_count = count
            self.item_order_list.append(order_code)
            self.item_count_list.append(order_count)
            eel.console_js("注文を受け付けました")
            eel.console_js (f"注文番号：{order_code}")
            eel.console_js (f"注文数：{order_count}")
        else:
            eel.console_js(f"注文内容一覧{self.item_order_list}")
            eel.console_js(f"注文数一覧{self.item_count_list}")
            eel.console_js("注文終了")

    #==========登録キャンセル（注文内容全件削除）==========
    def clear_order(self):
            eel.console_js("注文をキャンセルしました")
            eel.console_js("=======================")
            eel.console_js("【 キャンセル一覧 】")
            eel.console_js(f"注文内容一覧{self.item_order_list}")
            eel.console_js(f"注文数一覧{self.item_count_list}")
            eel.console_js("=======================")
            self.item_order_list.clear()
            self.item_count_list.clear()

    #==========合計金額計算==========
    def order_detail(self):

        self.make_receipt("************************"+"\n"+"ご注文内容")
        self.make_receipt("************************")
        total_price = 0
        for order_code, order_count in zip(self.item_order_list, self.item_count_list):
            for im in self.item_master:
                item_code = im[0]
                item_name = im[1]
                item_price = im[2]
                if int(order_code) == int(item_code):
                    subtotal_price = int(item_price)*int(order_count)
                    total_price = total_price + subtotal_price
                    self.make_receipt(f"商品名：{item_name}")
                    self.make_receipt(f"価格：￥{item_price}")
                    self.make_receipt(f"注文数：{order_count}個")
                    self.make_receipt(f"小計：￥{subtotal_price}")
        self.make_receipt(f"合計金額：￥{total_price}")
        self.make_receipt("************************")
        return total_price

    #==========おつり計算==========
    def bill(self, receive_money, total_price):
        # 計算
        return_money = int(receive_money)-int(total_price)
        # レシート作成
        self.make_receipt("******************************")
        self.make_receipt(f"お預かり金額：￥{receive_money}")
        self.make_receipt(f"お支払金額：￥{total_price}")
        self.make_receipt(f"おつり：￥{return_money}")
        self.make_receipt("******************************")
        self.make_receipt("==============================")
        self.make_receipt(self.datetime_receipt)
        self.make_receipt("==============================")
        # おつり
        return return_money


# Orderクラスのインスタンス化（グローバル領域）
csv = INPUT_CSV
item_master=read_item_master_csv(csv)
order = Order(item_master)

### メイン処理
def main():
    print("注文開始")
    
if __name__ == "__main__":
    main()
    