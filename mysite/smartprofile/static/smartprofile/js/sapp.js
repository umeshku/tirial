
function complex_table() {
  var c = document.getElementById("complex_table").childNodes;
  var i;
  var txt=[];

  for (i = 0; i < c.length; i++) {
    if (c[i].nodeName=="TABLE"){
      var table=c[i];
    //  txt=Table.rows[1].cells.length;
      var j;
      for(j=0; j<table.rows[0].cells.length;j++){
        txt.push(table.rows[0].cells[j].innerText);
      }
    }
   }
   const div = document.querySelector('.dropdown-menu')
   txt.forEach(txt => {
  div.innerHTML += `<li><input type='checkbox' class='form-check-input' value='hide' checked/>${txt}</li>`;
})

}

// function myFunction(value) {
//   text = "<li>";
//     text += "<input type='checkbox' class='form-check-input' value='hide' checked/>" + value;
//     text += "</li>";
//     document.getElementById("demo").innerHTML = text;
// }

function hide_show_table(col_name){
 var checkbox_val=document.getElementById(col_name).value;
 if(checkbox_val=="hide")
 {
  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="none";
  }
  document.getElementById(col_name+"_head").style.display="none";
  document.getElementById(col_name).value="show";
 }

 else
 {
  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="table-cell";
  }
  document.getElementById(col_name+"_head").style.display="table-cell";
  document.getElementById(col_name).value="hide";
 }
}
