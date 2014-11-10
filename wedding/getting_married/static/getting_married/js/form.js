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


                })
           })
});
