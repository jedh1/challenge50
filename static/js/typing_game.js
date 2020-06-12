const word = document.getElementById('word');
const text = document.getElementById('text');
const scoreEl = document.getElementById('score');
const timeEl = document.getElementById('time');
const endgameEl = document.getElementById('end-game-container');
const settingsBtn = document.getElementById('settings-btn');
const settings = document.getElementById('settings');
const settingsForm = document.getElementById('settings-form');
const difficultySelect = document.getElementById('difficulty');

// List of words for game
const words = [
"generally","fire","island","parent","swept","right","club","hall","increase","food","that","bottom","something","volume","wild","traffic","stretch","spider","go","accurate","it","tropical","pressure","motion","morning","walk","chosen","learn","front","sun","color","made","alone","send","blew","because","ourselves","ear","very","ants","giant","layers","coffee","shot","steam","high","job","minute","pot","stepped","already","cow","mathematics","customs","stood","government","south","we","shown","proud","great","own","provide","party","examine","material","stone","twice","coming","curious","his","saved","brother","produce","short","play","treated","egg","freedom","horse","occasionally","careful","tomorrow","corn","quick","newspaper","iron","upward","dear","balloon","sort","all","tightly","date","noun","within","plain","wherever","movie","nine","middle","catch","keep","model","work","fine","gun","opposite","eat","grew","nearest","she","tax","remember","lying","writing","eager","equator","fight","enemy","gently","shut","judge","social","street","ability","die","empty","mill","hope","hearing","boat","season","film","wave","refused","piano","wooden","chart","limited","poor","case","news","rush","thy"
];

// Init word
let randomWord;

// Init score
let score = 0;

// Init time
let time = 10;

// Set difficulty to value in localStorage or medium
let difficulty =
   localStorage.getItem('difficulty') !== null
   ? localStorage.getItem('difficulty')
   : 'medium';

// Set difficulty select value
difficultySelect.value =
   localStorage.getItem('difficulty') !== null
   ? localStorage.getItem('difficulty')
   : 'medium';

// Focus on text on start
text.focus();

// Start counting down
const timeInterval = setInterval(updateTime, 1000);

// Generate random word from array
function getRandomWord() {
   return words[Math.floor(Math.random() * words.length)];
}

// Add word to DOM
function addWordtoDOM() {
   randomWord = getRandomWord();
   word.innerHTML = randomWord;
}

// Update score
function updateScore() {
   score++;
   scoreEl.innerHTML = score;
}

// Update time
function updateTime() {
   time--;
   timeEl.innerHTML = time + 's';

   if(time === 0) {
      clearInterval(timeInterval);
      // end game
      gameOver();
   }
}

// Game over, show end screen
function gameOver() {
   endgameEl.innerHTML = `
      <h1>Time ran out</h1>
      <p>Your final score is ${score}</p>
      <button onclick="location.reload()">Reload</button>
   `;
   endgameEl.style.display = 'flex';
}

addWordtoDOM();

// Event Listeners

// Typing
text.addEventListener('input', e => {
   const insertedText = e.target.value;

   if(insertedText === randomWord) {
      addWordtoDOM();
      updateScore();

      // Clear text input
      e.target.value = '';

      if(difficulty === 'hard') {
         time += 1;
      } else if (difficulty === 'medium') {
         time += 3;
      } else {
         time += 5;
      }

      updateTime();
   }
});

// Settings button click to hide
settingsBtn.addEventListener('click', () => settings.classList.toggle('hide'));

// Settings select
settingsForm.addEventListener('change', e => {
   difficulty = e.target.value;
   localStorage.setItem('difficulty', difficulty);
});
