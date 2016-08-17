
var manualSendResults = true;
var order = Math.round(Math.random());
//alert(order);
//var shuffleSequence = [mySeqNC,mySeqCN][order];
var shuffleSequence = seq("endSurvey");

var defaults = [
  "Separator", {
    transfer: "keypress",
    normalMessage: "Please wait for the next statement.",
    errorMessage: "Wrong. Please wait for the next statement."
  },
  "AcceptabilityJudgment", {countsForProgressBar: false,
    as: ["1", "2", "3", "4", "5", "6", "7"],
    presentAsScale: true,
    instructions: "Use number keys or click boxes to answer.",
    leftComment: "(bad)", rightComment: "(good)",
	countsForProgressBar: true
  },
  "Question", {
    as: ["yes","no"],
    randomOrder: false,
	presentHorizontally: true,
	autoFirstChar: true
  },  
   "PracticeQuestion", {
    as: ["yes","no"],
    html: "<h3 style='text-align:center; color:blue;'>Practice</h3>",
    randomOrder: false,
	presentHorizontally: true,
	autoFirstChar: true,
	hideProgressBar: true,
	countsForProgressBar: false
  }, 
  "Message", {
    hideProgressBar: true
  },
  "Form", {
    hideProgressBar: true,
    continueOnReturn: true
  }

];

var code = Math.floor(Math.random()*1000000);
var completionMessage ='<center><h3>Thank you for your participation!</h3><p>This study was designed to assess how quickly and accurately human users respond to statements in plain English (e.g. "John sees a letter") versus a restricted computer-readable form of English (e.g. "The person John sees the letter l1"). Your responses will help us design computer-readable languages that can still be quickly and accurately understood by human users.</p><p>Your code is:</p>'+code.toString()+'<p>Be sure to enter this code on the Amazon Mechanical Turk site so that you can be rewarded for completing this HIT.</p></center>';
var completionErrorMessage = "The transmission of the results failed!  Please contact erin.g.zaroukian.ctr@mail.mil with your participation code: " + code.toString(); 

function uniqueMD5() {
    // Time zone.
    var s = "" + new Date().getTimezoneOffset() + ':';

    // Plugins.
    var plugins = [
        "Java",
        "QuickTime",
        "DevalVR",
        "Shockwave",
        "Flash",
        "Windows Media Player",
        "Silverlight",
        "VLC Player"
    ];
    for (var i = 0; i < plugins.length; ++i) {
        var v = PluginDetect.getVersion(plugins[i]);
        if (v) s += plugins[i] + ':' + v;
    }

    // Whether or not cookies are turned on.
    createCookie("TEST", "TEST", 0.01); // Keep it for 0.01 days.
    if (readCookie("TEST") == "TEST")
        s += "C";

    // Screen dimensions and color depth.
    var width = screen.width ? screen.width : 1;
    var height = screen.height ? screen.height : 1;
    var colorDepth = screen.colorDepth ? screen.colorDepth : 1;
    s += width + ':' + height + ':' + colorDepth;

    return b64_md5(s);
}





var items = [
	["intro","Form", {html: {include: "survey.html"}}
	],
	["intro","Message", {html: {include: "intro.html"}}
	],
	["toPractice","Message", {html: {include: "intro2.html"}}
	],
	["endPractice","Message", {html: {include: "introEnd.html"}}
	],
	["toSUS","Message", {html: "<p>You will now be asked a series of questions about the sentence-diagram system you just used.</p>"}
	],
	["endSurvey","Form", {html: {include: "endSurvey.html"}}
	],	
	["endSurvey", "Question", {
		q: code.toString(), 
		as: ['done','done'],
		timeout: 1
		}
	],
	["endSurvey", "__SendResults__", { }],
	["endSurvey","Message", {html: { '<center><h3>Thank you for your participation!</h3><p>This study was designed to assess how quickly and accurately human users respond to statements in plain English (e.g. "John sees a letter") versus a restricted computer-readable form of English (e.g. "The person John sees the letter l1"). Your responses will help us design computer-readable languages that can still be quickly and accurately understood by human users.</p><p>Your code is:</p>'+code.toString()+'<p>Be sure to enter this code on the Amazon Mechanical Turk site so that you can be rewarded for completing this HIT.</p></center>';}, 
							transfer: null }
	],

	["break","Message", {html: "<p>You are now halfway through the experiment.</p><p>Feel free to take a break.</p><p>The second half will the much like the first half, but the sentences you read will be in a different form.</p>"}
	],
	["conf", "AcceptabilityJudgment", {
		s: "",
		q: "How confident are you in the response you just gave?",
		leftComment: "not confident at all?", rightComment: "very confident?",
		countsForProgressBar: true
	}],
	["confPractice", "AcceptabilityJudgment", {
		hideProgressBar: true,
		s: "",
		q: "How confident are you in the response you just gave?",
		leftComment: "not confident at all?", rightComment: "very confident?"
	}],
	["sep", "Message", {
		html: "<p style='text-align:center; font-style:italic;'>Remember to respond to the diagrams as <b>quickly</b> and as <b>accurately</b> as possible. <p/>",
		countsForProgressBar: false,
		hideProgressBar: false
	}],
	["sepPractice", "ClickSeparator", {
		html: "<p style='text-align:center; font-style: italic;'>Remember to respond to the diagrams as <b>quickly</b> and as <b>accurately</b> as possible. <p/>",
		normalMessage: "<p style='text-align:center; font-weight:bold; color:green;'>Correct!</p>",
		errorMessage: "<p style='text-align:center; font-weight:bold; color:red;'>Incorrect!</p> ",
		hideProgressBar: true,
		countsForProgressBar: false
	}]
	
	

];

items = items.concat(newTestItems);
items = items.concat(newSUSItems);

//alert(items);
