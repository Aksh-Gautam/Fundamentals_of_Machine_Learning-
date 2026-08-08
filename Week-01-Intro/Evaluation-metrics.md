EVALUATION METRICS

#Regression metrics: 

Evaluation metrics are important because they measure how well the model works, they ensure the model meets its objectives.

 1. Mean Absolute Error(MAE): it calculates the average of difference between predicted and the actual values.
   
    $\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$.
 here yi = actual vlaue and ^yi = predicted value

 2. Mean Squared Error(MSE): calcuates the average of squared differences between predicted and actual values, squaring the difference ensure larger errors are penalised making it sesnitive to outliers

 \(\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2\)

 3. Roor Mean Squared Error(RMSE): Square root of MSE



 Like MSE it heavily penalises larger error. It is useful when we want to know how much our prediction deviates from the actual values in terms of same scale. 

 4. Root mean squared logarithmic error(RMSLE): Useful when target variable spans wide range of values RMSLE is useful where we are predicting qualities that very greatly in scale like predicting prices or population.  

 5. R2Score(R-Squared): represents the proportion of variance in the dependent variable that is predictable from independent variable

 -->R2 value close to 1 shows a model that explain most of the varuance R2 value close to 0 shows the model does not explain much of the variance in data.
 --> R2 score is used to access the goodness of fit of the regression models 

 \(R^{2}=1-\frac{SS_{res}}{SS_{tot}}=1-\frac{\sum (y_{i}-\^{y}_{i})^{2}}{\sum (y_{i}-\={y})^{2}}\)

 yi= actual values
 ^yi = predicted values 
 y- = mean of the actual values

 
#CLASSIFICATION METRICS:
 1. Accuracy: proportion of correct predictions made by a model out of all predictions.

 Accuracy = Number of correct predictions / total number of predictions 
 in case of imbalanced datasets where a dataset with 90% class A and 10% of class B, accuracy will predict only for class Aand wil fail to identify class B 

 2. Precision: measures how many of the positive predictions are made by model are actually correct. 
 
 Precision = True Positibe/True Positive + False Positive

 it is useful when cost of the FP is high such as in medical diagnosis where predicting a disease when it is not present can have serious concequences 

 3. Senstivity/Recall: how many of the actual positive cases were correctly identified by the model. It is important when a mission positive case(FN) is more costly than FP(false positive) is more costly than FP (False positive) recall is a key metrics in medical diagnosis

 TP / TP + FN 
 
 4. F1 Score: It is the harmonic mean of percision and recall, if F1 score is high means the model performs well on both metrics(percision and recall) lower recall and higher percision gives great accuracy but then it misses large no. of instances , more the F1 score higher will be the performance. 

 F1 score = 2 * percision * recall/percision + recall 
 range of F1 score is [0,1]  

 5. AUC-ROC Curve: Evalutes the model over a spectrum of threshold where precision, recall and F1 score provides insight about a model over only a single threshold.
 ROC curve is graphical representation of true positive rates vs the false PR at different classification thresholds

 TPR = TP/TP+FN 
 TPR -- measures out of all actual positive cases how many did the model correctly identify 
 TNR = TN/TN+FP 
 TNR-- measures how many actual negative instances were correctly identified by the model 
 How to read AUC values? 
 AUC ranges from 0-1 
 1- perfect model 
 0.8 to 0.9 - good model 
 0.7 to 0.8 - accepetable model
 upto 0.5 - random guessing 
 less than 0.5 - Worse than random guessing

 6. confusion matrix:     actual
                    pass [TP]|[FP]
        predicted           
                    Fail [FN]|[TN]
                        pass    fail
 it is a NXN matrix where N is the no of classes/categories to be predicted if we have N = 2 we get 2*2 matrix 

 