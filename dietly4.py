import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import os
import csv
from astropy.io import fits
import pandas as pd
from scipy.interpolate import UnivariateSpline
from matteo3 import setup, left, plot, nw, wo, meals, check, check_setup, check_language, database_update, database_search, add_user_name, select_first_user, select_user,past_meals,simulation


arr = os.listdir('.')


today = date.today()
today=today.strftime("%d_%m_%Y")
#start=input('')
extracal=0
if 'core.npy' not in arr:
    in_core = np.rec.array([1400.0,350.0,490.0,560.0,'eng','NoNe'], names=['top','top_red','top_yellow','top_green','lang','user'])
    print('')
    first_usr = add_user_name(in_core)
    print('Welcome to Dietly, '+first_usr+'! Benvenuto/a su Dietly, '+first_usr+'! Bienvenido/a en Dietly, '+first_usr+'!')
    print('')
    core2 = np.rec.array([1400.0,350.0,490.0,560.0,'eng',first_usr], names=['top','top_red','top_yellow','top_green','lang','user'])
    usr_msk = (core2['user'] == first_usr)
    initial_top,initial_top_red,initial_top_yellow,initial_top_green=core2[usr_msk][0][0],core2[usr_msk][0][1],core2[usr_msk][0][2],core2[usr_msk][0][3]
    initial_red,initial_yellow,initial_green=0.0,0.0,0.0
    core,top,top_red,top_yellow,top_green,usr = setup(arr,core2,today,initial_top,initial_top_red,initial_top_yellow,initial_top_green,initial_red,initial_yellow,initial_green,first_usr,extracal)
    usr_msk = (core['user'] == usr)
    if core[usr_msk][0][4]=='eng':
        print('What is your initial weight (in Kg)?')
    if core[usr_msk][0][4]=='ita':
        print('Qual è il tuo peso iniziale (in Kg)?')
    if core[usr_msk][0][4]=='esp':
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
    top=float(core[usr_msk][0][0])
    top_red=float(core[usr_msk][0][1])
    top_yellow=float(core[usr_msk][0][2])
    top_green=float(core[usr_msk][0][3])
    red,yellow,green=0.0,0.0,0.0
    if core[usr_msk][0][4]=='eng':
        print('Would you like to start using Dietly?')
    if core[usr_msk][0][4]=='ita':
        print('Vuoi iniziare ad usare Dietly?')
    if core[usr_msk][0][4]=='esp':
        print('Quieres empiezar a usar Dietly?')
    start = input('')
    if start==str(''):
        start='si'
    start=check(start,core[usr_msk][0][4])
    print('')
    if start == 'y' or start == 'yes' or start == 'si' or start == 's' or start == 'yep' or start == 'eja' or start == '':
        c=1
        arr = os.listdir('.')
        df = pd.DataFrame({'top': [top], 'red_left': [top_red], 'yellow_left': [top_yellow], 'green_left': [top_green], 'red': [0], 'yellow': [0], 'green': [0], 'ingredients': [str('-')], 'calories': [0], 'color': [str('-')], 'meal': [str('-')]})
        df.to_csv(usr+'_'+today+'.csv',index=False)
    if start == 'no' or start == 'n' or start == 'nop' or start == 'nope':
        c=0
        print('Salvarì!')
        print('')
else:
    weight=np.load('weight.npy',allow_pickle=True)
    days=np.load('days.npy',allow_pickle=True)
    core=np.load('core.npy',allow_pickle=True)
    usr,core,days,weight=select_first_user(core,arr,today,days,weight,extracal)
    usr_msk = (core['user'] == usr)

    start = 'yes'
    c=1
    print('')
    if usr+'_'+today+'.csv' not in arr:
        top=float(core[usr_msk][0][0])
        top_red=float(core[usr_msk][0][1])
        top_yellow=float(core[usr_msk][0][2])
        top_green=float(core[usr_msk][0][3])
        red,yellow,green=0.0,0.0,0.0
        df = pd.DataFrame({'top': [top], 'red_left': [top_red], 'yellow_left': [top_yellow], 'green_left': [top_green], 'red': [red], 'yellow': [yellow], 'green': [green], 'ingredients': ['-'], 'calories': [0], 'color':['-'], 'meal': ['-']})
        df.to_csv(str(usr)+'_'+str(today)+'.csv',index=False)
    else:
        df = pd.read_csv(str(usr)+'_'+str(today)+'.csv',sep=",", header=None)
        full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(df[0][1:]).astype(float), np.array(df[1][1:]).astype(float), np.array(df[2][1:]).astype(float), np.array(df[3][1:]).astype(float), np.array(df[4][1:]).astype(float), np.array(df[5][1:]).astype(float), np.array(df[6][1:]).astype(float), np.array(df[7][1:]), np.array(df[8][1:]).astype(float), np.array(df[9][1:]), np.array(df[10][1:])
        top, top_red, top_yellow, top_green, red, yellow, green=full_top[-1], full_top_red[-1], full_top_yellow[-1], full_top_green[-1], full_red[-1], full_yellow[-1], full_green[-1]
        

