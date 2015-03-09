
window.onload = function() {

var div = document.createElement('li');

div.className = 'presu';
capa = document.getElementById("suit_form_tabs"); 
div.innerHTML= '<button type="button" onclick="location.href=\'/admin/presupuesto/ \'" class="btn btn-high btn-info" name="pre">Ver Presupuesto</button>';
 
capa.appendChild(div);

}

