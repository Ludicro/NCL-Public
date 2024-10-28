const PRE_CHECK = 'SXc0bnRDYW5keQ==';

const { btoa } = window;

async function checkPassword() {
  const inp = $('#password').val();
  const contentDiv = $('#flag-container');
  contentDiv.empty();
  if (btoa(inp) === PRE_CHECK) {
    const res = await superagent.post('/check')
      .send({
        password : inp,
      })
    ;
    if (res.body.message) {
      contentDiv.append(`<p>${res.body.message}</p>`);
    } else if (res.body.flag) {
      contentDiv.append(`<p>${res.body.flag}</p>`);
    }
  } else {
    contentDiv.append('Incorrect');
  }
}
