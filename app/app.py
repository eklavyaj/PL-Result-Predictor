from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pandas as pd
import pickle as p



def desc(HomeTeam, AwayTeam, winner):
    positions = pd.read_csv('csv_files/final_positions.csv')
    homeform = np.mean(positions['form'][positions['team']==HomeTeam])
    awayform = np.mean(positions['form'][positions['team']==AwayTeam])
    if((winner=='H') & ((homeform-awayform)>0)):
        team='Home'
        upset='No'
        homeadv='Yes'
    elif((winner=='H') & ((homeform-awayform)<0)):
        team='Home'
        upset='Yes'
        homeadv='Yes'
    elif((winner=='A') & ((homeform-awayform)>0)):
        team='Away'
        upset='Yes'
        homeadv='No'
    elif((winner=='A') & ((homeform-awayform)<0)):
        team='Away'
        upset='No'
        homeadv='No'
    elif((winner=='D') & (((homeform-awayform)>-0.15) & ((homeform-awayform)<0.15))):
        team = 'Draw'
        upset='No'
        homeadv='Neutral'
    elif((winner=='D') & ((homeform-awayform)>0.15)):
        team = 'Draw'
        upset='Yes'
        homeadv='No'
    elif((winner=='D') & ((homeform-awayform)<-0.15)):
        team = 'Draw'
        upset='Yes'
        homeadv='Yes'
    else:
        team = 'Draw'
        upset='Neutral'
        homeadv='Neutral'
    return [HomeTeam, AwayTeam, team, upset, homeadv]
    # print('{} vs. {} : {} \nUpset : {}\nHome Advantage : {}'.format())


def predict_winner(HomeTeam , AwayTeam , HTR):
    AllTeams = p.load(open('pickle_files/allteams.pickle', 'rb'))
    AllResults = p.load(open('pickle_files/allresults.pickle', 'rb'))

    rfc = p.load(open('pickle_files/final_predictions.pickle', 'rb'))
    hometeam = AllTeams[HomeTeam]
    awayteam = AllTeams[AwayTeam]
    htr = AllResults[HTR]
    case = np.array([hometeam,awayteam,htr])
    case = case.reshape(1,3)

    FTR = (rfc.predict(case))

    if(FTR == 1):
        return desc(HomeTeam , AwayTeam, 'D')
    elif (FTR == 0) :
        return desc(HomeTeam, AwayTeam , 'A')
    else :
        return desc(HomeTeam , AwayTeam , 'H')
        
def result(hteam, ateam, htime):

    [a, b, c, d, e] = predict_winner( hteam,ateam,htime)

    if htime == "H":
        output = a + " vs. " + b +" with the home team, " + a + ",winning at half time.\n" 
    elif htime == "A":
        output = a + " vs. " + b +" with the away team, " + b + ", winning at half time.\n" 
    elif htime == "D":
        output =  a + " vs. " + b + " with both teams tied at a half time.\n"

    output += "Match ended "

    if c == "Home":
        output += "and the winner is the home team, " + hteam +".\n"
        if d == "Yes":
            output += "It is an upset.\n"
        else:
            output += "It is not an upset.\n"
        if e == "Yes":
            output += hteam + " exploited their home advantage.\n"
        elif e == "No":
            output += hteam + " could not exploit their home advantage.\n"
        else:
            output += "It was a tough match.\n"

    elif c == "Away":
        output += "and the winner is the away team, " + ateam +".\n"
        if d == "Yes":
            output += "It is an upset.\n"
        else:
            output += "It is not an upset.\n"
        if e == "Yes":
            output += hteam + " exploited their home advantage.\n"
        elif e == "No":
            output += hteam + " could not exploit their home advantage.\n"
        else:
            output += "It was a tough match.\n"
    
    elif c == "Draw":
        output += "in a draw.\n"
        if d == "Yes":
            output += "It is an upset.\n"
        else:
            output += "It is not an upset.\n"
        if e == "Yes":
            output += hteam + " exploited their home advantage.\n"
        elif e == "No":
            output += hteam + " could not exploit their home advantage.\n"
        else:
            output += "It was a tough match.\n"

    return output


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    hteam = request.form['hteam']
    ateam = request.form['ateam']
    htime = request.form['htime']
    if hteam == ateam :
        return "Please enter different teams."

    output = result(hteam, ateam, htime)
    return output

if __name__ == "__main__":
    app.run()

