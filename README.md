### POSシステム課題進化版です。課題４で作成したPOSシステムアプリにデスクトップアプリとしての
### UIをつけていきます。


# １
課題３で作成したデスクトップUIを参考に、POSシステム用のUIを作成してください
（必要な項目：商品コード入力欄、個数入力欄、入力した商品情報の表示欄、お預かり金額入力欄、合計金額の表示欄など）
　※必要と判断した項目は追加いただいて構いません
 
# ２
UIとPython側を連動させて、POSシステムのデスクトップアプリ版を完成させてください

# ３（発展版）
マスタデータ（商品コード、商品名、価格）をCSVファイルから読み込んで登録できるようにしてください

# ４（発展版）
このPOSシステムに不足している機能を１つ考えて追加してください
⇒注文キャンセル機能：functionを作成して、合計金額からマイナスする項目を作成する必要あり


【自分用メモ】

<!-- Javascriptのアロー関数等、最新の書き方　　https://press.monaca.io/atsushi/5192 -->


<!-- async await　の記述方法 -->
async function total_fnc() {

  let total = await eel.order_detail()();
  console.log(total);
  document.getElementById("total_price").value = total;

};


⇒　https://deecode.net/?p=809

