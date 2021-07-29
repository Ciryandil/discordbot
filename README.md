# A Discord bot to detect toxic messages

* **bot.py** contains the bot code. Presently it just mentions the user and asks them to be respectful. 
* **processfuncs** contains code to preprocess a message,tokenize it, feed to the neural network, and obtain a classification
* **comment_class_model** is our neural network built with Keras 
* **tokenizer** is the string tokenizer
* **comment_classifier** is a notebook containing the code to extract data and train our models

## TODO:

* Implement warning system
* Log users in file for repeated toxicity