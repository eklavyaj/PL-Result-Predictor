# Premier-League-Result-Predictor

# Introduction
I would call this a 101 machine learning project. The aim was to analyze the data of over 8000 English Premier League fixtures spread across 20 seasons. Eventually implemented a machine learning model to predict the final result of a match between two two teams whose status (who is winning, or if scores are level) at half time is known. Also created a flask app which takes input the above mentioned variables using a form and then displays the result.

# Implementation
To run on local server:
~~~
conda create -n <name_env>
conda activate <name_env>
conda install pip
pip install -r requirements.txt
python3 app.py
~~~
After this go to your local host and play with the app. 

# Accuracy:
High randomness of data makes it difficult to achieve high accuracy in predicting the correct labels. With only a few features for the model to learning and a large number unique instances, the classification algorithm achieved an accuracy of 61.83%. After trying different models like K-Neighbors Classification, Naive Bayes, logistic Regression, Decision Tree Classification and an SVM, Random Forest Classifier outshone the others. 

# Result:

![](results/input.png)![](results/output.png)

# Scope for Improvement:
    1. The performance of teams in this case is being driven more by the historical data than the recent performance of the team. This prohibits the effective evaluation of current winning rate of a team and dismisses the chance of having outliers. 
    2. Adding CSS/Bootsrap to my flask app and hosting on a server. 
    3. This model, with the help of a few more parameters can predict the result before the match has even begun.



# References:
https://www.researchgate.net/publication/324606105_Predicting_Premiership_Football_Match_Results_Machine_vs_Men_-_Can_predictive_models_outperform_human_experts?enrichId=rgreq-ca1c07ce10e01c55f2a321e9ba22f050-XXX&enrichSource=Y292ZXJQYWdlOzMyNDYwNjEwNTtBUzo2MjgzODc0Mzc2MjEyNTVAMTUyNjgzMDY0ODY5Ng%3D%3D&el=1_x_2&_esc=publicationCoverPdf
