# Bollywood-Revenue-Prediction
Predicting upcoming  bollywood movie prediction and Verdict

## INTRODUCTION

The production of a movie begins with construction of a script and screenplay. Then the film-making team is assembled, filming locations are decided, and investors are attracted. Then filming occurs, with after effects and editing. Last is distribution. To support the investment decisions of a movie, a prediction of profitability has to be done before the actual production. Predictions made right after release may have more data and maybe more accurate, but it will be late for investors to make their decisions.
In this project, we will apply machine learning algorithms such as linear regression, logistic regression, multiclass Naive Bayes, SVM and k-means to predict box office collection for movies. 
We will classify movies as ‘Flop’, ‘Hit’ and ‘Super hit’ on the basis of the return over investment the movie has made in the domestic box office i.e. if a movie was made on a budget of 40 crores and it grossed only 36 crores in the Indian box office then it will be classified as a ‘Losing’ movie, even if it might have more earnings worldwide.

## Process

In this project, we define revenue prediction as a discrete prediction task using supervised learning. We have a set of training examples ( X(1), Y(1), X(2), Y(2), … , X(n), Y(n) );  where each X(i) = [ x1, x2, … , xn ]T  corresponds to a vector of input features for a particular movie and each Y(i)∈ R6 is a categorical dependent variable corresponding to one of six possible revenue categories.
We can model the relationship between X(i) and Y(i) in a variety of ways. During the experimentation phase of this project, we utilized five different types of models to categorize the input into a revenue category, and further we used the result from those categorizations to approximate the domestic box office collection of the movie represented by the input vector.
Our dataset was collected from multiple sources after cross validation as the figures for Budget and Box Office Collection were varying over the multiple websites we were dependent on. In our final dataset, we had over 65% of the movies which generated less domestic collection than their budget.
Our hypothesis for this learning problem is in a higher dimensional space than the number of samples we have available. We are victims of the Curse of Dimensionality.
To deal with this issue we have used SVM with linear kernel, because the last thing we want is to project the data into an even higher dimensional space.
A basic rule of thumb is mentioned NTU’s ‘A practical guide to support vectors classification’ which says:
If the number of features is large, one may not need to map data to a higher dimensional space. That is, the nonlinear mapping does not improve the performance. Using the linear kernel is good enough, and one only searches for the parameter C.

## Accuracy 

Model               | Accuracy                 | Recommendation
------------------- | ------------------------ | ------------
Linear Model        | 0.77                     | definitely
SVM linear kernel   | 0.53                     | can use
Naive Bayes         | 0.40                     | prefer this for hit/superhit
KNN                 | 0.52                     | gives all flop - dont use
Logistic Regression | 0.56                     | little better than knn - dont use
Randforest          | 0.56(Gini)/0.57(Entropy) | same problem as KNN - dont use

### Confusion Matrix ###

Model               | Confusion Matrix / Graph
------------------- |---------------------------------------------------------------------------------------------------------------------------
KNN                 |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/KNN.PNG "KNN")
Logistic Regression |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Logistic_reg.PNG "Logistic_reg")
Naive Bayes         |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Naive_bayes.PNG "Naive_bayes")
SVM                 |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/SVM.PNG "SVM")
Linear Regression   |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/linear_reg.PNG "linear_reg")

## RESULT ##

Some test result are as follows: 

Movie               | Result
------------------- |---------------------------------------------------------------------------------------------------------------------------
Padmaavat           |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Padmaavat.PNG "linear_reg")
Piku                |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Piku.PNG "linear_reg")
Raazi               |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Raazi.PNG "linear_reg")
Thugs_of_hindustan  |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Thugs_of_hindustan.PNG "linear_reg")
Badaahi Ho          |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/badhaai_ho.PNG "linear_reg")
Pink                |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/pink.PNG "linear_reg")
Zero                |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Zero.PNG "linear_reg")
Stree               |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Stree.PNG "linear_reg")
RockOn 2            |![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/Rockon_2.PNG "linear_reg")

### FLOW DIAGRAM ###

Flow_Diagram ![picture alt](https://github.com/yashraj9892/Bollywood-Revenue-Prediction/blob/master/Pics/flow-Diagram.jpg "linear_reg")

### ACCURACY ###

  output  = accuracy of (Naive Bayes)*accuracy(linear Regression)
  output  = 30.8%


