# Q1: What database is this app using?
**A1:** Looking at the JS code, you see the information that is getting displayed is coming from the page `/games`. 

Looking inside we see that the page is full of [JSON data](/Fall2024/WebApp/IndieMetro(Hard)/games.json).

Inside each of these, there is a field that doesn't fit anything that's shown. Researching that will give you the answer.

# Q2: What is the flag?
**A2:**

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