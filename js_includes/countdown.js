function initializeClock(){
	var timeInSeconds = 10; 
	var currentTime = Date.parse(new Date()); 
	return new Date(currentTime + timeInSeconds*1000);
	//var timeInterval = setInterval(updateClock(), 1000);	
}

function getTimeRemaining(endtime){  
	var t = Date.parse(endtime) - Date.parse(new Date());  
	var seconds = Math.floor( (t/1000) % 60 );  
	return { 
		"total": t,
		"seconds": seconds  
	};
}

function updateClock(){
	
	t = getTimeRemaining(deadline)
	try{
		document.getElementById("clockdiv").innerHTML = "seconds remaining: " + t.seconds;
		if(t.total<=0){
			clearInterval(timeInterval);
		}		
	}
	catch(err){
		throw(err);
		//It's fine, there's no clockdiv on this page
	}
}





//updateClock();	
//var timeInterval = setInterval(updateClock, 1000);
	
/* function initializeClock(){

var timeInSeconds = 10; 
var currentTime = Date.parse(new Date()); 
); 
}

function updateClock(){
function getTimeRemaining(endtime){  
	var t = Date.parse(endtime) - Date.parse(new Date());  
	var seconds = Math.floor( (t/1000) % 60 );  
	return {    "total": t,    "seconds": seconds  };
	}
}
	
var timeInterval = setInterval(function(){   
	var t = getTimeRemaining(deadline);
	try{
		document.getElementById("clockdiv").innerHTML = "seconds remaining: " + t.seconds;
		if(t.total<=0){
			clearInterval(timeInterval);
		}		
	}
	catch(err){
		//It's fine, there's no clockdiv on this page
	}
	},1000) */