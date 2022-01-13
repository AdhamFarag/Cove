import nltk
from nltk.stem.lancaster import LancasterStemmer
from sqlalchemy import true
stemmer = LancasterStemmer()
# things we need for Tensorflow
import numpy as np
import pickle
import random
# import tensorflow as tf
import tflearn
import pickle

#training_data_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'training_data')
training_data_file_path = "Training Material\\training_data"
data = pickle.load( open(training_data_file_path, "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# import our chat-bot intents file
import json
#JSON_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset\data.json')
JSON_file_path = "dataset\\data.json"
with open(JSON_file_path) as json_data:
    intents = json.load(json_data)
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net)

# logs_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tflearn_logs')
model = tflearn.DNN(net, tensorboard_dir='./tflearn_logs')

# load our saved model
model.load('./models/model.tflearn')

def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
    return(np.array(bag))


def response(sentence,Detailed=False):
    '''
    takes in sentece as input and return back response from the bot based on the data
    or returns the pattern and the data for future enhancments that might need to use existing patterns
    '''
    results = model.predict([bow(sentence, words)])[0]
    results_index = np.argmax(results)
    tag = classes[results_index]
    for tg in intents["intents"]:
        if tg['tag'] == tag:
            responses = tg['responses']
            patterns = tg["patterns"]
    if (Detailed):
        return(random.choice(responses),patterns)
    else:
        return(random.choice(responses))



print(response("hello"))