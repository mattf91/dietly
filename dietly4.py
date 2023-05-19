import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import os
import csv
from astropy.io import fits
import pandas as pd
from matteo3 import setup, left, plot, nw, wo, meals, check, check_setup, check_language, database_update, database_search, add_user_name

"""
TO DO:
- add comments to everything, so that you can understand;
- for the user: if you want, add the function that allows you to switch between users. for now, to change user, you have to close dietly and re-open it;
- create only one csv file for each user, instead of one per day;
"""





arr = os.listdir('.')


today = date.today()
today=today.strftime("%d_%m_%Y")
#start=input('')
if 'core.npy' not in arr:
    print('')
    first_usr = add_user_name()
    print('Welcome to Dietly, '+first_usr+'! Benvenuto/a su Dietly, '+first_usr+'! Bienvenido/a en Dietly, '+first_usr+'!')
    print('')
    core2 = np.rec.array([1400.0,350.0,490.0,560.0,'eng',first_usr], names=['top','top_red','top_yellow','top_green','lang','user'])
    usr_msk = (core2['user'] == first_usr)
    initial_top,initial_top_red,initial_top_yellow,initial_top_green=core2[usr_msk][0],core2[usr_msk][1],core2[usr_msk][2],core2[usr_msk][3]
    initial_red,initial_yellow,initial_green=0.0,0.0,0.0
    core,top,top_red,top_yellow,top_green,usr = setup(arr,core2,today,initial_top,initial_top_red,initial_top_yellow,initial_top_green,initial_red,initial_yellow,initial_green,first_usr)
    usr_msk = (core['user'] == usr)
    if core[usr_msk][4]=='eng':
        print('What is your initial weight (in Kg)?')
    if core[usr_msk][4]=='ita':
        print('Qual è il tuo peso iniziale (in Kg)?')
    if core[usr_msk][4]=='esp':
        print('Cual es tu peso inicial (en Kg)?')
    in_weight = input('')
    if in_weight==str(''):
        in_weight=86.0
    else:
        in_weight=float(in_weight)
    print('')
    days, weight = np.rec.array([str(usr),today], names=['user','date']), np.rec.array([str(usr),in_weight], names=['user','weight'])
    np.save('days.npy',days)
    np.save('weight.npy',weight)
    usr_msk = (core['user'] == usr)
    top=float(core[usr_msk][0])
    top_red=float(core[usr_msk][1])
    top_yellow=float(core[usr_msk][2])
    top_green=float(core[usr_msk][3])
    red,yellow,green=0.0,0.0,0.0
    if core[usr_msk][4]=='eng':
        print('Would you like to start using Dietly?')
    if core[usr_msk][4]=='ita':
        print('Vuoi iniziare ad usare Dietly?')
    if core[usr_msk][4]=='esp':
        print('Quieres empiezar a usar Dietly?')
    start = input('')
    if start==str(''):
        start='si'
    start=check(start,core[usr_msk][4])
    print('')
    if start == 'y' or start == 'yes' or start == 'si' or start == 's' or start == 'yep' or start == 'eja':
        arr = os.listdir('.')
        df = pd.DataFrame({'top': [top], 'red_left': [top_red], 'yellow_left': [top_yellow], 'green_left': [top_green], 'red': [0], 'yellow': [0], 'green': [0], 'ingredients':['-'], 'calories':[0], 'color':['-'], 'meal':['-']})
        df.to_csv(''+today+'_'+usr+'.csv',index=False)
    if start == 'no' or start == 'n' or start == 'nop' or start == 'nope':
        print('Salvarì!')
        print('')
else:
    weight=np.load('weight.npy',allow_pickle=True)
    days=np.load('days.npy',allow_pickle=True)
    core=np.load('core.npy',allow_pickle=True)
    print('Users list:')
    print('Lista Utenti:')
    print('Lista Usuarios:')
    print('')
    print(core['user'])
    print("If you are among them, type your User name; otherwise type 'add'.")
    print("Se sei uno di questi Utenti, scrivi il tuo nome Utente; altrimenti, scrivi 'agg'.")
    print("Si uno de estos Usuarios, escribe tu Usuario; de lo contrario, escribe 'agr.'")
    print('')
    temp_usr = str(input(''))
    bb = 0
    while bb == 0:
        if temp_usr in core['user']:
            usr = temp_usr
            usr_msk=(core['user']==usr)
            if core[usr_msk][4] == 'eng':
                print('Welcome back, '+usr)
                print('')
            if core[usr_msk][4] == 'ita':
                print('Bentornato/a, '+usr)
                print('')
            if core[usr_msk][4] == 'esp':
                print('Bienvenido/a de vuelta, '+usr)
                print('')
            bb=1
        if temp_usr == 'add' or temp_usr == 'agg' or temp_usr == 'agr':
            core,top,top_red,top_yellow,top_green,usr = setup(arr,core,today,1400.0,350.0,490.0,560.0,0.0,0.0,0.0,temp_usr)
            usr_msk=(core['user']==usr)
            bb=1
        if temp_usr not in core['user'] and (temp_usr != 'add' and temp_usr != 'agg' and temp_usr != 'agr'):
            print('Sorry, could you repeat?')
            print('Non ho capito, puoi ripetere?')
            print('Lo siento, puedes repetir?')
            print('')
            temp_usr = str(input(''))



    start = 'yes'
    print('')
    if start == 'y' or start == 'yes' or start == 'si' or start == 's' or start == 'yep' or start == 'eja':
        if today+'_'+usr+'.csv' not in arr:
            top=float(core[usr_msk][0])
            top_red=float(core[usr_msk][1])
            top_yellow=float(core[usr_msk][2])
            top_green=float(core[usr_msk][3])
            red,yellow,green=0.0,0.0,0.0
            df = pd.DataFrame({'top': [top], 'red_left': [top_red], 'yellow_left': [top_yellow], 'green_left': [top_green], 'red': [red], 'yellow': [yellow], 'green': [green], 'ingredients':['-'], 'calories':[0], 'color':['-'], 'meal':['-']})
            df.to_csv(str(today)+'_'+usr+'.csv',index=False)
            

