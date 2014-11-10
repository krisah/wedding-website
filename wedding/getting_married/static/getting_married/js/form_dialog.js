$(document).ready(function(){
    $("#submit").dialog({ 
        autoOpen: false,
        dialogClass: "no-close",
        closeOnEscape: false,
        draggable: false,
        modal: true,
        title: 'Form Post',
        buttons: [ 
            {
                text: "close",
                click: function(){
                    $(this).dialog("close");
                    }
             }
            ]
    });
         $( "#submit" ).bind( "dialogclose", function(event, ui) { 
                    location.reload('true' );
    });


    $( "#creat-user" ).click( function() {
            $('#submit') .dialog( "open" );
                    
                 });

});



