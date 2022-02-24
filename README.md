## Part 1
## Answer 1

The digits has been extracted  with regex function after all the words of ID and Code

## Answer 3
STEPS:
     
     
     1. After preprocessing the text i computed the simlarity score of long and Short description and  groupy by the mean of the score with respect to each rank and want to analyse if the simmilarity score is affecting the Rank or not.
    
    2. Are Ranks are ordered in ascending order with respect to the mean of  difference between the days from date and Date of Last Description Change.
    
    3. Extract the ranks where the keyword are present both in Short and  Long Description Text. 
    
    4. figure out the APP id where the rank mean is less and they are on Top.





 INSIGHTS
 1. Top Ranks shown  on the basis of Simmilarity score of Short & Long Description .where the similarity score is maximum i have extracted those ranks where simmilarity score is        maximum
 2.  Ranks are shown as ordered in ascending order according to the mean of difference between Date and Date of Last Description Change.
 3.  APP ID are shown where the Rank Mean is less and and they have good ranks.


## Part2
## Answer

For checking the Grammar score i have preprocessed the text and used pretrained model to predict the correct grammatical sentences and then used pairwise cosine simmilarity between two text to compute the correctness of the score and then divide by 10 to scale their acuracy on the scale of (1 to 10).




# More Bonus points (You can write answers to these in ReadMe)

1.  As  from a middle class family did not had any kind of problem which is very rare but yes there were Some personal hicups.

2. The set of pairs (a, b) for all real a ≥ b

 






