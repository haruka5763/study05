
function entry_fnc() {
  const codes = Document.getElementById("item_code").value;
  const counts = Document.getElementById("order_count").value;
  eel.receive_order(codes, counts);
  const console = Document.getElementById("console_area");
  console.value = "注文番号："+codes+"/n"+"注文数："+counts+"/n";
  };

function end_fnc() {
  const code = 0
  const count = 0
  eel.receive_order(code, count);
  };

eel.expose(view_log_js)
function view_log_js(text){
  order.value += text + "\n"
}