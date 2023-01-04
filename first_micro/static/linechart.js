
d3
.csv("/first_micro/data/data_egea.csv")
.then(makeChart);

// Line chart
new Chart(document.getElementById("myCanvas"), {
    type: 'line',
    data: {
      labels: date,
      datasets: [{
          data: data_egea[egea],
          label: "Egea",
          borderColor: "#3e95cd",
          fill: false
         }]},
        
        options: {
            title: {
              display: true,
              text: 'Research of the word "Egea" over time'
            },
            hover: {
             mode: 'index',
             intersect: true
            },
        }});
        
        