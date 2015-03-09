
window.onload = function() {

	var div = document.createElement('div');


	var submitRow = document.getElementsByClassName('submit-row');
	var deleteButton = document.getElementsByClassName('deletelink');

	var urlActual = document.URL;
	var urlSplitted = urlActual.split('/');

	var proyectoId = urlSplitted[urlSplitted.length - 2];

	div.innerHTML= '<button type="button" onclick="location.href=\'/admin/presupuesto/'+proyectoId+'\'" class="btn btn-high btn-success" style="margin-top:20px;" name="pre"><i class="icon-list icon-white"></i>&nbsp;&nbsp;Ver Presupuesto</button>';

	if (proyectoId == "add") {
		// Es cuando se agrega así que no se pone el botón de Ver Presupuesto
	}else{
		submitRow[0].appendChild(div);		
	}
	

}

