const ctx = document.getElementById("revenueChart");

if(ctx){

new Chart(ctx,{

type:"line",

data:{

labels:["Jan","Feb","Mar","Apr","May","Jun"],

datasets:[{

label:"Revenue",

data:[12,19,14,28,35,45]

}]

}

});

}