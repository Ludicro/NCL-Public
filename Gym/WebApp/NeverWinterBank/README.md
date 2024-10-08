# Challenge

## Question 1
What is the path of the leaked file?

## Question 2
What is the flag?

# Analysis 
## Determine Normal Usage
This is a login portal. When giving random credentials, it informs that the credentials are incorrect.

## Web App Exploit Checklist (for NCL but these are good to check in any web app exploit test)
- [X] Robots.txt
- [ ] Sitemap.xml
- [ ] Cookies
- [X] Javascript code

### Robots.txt
Navigating to `/robots.txt` will show the following page is hidden from bots: `/dev/rel.js`.

Navigating to this page shows what looks to be Javascript code and skimming it suggests that this is the backend code!

### Javascript
#### Source
1. The function `transfer()` will take the value of the amount put into the `#transferAmt` input field and set the `amount` variable to this value
2. Agent will send a post request to `/transfer`
   - Sends the `amount`
   - Sends the `account` which is set to 'ForgeOfNeverWinter'
3. Then reloads the page

#### /dev/rel.js


# Result
We are taken to a page with the flag and a cookie is added called `flag` with the value as the solution
