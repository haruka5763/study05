import csv
import pandas as pd
import sys
import datetime


# 定数
INPUT_CSV = "./item_master.csv"
RECEIPT = "./receipt"


### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

# csvからマスタ情報取得　Task3
def item_master_csv(csv):

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

    def make_receipt(self, text):
        with open(RECEIPT+"/"+f"{self.datetime_receipt}.txt","a",encoding="utf-8_sig") as f:
            f.write(text+"\n")
            eel.view_log_js("『{}』はいます".format(word))

    def receive_order(self, code, count):
        print("注文登録を開始します")
        while True:
            if int(code) != 0:
                order_code =  code
                order_count = count
                self.item_order_list.append(order_code)
                self.item_count_list.append(order_count)
                print("注文を受け付けました")
            else:
                print("ご注文ありがとうございました!")
                sys.exit
                break


    # オーダーの詳細情報取得 Task1
    def order_detail(self):
        print("オーダーが入りました")
        print("************************")
        self.make_receipt("************************"+"\n"+"ご注文内容")
        self.make_receipt("************************")


        total_price = 0

        for order_code, order_count in zip(self.item_order_list, self.item_count_list):
            for im in self.item_master:
                item_code = im[0]
                item_name = im[1]
                item_price = im[2]
                if int(order_code) == int(item_code):
                    print(f"商品名：{item_name}")
                    print(f"価格：￥{item_price}")
                    print(f"注文数：{order_count}個")
                    subtotal_price = int(item_price)*int(order_count)
                    print(f"小計：￥{subtotal_price}")
                    total_price = total_price + subtotal_price
                    self.make_receipt(f"商品名：{item_name}")
                    self.make_receipt(f"価格：￥{item_price}")
                    self.make_receipt(f"注文数：{order_count}個")
                    self.make_receipt(f"小計：{subtotal_price}個")

        print(f"合計金額：{total_price}")
        print("************************")
        self.make_receipt(f"合計金額：{total_price}")
        self.make_receipt("************************")

        return total_price

    def bill(self, total_price, receive_money):
        
        f"お預かり金額 : ￥{receive_money}"
        print(f"お支払い金額：￥{total_price}")
        return_money = int(receive_money)-int(total_price)
        print(f"おつり：￥{return_money}")

        self.make_receipt("******************************")
        self.make_receipt(f"お預かり金額：￥{receive_money}")
        self.make_receipt(f"お支払金額：￥{total_price}")
        self.make_receipt(f"おつり：￥{return_money}")
        self.make_receipt("******************************")
        self.make_receipt("==============================")
        self.make_receipt(self.datetime_receipt)
        self.make_receipt("==============================")


### メイン処理
def main():
    
    # マスタ登録 Task3
    csv = INPUT_CSV
    item_master=item_master_csv(csv)
    # Order classのインスタンス生成
    order = Order(item_master)

    print("注文開始")



    
if __name__ == "__main__":
    main()
    