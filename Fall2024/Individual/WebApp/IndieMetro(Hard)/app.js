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
        )
      ;
  
      cards.append(card);
    });
  }());
  