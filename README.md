# Simple-Text-Obfuscator
Obfuscate and decode any string

# How to use?

**YOU NEED TO INSTALL PYTHON TO USE OBFUSCATOR**

To obfuscate write `python3 main.py` in console in main.py file directory
Then write word you need to obfuscate and press enter.
Then write length of obfuscated string
**IT MUST BE A MULTIPLE OF 3**
After that you get file named `output.txt` which contains your obfuscated word.

To decode write `python3 decode.py` in console in decode.py file directory
Then write name of txt file with obfuscated word.
After that you get your decoded word in console.

# How it works?

### Obfuscating

At first it generates random digits, lower-case letters and upper-case letters.
Than it randomly shuffles it and put's your string in random position.
Coordinates to decode are in the end of the obfuscated text.
For example: 4JxzPYTHONS4P10
Number after P is last coordinate of word
Number after S is first coorinate of word
