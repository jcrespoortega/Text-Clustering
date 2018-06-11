# Results

Finally I present the performance of the differents approach, in order to measure its accuracy I will use Adjusted Rand Score metric.

\documentclass[10pt]{article}

\begin{document}
\begin{table}[htbp]
\begin{center}
\begin{tabular}{|l|l|l|l|}
\hline
Fase&Terms&Unique Term& Adjusted Rand Score\\
\hline \hline
Fase 1&15659&3334&0.0140480591497\\ \hline
Fase 2&8425&3167& 0.722117202268\\ \hline
Fase 3&8425&2411& 0.722117202268\\ \hline
Fase 4&8696&2446&0.650602409639\\ \hline
Fase 5&3300&1631&0.722117202268431\\ \hline
Fase 6&656&189&0.914285714286\\ \hline
\end{tabular}
\caption{Comparación}
\label{tabla:sencilla}
\end{center}
\end{table}

\end{document}


Lemmatization proccess achieve a result slightly worse result that Steamming the differences beetwen this tecniques are that stemming is 
faster but it dose't take into account the context only works with the words, however it achve a better results.

N-grams is a good approach in order to detect share vocabulary, but it has a high computational cost. It is important to compute differents
n-grams size and frequenties, here an experiment:

n top Terms Unique Term Ajusted Rand Score
75 1650 798 0.48105436573311366 
100 2200 1065 0.6028065893837706 
150 3300 1631 0.722117202268431 
200 4400 2216 0.48105436573311366 
300 6600 3380 0.48105436573311366


Tamaño Ajusted Rand Score
2 0.001
3 0.4 
4 0.481 
5 0.72


Named Entities outpreform the rest of techniques, this is because in this example we are doing a classification for news articles. In 
ssituations like this only with the response about How? When? Where?.. you can classify those texts, and named entities are the response to these
questions. The problem is when the response of the questions are the same but we have a different context in texts.
Both libraries achieves the same ADjusted Rand Score.




