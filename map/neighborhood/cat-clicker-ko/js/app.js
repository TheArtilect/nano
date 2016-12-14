var initialCats = [
    {
        clickCount: 0,
        name: 'Tabby',
        imgSrc: 'img/434164568_fea0ad4013_z.jpg',
        nicknames: ['Dr. StrangeHate', 'Chairman Meow']
    },
    {
        clickCount: 0,
        name: 'Monster',
        imgSrc: 'img/1413379559_412a540d29_z.jpg',
        nicknames: ['Chairman Meow', 'Catclops']
    },
    {
        clickCount: 0,
        name: 'Roger',
        imgSrc: 'img/9648464288_2516b35537_z.jpg',
        nicknames: ['Chairman Meow', 'Catclops']
    }

];

var Cat = function (data){
    this.clickCount = ko.observable(data.clickCount);
    this.name = ko.observable(data.name);
    this.imgSrc = ko.observable(data.imgSrc);
    this.nicknames = ko.observable(data.nicknames);


    this.level = ko.computed(function(){
        var level;
        var click = this.clickCount();
        if (click <= 2){
            level = 'Newborn';
        } else if (click < 12){
            level = 'Infant';
        } else if (click < 18){
            level = 'Teen';
        } else if (click < 25){
            level = 'Youngin';
        } else if (click < 65){
            level = 'Adult';
        } else{
            level = "Viejo";
        };
        return level
    }, this);


}



var ViewModel = function(){
    var self = this;

    this.catList = ko.observableArray([]);

    initialCats.forEach(function(catItem){
        self.catList.push ( new Cat(catItem));
    });

    this.getCurrentCat = function(clicked){
        self.currentCat(clicked)
    }

    this.currentCat = ko.observable( this.catList()[0] );

    this.incrementCounter = function(){
        self.currentCat().clickCount(self.currentCat().clickCount() + 1);

    };


}


ko.applyBindings(new ViewModel())
