import os
from flask import Flask, render_template,request
from joblib import load
import numpy as np
from picher import predict as predict_picher
from fielder import predict as predict_fielder
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

upload_folder = './statics/piching_data'


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/picher', methods=['GET', 'POST'] )
def picher():
    if request.method == 'GET':
        return render_template("picher.html")
    elif request.method == "POST":
        try:
            epa = request.form['epa']
            game = request.form['game']
            win = request.form['win']
            lose = request.form['lose']
            save = request.form['save']
            hold = request.form['hold']
            WR = request.form['WR']
            batter = request.form['batter']
            IP = request.form['IP']
            hit = request.form['hit']
            HRA = request.form['HRA']
            walk = request.form['walk']
            HP = request.form['HP']
            strikeout = request.form['strikeout']
            CP = request.form['CP']
            selfblame = request.form['selfblame']
            WHIP = request.form['WHIP']
            DIPS = request.form['DIPS']
            answer = np.array([epa,game,win,lose,save,hold,
                        WR,batter,IP,hit,HRA,walk,HP,strikeout,
                        CP,selfblame,WHIP,DIPS])
            piching_data = {"epa":epa,"game":game,"win":win,"lose":lose,"save":save
                ,"hold":hold,"WR":WR,"batter":batter,"IP":IP,"hit":hit,
                "HRA":HRA,"walk":walk,"HP":HP,"strikeout":strikeout,"CP":CP,"selfblame":selfblame,
                "WHIP":WHIP,"DIPS":DIPS}
            result = predict_picher(answer)[0]
            money_str = str(round(result))
            if len(money_str)>= 5:
                money_str = money_str[0] + "億" + money_str[1:]
            return render_template('picher_result.html' ,result=money_str,picher=piching_data)
        except Exception as e:
            error_message = "数字が入力されていません".format(str(e))
            return render_template("picher.html",error_message=error_message)
@app.route('/fielder',methods=['GET', 'POST'])
def fielder():
    if request.method == "GET":
        return render_template("fielder.html")
    elif request.method == "POST":
        try:
            average = request.form['average']
            game_f = request.form['game_f']
            bat = request.form['bat']
            number = request.form['number']
            hit_f = request.form['hit_f']
            HR = request.form['HR']
            RBI = request.form['RBI']
            steal = request.form['steal']
            walk_f = request.form['walk_f']
            HP_f = request.form['HP_f']
            strikeout_f = request.form['strikeout_f']
            sacrifice = request.form['sacrifice']
            double = request.form['double']
            base = request.form['base']
            slugging = request.form['slugging']
            OPS = request.form['OPS']
            answer_f = np.array([average,game_f,bat,number,hit_f,
                                HR,RBI,steal,walk_f,HP_f,
                                strikeout_f,sacrifice,double,base,slugging,OPS])
            fielding_data = {"average":average,"game_f":game_f,"bat":bat,"number":number,"hit_f":hit_f
                            ,"HR":HR,"RBI":RBI,"steal":steal,"walk_f":walk_f,"HP_f":HP_f,
                            "strikeout_f":strikeout_f,"sacrifice":sacrifice,"double":double,
                            "base":base,"slugging":slugging,"OPS":OPS}
            money_f = predict_fielder(answer_f)[0]
            money_str = str(round(money_f))
            if len(money_str)>= 5:
                money_str = money_str[0] + "億" + money_str[1:]
            return render_template('fielder_result.html' ,money=money_str,money_f=money_f,fielder=fielding_data)
        except Exception as e:
            error_message = "数字が入力されていません".format(str(e))
            return render_template("fielder.html", error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)