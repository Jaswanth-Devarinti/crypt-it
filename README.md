# crypt-it(OTP)
Encrypting the text using one time padding is quite old technique, still it has it's unique uses.
This project needs two things, that are key concepts for one time padding(OTP).
XOR opertion along with PRG(pseudo random number generator).To do the xor operation we need to have a pseudo random number with same bit size as binary form of msg.
Thus size of binary msg is calculated and then using some operations on key given PRG is generated who's bit length is same as bit length of msg.
For generation PRG with bit length same as the msg, I used another module named PRG.
It does some operation on key and the PRG is generated and then converted into ascii format.
Then XOR operation is done and the result binary code is converted to ascii.
This is ciphertext.
To decipher it, same process is followed. An attacker with our ciphertext, can't decipher it unless he has our algorithm and PRG.
code included the deciphering at the end of code.
You can remove it if you want.
