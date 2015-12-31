

function createPieChart(raceId) {
	var width = 600,
	    height = 400,
	    radius = Math.min(width, height) / 2;
	
	var color = d3.scale.ordinal()
	    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

	var arc = d3.svg.arc()
	    .outerRadius(radius - 10)
	    .innerRadius(0);

	var labelArc = d3.svg.arc()
	    .outerRadius(radius - 40)
	    .innerRadius(radius - 40);

	var pie = d3.layout.pie()
	    .sort(null)
	    .value(function(d) { return d.score; });

	var svg = d3.select("#pie_chart").append("svg")
	    .attr("width", width)
	    .attr("height", height)
	  .append("g")
	    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

	d3.json("/race/"+raceId+"/score_pie_chart", function(error, data) {
	  if (error) throw error;

	  var g = svg.selectAll(".arc")
	      .data(pie(data))
	    .enter().append("g")
	      .attr("class", "arc");

	  g.append("path")
	      .attr("d", arc)
	      .style("fill", function(d) { return color(d.data.horse); });

	  g.append("text")
	      .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
	      .attr("dy", ".35em")
	      .text(function(d) { return d.data.horse; });
	});

	function type(d) {
	  d.score = +d.score;
	  return d;
	}
}

function createDistributionChart(raceId) {
	var data = [];

	getData(); // popuate data 

	// line chart based on http://bl.ocks.org/mbostock/3883245
	var margin = {
	        top: 20,
	        right: 50,
	        bottom: 30,
	        left: 50
	    },
	    width = 600 - margin.left - margin.right,
	    height = 400 - margin.top - margin.bottom;

	var x = d3.scale.linear()
	    .range([0, width]);

	var y = d3.scale.linear()
	    .range([height, 0]);

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left");

	var line = d3.svg.line()
	    .x(function(d) {
	        return x(d.q);
	    })
	    .y(function(d) {
	        return y(d.p);
	    });

	var svg = d3.select("#distribution_chart").append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	    .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	x.domain(d3.extent(data, function(d) {
	    return d.q;
	}));
	y.domain(d3.extent(data, function(d) {
	    return d.p;
	}));

	svg.append("g")
	    .attr("class", "x axis")
	    .attr("transform", "translate(0," + height + ")")
	    .call(xAxis);

	svg.append("g")
	    .attr("class", "y axis")
	    .call(yAxis);

	svg.append("path")
	    .datum(data)
	    .attr("class", "line")
	    .attr("d", line);

	function getData() {
		// loop to populate data array with 
		// probabily - quantile pairs
		for (var i = 0; i < 100000; i++) {
		    q = normal() // calc random draw from normal dist
		    p = gaussian(q) // calc prob of rand draw
		    el = {
		        "q": q,
		        "p": p
		    }
		    data.push(el)
		};

		// need to sort for plotting
		//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
		data.sort(function(x, y) {
		    return x.q - y.q;
	});	

	}

	// from http://bl.ocks.org/mbostock/4349187
	// Sample from a normal distribution with mean 0, stddev 1.
	function normal() {
	    var x = 0,
	        y = 0,
	        rds, c;
	    do {
	        x = Math.random() * 2 - 1;
	        y = Math.random() * 2 - 1;
	        rds = x * x + y * y;
	    } while (rds == 0 || rds > 1);
	    c = Math.sqrt(-2 * Math.log(rds) / rds); // Box-Muller transform
	    return x * c; // throw away extra sample y * c
	}

	//taken from Jason Davies science library
	// https://github.com/jasondavies/science.js/
	function gaussian(x) {
		var gaussianConstant = 1 / Math.sqrt(2 * Math.PI),
			mean = 0,
	    	sigma = 1;

	    x = (x - mean) / sigma;
	    return gaussianConstant * Math.exp(-.5 * x * x) / sigma;
	};
}

function createScatterplot(raceId) {
	var margin = {top: 30, right: 50, bottom: 30, left: 40},
    width = 600 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

	var x = d3.scale.linear()
	    .range([0, width]);

	var y = d3.scale.linear()
	    .domain([0,12])
	    .range([height, 0]);

	var color = d3.scale.category10();

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left");

	var svg = d3.select("#scatterplot_graph").append("svg")
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	d3.json("/race/"+raceId+"/scatter_plot_graph", function(error, data) {

	  x.domain(d3.extent(data, function(d) { return d.score; })).nice();

	  svg.append("g")
	      .attr("class", "x axis")
	      .attr("transform", "translate(0," + height + ")")
	      .call(xAxis)
	    .append("text")
	      .attr("class", "label")
	      .attr("x", width)
	      .attr("y", -6)
	      .style("text-anchor", "end")
	      .text("Score");

	  svg.selectAll(".dot")
	      .data(data)
	    .enter().append("circle")
	      .attr("class", "dot")
	      .attr("r", 6.5)
	      .attr("cx", function(d) { return x(d.score); })
	      .attr("cy", function(d) { return y(d.num); })
	      .style("fill", function(d) { return color(d.horse); });

	  var legend = svg.selectAll(".legend")
	      .data(color.domain())
	    .enter().append("g")
	      .attr("class", "legend")
	      .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

	  legend.append("rect")
	      .attr("x", width)
	      .attr("width", 18)
	      .attr("height", 18)
	      .style("fill", color);

	  legend.append("text")
	      .attr("x", width - 24)
	      .attr("y", 9)
	      .attr("dy", ".35em")
	      .style("text-anchor", "end")
	      .text(function(d) { return d; });

	});
}
	
