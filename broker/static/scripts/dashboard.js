import { userDeposit, userEarning, earn} from './transaction.js';


function createBarChart(){
  const months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP'];
  const categories = ['General', 'Etherium', 'Bitcoin'];
  const salesData = [
    [10000, 150000, 50000, 200000, 550000, 100000, 300000, 450000, 500000, 250000], 
    [400000, 200000, 50000, 100000, 125000, 250000, 150000, 175000, 75000, 225000],  
    [25000, 100000, 40000, 20000, 70000, 30000, 50000, 60000,  80000, 90000]         
  ];

  const categoryColors = ['rgb(24, 230, 230)', 'rgb(23, 16, 56)', 'rgb(129, 248, 159)'];

  const traces = categories.map((category, index) => ({
    x: months,
    y: salesData[index],
    type: 'bar',
    marker: {
      color: categoryColors[index]
    },
    name: category,
  }));


  const layout = {
    title: 'Past months Total Investments',
    xaxis: {
      title: 'Month',
    },
    yaxis: {
      title: 'Records',
      range: [0, 600000],
      tickformat: '$,d', 
    },
    barmode: 'stack', 
    plot_bgcolor: 'rgb(4, 0, 26)', 
    paper_bgcolor: 'rgb(4, 0, 26)', 
    bargap: 0.6,  
    
    bargroupgap: 0.001
  };


  Plotly.newPlot('chart', traces, layout);
}
createBarChart();


document.querySelector('.balance-fig').innerHTML = `$${userDeposit}`;
document.querySelector('.earnings-fig').innerHTML = `$${userEarning}`;


function showPopup() {
  document.querySelector('.hidden').classList.add('show-popup');


  setTimeout(() => {
    document.querySelector('.hidden').classList.remove('show-popup');

  }, 3000);
}


document.addEventListener("DOMContentLoaded", function() {
  const mineButton = document.getElementById("mineButton");
  const countdownDiv = document.getElementById("countdown");

  let hours = 0;
  let minutes = 0;
  let seconds = 20;
  let countdownInterval;

  function startCountdown() {
 
      mineButton.disabled = true;
      earn();
      const earningsFig = document.querySelector('.earnings-fig');
      earningsFig.innerHTML = `$${parseFloat(userEarning.toFixed(2))}`;

      const remainingTime = localStorage.getItem('remainingTime');
      if (remainingTime) {
          const timeArray = remainingTime.split(':');
          hours = parseInt(timeArray[0]);
          minutes = parseInt(timeArray[1]);
          seconds = parseInt(timeArray[2]);
      } else {
          hours = 0;
          minutes = 0;
          seconds = 20;
      }

      clearInterval(countdownInterval);
      countdownInterval = setInterval(updateCountdown, 1000);
  }

  function updateCountdown() {
      if (hours === 0 && minutes === 0 && seconds === 0) {
          clearInterval(countdownInterval);
          countdownDiv.style.display = 'none';
          mineButton.style.display = 'inline';
          mineButton.disabled = false;
          localStorage.removeItem('remainingTime');
      } else {
          if (seconds === 0) {
              if (minutes === 0) {
                  hours--;
                  minutes = 59;
                  seconds = 59;
              } else {
                  minutes--;
                  seconds = 59;
              }
          } else {
              seconds--;
          }

          mineButton.style.display = 'none';
          countdownDiv.style.display = 'inline';
          countdownDiv.style.backgroundColor = '#2177b1';
          countdownDiv.innerText = (`${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`);


          localStorage.setItem('remainingTime', `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`);
      }
  }

  if (userDeposit < 50){
    mineButton.disabled = true;
    mineButton.classList.add('disabled-btn')
    mineButton.addEventListener("click", showPopup);
  }else{

  mineButton.addEventListener("click", startCountdown);

  const remainingTime = localStorage.getItem('remainingTime');
  if (remainingTime) {
      startCountdown();
  }};
  
});