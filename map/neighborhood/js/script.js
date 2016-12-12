
class Cat {
    constructor(name, pic_link){
        this.name = name;
        this.pic_link = pic_link;
        this.count = 0
    }
}

var a = new Cat("Dr. StrangeHate",
        "https://lh3.ggpht.com/nlI91wYNCrjjNy5f-S3CmVehIBM4cprx-JFWOztLk7vFlhYuFR6YnxcT446AvxYg4Ab7M1Fy0twaOCWYcUk=s0#w=640&h=426")
var b = new Cat("Chairman Meow",
        "https://lh3.ggpht.com/kixazxoJ2ufl3ACj2I85Xsy-Rfog97BM75ZiLaX02KgeYramAEqlEHqPC3rKqdQj4C1VFnXXryadFs1J9A=s0#w=640&h=496")

var c = new Cat("Samael", "http://i.imgur.com/WqlTIIG.jpg")
var d = new Cat("Tony Rocky Horror", "http://i.imgur.com/Ro2p5sJ.jpg")
var e = new Cat("Antwan Rockamura", "http://i.imgur.com/lSQIVYf.jpg")

cats = [a, b, c, d, e]

function startPage() {

    for (var i = 0; i < cats.length; i++){
        var name = cats[i]['name']

        var cat_li = "<li id='%ID%' class='cat-id'>%NAME%</li>".replace("%NAME%", name)
        var cat_id = cat_li.replace("%ID%", i)
        $(".cats").append(cat_id)

    }

    $(".cat-id").on("click", function(){
        var id = parseInt($(this).attr("id"))
        $('.name').attr("id", id.toString())


        var name = cats[id]['name']
        var imgSrc = cats[id]["pic_link"]
        var count = cats[id]['count']

        $(".name").html(name);
        $("#cat-pic").attr("src", imgSrc)
        counter = count.toString()
        $("#counter").html(counter)


    })

    $("#cat-pic").on("click", function(){
        var id = parseInt($("h2").attr("id"))
        count = cats[id]['count'] += 1
        cats[id]['count'] =  count
        counter = count.toString()
        $("#counter").html(counter)
    })



};


$(document).ready(startPage);
$(document).on('page:load', startPage);
