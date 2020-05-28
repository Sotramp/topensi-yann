$(document).ready(function(){
    
    $('#type').change(function(){
        $('tr').hide()
        if($('#type').val() != 'Tous les types' && $('#client').val() == 'Tous les clients'){ 
            $('tr').each(function(){
                var tr = $(this);
                if(tr.find("th").text() != ""){
                    tr.show()
                }
                if(tr.find('td:eq(3)').text() == $('#type').val() ){
                    tr.show()   
                }
            });
        } else if($('#type').val() != 'Tous les types' && $('#client').val() != 'Tous les clients') {
            $('tr').each(function(){
                var tr = $(this);
                if(tr.find("th").text() != ""){
                    tr.show()
                }
                if(tr.find('td:eq(3)').text() == $('#type').val() && tr.find('td:eq(0)').text() == $('#client').val()){
                    tr.show()
                }
            });
        } else if($('#type').val() == 'Tous les types' && $('#client').val() != 'Tous les clients'){
            $('tr').each(function(){
                var tr = $(this);
                if(tr.find("th").text() != ""){
                    tr.show()
                }
                if(tr.find('td:eq(0)').text() == $('#client').val()){
                    tr.show()
                }
            });
        } else {
            $('tr').show()
        }
    })
    $('#client').change(function(){
        $('tr').hide()
        if($('#type').val() != 'Tous les types' && $('#client').val() == 'Tous les clients'){ 
            $('tr').each(function(){
                var tr = $(this);
                if(tr.find("th").text() != ""){
                    tr.show()
                }
                if(tr.find('td:eq(3)').text() == $('#type').val() ){
                    tr.show()   
                }
            });
        } else if($('#type').val() != 'Tous les types' && $('#client').val() != 'Tous les clients') {
            $('tr').each(function(){
                var tr = $(this);
                if(tr.find("th").text() != ""){
                    tr.show()
                }
                if(tr.find('td:eq(3)').text() == $('#type').val() && tr.find('td:eq(0)').text() == $('#client').val()){
                    tr.show()
                }
            });
        } else if($('#type').val() == 'Tous les types' && $('#client').val() != 'Tous les clients'){
            $('tr').each(function(){
                var tr = $(this);
                if(tr.find("th").text() != ""){
                    tr.show()
                }
                if(tr.find('td:eq(0)').text() == $('#client').val()){
                    tr.show()
                }
            });
        } else {
            $('tr').show()
        }
        
    })

    
});

                
