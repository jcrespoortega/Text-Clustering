# Results

Finally I present the performance of the differents approach, in order to measure its accuracy I will use Adjusted Rand Score metric.


|Fase          | Adjusted Rand Score|
| ---          | ---                |
|Steaming      | 0.722117202268     |
|Lemmatization |0.650602409639      |
|N-grams       |0.722117202268431   |
|Named entites | 0.914285714286     |



Lemmatization proccess achieve a result slightly worse result that Steamming the differences beetwen this tecniques are that stemming is 
faster but it dose't take into account the context only works with the words, however it achve a better results.

N-grams is a good approach in order to detect share vocabulary, but it has a high computational cost. It is important to compute differents
n-grams size and frequenties, here an experiment:

|n top      |Ajusted Rand Score  |
| ---       | ---                |
|75         |0.48105436573311366 |
|100        |0.6028065893837706  |
|150        |0.722117202268431   |
|200        |0.48105436573311366 |
|300        |0.48105436573311366 |


|Size | Ajusted Rand Score|
| --- | ---               |
|2    |0.001              |
|3    |0.4                |
|4    |0.481              |
|5    |0.72               |


Named Entities outpreforms the rest of techniques, this is because in this example we are doing a classification for news articles. In 
ssituations like this only with the response about How? When? Where?.. you can classify those texts, and named entities are the response to these
questions. The problem is when the response of the questions are the same but we have a different context in texts.
Both libraries achieves the same ADjusted Rand Score.




