function renderCart(cart) {
    const list = $('#list');
    list.empty();
    _.each(cart, (count, item) => {
      list.append($('<li>').text(`${count} - ${item}`));
    });
  }
  
  async function add(item) {
    try {
      const res = await superagent.post('/add').send({ item, amount : 1 });
      const { body : cart } = res;
      renderCart(cart);
    } catch (err) {
      console.log(err);
    }
  }
  
  async function clearCart() {
    try {
      const res = await superagent.get('/clear');
      const { body : cart } = res;
      renderCart(cart);
    } catch (err) {
      console.log(err);
    }
  }
  