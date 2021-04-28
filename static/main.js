
$(document).ready(function() {

$("#source-lan").change(function() {
        var val = $(this).val();
        $("#target-lan").html(options[val]);
    });


    var options = {
        "ach" :'<option id="en-tgt"  value="en"> English</option>',
        "adh" : '<option id="en-tgt"  value="en"> English</option>',
        "luo" : '<option id="en-tgt"  value="en"> English</option>',
        "en" : '<option id="acholi-tgt" name="ach-tgt" value="ach" > Acholi</option><option id="adhola-tgt"  value="adh"> Dhopadhola</option><option id="luo-tgt" value="luo"> Dholuo</option>'
    };

});