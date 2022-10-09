/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */


function CreateOrderRow(id,name,description,price,weight,quantity){
  // Find a <table> element with id="myTable":
    var table = document.getElementById("order-table");

    // Create an empty <tr> element and add it to the 1st position of the table:
    var row = table.insertRow(-1);

    // Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);

    // Add some text to the new cells:
    cell1.innerHTML = id;
    cell2.innerHTML = name;
    cell3.innerHTML = description;
    cell4.innerHTML = price;
    cell5.innerHTML = weight;
    cell6.innerHTML = '<font size=2><a href="#" id="btn-plus"  class="qty_btn"> + </a></font> <label id="qty">'+ quantity +' </label><font size=2><a href="#" id="btn-minus" class="qty_btn"> - </a></font>';
}

$(document).ready(function(){
  $("table").on('click',".qty_btn",function(){
    // console.log("TEXT: " + $(this).closest("td").find("#qty").text());
    // console.log("TEXT: " + $(this).closest("td").find("#qty").html());
    var x = $(this).closest("td").find("#qty").text();
    if ($.isNumeric(x)){
      if($(this).attr("id") == "btn-plus")
        x++;
      else if($(this).attr("id") == "btn-minus" && x>1)
        x--;
      $(this).closest("td").find("#qty").text(x);
    }
  });
});
