# Q1: What server side web framework does this app use?
**A1:** Capture a request however you like and in the response look for the line `X-Powered-By: Express`

# Q2: What is the flag you obtain after adding 100 or over eggs to your cart?
**A2:** We see that the JS is expecting a payload of `{ item, amount : 1 }`. 

Changing the amount to 100, doesn't work so we can assume there is a check for the amount on the backend. 

If we try to break it by modifying the payload to be something like `{item, amount: "100"}`, this does break the program and shows the flag in your cart.