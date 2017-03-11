import os
import numpy as np
import time
import datetime
import json
import csv
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer();

#print (len(documents), "documents")
#print (len(classes), "classes", classes)
#print (len(words), "unique stemmed words", words)

# sample training/output
#i = 0
#w = documents[i][0]
#print ([stemmer.stem(word.lower()) for word in w])
#print (training[i])
#print (output[i])

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)
 
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)

    return(np.array(bag))

def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        print ("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2


# probability threshold
ERROR_THRESHOLD = 0
# load our calculated synapse values
synapse_file = 'ml/synapses.json' 
with open(synapse_file) as data_file: 
    synapse = json.load(data_file) 
    classes = np.asarray(synapse['classes']) 
    synapse_0 = np.asarray(synapse['synapse0']) 
    synapse_1 = np.asarray(synapse['synapse1'])
    words = np.asarray(synapse['words'])

def classify(sentence, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ] 
    results.sort(key=lambda x: x[1], reverse=True) 
    return_results =[[classes[r[0]],r[1]] for r in results]
    #print ("%s \n classification: %s" % (sentence, return_results))
    return return_results

# classify("sudo make me a sandwich")
# classify("how are you today?")
#classify("Democrats are the worst")
#classify("I love French fries")
#print ()
#classify("I love fake news.", show_details=True)

def final_classify(sentence, show_details=False):
    result = classify(sentence, show_details)
    end = 0
    value = 1
    for r in result:
        if r[1] > end:
            end = r[1]
            value = r[0]
    
    return value

