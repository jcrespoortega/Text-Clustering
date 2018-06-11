import nltk
from nltk.util import ngrams
import re, pprint, os, numpy
import nltk
from sklearn.metrics.cluster import *
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score
import string
from newspaper import Article
from textblob import TextBlob


def cluster_texts(texts, clustersNumber, distance):
    #Load the list of texts into a TextCollection object.
    collection = nltk.TextCollection(texts)
    print(collection)
    print(set(collection))
    print("Created a collection of", len(collection), "terms.")

    #get a list of unique terms
    unique_terms = list(set(collection))
    print(type(unique_terms))
    print(unique_terms)
    print("Unique terms found: ", len(unique_terms))

    ### And here we actually call the function and create our array of vectors.
    vectors = [numpy.array(TF(f,unique_terms, collection)) for f in texts]
    print("Vectors created.")

    # initialize the clusterer
    clusterer = AgglomerativeClustering(n_clusters=clustersNumber,
                                      linkage="average", affinity=distanceFunction)
    clusters = clusterer.fit_predict(vectors)

    return clusters

# Function to create a TF vector for one document. For each of
# our unique words, we have a feature which is the tf for that word
# in the current document
def TF(document, unique_terms, collection):
    word_tf = []
    for word in unique_terms:
        word_tf.append(collection.tf(word, document))
    return word_tf

def word_grams(words):
    s = []
    for ngram in ngrams(words, n=2):
            s.append(' '.join(str(i) for i in ngram))
    return s

filenames = [

]


if __name__ == "__main__":
    # Empty list to hold text documents.
    texts = []
    ng2 = []

    for filename in filenames:

        text_p = open(filename, "rb")
        texto_plano = text_p.read()
        text_p.close()

        a = Article(filename)
        a.set_html(texto_plano)
        a.parse()
        a.nlp()

        t = a.text

        print(filename)
        trans = TextBlob(t)

        if trans.detect_language() != "en":
            ing = (trans.translate(to='en'))
            t = ing

        text_cleared = ""
        # Para carácter en el texto comprobamos si es un símbolo de puntuación.
        for letter in str(t):
            if not letter in string.punctuation:
                text_cleared = text_cleared + letter

        ng = word_grams(t)

        values = set(ng)
        print(values)

        lis = []

        for x in values:
            j = 0
            for i in ng:
                if i == x:
                    j += 1
            lis.append([x, j])
        lis.sort(key=lambda tup: tup[1], reverse=True)
        lis = lis[0:150]
        fin = []

        for i in range(len(lis)):
            fin.append(lis[i][0])

        print(fin)

        text_2 = nltk.Text(fin)
        print(type(text_2))
        print(text_2)

        print('nuevo texto')
        texts.append(text_2)


    print("Prepared ", len(texts), " documents...")
    print("They can be accessed using texts[0] - texts[" + str(len(texts)-1) + "]")

    distanceFunction ="cosine"
    #distanceFunction = "euclidean"
    test = cluster_texts(texts,5,distanceFunction)
    print("test: ", test)
    # Gold Standard
    reference =[0, 5, 0, 0, 0, 2, 2, 2, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 0, 2, 5]
    print("reference: ", reference)

    # Evaluation
    print("rand_score: ", adjusted_rand_score(reference,test))

