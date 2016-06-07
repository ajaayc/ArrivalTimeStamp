function recordRate()
{
    alert("Beginning of function!")
    $.ajax({
	//<iframe src="https://docs.google.com/forms/d/1IFjsbafZddKlqVogD9Rm49XIWP1mVWUGg7g0m8W0UkI/viewform?embedded=true#start=embed" width="760" height="500" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
	//Form Key:
	//1IFjsbafZddKlqVogD9Rm49XIWP1mVWUGg7g0m8W0UkI
        url: "https://docs.google.com/1IFjsbafZddKlqVogD9Rm49XIWP1mVWUGg7g0m8W0UkI/formResponse",
        data: {},
        type: "POST",
        dataType: "xml",
        statusCode: {
            0: function (){
                //Success message
		alert("Successfully sent timestamp! Code 0")
            },
            200: function (){
                //Fail Message
		alert("Successfully sent timestamp! Code 200")
            },
            400: function (){
                //Fail Message
		alert("Failed at sending timestamp!")
            },
	    404: function (){
                //Fail Message
		alert("FAILED!")
            }
        }
    });
    alert("Reached end of function!")
}
