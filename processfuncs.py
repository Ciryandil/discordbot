

def process_text(text):
    import re

    text = text.strip()
    removefword = re.compile(re.escape('fucking'), re.IGNORECASE)
    text = removefword.sub('', text)

    return text 

def get_tokens(text):
    import pickle
    from keras.preprocessing.sequence import pad_sequences
    
    text_list=[text]

    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
    
    tokenized_text_list = tokenizer.texts_to_sequences(text_list)
    tokenized_text_list = pad_sequences(tokenized_text_list, maxlen = 200)
    return tokenized_text_list

def get_probs(text):

    from keras import models 
    text = process_text(text)
    token_list = get_tokens(text)

    comment_model = models.load_model('comment_class_model.h5')
    probs = comment_model.predict(token_list)
    probs = probs.flatten()
    probs = probs.tolist()
    labels = ['toxic', 'severely toxic', 'obscene', 'threat', 'insult', 'identity hate']
    prob_dictionary = dict(zip(labels,probs)) 
    
    return prob_dictionary


sentence = input('give text: ')
print(process_text(sentence))
print(get_tokens(sentence))
print(get_probs(sentence))