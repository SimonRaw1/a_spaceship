function submit_request() {
    axios.get('/submit')
  .then( (response) => {
    // handle success
  
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
}
function getValue(ddl) {
  var select = document.getElementById(ddl).value;
  if (select == "1") {
    return "squat"
  }
  if (select == "2") {
    return "bench"
  }
  if (select == "3") {
    return "deadlift"
  }
  return null;
}
function display_request(selection) {
  axios.get(`/display/${selection}`)
.then( (response) => {
  // handle success
  var div = document.getElementById("json_table");
  div.innerHTML = response.data;
})
.catch(function (error) {
  // handle error
  console.log(error);
})
}
$( "#submit_button" ).on( "click", function() {
    selection = getValue("select1");
    // window.location = "display";
    console.log(selection);
    display_request(selection);
    
  } );

$( "#squat_display_button" ).on( "click", function() {
    display_request("squat");
 } );

 $( "#bench_display_button" ).on( "click", function() {
    display_request("bench");
} );

$( "#deadlift_display_button" ).on( "click", function() {
    display_request("deadlift");
} );


$(document).ready( () => {
    console.log("We are ready!");
});


