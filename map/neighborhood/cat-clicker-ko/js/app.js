var ViewModel = function(){
    this.clickCount = ko.observable(0);
    this.name = ko.observable('Tabby');
    this.imgSrc = ko.observable('img/434164568_fea0ad4013_z.jpg');
    this.imgAttribution = ko.observable('https://www.flickr.com/photos/big');
    this.level = ko.observable('Newborn')


    this.incrementCounter = function(){
        this.clickCount(this.clickCount() + 1);

        if (this.clickCount() > 30){
            this.level('Youngie');
        } else if (this.clickCount() > 20) {
            this.level('Teen');
        } else if (this.clickCount() > 10) {
            this.level('Infant');
        }
    };

}


ko.applyBindings(new ViewModel())
