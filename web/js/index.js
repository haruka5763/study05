
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


async function total_fnc() {

  let total = await eel.order_detail()();
  document.getElementById("total_price").value = total;

};



async function bill_fnc() {
  let total_price = document.getElementById("total_price").value;
  let receive_money = document.getElementById("receive_money").value;
  let return_money = await eel.bill(receive_money, total_price)();

  document.getElementById("return_money").value = return_money;

  };

eel.expose(receipt_js)
function receipt_js(text){
  receipt_area.value += text + "\n"
}