from newspaper import Article
from textblob import TextBlob
import re, pprint, os, numpy
import nltk
from sklearn.metrics.cluster import *
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer







def cluster_texts(texts, clustersNumber, distance):
    #Load the list of texts into a TextCollection object.
    collection = nltk.TextCollection(texts)
    print("Created a collection of", len(collection), "terms.")

    #get a list of unique terms
    unique_terms = list(set(collection))
    print(unique_terms[:50])
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


#Introducimos la dirreción de los archivos html.
#Además así será el orden con el que saldra la referencia.

filenames = ["./corpus/Mini-Merkel given crucial CDU job as chancellor looks to future _ World news _ The Guardin.html",
             "./corpus/All 66 on board plane that crashed in Iranian mountains 'believed '.html",
             "./corpus/Angela Merkel appears to anoint successor with promotion  'mini-Merkel'.html",
             "./corpus/Annegret Kramp-Karrenbauer candidata de Merkel a sucederla como presidenta  CDU.html",
             "./corpus/As Merkel calls on Pope Francis, is a partnership in  works_.html",
            "./corpus/Catalan MP and leading independence activist flees country to avoid facing trial Madrid _ The Independent.html",
             "./corpus/Catalan Politician Leaves for Switzerland Days Before Court Date -  New York Times.html",
             "./corpus/Crisis in Catalonia_ Pro-Catalan independence politician flees to Switzerland to avoid court date _  English _ EL PAÍS.html",
             "./corpus/El Vaticano reactiva la comisión sobre abusos sexuales ante críticas  Español.html",
            "./corpus/Hallan los restos del avión siniestrado en las montañas de Irán _ Internacionl.html",
             "./corpus/Iran Plane Crash Leads to Search-and-Rescue Effort at 14,500 Feet -  New York Times.html",
            "./corpus/Iran plane crash_ Agonising wait continues for relatives - BBC Nws.html",
             "./corpus/Iran plane crash_ Search continues for missing Aseman Airlines plane - BBC Nws.html",
             "./corpus/Mueren 66 personas al estrellarse un avión comercial en Irn.html",
            "./corpus/Oxfam Haiti scandal_ Suspects 'physically threatened' witnesses - BBC Nws.html",
             "./corpus/Oxfam Says Workers in Haiti Threatened Witness to Misconduct -  New York Times.html",
             "./corpus/Oxfam tendrá una comisión independiente para evitar los abuos.html",
            "./corpus/Oxfam was warned a decade ago about the crisis in sex abuse among world's aid workes.html",
             "./corpus/Pope Francis wowed the world but, five years on, is in troubled waters _ World news _ he Guardian.html",
             "./corpus/Reaction to remarks by Angela Merkel and Emmanuel Macron at Bonn climate summit _ Oxfam Internationl.html",
            "./corpus/The far-left separatists who took Catalonia to the brik.html",
             "./corpus/Un avión con 66 pasajeros a bordo se estrella en una zona montañosade Irán.html"]

if __name__ == "__main__":

    texts = []

    # Conjunto con las stopwords en ingles.
    stop = set(stopwords.words('english'))

    #Funcion de stemming ingles.
    stemmer = PorterStemmer()

    # Conjunto con las stopwords en español.
    stop_esp = set(stopwords.words('spanish'))

    # Funcion de stemming español.
    stemmer2 = SnowballStemmer("spanish")

    for filename in filenames:

        #Abrimos el archivo html y realizamos el proceso de limipeza mediante newsarticle3k

        text_p = open(filename, "rb")
        texto_plano = text_p.read()
        text_p.close()



        a = Article(filename)
        a.set_html(texto_plano)
        a.parse()
        a.nlp()

        t = a.text

        #En la variable t ya tenemos recgido el texto para trabajr con el

        text_cleared = ""
        # Para carácter en el texto comprobamos si es un símbolo de puntuación.
        for letter in str(t):
            if not letter in string.punctuation:
                text_cleared = text_cleared + letter

        print(filename)


        trans = TextBlob(text_cleared)

        #La transformamos un un obejto Text.Blob

        if trans.detect_language() != "en":

            # Limpieza de stop-words

            tokens = nltk.word_tokenize(text_cleared)
            text = []
            for word in tokens:
                if word not in stop_esp:
                    text.append(word)

            # Stemming

            stemmeds = []
            # Para cada token del texto obtenemos su raíz.
            for word_2 in text:
                stemmed = stemmer2.stem(word_2)
                print(stemmed)
                stemmeds.append(stemmed)


        else:
            # Limpieza de stop-words

            tokens = nltk.word_tokenize(text_cleared)
            text = []
            for word in tokens:
                if word not in stop:
                    text.append(word)

            # Stemming

            stemmeds = []
            # Para cada token del texto obtenemos su raíz.
            for word_2 in text:
                stemmed = stemmer.stem(word_2)
                print(stemmed)
                stemmeds.append(stemmed)

        print('nuevo texto')

        text_2 = nltk.Text(stemmeds)
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