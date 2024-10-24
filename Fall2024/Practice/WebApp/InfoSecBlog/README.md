# Blog Post Questions and Answers

## Q1: How many total posts have been made?
**A1:** Count the amount on the page (5)

---

## Q2: What is the author's username?
**A2:** Look at the author's name on each post (charles)

---

## Q3: What is the URL path that the author does not want search engine crawlers to visit?
**A3:** `/admin`  
**A3 (walkthrough):** Go to `[yoursite].com/robots.txt` and look at the entry.

---

## Q4: What is the name of the server-side web framework used by the blog?
**A4:** Express  
**A4 (walkthrough):** Capture a request however you like and in the response look for the line `X-Powered-By: Express`.

---

## Q5: What is the flag?
**A5:** *the flag*
**A5 (walkthrough):**

If you look at your cookies, you will notice that you have a cookie named `session`.  
Logging out and back does not change the cookie.  
Making a different account gives a new session cookie.  
This means that each username will have a cookie.  
You can also test this by changing the current cookie to that of the cookie for your first user and see that your username changes.  

We see the cookies are in base64. If we decode them, we can see they are in the format of:
`{"username":"test","signature":"j9JRafdy07npGgqyu38wAH0NchkS+Qw7MPJOU0DgmK2HCzhdKLBofdUVCw+JjV0vDr9Ji5eEkbvCM9Il7dZBOPFBamjdtdMtKdywMQk085PQ3ngeciBN3eAkKFwF7mSpzAwHJ4rycXv3a8k8A45cmuRY3GZLCGV+7/h3HfObkTE="}`

So we know that this gives us a payload with the information `username` and `signature`.  
Reading through the blog, we see he talks about signing things and even gives us his public key.  
However, we can also see he A) wrote this in JavaScript and B) gives the file paths to his keys.  
So to get his private key, we can just navigate to the path `[yoursite].com/keys/private`.

Now you can do the complicated thing that I did where I made a whole script to take the private key, sign the username `charles`, put the signature in base64, add the signature to the payload, and then base64 encode the whole thing. *(This was a struggle for way too long because I kept signing the whole payload, not just the username).* Then replace the cookie with the new session token you just created.


Or you can just go into CyberChef and RSA sign the username, base64 encrypt it, throw that into a payload, and base64 encrypt the whole thing.
