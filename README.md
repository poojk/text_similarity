# Text_similarity

Compares the similarity between two pieces of texts by using a metric. Exactly similar documents get a score of 1 and entirely dissimilar documents get a score of 0. So, the level of similarity lies in the range of 0-1.

The metric that has been used to determine the level of similarity between texts is the "Cosine Similarity".

<hr/>

## Why Cosine Similarity?

It is a highly efficient method used in information retrieval. It makes use of term frequencies in a document or in our case abstract pieces of text and then compares it against it with each other by assigning the weights of 1 meaning presence and 0 meaning absence of the term. These weights are built into seperate vectors.

In the vector space (IR) model you are comparing two very sparse vectors in very high dimensions. Cosine similarity is calculated using only the dot product and magnitude of each vector, and is therefore affected only by the terms the two vectors have in common. Cosine thus has some meaningful semantics for ranking similar documents, based on mutual term frequency.

The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance because of the size  they could still have a smaller angle between them. Smaller the angle, higher the similarity.

## App

![github-small](https://github.com/poojk/text_similarity/blob/main/screenshot.png)

## Assumptions

With respect to the similarity determination, there were a few assumptions that had been made, making sure that the algorithm performs more efficiently. These assumptions are,
* The words are compared against a dictionary of the most common stop words. When a presence of such words are encountered, they are ignored. More precisely, these stop words do not play any role in determining the level of similarity.
* One another important consideration would be contractions of words. For example, "don't" and "do not" mean the same thing but would be considered as different words by general consideration. This ambiguity is also resolved by using another dictionary of contractions.
* Punctuations are ignored.
* Order of words is not considered in this case. Hence the algorithm is purely based on the occurences of words in abstracts of texts.

## Execution Steps

1. Clone the repository locally by executing the following command in the cli.
    ```
    $git clone https://github.com/poojk/text_similarity
    $cd text_similarity
    ```
    
2. The 'run.sh' file in the home directory can be used for execution. Also, execution can be triggered by executing the following command in the terminal 
    ```
    python ./text_similarity/app.py
    ```
  ## Execution via Docker Hub
  
1. After cloning the git repository, the docker image from any container repository should be built locally. It looks something like this (mind the period at the end),
   ```
   docker build -t raveenapoojak/docker101tutorial .
   ```
   
2. Then, the following command should be executed, after which the app can be found at http://localhost:8888. Here localhost indicated the IP address from where the app is being accessed.

   ```
   docker run -p 8888:5000 raveenapoojak/docker101tutorial
   ```
The above command used port 5000 for the server inside the container and exposed this externally on port 8888. Head over to the URL with port 8888, where the app should be live.


