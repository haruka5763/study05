
function entry_fnc() {
  const codes = document.getElementById("item_code").value;
  const counts = document.getElementById("order_count").value;
  eel.receive_order(codes, counts);
  // const console = document.getElementById("console_area");
  // 入力エリアクリア
  document.getElementById("item_code").value = "";
  document.getElementById("order_count").value = "";
  };

function end_fnc() {
  const code = 0
  const count = 0
  eel.receive_order(code, count);
  };

eel.expose(console_js)
function console_js(text){
  console_area.value += text + "\n"
}

function total_fnc() {
  let total = eel.order_detail();
  document.getElementById("total_price").value = total;

  };

function bill_fnc() {
  total_price = document.getElementById("total_price").value;
  receive_money = document.getElementById("receive_money").value;
  return_money = eel.bill(total_price, receive_money);

  document.getElementById("return_money").value = return_money;

  };

eel.expose(receipt_js)
function receipt_js(text){
  receipt_area.value += text + "\n"
}