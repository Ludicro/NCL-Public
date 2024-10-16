const crypto = require('crypto');

// Include the private key directly in the code
const PRIVATE_KEY = `-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDku/9mnwqcgB5IMQtKLoiGJqD2THVhFK2MBqiHjZ8wVum50vXy
e9yFmwBNCgdpMEFGxc+4Ajsv9ueQvhiR7e0qYO1cUdMoGMFkCvuYvGoSlbLIgQnF
q8FbZv7oteW8ITmYhkqikJ9qqC9jVErIGhB8cTlx5wpRm7V0AP/C1QksxQIDAQAB
AoGANrRnvulmpktV8roYEyPR7xOqB339zLwfTZACGnlaizseJx03SUkqUqHhjotJ
fnTWB9EjfsS51xzcARgV1EDtKXO9+QPlJsmYj1mL9fVdMd+GoNIjZVR2+hJ7D+fY
SJy6Qddhfrz5rpCQ8YV1uWFIQwFjag0GerL/PUFjM3CRe7kCQQD4zvJJjjhdlkpX
XbFJY5LoOoN5azW5m/vQSoqpLdjst9Clam1FJ+dJ6+/Q3Lzp2AucKUmCcYWkutwb
4mNqE6G/AkEA61iDi9frmmH+6gQnx2G2pFkRgO+MhK2+S4XHrN/c2fn7Ej6LXGF4
rroO9lOzmHZN+9zqKGsRx5UIMF5ldvcKewJBAM816mp/20l1xOwFx4RLPSnSsXQJ
aXDvC0RpEBndaO+cFlPs0pvpo6HYsJzNeTd3ChQ//kx4psiOJonCfPD28JkCQDjA
s5g5jXtBPnO4ZM9T5PNk9y+clMo6C7WyoSAzK9L00XLo2jqA1tVr0MfeD2Uowk2G
TIFKsJLsgXkIindRw5kCQQCclbh/dpchNHO+uZaD2OijzwZHBM5BgJ0fy4O7IMw/
aNMiboJ3a09LUqvOIp3r5QQuohcQog/IzxF1Leu2VHxu
-----END RSA PRIVATE KEY-----`;

// Sign the data
function sign(data) {
    const sign = crypto.createSign('RSA-SHA256');
    sign.update(data);
    sign.end();
    return sign.sign(PRIVATE_KEY, 'base64');
}

// Create the new payload
const payload = { username: 'charles', signature: '' };
const payloadJson = JSON.stringify(payload);

// Generate the signature
payload.signature = sign(payloadJson);

// Convert the final payload to base64
const finalPayloadBase64 = Buffer.from(JSON.stringify(payload)).toString('base64');

console.log("New session key:", finalPayloadBase64);
