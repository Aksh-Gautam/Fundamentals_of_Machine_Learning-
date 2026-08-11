#Logistic Regression:
It is a supervised ML algorithm used to classification. 
--> It predicts Categorical values(yes/no, spam/no, spam,0/1) using Sigmoid function to map prediction to a S-shaped curve between 0-1. 
--> The sigmoid function converts raw output into a probability value between 0 and 1  
--> in Logistic regression we use a threshold value [0.5] to decide the class label
--> If sigmoid output is same or above the threshold input isclassified as 1
--> If sigmoid output is below the threshold input 
 #Working:
 losistic regression computes linear combination of input features z= wX+b and pass it through sigmoid function to produce probability between 0 and 1. This probability is then used to assign inputs to a class. 
 If the output of the sigmoid function is less than the threshold then the class is 0, if it is greater than equal to the threshold it is 1.

 z = wx+b
 apply LoR
 sigma(z) = 1/1+e^-z
 sigma(z) --> 1  then z --> infinity
 sigma(z) --> 0 then z --> - infinity


p(x)/ 1-p(x) = e^-z
here p(x) = probability of the event 
     1-p(x) = probaility not occured 
 
ratio of p(x) : 1-p(x) = odd of dependent event 

applying nature log to p(x)/1-p(x) we get log-odds/logit

log [p(x)/1-p(x)] = z
log [p(x)/1-p(x)] = WX + b
p(x)/1-p(x) = e^(WX+b)
p(x) = e^WX+b (1-p(x))
p(x) = e^WX+b - e^WX+b p(x)
p(x) + p(x) e^WX+b= e^WX+b
p(x) (1 + e^WX+b) = e^WX + b
p(x) = e^WX+b/
