from newspaper import Article
import io
from textblob import TextBlob
import re, pprint, os, numpy
import nltk
from sklearn.metrics.cluster import *
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score
from nltk.util import ngrams


def cluster_texts(texts, clustersNumber, distance):
    #Load the list of texts into a TextCollection object.
    collection = nltk.TextCollection(texts)
    print("Created a collection of", len(collection), "terms.")

    #get a list of unique terms
    unique_terms = list(set(collection))
    print("Unique terms found: ", len(unique_terms))

    #get named entitites:

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


filenames = [

]

if __name__ == "__main__":

    texts = []

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


        En = []

        tokenized_sentence = nltk.word_tokenize(str(t))
        tagged_sentence = nltk.pos_tag(tokenized_sentence)
        namedEnt = nltk.ne_chunk(tagged_sentence, True)

        for i in namedEnt:
            if len(i) == 1:
                En.append(i[0][0])

        text_2 = nltk.Text(En)

        print('nuevo texto')
        texts.append(text_2)

    print("Prepared ", len(texts), " documents...")
    print("They can be accessed using texts[0] - texts[" + str(len(texts) - 1) + "]")

    distanceFunction = "cosine"
   # distanceFunction = "euclidean"
    test = cluster_texts(texts, 5, distanceFunction)
    print("test: ", test)
    # Gold Standard
    reference = [0, 5, 0, 0, 0, 2, 2, 2, 3, 5, 5, 5, 5, 5, 4, 4, 4, 4, 3, 0, 2, 5]
    print("reference: ", reference)

    # Evaluation
    print("rand_score: ", adjusted_rand_score(reference, test))


