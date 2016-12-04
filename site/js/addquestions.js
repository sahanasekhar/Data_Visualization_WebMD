function add(questionId, year, color, value, topicname) {

  console.log(questionId);
  //console.log(color);

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


  function load() {


    document.getElementById("blahdiv").innerHTML = "";
    var file = "mainDataF" + year + ".json";
    //console.log(str);    
    loadJSON(file, function (response) {

      var actual_JSON = JSON.parse(response);

      // console.log(actual_JSON[0]["questionTitle"]);
      //console.log(actual_JSON[0]["answerContent"]);
      //console.log(actual_JSON.length());
      //console.log(actual_JSON); 
      /*if(topicname!=null)
      {
        var maindiv = document.getElementById("blahdiv");
      var topicheader = document.createElement('h4');
      topicheader.textContent = topicname +" related questions";
      maindiv.appendChild(topicheader);
    }*/
      var outerpanel = ["panel-default", "panel-primary", "panel-success", "panel-info", "panel-warning", "panel-danger"];

      for (var i = 0; i < actual_JSON.length; i++) {
        if (actual_JSON[i]["questionId"] == questionId) {
          var maindiv = document.getElementById("blahdiv");

          var heading = document.createElement('div');
          heading.id = "header";
          heading.className = "panel" + ' ' + outerpanel[3];
          maindiv.appendChild(heading);

          var contentheader = document.createElement('div');
          contentheader.className = "panel-heading";
          contentheader.textContent = "QuestionId: "+questionId;
          heading.appendChild(contentheader);

          var div = document.createElement('div');
          div.id = "iddiv";
          div.className = 'panel' + ' ' + outerpanel[1];

          maindiv.appendChild(div);


          var insidediv1 = document.createElement('div');
          insidediv1.className = "panel-heading";
          insidediv1.id = "insidiv1";
          insidediv1.textContent = actual_JSON[i]["questionTitle"];
          insidediv1.style.backgroundColor = color;
          div.appendChild(insidediv1);


          var insidediv2 = document.createElement('div');
          insidediv2.className = "panel-body";
          insidediv2.id = "insidiv2";
          insidediv2.textContent = actual_JSON[i]["answerContent"];
          insidediv2.title = value;
          insidediv2.datatoggle = "tooltip";


          div.appendChild(insidediv2);
        }
      }


    });


  }

  load();
}


function add1(part, topicname, year, color) {

  //console.log(questionId);
  //console.log(color);
  if (part === "primary")

    name = "topicName";
  else {
    if (isNaN(topicname))
      name = "memberName";
    else
      name = "answerMemberId";
  }

  //console.log(name);
  //console.log(topicname);

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


  function load() {


    document.getElementById("blahdiv").innerHTML = "";
    var file = "mainDataF" + year + ".json";
    //console.log(str);    
    loadJSON(file, function (response) {

      var actual_JSON = JSON.parse(response);

      // console.log(actual_JSON[0]["questionTitle"]);
      //console.log(actual_JSON[0]["answerContent"]);
      //console.log(actual_JSON.length());
      //console.log(actual_JSON); 
      var outerpanel = ["panel-default", "panel-primary", "panel-success", "panel-info", "panel-warning", "panel-danger"];

      for (var i = 0; i < actual_JSON.length; i++) {
        if (actual_JSON[i][name] == topicname) {
          var maindiv = document.getElementById("blahdiv");

          var div = document.createElement('div');
          div.id = "iddiv";
          div.className = 'panel' + ' ' + outerpanel[1];

          maindiv.appendChild(div);


          var insidediv1 = document.createElement('div');
          insidediv1.className = "panel-heading";
          insidediv1.id = "insidiv1";
          insidediv1.textContent = actual_JSON[i]["questionTitle"];
          insidediv1.style.backgroundColor = color;
          div.appendChild(insidediv1);


          var insidediv2 = document.createElement('div');
          insidediv2.className = "panel-body";
          insidediv2.id = "insidiv2";
          insidediv2.textContent = actual_JSON[i]["answerContent"];


          div.appendChild(insidediv2);
        }
      }


    });


  }

  load();
}