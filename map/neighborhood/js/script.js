
function startPage() {
    count = 0

    $("#cat-pic").on('click', function(){
        count += 1
        $("#counter").html("Clicks: %COUNT%".replace('%COUNT%', count));
    })

};


$(document).ready(startPage);
$(document).on('page:load', startPage);
