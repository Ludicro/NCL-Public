# Q1: What programming language is this code written in?
**A1:** The code has some unique identifiers such as using `println!` for the print statements. Looking these up will show the language of the code quickly.

# Q2: What is the flag?
**A2:** The code is checking the input and performs XOR on each byte with the key 0x84. 

Then it compares the XOR result against the predefined array of bytes. 

To solve this:
1. Take each byte from the check vector: `[215, 207, 221, 169, 199, 214, 197, 198, 169, 189, 178, 182, 181]`
2. XOR each byte with 0x84 again to get the original ASCII values
3. Convert the resulting bytes back to characters

The XOR operation can be reversed:
- If A ^ B = C
- Then A = B ^ C