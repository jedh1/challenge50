const output = document.querySelector('.output');
const btn = document.querySelector('button');

let url;
const feedID = '1m0-4lG1745czuznNwFTKT5fS7vGiWCj5B-wtiT0LqQg';
const feed = 'https://spreadsheet.google.com/feeds/list/'+feedID+'/1/public/values?alt=json';

let myData = [
   ["Title", "Content"],
   ["Row1", "Content1"],
   ["Row2", "Hello"],
   ["Row2", "Data"],
];

btn.addEventListener('click', () => {
   createCSV(myData);
})

function clean(row) {
   let response = '';
   row.forEach((cell,index) => {
      console.log(cell);
      cell = cell == null ? '' : cell.toString();
      if(cell.search(/("|,|\n)/g) >= 0 ) cell = '"' + cell + '"';
      if(index>0) {
         response += ",";
      }
      response += cell;
   })
   return response;
}

function createCSV(data){
   console.log(data);
   let file;
   let holder = '';
   if(url !== null){
      window.URL.revokeObjectURL(url);
   }
   let filename = "test.csv";
   let properties = {
      type:"text/csv;charset=utf-8;"
   };
   data.forEach(item => {
      holder += clean(item) + '\n';
   })
   file = new File([holder], filename, properties);
   let link = document.createElement('a');
   url = window.URL.createObjectURL(file);
   link.setAttribute('href',url);
   link.setAttribute('download', filename);
   link.style.visibility = 'hidden';
   document.body.appendChild(link);
   link.click();
   document.body.removeChild(link);
   console.log(holder);
}

function loadJSON() {
   fetch(feed).then( res => {
      return res.json()
   }).then( data => {
      console.log(data);
      let mainArray = [];
      let heading = [];
      let headingRun = true;
      data.feed.entry.forEach( item => {
         console.log(item);
         let holder = [];
         for(let key in item){
            if(key.substring(0,3) == 'gsx'){
               if(headingRun) {
                  heading.push(key.split("$")[1]);
               }
               holder.push(item[key].$t);
            }
         }
         if(headingRun) {
            headingRun = false;
            mainArray.push(heading);
         }
         mainArray.push(holder);
      })
      console.log(mainArray);
      myData = mainArray;
   })
}

document.addEventListener('DOMContentLoaded', loadJSON);
