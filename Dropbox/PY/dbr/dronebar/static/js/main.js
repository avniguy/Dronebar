/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */


function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else
    alert("Geolocation is not supported by this browser.");
}

function showPosition(position) {
  [position.coords.latitude,position.coords.longitude];
  document.getElementById("location").value=String(position.coords.latitude)+","+String(position.coords.longitude);
}

function CreateOrderRow(id,name,description,price,weight,quantity){

  getLocation();

  if(!isNaN(document.getElementById("total_order_weight").innerText)){
    maxPayload = parseFloat(document.getElementById("max_payload").value);
    maxOrderWeight = parseFloat(document.getElementById("total_order_weight").innerText);

    if(maxPayload > (maxOrderWeight + parseFloat(weight))){

      // Find a <table> element with id="myTable":
        var table = document.getElementById("order-table");

      //check if row for this item exists then add qty to existing row
        for (var i = 0, row; row = table.rows[i]; i++) {
          var indicator=false;
          var tmp_price = 0;
          var tmp_weight = 0;

           //iterate through rows
           //rows would be accessed using the "row" variable assigned in the for loop
           for (var j = 0, col; col = row.cells[j]; j++) {
             if(row.cells[j].id == "item_id" && row.cells[j].innerHTML == id){
               indicator = true;
             }

             if(indicator == true && row.cells[j].id == "qty"){
                var str = row.cells[j].innerText;
                var res = str.replace(/\D/g, "");
                var num = parseInt(res);
                row.cells[j].innerHTML = '<font size=2><a href="#" id="btn-plus"  class="qty_btn"> + </a></font> <label id="qty_">'+(num=num+1)+' </label><font size=2><a href="#" id="btn-minus" class="qty_btn"> - </a></font>';//parseInt(res)+1;
              }

              if(indicator == true && row.cells[j].id == "price"){
                tmp_price = parseFloat(row.cells[j].innerText);
                document.getElementById("total_order_price").innerText = parseFloat(document.getElementById("total_order_price").innerText) + tmp_price;
              }

              if(indicator == true && row.cells[j].id == "weight"){
                tmp_weight = parseFloat(row.cells[j].innerText);
                document.getElementById("total_order_weight").innerText = parseFloat(document.getElementById("total_order_weight").innerText) + tmp_weight;
              }

              if(indicator == true && row.cells[j].id == "total_price")
                row.cells[j].innerText = parseFloat(num * tmp_price).toFixed(2);

              if(indicator == true && row.cells[j].id == "total_weight")
                row.cells[j].innerText = parseFloat(num * tmp_weight).toFixed(2);
           }

           if(indicator==true)
            return;
        }

        // Create an empty <tr> element and add it to the 1st position of the table:
        var row = table.insertRow(1);
        row.setAttribute("class", "order_row");

        // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
        var cell4 = row.insertCell(3);
        var cell5 = row.insertCell(4);
        var cell6 = row.insertCell(5);
        var cell7 = row.insertCell(6);
        var cell8 = row.insertCell(7);
        var cell9 = row.insertCell(8);

        // Add some tex9t to the new cells:
        cell1.innerHTML = id;
        cell1.id="item_id";
        cell2.innerHTML = name;
        cell2.id="name";
        cell3.innerHTML = description;
        cell3.id="description";
        cell4.innerHTML = price;
        cell4.id="price";
        cell5.innerHTML = weight;
        cell5.id="weight";
        cell6.innerHTML = '<font size=2><a href="#" id="btn-plus" class="qty_btn"> + </a></font> <label id="qty_">'+quantity+'</label><font size=2><a href="#" id="btn-minus" class="qty_btn"> - </a></font>';
        cell6.id="qty";
        cell7.innerHTML = price;
        cell7.id = "total_price";
        cell8.innerHTML = weight;
        cell8.id = "total_weight";
        cell9.innerHTML = '<a href="#" id="btn-trash" class="trash_btn"><span class="glyphicon glyphicon-trash"></span> Delete</a>';

        var totalOrderPrice = parseFloat(document.getElementById("total_order_price").innerText) + price;
        var totalOrderWeight = parseFloat(document.getElementById("total_order_weight").innerText) + weight;

        console.log("totalOrderPrice="+totalOrderPrice+" totalOrderWeight="+totalOrderWeight);

        document.getElementById("total_order_price").innerText = totalOrderPrice;
        document.getElementById("total_order_weight").innerText = totalOrderWeight;
      }
      else
        alert("You exceeded maximum droan payload weight");
    }
}

