const myWords = ['javascript', 'coding', 'python', 'blueberries', 'summer', 'mahagony']
let cur = 0;
let startTime = 0;

// Initialize game
function init() {
   console.log('ready');
   let div = document.createElement('div');
   div.setAttribute('class','message');
   div.innerText = "Hover over the boxes to see the scrambled words. Select the correct words to win. Press start button";
   document.body.appendChild(div);
   let button = document.createElement('button');
   button.type = 'button';
   document.body.appendChild(button);
   button.innerText = 'Start Game';
   button.addEventListener('click', start);
   let div1 = document.createElement('div');
   div1.classList.add('game');
   document.body.appendChild(div1);
}

function start() {
   cur = 0;
   startTime = Date.parse(new Date());
   console.log(startTime);
   this.style.display = 'none';
   let tempArr = myWords.slice(0);
   tempArr.sort( (a,b) => {
      return 0.5 - Math.random();
   });
   const game = document.querySelector('.game');
   tempArr.forEach( item => {
      let temp = item.split("");
      temp.sort( (a,b) => {
         return 0.5 - Math.random()
      });
      let temp1 = temp.join("");
      let div = document.createElement('div');
      div.innerText = "Select";
      div.classList.add('box');
      div.word = item;
      div.addEventListener('mouseenter', function() {
         div.style.backgroundColor = "white";
         div.innerText = temp1;
      })
      div.addEventListener('mouseleave', function() {
         div.style.backgroundColor = "red";
         div.innerText = 'select';
      })
      div.addEventListener('click', function() {
         if(div.word === myWords[cur]) {
            console.log('right');
            this.classList.add('hidden');
            cur++;
            nextWord();
         } else {
            console.log('wrong');
         }
      })
      game.appendChild(div);
   })
   nextWord();
}

function nextWord() {
   if(cur >= myWords.length) {
      let endTime = Date.parse(new Date());
      let duration = (endTime - startTime)/1000;
      document.querySelector('.game').innerHTML = '';
      document.querySelector('button').style.display='block';
      message('You have selected all the words. You win! This round took ' + duration + ' seconds.');
   } else {
      message('Hover over the boxes to see words. Select the correct word: '+myWords[cur]);
   }
}

function message(output) {
   document.querySelector('.message').innerHTML = output;
}

// Event Listeners
window.addEventListener('load', init);