#creating the new daily file
usr = str(usr)
usr_days_msk = (days['user'] == usr)
usr_weight_msk = (weight['user'] == usr)
nnn=0
while c==1:
    if core[usr_msk][0][4] == 'eng':
        if nnn == 0:
            print('What would you like to do?')
        if nnn == 1:
            print('Would you like to do something else?')
        print('')
        print('"nw" to insert the new weight')
        print('"dtb" to access/update the database of ingredients')
        print('"sim" to simulate a meal')
        print('"meal" to insert a new meal')
        print('"past" to update the meals of a past day')
        print('"plot" to see the weight trend')
        print('"wo" to log a workout session')
        print('"left" to know the remaining calories')
        print('"setup" to set a new language or the new parameters of the diet')
        print('"user" to change/add user')
        print('"close" to close Dietly')
    if core[usr_msk][0][4] == 'ita':
        if nnn == 0:
            print('Cosa vorresti fare?')
        if nnn == 1:
            print("Vorresti fare qualcos'altro?") 
        print('')
        print('"nw" per inserire una nuova pesata')
        print('"dtb" per leggere/aggiornare il database degli ingredienti')
        print('"sim" per simulare un pasto')
        print('"meal" per inserire un nuovo pasto')
        print('"past" per aggiornare i pasti di un giorno passato')
        print('"plot" per vedere il grafico del peso')
        print('"wo" per caricare una sessione di allenamento')
        print('"left" per sapere le calorie giornaliere rimaste')
        print('"setup" per cambiare lingua o per settare nuovi parametri della dieta')
        print('"user" per cambiare/aggiungere un utente')
        print('"close" per uscire da Dietly')
    if core[usr_msk][0][4] == 'esp':
        if nnn == 0:
            print('Que querias hacer?')
        if nnn == 1:
            print('Querias hacer algo màs?')
        print('')
        print('"nw" para inserir un nuevo peso')
        print('"dtb" para leer/actualizar el database de los ingredientes')
        print('"sim" para simular una comida')
        print('"meal" para inserir una comida')
        print('"past" para actualizar las comidas de un dia pasado')
        print('"plot" para ver el grafico de el peso')
        print('"wo" para registrar una sesione de entrenamiento')
        print('"left" para conocer las calorias restantes')
        print('"setup" para cambiar idioma o para settar una nueva configuracion de la dieta')
        print('"user" para cambiar/agregar un usuario')
        print('"close" para salir de Dietly')
    print('')
    xx=0
    while xx ==0:
        func= input('')
        print('')
        if func == 'nw' or func == 'dtb' or func == 'meal' or func == 'past' or func == 'plot' or func == 'wo' or func == 'left' or func == 'user' or func == 'setup' or func == 'close' or func == 'sim':
            xx=1
        else:
            if core[usr_msk][0][4] == 'eng':
                print('Sorry, could you repeat?')
            if core[usr_msk][0][4] == 'ita':
                print('Non ho capito, puoi ripetere?')
            if core[usr_msk][0][4] == 'esp':
                print('Lo siento, puedes repetir?')
            print('')
            xx=0

    if func == 'nw':
        weight,days=nw(weight,days,core,today,str(usr))
        usr_days_msk = (days['user'] == usr)
        usr_weight_msk = (weight['user'] == usr)
        next_fun=input('')
    if func == 'dtb':
        database_update(core[usr_msk][0][4])
        next_fun=input('')
    if func == 'sim':
        simulation(core,usr)
        next_fun=input('')
    if func == 'meal':
        top,top_red,top_yellow,top_green,red,yellow,green = meals(top,top_red,top_yellow,top_green,red,yellow,green,core[usr_msk][0],today,str(usr))
        next_fun=input('')
    if func == 'past':
        past_meals(core,str(usr),arr)
        next_fun=input('')
    if func == 'plot':
        plot(core[usr_msk][0],days[usr_days_msk]['date'],weight[usr_weight_msk]['weight'],str(usr))
    if func == 'wo':
        top,top_red,top_yellow,top_green,extracal = wo(top,top_red,top_yellow,top_green,red,yellow,green,core,today,str(usr))
        next_fun=input('')
    if func == 'left':
        left(top_red,top_yellow,top_green,core[usr_msk][0][4])
        next_fun=input('')
    if func == 'user':
        usr,core,days,weight = select_user(core,arr,today,days,weight,usr,extracal)
        usr_msk=(core['user']==usr)
        usr_days_msk = (days['user'] == usr)
        usr_weight_msk = (weight['user'] == usr)
        df = pd.read_csv(str(usr)+'_'+str(today)+'.csv',sep=",", header=None)
        full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(df[0][1:]).astype(float), np.array(df[1][1:]).astype(float), np.array(df[2][1:]).astype(float), np.array(df[3][1:]).astype(float), np.array(df[4][1:]).astype(float), np.array(df[5][1:]).astype(float), np.array(df[6][1:]).astype(float), np.array(df[7][1:]), np.array(df[8][1:]).astype(float), np.array(df[9][1:]), np.array(df[10][1:])
        top, top_red, top_yellow, top_green, red, yellow, green=full_top[-1], full_top_red[-1], full_top_yellow[-1], full_top_green[-1], full_red[-1], full_yellow[-1], full_green[-1]
        next_fun=input('')
    if func == 'setup':
        core,top,top_red,top_yellow,top_green,usr=setup(arr,core,today,top,top_red,top_yellow,top_green,red,yellow,green,usr,extracal)
        usr_msk=(core['user']==usr)
        usr_days_msk = (days['user'] == usr)
        usr_weight_msk = (weight['user'] == usr)
        next_fun=input('')
    if func == 'close':
        print('Salvarì!')
        print('')
        break
    nnn=1
    
