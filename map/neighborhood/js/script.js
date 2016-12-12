
function startPage() {
    var count_1 = 0
    var count_2 = 0
    $("#name-1").html("Dr. StrangeHate")
    $("#name-2").html("Chairman Meow")
    $("#cat-pic-1").on('click', function(){
        count_1 += 1
        $("#counter-1").html("Clicks: %COUNT%".replace('%COUNT%', count_1));
    })
    $("#cat-pic-2").on('click', function(){
        count_2 += 1
        $("#counter-2").html("Clicks: %COUNT%".replace('%COUNT%', count_2));
    })



};


$(document).ready(startPage);
$(document).on('page:load', startPage);
