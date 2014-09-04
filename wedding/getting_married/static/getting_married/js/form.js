// Attach a submit handler to the form
$(function() {
        $( "form#comment" ).submit(function( event ) {

            // Stop form from submitting normally
            event.preventDefault();

            var $form = $( this ),
            term = $form.find( "input[name='guest']" ).val(),
            term2 = $form.find( "textarea[name='comment']" ).val(),
            url = $form.attr( "action" );

            // Send the data using post
            
            var posting = $.ajax( {
                "url": url,  
                "type": "POST",
                "data": JSON.stringify({ guest: term, comment: term2 }),
                "dataType": "application/json",
                "contentType": "application/json",
                }).done(function(data){
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
                    });
        })
});
