

document.getElementById("start").onclick = function() {
  eel.main();
  };


document.getElementById("entry").onclick = function() {
  code = Document.getElementById("item_code");
  count = Document.getElementById("order_count");
  eel.receive_order(code, count);
  };

document.getElementById("end").onclick = function() {
  code = int(0)
  count = int(0)
  eel.receive_order(code, count);
  };

eel.expose(view_log_js)
function view_log_js(text){
  order.value += text + "\n"
}