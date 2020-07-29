# Premier-League-Result-Predictor
Purpose:

This predictor predicts the winner of two teams at full-time based on past fixture results of the two teams as well as other factors like home/away advantage. The predictor inputs the home team , the away team and the result at half-time and outputs the prediction of the result at full-time.

There are Visualisations of statistic comparisons between teams as well.

Accuracy:
The predictor performs very well in regards to the human level error (47% , predicting the result before match has begun). After trying various models to get the best accuracy score, RandomForestClassifier turned out to be the most accurate classifier with an accuracy score of 61.46%. 

Scope for Improvement:
The performance of teams in this case is being driven more by the historical data than the recent performance of the team. This prohibits the effective evaluation of current winning rate of a team and dismisses the chance of having outliers. 
This model, with the help of a few more parameters can predict the result before the match has even begun. (I had access to limited data)

References:
https://www.researchgate.net/publication/324606105_Predicting_Premiership_Football_Match_Results_Machine_vs_Men_-_Can_predictive_models_outperform_human_experts?enrichId=rgreq-ca1c07ce10e01c55f2a321e9ba22f050-XXX&enrichSource=Y292ZXJQYWdlOzMyNDYwNjEwNTtBUzo2MjgzODc0Mzc2MjEyNTVAMTUyNjgzMDY0ODY5Ng%3D%3D&el=1_x_2&_esc=publicationCoverPdf