$(document).ready(function(){

  // life_orders.html script
  $("form").on('click',"#fictive_delete",function(){
    $(this).closest("tr").remove();
  });
// order_create.html script
  $("table").on('click',".qty_btn",function(){
    var x = $(this).closest("td").find("#qty_").html();//row qty
    // console.log("QTY_ = " + x);
    var w = parseFloat($(this).closest("tr").find("#weight").text()); //item weight
    // console.log("WEIGHT =" + w);
    var tow = parseFloat($("#total_order_weight").text()); // total order weight
    // console.log("total_order_weight = "+ tow);
    var mxw = parseFloat($("#max_payload").val()); // total order weight
    // console.log("max_payload = "+ mxw);

    if ($.isNumeric(x)){
      // console.log("qty_ is numeric");
      if($(this).attr("id") == "btn-plus")
        if((tow + w) <= mxw){ //if we can add more weight to the current order
          x++;
          tow += w;
        }
        else
          alert("Maximum weight exceeded");
      else if($(this).attr("id") == "btn-minus" && x>1){
        x--;
        tow -= w;
      }

      $("#total_order_weight").text(tow);
      $(this).closest("td").find("#qty_").html(x);

      // r_qty = $(this).closest("td").find("#qty").text();
      // console.log("r_qty = "+r_qty);
      r_price = $(this).closest("tr").find("#price").text();
      // console.log("r_price = "+r_price);
      r_weight = $(this).closest("tr").find("#weight").text();
      // console.log("r_weight = "+r_weight);

      $(this).closest("tr").find("#total_price").text(parseFloat(r_price * x).toFixed(2)); //row price
      $(this).closest("tr").find("#total_weight").text(parseFloat(r_weight * x).toFixed(2)); // row weight

      var total_order_weight = parseFloat(0);
      var total_order_price =  parseFloat(0);

      $("#order-table  #total_price").each(function(){
        total_order_price += parseFloat($(this).text());
        // console.log("Total Price=" + $(this).text());
      });

      $("#order-table  #total_weight").each(function(){
        total_order_weight += parseFloat($(this).text());
        // console.log("Total Weight=" + $(this).text());
      });

      $("#total_order_price").text(parseFloat(total_order_price).toFixed(2));
      $("#total_order_weight").text(parseFloat(total_order_weight).toFixed(2));


    }
  });
  // order_create.html script
  $("table").on('click',"#btn-trash",function(){
    var row_price = $(this).closest("tr").find("#total_price").text();
    var row_weight = $(this).closest("tr").find("#total_weight").text();

    var total_price = $("#total_order_price").text();
    var total_weight = $("#total_order_weight").text();

    $("#total_order_price").text(parseFloat(total_price - row_price).toFixed(2));
    $("#total_order_weight").text(parseFloat(total_weight - row_weight).toFixed(2));

    $(this).closest("tr").remove();
  });
  // order_create.html script
  $("#order_form").submit(function(event) {
    var jsonData ;
    var order_rows = [];
    $('#order-table > tbody > .order_row').each(function(index, tr) {
        // create new input hidden for each row - will be returned to the view
        item_id = parseInt($(this).find("#item_id").text());
        qty = parseFloat($(this).find("#qty_").html() ); //.replace(/\D/g, ""));
        price = parseFloat($(this).find("#price").text());

        jStr = {'item':item_id,'quantity':qty,'item_price':price};
        order_rows[index] = jStr;
    });

    jsonData = {'order_price':parseInt($("#total_order_price").text()),'order_weight':parseInt($("#total_order_weight").text()),'geolocation':$("#location").val(), "order_rows":order_rows};

    if(order_rows.length > 0)
      // alert("yes");
      $("#total_order_data").val(JSON.stringify(jsonData));
      // alert($("#id_shop").find(":selected").val());
      $("#shop_id").val($("#id_shop").find(":selected").val())
      // alert(JSON.stringify(jsonData));
  });
  // life_orders.html script
  $("table").on('click',"#next_step",function(){
    var orId = $(this).parent().siblings("#order_id").html();
    $("#order_id_proceed").val(orId);
  });
  // life_orders.html script
  $("table").on('change',"#drones_select",function(){
    var droneSelected = $('#drones_select').find(":selected").text();
    if ($(this).find(":selected").val() > 0){
      var a = $(this).parent().parent().closest("tr").find("#next_step");
      a.prop( "disabled",false);
      $("#order_drone").val($(this).val());
    }
  });
  // life_orders.html script
  $("table").on('click',"#shop_drone_delete",function(){
    var currentVal = $("#shop_droan_to_delete").val();
    var drId = $(this).parent().siblings("#drone_id").html();
    $("#shop_droan_to_delete").val(currentVal + "," + drId);
    $(this).closest("tr").remove();

  });

  $("table").on('click',"#next_step",function(){
     var orId = $(this).parent().siblings("#order_id").html();
     $("#order_id_proceed").val(orId);
   });



});
