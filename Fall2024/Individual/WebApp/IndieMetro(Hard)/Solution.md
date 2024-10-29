# Q1: What database is this app using?
**A1:** Looking at the JS code, you see the information that is getting displayed is coming from the page `/games`. 

Looking inside we see that the page is full of [JSON data](/Fall2024/WebApp/IndieMetro(Hard)/games.json).

Inside each of these, there is a field that doesn't fit anything that's shown. Researching that will give you the answer.

# Q2: What is the flag?
**A2:** Apparently the solution to this was seeing that LokiJS is a NOSQL database and using an injection in the URL of the get page that looks like: `/games?id[$exists]=true&release[$exists]=false`. 

There's a similar injection on PayloadsAllTheThings but I just didn't see the NOSQL on the GitHub cause I can't read.

I was close at one point as I was doing URLs like: `/games?id=1` to see if I got a response but I am not familiar enough with web app exploitation to have processed the results I was getting (or more specifically *wasn't* getting).

*This was me trying to see if the solution lied in sending commands to the console*
Using the following code in the dev console will get whichever `$loki` value matches from the JSON:
```js
(async function() {
    const { body: games } = await superagent.get('/games'); // Fetch the games data
    const entry = games.find(game => game.$loki === 1); // Find the entry with id 0
    console.log(entry); // Log the entry to the console
})();
```


```js
(async function load() {
    const cards = $('#cards');
  
    const { body : games } = await superagent.get('/games');
  
    _.each(games, (game) => {
      console.log(game);
      const card = $('<div>', { class : 'card' })
        .append(
          $('<div>').addClass('content').append(
            $('<div>').addClass('header').text(game.title)
          )
            .append($('<div>').addClass('description').text(game.description))
            .append($('<div>').addClass('$loki').text(game.$loki))
        )
      ;
  
      cards.append(card);
    });
  }());
```