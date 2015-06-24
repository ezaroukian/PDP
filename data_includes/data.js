
var manualSendResults = false;

var shuffleSequence = mySeq;

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
    leftComment: "(bad)", rightComment: "(good)"
  },
  "Question", {
    as: ["yes","no"],
    randomOrder: false,
	presentHorizontally: true,
	autoFirstChar: true,
  },  
   "PracticeQuestion", {
    as: ["yes","no"],
    html: "<h3 style='text-align:center; color:blue;'>Practice</h3>",
    randomOrder: false,
	presentHorizontally: true,
	autoFirstChar: true,
	hideProgressBar: true,
  }, 
  "Message", {
    hideProgressBar: true
  },
  "Form", {
    hideProgressBar: true,
    continueOnReturn: true,
  }
];

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
	["break","Message", {html: "<p>You are now halfway through the experiment.</p><p>Feel free to take a break</p>"}
	],
	["conf", "AcceptabilityJudgment", {
		s: "",
		q: "How confident are you in the response you just gave?",
		leftComment: "not confident at all?", rightComment: "very confident?"
	}],
	["confPractice", "AcceptabilityJudgment", {
		hideProgressBar: true,
		s: "",
		q: "How confident are you in the response you just gave?",
		leftComment: "not confident at all?", rightComment: "very confident?",
	}],
	["sep", "SeparatorHTML", {
		normalMessage: "<p style='text-align:center; font-style:italic;'>Remember to respond to the diagrams as <b>quickly</b> and as <b>accurately</b> as possible. <p/> <p style='text-align:center; font-style: italic;'>Press any key to continue.</p>",
		ignoreFailure: true
	}],
	["sepPractice", "SeparatorHTML", {
		normalMessage: "<p style='text-align:center; font-weight:bold; color:green;'>Correct!</p><p style='text-align:center; font-style: italic;'>Remember to respond to the diagrams as quickly and as accurately as possible. <p/> <p style='text-align:center; font-style: italic;'>Press any key to continue.</p>",
		errorMessage: "<p style='text-align:center; font-weight:bold; color:red;'>Incorrect!</p><p style='text-align:center; font-style: italic;'>Remember to respond to the diagrams as quickly and as accurately as possible. <p/> <p style='text-align:center; font-style: italic;'>Press any key to continue.</p>",
		hideProgressBar: true
	}],

];

items = items.concat(newTestItems);
items = items.concat(newSUSItems);

//alert(items);