#creating the new daily file
usr = str(usr)
usr_days_msk = (days['user'] == usr)
usr_weight_msk = (weight['user'] == usr)
if today != days[usr_days_msk][-1]:
    top=float(core[usr_msk][0])
    top_red=float(core[usr_msk][1])
    top_yellow=float(core[usr_msk][2])
    top_green=float(core[usr_msk][3])
    red,yellow,green=0.0,0.0,0.0
    df = pd.DataFrame({'top': [top], 'red_left': [top_red], 'yellow_left': [top_yellow], 'green_left': [top_green], 'red': [0], 'yellow': [0], 'green': [0], 'ingredients':['-'], 'calories':[0], 'color':['-'], 'meal':['-']})
    df.to_csv(str(today)+'_'+usr+'.csv',index=False)

#accessing to previous data from today
if str(today)+'_'+usr+'.csv' in arr:
    df = pd.read_csv(str(today)+'_'+usr+'.csv',sep=",", header=None)
    full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(df[0][1:]).astype(float), np.array(df[1][1:]).astype(float), np.array(df[2][1:]).astype(float), np.array(df[3][1:]).astype(float), np.array(df[4][1:]).astype(float), np.array(df[5][1:]).astype(float), np.array(df[6][1:]).astype(float), np.array(df[7][1:]), np.array(df[8][1:]).astype(float), np.array(df[9][1:]), np.array(df[10][1:])
    top, top_red, top_yellow, top_green, red, yellow, green=full_top[-1], full_top_red[-1], full_top_yellow[-1], full_top_green[-1], full_red[-1], full_yellow[-1], full_green[-1]

    


c=1
if start  == 'y' or start == 'yes' or start == 'si' or start == 's' or start == 'yep' or start == 'eja':
    c=1
if start == 'no' or start == 'n' or start == 'nop' or start == 'nope':
    c=0

while c==1:
    if core[usr_msk][4] == 'eng':
        print('What would you like to do?')
        print('')
        print('"nw" to insert the new weight')
        print('"database" to access/update the database of ingredients')
        print('"meal" to insert a new meal')
        print('"plot" to see the weight trend')
        print('"wo" to log a workout session')
        print('"left" to know the remaining calories')
        print('"setup" to set a new language or the new parameters of the diet')
        print('"close" to close Dietly')
    if core[4] == 'ita':
        print('Cosa vorresti fare?')
        print('')
        print('"nw" per inserire una nuova pesata')
        print('"database" per leggere/aggiornare il database degli ingredienti')
        print('"meal" per inserire un nuovo pasto')
        print('"plot" per vedere il grafico del peso')
        print('"wo" per caricare una sessione di allenamento')
        print('"left" per sapere le calorie giornaliere rimaste')
        print('"setup" per cambiare lingua o per settare nuovi parametri della dieta')
        print('"close" per uscire da Dietly')
    if core[4] == 'esp':
        print('Que querias hacer?')
        print('')
        print('"nw" para inserir un nuevo peso')
        print('"database" para leer/actualizar el database de los ingredientes')
        print('"meal" para inserir una comida')
        print('"plot" para ver el grafico de el peso')
        print('"wo" para registrar una sesione de entrenamiento')
        print('"left" para conocer las calorias restantes')
        print('"setup" para cambiar idioma o para settar una nueva configuracion de la dieta')
        print('"close" para salir de Dietly')
    print('')
    func= input('')
    print('')
    if func == 'nw': weight,days=nw(weight[usr_weight_msk][0],days[usr_days_msk][0],core[usr_msk],today,str(usr))
    if func == 'database': database_update(core[usr_msk][4])
    if func == 'meal': top,top_red,top_yellow,top_green,red,yellow,green = meals(top,top_red,top_yellow,top_green,red,yellow,green,core[usr_msk],today,str(usr))
    if func == 'plot': plot(core[usr_msk],days[usr_days_msk][0],weight[usr_weight_msk][0],str(usr))
    if func == 'wo': top,top_red,top_yellow,top_green = wo(top,top_red,top_yellow,top_green,red,yellow,green,core[usr_msk],today,str(usr))
    if func == 'left': left(top,top_red,top_yellow,red,yellow,green,core[usr_msk][4])
    if func == 'setup':
        core,top,top_red,top_yellow,top_green,usr=setup(arr,core[usr_msk],today,top,top_red,top_yellow,top_green,red,yellow,green,usr)
        usr_msk=(core['user']==usr)
    if func == 'close':
        print('')
        print('Salvarì!')
        print('')
        break
    if core[usr_msk][4] == 'eng':
        print('Would you like to do something else?')
    if core[usr_msk][4] == 'ita':
        print("Vorresti fare qualcos'altro?")
    if core[usr_msk][4] == 'esp':
        print('Querias hacer algo màs?')
    done = input('')
    done=check(done,core[usr_msk][4])
    print('')
    if done == 'no' or done == 'n' or done == 'nop' or done == 'nope':
        c=0
        print('Salvarì!')
        print('')
    if done == 'y' or done == 'yes' or done == 'si' or done == 's' or done == 'yep' or done == 'eja':
        c=1
        
        
        
        
