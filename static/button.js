//Got instructions from https://wiki.base22.com/pages/viewpage.action?pageId=72942000
//Form URL:
//https://docs.google.com/forms/d/1IFjsbafZddKlqVogD9Rm49XIWP1mVWUGg7g0m8W0UkI/viewform
//Sample URL:
//https://docs.google.com/a/YOURDOMAIN.com/forms/d/15QFO2VE44-9gAwcJeTPPWvxAX7v_1Ye9qmjdX2VzLBw/formResponse
//Replace YOURDOMAIN.com with umich.edu
function recordRate()
{
    console.log("Beginning of function!")
    console.log("ayyyyyyyyyyy")
    $.ajax({

	//Form Key:
	//1IFjsbafZddKlqVogD9Rm49XIWP1mVWUGg7g0m8W0UkI
	url: "https://docs.google.com/a/umich.edu/forms/d/1IFjsbafZddKlqVogD9Rm49XIWP1mVWUGg7g0m8W0UkI/formResponse",
        data: {},
        type: "POST",
        dataType: "xml",
        statusCode: {
            0: function (){
                //Success message
		console.log("Successfully sent timestamp! Code 0")
            },
            200: function (){
                //Fail Message
		console.log("Successfully sent timestamp! Code 200")
            },
            400: function (){
                //Fail Message
		console.log("Failed at sending timestamp!")
            },
	    404: function (){
                //Fail Message
		console.log("FAILED!")
            }
        }
    });
    console.log("Reached end of function!")
}
