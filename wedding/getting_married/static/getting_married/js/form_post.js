function formData(){
        $.getJSON( "http://krisandmarissa.com:8000/getting_married/guest_book_post/", function( data ) {
	    var comments = [];
	    $.each( data, function( key, val ) {
	        comments.push( "<div>"  + val.guest + ':' + "<br/>" + "<br/>"  +  '&nbsp &nbsp &nbsp &nbsp &nbsp' +  val.comment + "</div>" + "<hr/>" );
	});

        var div = document.getElementById('form_post');
        for (var i in comments) {
            div.innerHTML = div.innerHTML + comments[i];
        }
    });
}       
