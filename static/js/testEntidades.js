
window.onload = function() {
	

	$('#suit_form_tabs').find('li').find('a').each(function(){
		
		//if(myString.indexOf("1234") == 0)

		if ($(this).attr('href').match("^#merito")) {
		   $(this).fadeOut();
		}
	});


	$('#id_categoria').change(function(e){
		var categoria = $(this).val();

		$('#suit_form_tabs').find('li').find('a').each(function(){
		
			//if(myString.indexOf("1234") == 0)

			if ($(this).attr('href').match("^#"+categoria)) {
			   $(this).fadeIn();
			}
		});

	});

}