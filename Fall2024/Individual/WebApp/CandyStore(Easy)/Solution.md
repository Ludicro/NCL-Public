# Q1: What is the endpoint the password is sent to?
**A1:** Look at the JS for the page, in the function `checkPassword()`, trace it until you see where the POST request is sent.

# Q2: What is the flag?
**A2:** 
Inside the JS, the first thing we see is a const variable called `PRE_CHECK` being set to what is clearly Base64.

We then later see in the JS that our input is set to the value `inp`. After that, the if statement checks if `btoa(inp) == PRE_CHECK`, and if so, it will send the password to `QUESTION 1 ANSWER`. 

Looking up `btoa`, we know it is a function that takes a string and returns a Base64 encoded string. So the if statement is checking if the Base64 encoded version of our input is equal to the Base64 encoded version of the string `PRE_CHECK`.

We can then figure out the password by taking the Base64 encoded version of `PRE_CHECK` and decoding it.