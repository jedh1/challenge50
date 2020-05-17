const container = document.querySelector('.container');
const seats = document.querySelectorAll('.row .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');
const movieSelect = document.getElementById('movie');

populateUI();

let ticketPrice = +movieSelect.value;

// Functions
// Save selected movie index and price
function setMovieData(movieIndex, moviePrice) {
   localStorage.setItem('selectedMovieIndex', movieIndex);
   localStorage.setItem('selectedMoviePrice', moviePrice);
}

// Update total and count
function updateSelectedCount() {
   const selectedSeats = document.querySelectorAll('.row .seat.selected');
   // Copy selected seats into array. "..." spread syntax will copy values inside an array
   // Map through array and return a new array of indexes
   const seatsIndex = [...selectedSeats].map(function(seat) {
      return [...seats].indexOf(seat);
   });

   // Save selected seats. Need to convert array to string.
   localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

   // Obtain number of elements in node list
   const selectedSeatsCount = selectedSeats.length;
   count.innerText = selectedSeatsCount;
   total.innerText = selectedSeatsCount * ticketPrice;
}

// Get data from localstorage and populate UI
function populateUI () {
   const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));

   if(selectedSeats !== null && selectedSeats.length > 0) {
      seats.forEach((seat, index) => {
         if(selectedSeats.indexOf(index) > -1) {
               seat.classList.add('selected');
         }
      });
   }
   // Update selected movie
   const selectedMovieIndex = localStorage.getItem('selectedMovieIndex');
   if(selectedMovieIndex !== null) {
      movieSelect.selectedIndex = selectedMovieIndex;
   }

}

// Event Listeners
// Movie select Event
movieSelect.addEventListener('change', e => {
   ticketPrice = +e.target.value;
   setMovieData(e.target.selectedIndex, e.target.value);
   updateSelectedCount();
});

// Seat click event
container.addEventListener('click', e => {
   if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')
   ) {
      e.target.classList.toggle('selected');

      updateSelectedCount();
   }
});

// Initial count and total set
updateSelectedCount();
