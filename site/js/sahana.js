var color = {
	diabetes: "#6633cc",
	pain: "#651067",
	muscle: "#e67300",
	women_related: "#316395",
	lung_liver: "#8b0707",
	heart: "#0099c6",
	blood: "#b82e2e",
	infection: "#3366cc"
};

function call(year) {

	file = "userModelData" + year + ".json";
	//console.log(file);
	//document.getElementById("blahdiv").innerHTML = "";
	function loadJSON(file, callback) {

		var xobj = new XMLHttpRequest();
		xobj.overrideMimeType("application/json");
		xobj.open('GET', file, true); // Replace 'my_data' with the path to your file
		xobj.onreadystatechange = function () {
			if (xobj.readyState == 4 && xobj.status == "200") {
				// Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
				callback(xobj.responseText);
			}
		};
		xobj.send(null);
	}

	loadJSON(file, function (response) {

		var actual_JSON = JSON.parse(response);
		//console.log(actual_JSON);
		var data = actual_JSON;


		/*var data=[

		["women_related", "Robert Denver", 0.5407291787567883], ["pain", "Drew Sebring", 0.4859202725800154], ["pain", "Ann W. Edmundson", 0.416503160606981], ["women_related", "Heather Rob", 0.47548396551729116], ["heart", "ChristinaInDenver", 0.552158051937673665], ["diabetes", "Dan Jaris", 0.5288113196642984], ["heart", "David W. Stein", 0.37666347997866995], ["women_related", "Elizabeth Hanes", 0.4623494665901597], ["heart", "Mary Jane", 0.052158051937673665], ["heart", "Mary Jane", 0.052158051937673665], ["pain", "Mary Jane", 0.4388835385331528], ["pain", "Mary Jane", 0.28374498022050954], ["pain", "Mary Jane", 0.545157491112991], ["women_related", "Mary Jane", 0.34972852763118595], ["women_related", "Jane Harrison-Hohner", 0.6750189473656598], ["heart", "Kristen A. Binaso", 0.952158051937673665], ["infection", "Matthew Hoffman", 0.593766138397236], ["diabetes", "Matthew Hoffman", 0.4842828687914324], ["women_related", "Matthew Hoffman", 0.6587792037374086], ["women_related", "Matthew Hoffman", 0.6587893188033005], ["infection", "Matthew Hoffman", 0.5410011523658171], ["infection", "Matthew Hoffman", 0.3912314125279794], ["blood", "Matthew Hoffman", 0.2966068915307906], ["pain", "Matthew Hoffman", 0.23852614190717375], ["lung_liver", "Matthew Hoffman", 0.2936672462343827], ["diabetes", "Matthew Hoffman", 0.36527100942838076], ["diabetes", "Matthew Hoffman", 0.36563092107267825], ["diabetes", "Matthew Hoffman", 0.528814444024778], ["heart", "Matthew Hoffman", 0.40710247980686093], ["pain", "Matthew Hoffman", 0.40616016169403335], ["infection", "Matthew Hoffman", 0.4147808149739223], ["infection", "Matthew Hoffman", 0.5964134609687426], ["heart", "Matthew Hoffman", 0.4076463668776414], ["infection", "Matthew Hoffman", 0.4948019627819532], ["infection", "Matthew Hoffman", 0.405869068091445], ["infection", "Carolyn O'Neil", 0.3562557182192783], ["lung_liver", "Carolyn O'Neil", 0.43063775466138315], ["muscle", "Carolyn O'Neil", 0.5517669637848326], ["pain", "Carolyn O'Neil", 0.4038789088627594], ["women_related", "Carolyn O'Neil", 0.35983852722842863], ["heart", "Carolyn O'Neil", 0.412186413183487], ["women_related", "Carolyn O'Neil", 0.35256719828520316], ["pain", "Carolyn O'Neil", 0.40290673984545383], ["pain", "Carolyn O'Neil", 0.46200024883438484], ["diabetes", "Carolyn O'Neil", 0.28816078222328767], ["blood", "Carolyn O'Neil", 0.2851664237957946], ["heart", "Carolyn O'Neil", 0.28755017765376717], ["pain", "Carolyn O'Neil", 0.48591923184046015], ["pain", "Carolyn O'Neil", 0.3035208249665344], ["pain", "Carolyn O'Neil", 0.4035833196600888], ["lung_liver", "Melissa Palmer", 0.4567933702168219], ["diabetes", "Michael Dansinger", 0.5118631612080021], ["diabetes", "Michael W. Smith", 0.2685038297989958], ["pain", "Kate Madison", 0.5135721015454219], ["diabetes", "Sheldon Marks", 0.4960406965233724], ["pain", "Felicia Thomas", 0.39831216670024044], ["women_related", "Felicia Thomas", 0.41234502221788333], ["lung_liver", "Felicia Thomas", 0.3557386742447545], ["pain", "Felicia Thomas", 0.3199974179268488], ["pain", "Felicia Thomas", 0.5522565108288344], ["women_related", "Felicia Thomas", 0.31328300848669205], ["lung_liver", "Felicia Thomas", 0.508219646941257], ["diabetes", "Felicia Thomas", 0.5579705972521762], ["diabetes", "Felicia Thomas", 0.5263376280010188], ["diabetes", "Felicia Thomas", 0.4842819907981024], ["pain", "Felicia Thomas", 0.46922056768204223], ["muscle", "Felicia Thomas", 0.3176571087758899], ["infection", "Felicia Thomas", 0.23750544713922325], ["blood", "Felicia Thomas", 0.2758689005931884], ["infection", "Felicia Thomas", 0.4346790851481043], ["infection", "Felicia Thomas", 0.4250752430242612], ["heart", "Felicia Thomas", 0.052158051937673665], ["diabetes", "Felicia Thomas", 0.19999976171974407], ["infection", "Felicia Thomas", 0.4486304145168213], ["pain", "Felicia Thomas", 0.2662944508362075], ["pain", "Felicia Thomas", 0.5135671992209828], ["infection", "Felicia Thomas", 0.522471059817406], ["muscle", "Felicia Thomas", 0.3971176639664176], ["lung_liver", "Felicia Thomas", 0.24133377008888615], ["women_related", "Felicia Thomas", 0.7239395279909883], ["blood", "Felicia Thomas", 0.3060242961447235], ["pain", "Felicia Thomas", 0.5066605469479117], ["infection", "Felicia Thomas", 0.24448029151929582], ["pain", "Felicia Thomas", 0.30221778671648053], ["women_related", "Felicia Thomas", 0.27519440964390973], ["infection", "Felicia Thomas", 0.34797935660108614], ["blood", "Felicia Thomas", 0.2592864025620441], ["women_related", "Felicia Thomas", 0.5333054625925054], ["women_related", "Felicia Thomas", 0.6808947464508631], ["women_related", "Felicia Thomas", 0.42098250920229185], ["women_related", "Felicia Thomas", 0.5341143101522229], ["diabetes", "Felicia Thomas", 0.3188867650334335], ["heart", "Rose Pitt", 0.952158051937673665], ["pain", "Mellissa Green", 0.3199858537235827], ["pain", "Dory S", 0.5377725265884145]
		];*/
		var svg = d3.select("#svg1Container");
		svg.selectAll("*").remove();

		var svg = d3.select("#svg1Container").append("svg").attr("width", 900).attr("height", 1900);
		$("svg").css({
			top: 200,
			left: -30,
			position: 'absolute'
		});

		svg.append("text").attr("x", 360).attr("y", 80)
			.attr("class", "header").text("Topics and user Mapping");


		var g = [svg.append("g").attr("transform", "translate(150,100)"), svg.append("g").attr("transform", "translate(650,100)")];

		var bp = [viz.bP()
			.data(data)
			.min(12)
			.pad(1)
			.height(1700)
			.width(400)
			.barSize(35)
			.fill(d => color[d.primary]), viz.bP()
			.data(data)
			.value(d => d[3])
			.min(12)
			.pad(1)
			.height(1600)
			.width(300)
			.barSize(35)
			.fill(d => color[d.primary])
		];

		[0].forEach(function (i) {
			g[i].call(bp[i])

			g[i].append("text").attr("x", -50).attr("class", "words").attr("y", -8).style("text-anchor", "middle", "font-weight", "bold").text("Topics");
			g[i].append("text").attr("x", 420).attr("class", "words").attr("y", -8).style("text-anchor", "middle").text("Users");


			g[i].selectAll(".mainBars")
				.on("mouseover", mouseover)
				.on("mouseout", mouseout)
				.on("click", click);


			g[i].selectAll(".mainBars").append("text").attr("class", "label")
				.attr("x", d => (d.part == "primary" ? -30 : 20))
				.attr("y", d => +6)
				.text(d => d.key)
				.attr("text-anchor", d => (d.part == "primary" ? "end" : "start"));

			g[i].selectAll(".mainBars").append("text").attr("class", "perc")
				.attr("x", d => (d.part == "primary" ? -105 : 130))
				.attr("y", d => +6)
				.text(function (d) {
					return d3.format("0.0%")(d.percent)
				})
				.attr("text-anchor", d => (d.part == "primary" ? "end" : "start"));
		});

		function mouseover(d) {
			[0].forEach(function (i) {
				console.log(i)
				bp[i].mouseover(d);

				g[i].selectAll(".mainBars").select(".perc")
					.text(function (d) {
						return d3.format("0.0%")(d.percent)
					});
			});
		}

		function mouseout(d) {
			[0].forEach(function (i) {
				bp[i].mouseout(d);

				g[i].selectAll(".mainBars").select(".perc")
					.text(function (d) {
						return d3.format("0.0%")(d.percent)
					});
			});
		}
		d3.select(self.frameElement).style("height", "900px");
	});


	function click(d) {
		//console.log(d.part+"==>"+d.key);
		if (d.part === "secondary")
			color1 = "#000";
		else
			color1 = color[d.key];
		add1(d.part, d.key, year, color1);
		//console.log(color[d.key]);


	}

}