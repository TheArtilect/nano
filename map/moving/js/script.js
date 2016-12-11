
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var streetIn = $('#street').val();
    var cityIn = $('#city').val();
    var cityW = (cityIn.split(' ')).join("%20")
    var loc = streetIn + ",_" + cityIn;
    var url = "http://maps.googleapis.com/maps/api/streetview?size=600x400&location=%LOC%"
    var source = url.replace("%LOC%", loc)
    console.log(source)



    $('body').append("<img class='bgimg' id='picture' src='" + source + "'>");
    // YOUR CODE GOES HERE!

    var urlLoc = ((streetIn + " " + cityIn).split(" ")).join("+")
    var apiKey = "56444d2c06dd4e9aba0fefdcb12077da"

    var article = "https://api.nytimes.com/svc/search/v2/articlesearch.json" + "?api-key=" + apiKey + "&q=" + urlLoc + "&sort=newest";


  // $("#test").html(article)

    $.getJSON(article, function(data){
      $("#nytimes-header").text("NYT Articles About" + streetIn + ', ' + cityIn);
      articles = data.response.docs;
      for (var i = 0; i < articles.length; i++) {
        var article = articles[i];
        $("#nytimes-articles").append(
          "<li class='article'>" +
          "<a target='_blank' href='" + article.web_url + "'>" + article.headline.main + "</a>" +
          "<p>" + article.snippet + "</p>" +
          "</li>");
      };
    }).error(function() {
      $("#nytimes-header").text("New York Times Articles Could Not Be Loaded");
    })


    var addy = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + cityIn + "&format=json&callback=wikiCallback";


    	// $("#wikipedia-header").html(addy);

	var wikiRequestTimeout = setTimeout(function(){
		$("#wikipedia-links").text("failed to get wikipedia resources");
	}, 8000);

	$.ajax({
		url: addy,
		dataType: 'jsonp',
		success: function(wiki) {
			for (var i = 0; i < wiki[1].length; i++){
				var headline = wiki[1][i];
				var linkA = 'http://en.wikipedia.org/wiki/' + wiki[1][i];
				$("#wikipedia-links").append("<li>" +
    				"<a href='" + linkA + "'>" + headline + "</a>" +
    				"</li>")
			};

			clearTimeout(wikiRequestTimeout);
		}
	});


    return false;
};

$('#form-container').submit(loadData);
