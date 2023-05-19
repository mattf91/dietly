import numpy as np
import matplotlib.pyplot as plt
from datetime import date
import os
import csv
from astropy.io import fits
import pandas as pd


#allows you to add the first user
def add_user_name():
    cc=1
    while cc==1:
        print("New User's name: ")
        print("Nuovo nome Utente: ")
        print("Nuevo nombre Usuario: ")
        print("")
        name = str(input(''))
        print('')
        print("The user's name is "+name+", correct?")
        print("Il nome utente è "+name+", corretto?")
        print("El nombre del usuario es "+name+", correcto?")
        print('')
        confirm_name = input('')
        xx=1
        while xx==1:
            if confirm_name != 'y' and confirm_name != 'yes' and confirm_name != 'si' and confirm_name != 's' and confirm_name != 'yep' and confirm_name != 'eja' and confirm_name != 'no' and confirm_name != 'n' and confirm_name != 'nop' and confirm_name != 'nope':
                print('Sorry, could you repeat?')
                print('Non ho capito, puoi ripetere?')
                print('Lo siento, puedes repetir?')
                confirm_name = input('')
                xx=1
            else: xx=0
        if confirm_name == 'y' or confirm_name == 'yes' or confirm_name == 'si' or confirm_name == 's' or confirm_name == 'yep' or confirm_name == 'eja':
            cc=0
        if confirm_name == 'no' or confirm_name == 'n' or confirm_name == 'nop' or confirm_name == 'nope':
            cc=1
    return(name)





#spelling check 'yes'
def check(key,lang):
    x=1
    while x==1:
        if key != 'y' and key != 'yes' and key != 'si' and key != 's' and key != 'yep' and key != 'eja' and key != 'no' and key != 'n' and key != 'nop' and key != 'nope':
            if lang == 'eng':
                print('Sorry, could you repeat?')
            if lang == 'ita':
                print('Non ho capito, puoi ripetere?')
            if lang == 'esp':
                print('Lo siento, puedes repetir?')
            key = input('')
            x=1
        else: x=0

    return(str(key))


#spelling check 'setup'
def check_setup(key,lang):
    x=1
    while x==1:
        if key != 'lan' and key != 'par':
            if lang == 'eng':
                print('Sorry, could you repeat?')
            if lang == 'ita':
                print('Non ho capito, puoi ripetere?')
            if lang == 'esp':
                print('Lo siento, puedes repetir?')
            key = input('')
            x=1
        else: x=0

    return(str(key))



#spelling check 'lang'
def check_language(key,lang):
    x=1
    while x==1:
        if key != 'eng' and key != 'ita' and key != 'esp':
            if lang == 'eng':
                print('Sorry, could you repeat?')
            if lang == 'ita':
                print('Non ho capito, puoi ripetere?')
            if lang == 'esp':
                print('Lo siento, puedes repetir?')
            key = input('')
            x=1
        else: x=0

    return(str(key))




#per le impostazioni
def setup(arr,core,today,top,top_red,top_yellow,top_green,red,yellow,green,user):
    if 'core.npy' in arr and user != 'add' and user != 'agg' and user != 'agr':
        usr_msk = (core['user'] == str(user))
        z=1
        while z==1:
            if core[usr_msk][4]=='eng':
                print('Would you like to change the language (type: "lan") or the parameters of the diet (type: "par")?')
            if core[usr_msk][4]=='ita':
                print('Vuoi cambiare la lingua (digita: "lan") o i parametri della dieta (digita: "par")?')
            if core[usr_msk][4]=='esp':
                print('Quieres cambiar el idioma (digita: "lan") o los parametros de la dieta (digita: "par")?')
            choice = input('')
            print('')
            choice = check_setup(choice,core[usr_msk][4])
            print('')
            if choice == 'par':
                if core[usr_msk][4]=='eng':
                    print('You currently have the following setup:')
                    print(str(core[usr_msk][0])+' total calories per day')
                    print(str(float(core[usr_msk][1])*100/float(core[usr_msk][0]))+'% of red calories')
                    print(str(float(core[usr_msk][2])*100/float(core[usr_msk][0]))+'% of yellow calories')
                    print(str(float(core[usr_msk][3])*100/float(core[usr_msk][0]))+'% of green calories')
                    print('')
                    print('Would you like to change it?')
                if core[usr_msk][4]=='ita':
                    print('Al momento hai le seguenti impostazioni:')
                    print(str(core[usr_msk][0])+' calorie giornaliere totali')
                    print(str(float(core[usr_msk][1])*100/float(core[usr_msk][0]))+'% di calorie rosse')
                    print(str(float(core[usr_msk][2])*100/float(core[usr_msk][0]))+'% di calorie gialle')
                    print(str(float(core[usr_msk][3])*100/float(core[usr_msk][0]))+'% di calorie verdi')
                    print('')
                    print('Vuoi cambiarle?')
                if core[usr_msk][4]=='esp':
                    print('Ahora tienes esta configuracion:')
                    print(str(core[usr_msk][0])+' calorias totales cada dia')
                    print(str(float(core[usr_msk][1])*100/float(core[usr_msk][0]))+'% de calorias rojas')
                    print(str(float(core[usr_msk][2])*100/float(core[usr_msk][0]))+'% de calorias amarillas')
                    print(str(float(core[usr_msk][3])*100/float(core[usr_msk][0]))+'% de calorias verdes')
                    print('')
                    print('Quieres cambiarlas?')
                change=input('')
                change=check(change,core[usr_msk][4])
                print('')
                if change == 'no' or change == 'n' or change == 'nop' or change == 'nope':
                    if core[usr_msk][4]=='eng':
                        print('Would you like to change anything else?')
                    if core[usr_msk][4]=='ita':
                        print('Vuoi cambiare altro?')
                    if core[usr_msk][4]=='esp':
                        print('Quieres cambiar algo màs?')
                    el= input('')
                    el=check(el,core[usr_msk][4])
                    print('')
                    if el == 'y' or el == 'yes' or el == 'si' or el == 's' or el == 'yep' or el == 'eja':
                        z=1
                    if el == 'no' or el == 'n' or el == 'nop' or el == 'nope':
                        z=0
                        return(core,top,top_red,top_yellow,top_green,str(user))
                if change == 'y' or change == 'yes' or change == 'si' or change == 's' or change == 'yep' or change == 'eja':
                    if core[usr_msk][4]=='eng':
                        print('What is the chosen daily calories intake (in Kcal)?')
                    if core[usr_msk][4]=='ita':
                        print('Qual è il tuo fabbisogno calorico giornaliero (in Kcal)?')
                    if core[usr_msk][4]=='esp':
                        print('Cuantas calorias necesitas cada dia (in Kcal)?')
                    new_core_top=float(input(''))
                    print('')
                    if core[usr_msk][4]=='eng':
                        print('What is the percentage of red calories?')
                    if core[usr_msk][4]=='ita':
                        print('Qual è la percentuale di calorie rosse?')
                    if core[usr_msk][4]=='esp':
                        print('Cual es la percentual de calorias rojas?')
                    new_perc_red=float(input(''))
                    print('')
                    if core[usr_msk][4]=='eng':
                        print('What is the percentage of yellow calories?')
                    if core[usr_msk][4]=='ita':
                        print('Qual è la percentuale di calorie gialle?')
                    if core[usr_msk][4]=='esp':
                        print('Cual es la percentual de calorias amarillas?')
                    new_perc_yellow=float(input(''))
                    print('')
                    new_top_core_red = float(int(new_core_top*new_perc_red/100))
                    new_top_core_yellow = float(int(new_core_top*new_perc_yellow/100))
                    new_top_core_green= new_core_top-new_top_core_yellow-new_top_core_red
                    new_top=float(top)+new_core_top-float(core[0])
                    new_top_red=float(int(float(top_red)+(new_core_top-float(core[0]))*new_perc_red/100))
                    new_top_yellow=float(int(float(top_yellow)+(new_core_top-float(core[0]))*new_perc_yellow/100))
                    new_top_green=new_top-new_top_red-new_top_yellow
                    core[usr_msk][0],core[usr_msk][1],core[usr_msk][2],core[usr_msk][3],core[usr_msk][5]= new_core_top,new_top_core_red,new_top_core_yellow,new_top_core_green,user
                    if core[usr_msk][4]=='eng':
                        print('This is your new setup:')
                        print(str(core[usr_msk][0])+' total calories per day')
                        print(str(core[usr_msk][1])+' red calories')
                        print(str(core[usr_msk][2])+' yellow calories')
                        print(str(core[usr_msk][3])+' green calories')
                    if core[usr_msk][4]=='ita':
                        print('Queste sono le nuove impostazioni:')
                        print(str(core[usr_msk][0])+' calorie giornaliere totali')
                        print(str(core[usr_msk][1])+' calorie rosse')
                        print(str(core[usr_msk][2])+' calorie gialle')
                        print(str(core[usr_msk][3])+' calorie verdi')
                    if core[usr_msk][4]=='esp':
                        print('Esta es la nueva configuracion:')
                        print(str(core[usr_msk][0])+' calorias totales cada dia')
                        print(str(core[usr_msk][1])+' calorias rojas')
                        print(str(core[usr_msk][2])+' calorias amarillas')
                        print(str(core[usr_msk][3])+' calorias verdes')
                    print('')
                    np.save('core.npy',core)
                    
                    if core[usr_msk][4]=='eng':
                        print('Would you like to change anything else?')
                    if core[usr_msk][4]=='ita':
                        print('Vuoi cambiare altro?')
                    if core[usr_msk][4]=='esp':
                        print('Quieres cambiar algo màs?')
                    el= input('')
                    el=check(el,core[usr_msk][4])
                    print('')
                    if el == 'y' or el == 'yes' or el == 'si' or el == 's' or el == 'yep' or el == 'eja':
                        z=1
                    if el == 'no' or el == 'n' or el == 'nop' or el == 'nope':
                        z=0
                        df = pd.read_csv(str(today)+'_'+user+'.csv',sep=",", header=None)
                        full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(df[0][1:]).astype(float), np.array(df[1][1:]).astype(float), np.array(df[2][1:]).astype(float), np.array(df[3][1:]).astype(float), np.array(df[4][1:]).astype(float), np.array(df[5][1:]).astype(float), np.array(df[6][1:]).astype(float), np.array(df[7][1:]), np.array(df[8][1:]).astype(float), np.array(df[9][1:]), np.array(df[10][1:])
                        full_top[-1], full_top_red[-1], full_top_yellow[-1], full_top_green[-1]=new_top,(new_top_red),new_top_yellow,new_top_green
                        dw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
                        dw.to_csv(str(today)+'_'+user+'.csv',index=False)
                        return(core,new_top,new_top_red,new_top_yellow,new_top_green,str(user))
                    
            if choice == 'lan':
                if core[usr_msk][4]=='eng':
                    print('To which language would you like to switch? "eng" for English, "ita" for Italian, or "esp" for Espanol')
                    lan = input('')
                    print('')
                    lan = check_language(lan,core[usr_msk][4])
                    print('')
                    print('Would you like to switch to '+str(lan)+'?')
                if core[usr_msk][4]=='ita':
                    print('A che linguaggio vuoi passare? "eng" per inglese, "ita" per italiano, o "esp" per spagnolo')
                    lan = input('')
                    print('')
                    lan = check_language(lan,core[usr_msk][4])
                    print('')
                    print('Vuoi passare a '+str(lan)+'?')
                if core[usr_msk][4]=='esp':
                    print('A que idioma quieres cambiar? "eng" per ingles, "ita" para italiano, o "esp" para espanol')
                    lan = input('')
                    print('')
                    lan = check_language(lan,core[usr_msk][4])
                    print('')
                    print('Quieres cambiar a '+str(lan)+'?')
                
                conf=input('')
                conf=check(conf,core[usr_msk][4])
                print('')
                if conf == 'y' or conf == 'yes' or conf == 'si' or conf == 's' or conf == 'yep' or conf == 'eja':
                    core[usr_msk][4]=str(lan)
                    np.save('core.npy',core)
                if core[usr_msk][4]=='eng':
                    print('Would you like to change anything else?')
                if core[usr_msk][4]=='ita':
                    print('Vuoi cambiare altro?')
                if core[usr_msk][4]=='esp':
                    print('Quieres cambiar algo màs?')
                el= input('')
                el=check(el,core[usr_msk][4])
                print('')
                if el == 'y' or el == 'yes' or el == 'si' or el == 's' or el == 'yep' or el == 'eja':
                    z=1
                if el == 'no' or el == 'n' or el == 'nop' or el == 'nope':
                    z=0
                    return(core,top,top_red,top_yellow,top_green,str(user))
    if 'core.npy' not in arr:
        print('Which language would you prefer? "eng" for English, "ita" for Italian, or "esp" for Espanol')
        print('(You can change it later on by calling the "setup" function)')
        print('')
        print('Quale lingua preferisci? "eng" per inglese, "ita" per italiano, o "esp" per spagnolo')
        print('(La puoi cambiare in qualsiasi momento chiamando la funzione "setup")')
        print('')
        print('Cual idioma prefieres? "eng" para ingles, "ita" para italiano, o "esp" para espanol')
        print('(Lo puedes cambiar en cualquier momento llamando la funciòn "setup")')
        print('')
        lan = input('')
        print('')
        vv=0
        if lan != 'eng' and lan != 'ita' and lan != 'esp':
            while vv == 0:
                print('Sorry, could you repeat?')
                print('')
                print('Non ho capito, puoi ripetere?')
                print('')
                print('Lo siento, puedes repetir?')
                print('')
                lan = input('')
                if lan != 'eng' and lan != 'ita' and lan != 'esp':
                    vv=0
                else:
                    vv=1
            
        print('')
        if lan=='eng':
            print('What is the chosen daily calories intake?')
            top=input('')
            if top==str(''):
                top=1400.0
            else:
                top=float(top)
            print('')
            print('What is the percentage of red calories?')
            perc_red=input('')
            if perc_red==str(''):
                perc_red=25.0
            else:
                perc_red=float(perc_red)
            print('')
            print('What is the percentage of yellow calories?')
            perc_yellow=input('')
            if perc_yellow==str(''):
                perc_yellow=35.0
            else:
                perc_yellow=float(perc_yellow)
            print('')
        if lan=='ita':
            print('Qual è il tuo fabbisogno calorico giornaliero (in Kcal)?')
            top=input('')
            if top==str(''):
                top=1400.0
            else:
                top=float(top)
            print('')
            print('Qual è la percentuale di calorie rosse?')
            perc_red=input('')
            if perc_red==str(''):
                perc_red=25.0
            else:
                perc_red=float(perc_red)
            print('')
            print('Qual è la percentuale di calorie gialle?')
            perc_yellow=input('')
            if perc_yellow==str(''):
                perc_yellow=35.0
            else:
                perc_yellow=float(perc_yellow)
            print('')
        if lan=='esp':
            print('Cuantas calorias necesitas cada dia (in Kcal)?')
            top=input('')
            if top==str(''):
                top=1400.0
            else:
                top=float(top)
            print('')
            print('Cual es la percentual de calorias rojas?')
            perc_red=input('')
            print('')
            if perc_red==str(''):
                perc_red=25.0
            else:
                perc_red=float(perc_red)
            print('Cual es la percentual de calorias amarillas?')
            perc_yellow=input('')
            print('')
            if perc_yellow==str(''):
                perc_yellow=35.0
            else:
                perc_yellow=float(perc_yellow)
            print('')
        
        top_red = top*perc_red/100
        top_yellow = top*perc_yellow/100
        top_green= top-top_yellow-top_red
        core= np.rec.array([top,top_red,top_yellow,top_green,str(lan),str(user)],names=['top','top_red','top_yellow','top_green','lang','user'])
        usr_msk = (core['user'] == user)
        if core[usr_msk][4]=='eng':
            print('This is your new setup:')
            print(str(core[usr_msk][0])+' total calories per day')
            print(str(core[usr_msk][1])+' red calories')
            print(str(core[usr_msk][2])+' yellow calories')
            print(str(core[usr_msk][3])+' green calories')
        if core[usr_msk][4]=='ita':
            print('Queste sono le nuove impostazioni:')
            print(str(core[usr_msk][0])+' calorie giornaliere totali')
            print(str(core[usr_msk][1])+' calorie rosse')
            print(str(core[usr_msk][2])+' calorie gialle')
            print(str(core[usr_msk][3])+' calorie verdi')
        if core[usr_msk][4]=='esp':
            print('Esta es la nueva configuracion:')
            print(str(core[usr_msk][0])+' calorias totales cada dia')
            print(str(core[usr_msk][1])+' calorias rojas')
            print(str(core[usr_msk][2])+' calorias amarillas')
            print(str(core[usr_msk][3])+' calorias verdes')
        print('')
        np.save('core.npy',core)
        
        if str(today)+'_'+user+'.csv' in arr:
            dfr = pd.read_csv(str(today)+'_'+user+'.csv',sep=",", header=None)
            full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(dfr[0][1:]).astype(float), np.array(dfr[1][1:]).astype(float), np.array(dfr[2][1:]).astype(float), np.array(dfr[3][1:]).astype(float), np.array(dfr[4][1:]).astype(float), np.array(dfr[5][1:]).astype(float), np.array(dfr[6][1:]).astype(float), np.array(dfr[7][1:]), np.array(dfr[8][1:]).astype(float), np.array(dfr[9][1:]), np.array(dfr[10][1:])
            top, top_red, top_yellow, top_green, red, yellow, green=full_top[-1], full_top_red[-1], full_top_yellow[-1], full_top_green[-1], full_red[-1], full_yellow[-1], full_green[-1]
            full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal=np.append(full_top,(core[0]-red-yellow-green)), np.append(full_top_red,(core[1]-red)), np.append(full_top_yellow,(core[2]-yellow)), np.append(full_top_green,(core[3]-green)), np.append(full_red,red), np.append(full_yellow,yellow), np.append(full_green,green), np.append(full_ingr,'-'), np.append(full_cal,0), np.append(full_color,'-'),np.append(full_meal,'-')
            
            dfw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
            dfw.to_csv(str(today)+'_'+user+'.csv',index=False)
        if str(today)+'_'+user+'.csv' not in arr:
            dfw = pd.DataFrame({'top': [core[0]], 'red_left': [core[1]], 'yellow_left': [core[2]], 'green_left': [core[3]], 'red': [0], 'yellow': [0], 'green': [0], 'ingredients':['-'], 'calories':[0], 'color':['-'], 'meal':['-']})
        dfw.to_csv(str(today)+'_'+user+'.csv',index=False)
        return(core,top,top_red,top_yellow,top_green,str(user))
    
    if 'core.npy' in arr and (user == 'add' or user == 'agg' or user == 'agr'):
        usr = add_user_name()
        usr = str(usr)
        print('Welcome to Dietly, '+usr+'! Benvenuto/a su Dietly, '+usr+'! Bienvenido/a en Dietly, '+usr+'!')
        print('')
        print('Which language would you prefer? "eng" for English, "ita" for Italian, or "esp" for Espanol')
        print('(You can change it later on by calling the "setup" function)')
        print('')
        print('Quale lingua preferisci? "eng" per inglese, "ita" per italiano, o "esp" per spagnolo')
        print('(La puoi cambiare in qualsiasi momento chiamando la funzione "setup")')
        print('')
        print('Cual idioma prefieres? "eng" para ingles, "ita" para italiano, o "esp" para espanol')
        print('(Lo puedes cambiar en cualquier momento llamando la funciòn "setup")')
        print('')
        lan = input('')
        print('')
        vv=0
        if lan != 'eng' and lan != 'ita' and lan != 'esp':
            while vv == 0:
                print('Sorry, could you repeat?')
                print('')
                print('Non ho capito, puoi ripetere?')
                print('')
                print('Lo siento, puedes repetir?')
                print('')
                lan = input('')
                if lan != 'eng' and lan != 'ita' and lan != 'esp':
                    vv=0
                else:
                    vv=1
            
        print('')
        if lan=='eng':
            print('What is the chosen daily calories intake?')
            top=input('')
            if top==str(''):
                top=1400.0
            else:
                top=float(top)
            print('')
            print('What is the percentage of red calories?')
            perc_red=input('')
            if perc_red==str(''):
                perc_red=25.0
            else:
                perc_red=float(perc_red)
            print('')
            print('What is the percentage of yellow calories?')
            perc_yellow=input('')
            if perc_yellow==str(''):
                perc_yellow=35.0
            else:
                perc_yellow=float(perc_yellow)
            print('')
        if lan=='ita':
            print('Qual è il tuo fabbisogno calorico giornaliero (in Kcal)?')
            top=input('')
            if top==str(''):
                top=1400.0
            else:
                top=float(top)
            print('')
            print('Qual è la percentuale di calorie rosse?')
            perc_red=input('')
            if perc_red==str(''):
                perc_red=25.0
            else:
                perc_red=float(perc_red)
            print('')
            print('Qual è la percentuale di calorie gialle?')
            perc_yellow=input('')
            if perc_yellow==str(''):
                perc_yellow=35.0
            else:
                perc_yellow=float(perc_yellow)
            print('')
        if lan=='esp':
            print('Cuantas calorias necesitas cada dia (in Kcal)?')
            top=input('')
            if top==str(''):
                top=1400.0
            else:
                top=float(top)
            print('')
            print('Cual es la percentual de calorias rojas?')
            perc_red=input('')
            print('')
            if perc_red==str(''):
                perc_red=25.0
            else:
                perc_red=float(perc_red)
            print('Cual es la percentual de calorias amarillas?')
            perc_yellow=input('')
            print('')
            if perc_yellow==str(''):
                perc_yellow=35.0
            else:
                perc_yellow=float(perc_yellow)
            print('')
        
        top_red = top*perc_red/100
        top_yellow = top*perc_yellow/100
        top_green= top-top_yellow-top_red
        core= np.append(core,[top,top_red,top_yellow,top_green,str(lan),usr])
        usr_msk = (core['user'] == usr)
        if core[usr_msk][4]=='eng':
            print('This is your new setup:')
            print(str(core[usr_msk][0])+' total calories per day')
            print(str(core[usr_msk][1])+' red calories')
            print(str(core[usr_msk][2])+' yellow calories')
            print(str(core[usr_msk][3])+' green calories')
        if core[usr_msk][4]=='ita':
            print('Queste sono le nuove impostazioni:')
            print(str(core[usr_msk][0])+' calorie giornaliere totali')
            print(str(core[usr_msk][1])+' calorie rosse')
            print(str(core[usr_msk][2])+' calorie gialle')
            print(str(core[usr_msk][3])+' calorie verdi')
        if core[usr_msk][4]=='esp':
            print('Esta es la nueva configuracion:')
            print(str(core[usr_msk][0])+' calorias totales cada dia')
            print(str(core[usr_msk][1])+' calorias rojas')
            print(str(core[usr_msk][2])+' calorias amarillas')
            print(str(core[usr_msk][3])+' calorias verdes')
        print('')
        np.save('core.npy',core)
        
        if str(today)+'_'+usr+'.csv' in arr:
            dfr = pd.read_csv(str(today)+'_'+usr+'.csv',sep=",", header=None)
            full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(dfr[0][1:]).astype(float), np.array(dfr[1][1:]).astype(float), np.array(dfr[2][1:]).astype(float), np.array(dfr[3][1:]).astype(float), np.array(dfr[4][1:]).astype(float), np.array(dfr[5][1:]).astype(float), np.array(dfr[6][1:]).astype(float), np.array(dfr[7][1:]), np.array(dfr[8][1:]).astype(float), np.array(dfr[9][1:]), np.array(dfr[10][1:])
            top, top_red, top_yellow, top_green, red, yellow, green=full_top[-1], full_top_red[-1], full_top_yellow[-1], full_top_green[-1], full_red[-1], full_yellow[-1], full_green[-1]
            full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal=np.append(full_top,(core[0]-red-yellow-green)), np.append(full_top_red,(core[1]-red)), np.append(full_top_yellow,(core[2]-yellow)), np.append(full_top_green,(core[3]-green)), np.append(full_red,red), np.append(full_yellow,yellow), np.append(full_green,green), np.append(full_ingr,'-'), np.append(full_cal,0), np.append(full_color,'-'),np.append(full_meal,'-')
            
            dfw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
            dfw.to_csv(str(today)+'_'+usr+'.csv',index=False)
        if str(today)+'_'+usr+'.csv' not in arr:
            dfw = pd.DataFrame({'top': [core[0]], 'red_left': [core[1]], 'yellow_left': [core[2]], 'green_left': [core[3]], 'red': [0], 'yellow': [0], 'green': [0], 'ingredients':['-'], 'calories':[0], 'color':['-'], 'meal':['-']})
        dfw.to_csv(str(today)+'_'+usr+'.csv',index=False)
        return(core,top,top_red,top_yellow,top_green,str(usr))




#per sapere quante calorie sono rimaste 
def left(tot,tot_red,tot_yellow,Red,Yellow,Green,lan):
    if lan=='eng':
        print('You have '+str(tot)+' Kcal left today. Of which:')
        print('')
        print(str(tot_red)+' RED')
        print(str(tot_yellow)+' YELLOW')
    if lan=='ita':
        print('Ti rimangono '+str(tot)+' Kcal, oggi. Di cui:')
        print('')
        print(str(tot_red)+' ROSSE')
        print(str(tot_yellow)+' GIALLE')
    if lan=='esp':
        print('Te quedan '+str(tot)+' Kcal, hoy. De esas:')
        print('')
        print(str(tot_red)+' ROJAS')
        print(str(tot_yellow)+' AMARILLAS')
    print('')
    return()



#plotting function

def plot(core,days,weight,user):
    usr_msk = (core['user'] == user)
    usr_days_msk = (days['user'] == user)
    usr_weight_msk = (weight['user'] == user)
    if len(days[usr_days_msk])>1:
        l=min(6,len(days[usr_days_msk]))
        ll=-np.arange(1,l)
        loss=[]
        for i in ll:
            loss.append(float(weight[usr_weight_msk][i])-float(weight[usr_weight_msk][i-1]))
        avg_loss=np.mean(loss)
    if len(days[usr_days_msk])<2:
        avg_loss=0
    
    fig1 = plt.figure(figsize=(9,8))
    gs = fig1.add_gridspec(1,1)
    ax1= fig1.add_subplot(gs[0,0])
    if core[usr_msk][4]=='eng':
        ax1.set_ylabel(r"$Weight\,(kg)$", fontsize=18)
        ax1.set_xlabel(r"$Day$", fontsize=18)
    if core[usr_msk][4]=='ita':
        ax1.set_ylabel(r"$Peso\,(kg)$", fontsize=18)
        ax1.set_xlabel(r"$Data$", fontsize=18)
    if core[usr_msk][4]=='esp':
        ax1.set_ylabel(r"$Peso\,(kg)$", fontsize=18)
        ax1.set_xlabel(r"$Fecha$", fontsize=18)
    ax1.plot(days[usr_days_msk],weight[usr_weight_msk],linewidth=1,color='k')
    ax1.scatter(days[usr_days_msk],weight[usr_weight_msk],s=60,color='r')
    annotations=weight.astype(str)
    for h,label in enumerate(annotations):
        plt.annotate(label,(days[usr_days_msk],weight[usr_weight_msk]), fontsize=16, textcoords='data', xytext=(days[usr_days_msk],weight[usr_weight_msk]+0.2))
        plt.show()
    ax1.set_title(r"Average weekly loss: "+str(avg_loss)+r"$\,$Kg")
    ax1.set_xticks(ticks=days[usr_days_msk])
    ax1.set_xticklabels(labels=days[usr_days_msk],fontsize=10)
    plt.show(block=False)
    close= input('')
    plt.close('all')
    return()




#logging new weight
def nw(weight,days,core,today,user):
    usr_msk = (core['user'] == user)
    usr_days_msk = (days['user'] == user)
    usr_weight_msk = (weight['user'] == user)
    if today in days[usr_days_msk]:
        if core[usr_msk][4]=='eng':
            print('You already uploaded your weight today, do you want to modify it?')
        if core[usr_msk][4]=='ita':
            print('Hai già caricato il tuo peso oggi, lo vuoi modificare?')
        if core[usr_msk][4]=='esp':
            print('Ya cargaste tu peso hoy, quieres actualizarlo?')
        info=input('')
        info=check(info,core[usr_msk][4])
        print('')
        if info == 'y' or info == 'yes' or info == 'si' or info == 's' or info == 'yep' or info == 'eja':
            if core[usr_msk][4]=='eng':
                print('What is the new weight (in kg)?')
            if core[usr_msk][4]=='ita':
                print('Qual è la nuova pesata (in kg)?')
            if core[usr_msk][4]=='esp':
                print('Cual es el nuevo peso? (en kg)?')
            neweight=float(input(''))
            weight[usr_weight_msk][-1]=neweight
            np.save('weight.npy',weight)
            print('')
        
    
    if today not in days:
        if core[usr_msk][4]=='eng':
            print('Do you want to upload the new weight (in kg)?')
        if core[usr_msk][4]=='ita':
            print('Vuoi caricare la nuova pesata (in kg)?')
        if core[usr_msk][4]=='esp':
            print('Quieres cargar el nuevo peso? (en kg)')
        info=input('')
        info=check(info,core[usr_msk][4])
        print('')
        if info == 'y' or info == 'yes' or info == 'si' or info == 's' or info == 'yep' or info == 'eja':
            if core[usr_msk][4]=='eng':
                print('What is your weight (in kg) today?')
            if core[usr_msk][4]=='ita':
                print('Qual è il tuo peso (in kg) oggi?')
            if core[usr_msk][4]=='esp':
                print('Cual es tu peso (en kg) hoy?')
            print('')
            neweight=float(input(''))
            days=np.append(days,[user, today])
            weight=np.append(weight,[user, neweight])
            np.save('days.npy',days)
            np.save('weight.npy',weight)

    return(weight,days)
    


#workout part

def wo(top,top_red,top_yellow,top_green,red,yellow,green,core,today,user):
    usr_msk = (core['user'] == user)
    if core[usr_msk][4]=='eng':
        print('How many Kcal did you burn?')
    if core[usr_msk][4]=='ita':
        print('Quante Kcal hai bruciato?')
    if core[usr_msk][4]=='esp':
        print('Cuantas Kcal quemaste?')
    dd=0
    while dd==0:
        extracal=input('')
        try:
            extracal=float(extracal)
        except:
            if core[usr_msk][4] == 'eng':
                print('Sorry, could you repeat?')
            if core[usr_msk][4] == 'ita':
                print('Non ho capito, puoi ripetere?')
            if core[usr_msk][4] == 'esp':
                print('Lo siento, puedes repetir?')
            dd=0
        else:
            extracal=float(extracal)
            dd=1


    print('')
    extracal= int(extracal)/2
    if core[usr_msk][4]=='eng':
        print("Do you want to update today's info?")
    if core[usr_msk][4]=='ita':
        print('Vuoi aggiornare le informazioni di oggi?')
    if core[usr_msk][4]=='esp':
        print('Quieres actualizar las infociones de hoy?')
    info=input('')
    info=check(info,core[4])
    print('')
    if info == 'y' or info == 'yes' or info == 'si' or info == 's' or info == 'yep' or info == 'eja':
        top =top + extracal
        top_red=top_red+np.floor(extracal*0.25)
        top_yellow=top_yellow+np.floor(extracal*0.25)
        top_green=top-red-yellow-green
        dfr = pd.read_csv(str(today)+'_'+user+'.csv',sep=",", header=None)
        full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(dfr[0][1:]).astype(float), np.array(dfr[1][1:]).astype(float), np.array(dfr[2][1:]).astype(float), np.array(dfr[3][1:]).astype(float), np.array(dfr[4][1:]).astype(float), np.array(dfr[5][1:]).astype(float), np.array(dfr[6][1:]).astype(float), np.array(dfr[7][1:]), np.array(dfr[8][1:]).astype(float), np.array(dfr[9][1:]), np.array(dfr[10][1:])
        full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal=np.append(full_top,top), np.append(full_top_red,top_red), np.append(full_top_yellow,top_yellow), np.append(full_top_green,top_green), np.append(full_red,red), np.append(full_yellow,yellow), np.append(full_green,green), np.append(full_ingr,'-'), np.append(full_cal,0), np.append(full_color,'-'),np.append(full_meal,'-')
        
        dfw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
        dfw.to_csv(str(today)+'_'+user+'.csv',index=False)
    return(top,top_red,top_yellow,top_green)



#per controllare/aggiornare il database degli ingredienti

def database_update(lang):
    dfr_dtb = pd.read_csv('Database.csv',sep=",", header=None)
    fd_dtb, color_dtb, cal_dtb, density_dtb, units_dtb= np.array(dfr_dtb[0][1:]).astype(str), np.array(dfr_dtb[1][1:]).astype(str), np.array(dfr_dtb[2][1:]).astype(float), np.array(dfr_dtb[3][1:]).astype(float), np.array(dfr_dtb[4][1:]).astype(str)
    x=1
    while x==1:
        if lang=='eng':
            print('Which ingredient would you like to check?')
        if lang=='ita':
            print('Che ingrediente vorresti controllare?')
        if lang=='esp':
            print('Cual ingrediente querias verificar?')
        fd=input('')
        fd=str(fd)
        print('')
        if fd in fd_dtb:
            fd_msk= fd_dtb==fd
            if lang=='eng':
                print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' '+str(color_dtb[fd_msk][0])+' Kcal every '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0]))
                print('')
                print('Would you like to check another ingredient?')
            if lang=='ita':
                print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' '+str(color_dtb[fd_msk][0])+' Kcal ogni '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0]))
                print('')
                print('Vorresti controllare un altro ingrediente?')
            if lang=='esp':
                print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' '+str(color_dtb[fd_msk][0])+' Kcal cada '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0]))
                print('')
                print('Querias verifcar otro ingrediente?')
            other=input('')
            other=check(other,lang)
            print('')
            if other == 'no' or other == 'n' or other == 'nop' or other == 'nope':
                x=0
            if other == 'y' or other == 'yes' or other == 'si' or other == 's' or other == 'yep' or other == 'eja':
                x=1
        else:
            if lang=='eng':
                print(fd+' is not in the database. Do you want to add it?')
            if lang=='ita':
                print(fd+' non è nel database. Lo vuoi aggiungere (in inglese)?')
            if lang=='esp':
                print(fd+' no està en el database. Quieres agregarlo (en ingles)?')
            add = input('')
            add=check(add,lang)
            print('')
            if add == 'y' or add == 'yes' or add == 'si' or add == 's' or add == 'yep' or add == 'eja':
                zz = 1
                while zz == 1:
                    if lang=='eng':
                        print('What color are these calories?')
                        col=input('')
                        print('')
                        print('What is the calory intake...')
                        cal=input('')
                        print('')
                        print('...for this amount...')
                        den=input('')
                        print('')
                        print('...in these units (g for "grams", unit for "units", tsp for "teaspoons", slice for "slices")?')
                        un=input('')
                    if lang=='ita':
                        print('Di che colore sono le calorie di questo cibo?')
                        col=input('')
                        print('')
                        print('Qual è la quantità di calorie...')
                        cal=input('')
                        print('')
                        print('...per questa quantità di cibo...')
                        den=input('')
                        print('')
                        print('...in queste unità (g per "grammi", unit per "unità", tsp per "cucchiaini", slice per "fette")?')
                        un=input('')
                    if lang=='esp':
                        print('Cual es el color de las calorias de este ingrediente?')
                        col=input('')
                        print('')
                        print('Cual es la cuantidad de calorias...')
                        cal=input('')
                        print('')
                        print('...para esta cuantidad del ingrediente...')
                        den=input('')
                        print('')
                        print('...en estas unitas (g para "grammos", unit para "unidades", tsp para "cuchariditas", slice para "rebanadas")?')
                        un=input('')
                    print('')
                    if lang=='eng':
                        print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' Kcal every '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0])+'. Is it correct?')
                    if lang=='ita':
                        print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' Kcal ogni '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0])+". E' corretto?")
                    if lang=='esp':
                        print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' Kcal cada '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0])+'. Es correcto?')
                    print('')
                    correct=input('')
                    correct=check(correct,lang)
                    if correct =='no' or correct == 'n' or correct == 'nop' or correct == 'nope':
                        zz = 1
                    if correct == 'y' or correct == 'yes' or correct == 'si' or correct == 's' or correct == 'yep' or correct == 'eja':
                        fd_dtb=np.append(fd_dtb,fd)
                        color_dtb=np.append(color_dtb,col)
                        cal_dtb=np.append(cal_dtb,cal)
                        density_dtb=np.append(density_dtb,den)
                        units_dtb=np.append(units_dtb,un)
                        ix= np.argsort(fd_dtb)
                        fd_dtb,color_dtb,cal_dtb,density_dtb,units_dtb=fd_dtb[ix],color_dtb[ix],cal_dtb[ix],density_dtb[ix],units_dtb[ix]
                        dfw_dtb = pd.DataFrame({'food': [fd_dtb], 'color': [color_dtb], 'calories': [cal_dtb], 'every': [density_dtb], 'units': [units_dtb]})
                        dfw_dtb.to_csv('Database.csv',index=False)
                        zz = 0
                if lang=='eng':
                    print('Would you like to check another ingredient?')
                if lang=='ita':
                    print('Vorresti controllare un altro ingrediente?')
                if lang=='esp':
                    print('Quieres comprobar otro ingrediente?')
                other=input('')
                other=check(other,lang)
                print('')
                if other == 'no' or other == 'n' or other == 'nop' or other == 'nope':
                    x=0
                if other == 'y' or other == 'yes' or other == 'si' or other == 's' or other == 'yep' or other == 'eja':
                    x=1

            if add == 'no' or add == 'n' or add == 'nop' or add == 'nope':
                if lang=='eng':
                    print('Would you like to check another ingredient?')
                if lang=='ita':
                    print('Vorresti controllare un altro ingrediente?')
                if lang=='esp':
                    print('Quieres comprobar otro ingrediente?')
                other=input('')
                other=check(other,lang)
                print('')
                if other == 'no' or other == 'n' or other == 'nop' or other == 'nope':
                    x=0
                if other == 'y' or other == 'yes' or other == 'si' or other == 's' or other == 'yep' or other == 'eja':
                    x=1
    return()
    





#per accedere/aggiornare il database da dentro "meals"

def database_search(lang,dtb):
    fd_dtb, color_dtb, cal_dtb, density_dtb, units_dtb= np.array(dtb[0][1:]).astype(str), np.array(dtb[1][1:]).astype(str), np.array(dtb[2][1:]).astype(float), np.array(dtb[3][1:]).astype(float), np.array(dtb[4][1:]).astype(str)
    if lang=='eng':
        print('Which ingredient would you like to add?')
    if lang=='ita':
        print('Che ingrediente vorresti aggiungere?')
    if lang=='esp':
        print('Cual ingrediente querias agregar?')
    fd=input('')
    fd=str(fd)
    print('')
    if fd in fd_dtb:
        fd_msk= fd_dtb==fd
        if lang=='eng':
            print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' '+str(color_dtb[fd_msk][0])+' Kcal every '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0]))
        if lang=='ita':
            print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' '+str(color_dtb[fd_msk][0])+' Kcal ogni '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0]))
        if lang=='esp':
            print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' '+str(color_dtb[fd_msk][0])+' Kcal cada '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0]))
        print('')
        return(fd)
    else:
        """
        maybe add a spelling check here
        """
        if lang=='eng':
            print(fd+' is not in the database. Add it')
        if lang=='ita':
            print(fd+' non è nel database. Aggiungilo (in inglese)?')
        if lang=='esp':
            print(fd+' no està en el database. Agregalo (en ingles)?')
        print('')
        zz = 1
        while zz == 1:
            if lang=='eng':
                print('What color are these calories?')
                col=input('')
                print('')
                print('What is the calory intake...')
                cal=input('')
                print('')
                print('...for this amount...')
                den=input('')
                print('')
                print('...in these units (g for "grams", unit for "units", tsp for "teaspoons", slice for "slices")?')
                un=input('')
            if lang=='ita':
                print('Di che colore sono le calorie di questo cibo?')
                col=input('')
                print('')
                print('Qual è la quantità di calorie...')
                cal=input('')
                print('')
                print('...per questa quantità di cibo...')
                den=input('')
                print('')
                print('...in queste unità (g per "grammi", unit per "unità", tsp per "cucchiaini", slice per "fette")?')
                un=input('')
            if lang=='esp':
                print('Cual es el color de las calorias de este ingrediente?')
                col=input('')
                print('')
                print('Cual es la cuantidad de calorias...')
                cal=input('')
                print('')
                print('...para esta cuantidad del ingrediente...')
                den=input('')
                print('')
                print('...en estas unitas (g para "grammos", unit para "unidades", tsp para "cuchariditas", slice para "rebanadas")?')
                un=input('')
            print('')
            if lang=='eng':
                print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' Kcal every '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0])+'. Is it correct?')
            if lang=='ita':
                print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' Kcal ogni '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0])+". E' corretto?")
            if lang=='esp':
                print(str(fd_dtb[fd_msk][0])+': '+str(cal_dtb[fd_msk][0])+' Kcal cada '+ str(density_dtb[fd_msk][0]) +' '+ str(units_dtb[fd_msk][0])+'. Es correcto?')
            print('')
            correct=input('')
            correct=check(correct,lang)
            if correct =='no' or correct == 'n' or correct == 'nop' or correct == 'nope':
                zz = 1
            if correct == 'y' or correct == 'yes' or correct == 'si' or correct == 's' or correct == 'yep' or correct == 'eja':
                fd_dtb=np.append(fd_dtb,fd)
                color_dtb=np.append(color_dtb,col)
                cal_dtb=np.append(cal_dtb,cal)
                density_dtb=np.append(density_dtb,den)
                units_dtb=np.append(units_dtb,un)
                ix= np.argsort(fd_dtb)
                fd_dtb,color_dtb,cal_dtb,density_dtb,units_dtb=fd_dtb[ix],color_dtb[ix],cal_dtb[ix],density_dtb[ix],units_dtb[ix]
                dfw_dtb = pd.DataFrame({'food': [fd_dtb], 'color': [color_dtb], 'calories': [cal_dtb], 'every': [density_dtb], 'units': [units_dtb]})
                dfw_dtb.to_csv('Database.csv',index=False)
                zz = 0
        return(fd)







#logging the meals
def meals(top,top_red,top_yellow,top_green,red,yellow,green,core,today,user):
    usr_msk = (core['user'] == user)
    left(top,top_red,top_yellow,red,yellow,green,core[usr_msk][4])
    dfr_dtb = pd.read_csv('Database.csv',sep=",", header=None)
    fd_dtb = np.array(dfr_dtb[0][1:]).astype(str)

    x = 1
    while x == 1:
        fd = database_search(core[usr_msk][4],dfr_dtb)
        dfr_dtb = pd.read_csv('Database.csv',sep=",", header=None)
        fd_dtb, color_dtb, cal_dtb, density_dtb, units_dtb= np.array(dfr_dtb[0][1:]).astype(str), np.array(dfr_dtb[1][1:]).astype(str), np.array(dfr_dtb[2][1:]).astype(float), np.array(dfr_dtb[3][1:]).astype(float), np.array(dfr_dtb[4][1:]).astype(str)
        
        if core[usr_msk][4]=='eng':
            print('How much/many of this ingredient?')
        if core[usr_msk][4]=='ita':
            print('Inserire la quantità')
        if core[usr_msk][4]=='esp':
            print('Insertar la cantidad')
        qnt = float(input(''))
        print('')
        if core[usr_msk][4]=='eng':
            print("Which meal is it? ('b' for Breakfast, 'l' for Lunch, 'd' for Dinner, 's' for Snack)")
        if core[usr_msk][4]=='ita':
            print("Che pasto è? ('co' per COlazione, 'p' per Pranzo, 'ce' per CEna, 's' per Snack)")
        if core[usr_msk][4]=='esp':
            print("Que comida es? ('de' para DEsayuno, 'a' para Almuerzo, 'c' para Cena, 's' para Snack)")
        ml = input('')
        if ml== 'co' or ml== 'de': ml = 'b'
        if ml== 'p' or ml== 'a': ml = 'l'
        if ml== 'ce' or ml== 'c': ml = 'd'
        print('')

        fd_msk= fd_dtb==fd
        if color_dtb[fd_msk][0] == 'red':
            par_red_cal = cal_dtb[fd_msk][0]*qnt/density_dtb[fd_msk][0]
            temp_top = top-par_red_cal
            temp_red = top_red-par_red_cal
            if temp_top< (top_yellow+top_green):
                temp_yellow = temp_top-top_green
            else: temp_yellow = top_yellow
                #temp_yellow = min(top_yellow,(top_yellow+temp_red))
            temp_green = top-red-yellow-green-par_red_cal
            
            if core[usr_msk][4]=='eng':
                print(str(par_red_cal)+' '+str(color_dtb[fd_msk][0])+' Kcal')
                print('You would still have '+str(temp_red)+' red Kcal, '+str(temp_yellow)+' yellow Kcal, and '+str(temp_green)+' green Kcal left, for a total of ', str(temp_top)+' Kcal')
                print('')
                print('Would you like to log this food?')
            if core[usr_msk][4]=='ita':
                print(str(par_red_cal)+' Kcal rosse')
                print('Avresti ancora '+str(temp_red)+' Kcal rosse, '+str(temp_yellow)+' Kcal gialle, e '+str(temp_green)+' Kcal verdi rimaste, per un totale di ', str(temp_top)+' Kcal')
                print('')
                print('Vuoi loggare questo cibo?')
            if core[usr_msk][4]=='esp':
                print(str(par_red_cal)+' Kcal rojas')
                print('Dejarian todavia '+str(temp_red)+' Kcal rojas, '+str(temp_yellow)+' Kcal amarillas, y '+str(temp_green)+' Kcal vierdes, para un total de ', str(temp_top)+' Kcal')
                print('')
                print('Quieres salvar este ingrediente?')
            
            log = input('')
            log=check(log,core[usr_msk][4])
            print('')
            if log == 'y' or log == 'yes' or log == 'si' or log == 's' or log == 'yep' or log == 'eja':
                top,top_red,top_yellow,top_green,red=temp_top,temp_red,temp_yellow,temp_green,red+par_red_cal
                dfr = pd.read_csv(str(today)+'_'+user+'.csv',sep=",", header=None)
                full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(dfr[0][1:]).astype(float), np.array(dfr[1][1:]).astype(float), np.array(dfr[2][1:]).astype(float), np.array(dfr[3][1:]).astype(float), np.array(dfr[4][1:]).astype(float), np.array(dfr[5][1:]).astype(float), np.array(dfr[6][1:]).astype(float), np.array(dfr[7][1:]), np.array(dfr[8][1:]).astype(float), np.array(dfr[9][1:]), np.array(dfr[10][1:])
                full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal=np.append(full_top,top), np.append(full_top_red,top_red), np.append(full_top_yellow,top_yellow), np.append(full_top_green,top_green), np.append(full_red,red), np.append(full_yellow,yellow), np.append(full_green,green), np.append(full_ingr,str(fd)), np.append(full_cal,par_red_cal), np.append(full_color,str(color_dtb[fd_msk][0])),np.append(full_meal,str(ml))
                dfw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
                dfw.to_csv(str(today)+'_'+user+'.csv',index=False)
            if log == 'no' or log == 'n' or log == 'nop' or log == 'nope':
                print('')


        if color_dtb[fd_msk][0] == 'yellow':
            par_yellow_cal = cal_dtb[fd_msk][0]*qnt/density_dtb[fd_msk][0]
            temp_top = top-par_yellow_cal
            temp_yellow = top_yellow-par_yellow_cal
            if temp_top< (top_red+top_green):
                temp_red = temp_top-top_green
            else: temp_red = top_red
                #temp_red = min(top_red,(top_red+temp_yellow))
            temp_green = top-red-yellow-green-par_yellow_cal
            if core[usr_msk][4]=='eng':
                print(str(par_yellow_cal)+' '+str(color_dtb[fd_msk][0])+' Kcal')
                print('You would still have '+str(temp_red)+' red Kcal, '+str(temp_yellow)+' yellow Kcal, and '+str(temp_green)+' green Kcal left, for a total of ', str(temp_top)+' Kcal')
                print('')
                print('Would you like to log this food?')
            if core[usr_msk][4]=='ita':
                print(str(par_yellow_cal)+' Kcal gialle')
                print('Avresti ancora '+str(temp_red)+' Kcal rosse, '+str(temp_yellow)+' Kcal gialle, e '+str(temp_green)+' Kcal verdi rimaste, per un totale di ', str(temp_top)+' Kcal')
                print('')
                print('Vuoi loggare questo cibo?')
            if core[usr_msk][4]=='esp':
                print(str(par_yellow_cal)+' Kcal amarillas')
                print('Dejarian todavia '+str(temp_red)+' Kcal rojas, '+str(temp_yellow)+' Kcal amarillas, y '+str(temp_green)+' Kcal vierdes, para un total de ', str(temp_top)+' Kcal')
                print('')
                print('Quieres salvar este ingrediente?')
            
            log = input('')
            log=check(log,core[usr_msk][4])
            print('')
            if log == 'y' or log == 'yes' or log == 'si' or log == 's' or log == 'yep' or log == 'eja':
                top,top_red,top_yellow,top_green,yellow=temp_top,temp_red,temp_yellow,temp_green,yellow+par_yellow_cal
                dfr = pd.read_csv(str(today)+'_'+user+'.csv',sep=",", header=None)
                full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(dfr[0][1:]).astype(float), np.array(dfr[1][1:]).astype(float), np.array(dfr[2][1:]).astype(float), np.array(dfr[3][1:]).astype(float), np.array(dfr[4][1:]).astype(float), np.array(dfr[5][1:]).astype(float), np.array(dfr[6][1:]).astype(float), np.array(dfr[7][1:]), np.array(dfr[8][1:]).astype(float), np.array(dfr[9][1:]), np.array(dfr[10][1:])
                full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal=np.append(full_top,top), np.append(full_top_red,top_red), np.append(full_top_yellow,top_yellow), np.append(full_top_green,top_green), np.append(full_red,red), np.append(full_yellow,yellow), np.append(full_green,green), np.append(full_ingr,str(fd)), np.append(full_cal,par_yellow_cal), np.append(full_color,str(color_dtb[fd_msk][0])),np.append(full_meal,str(ml))
                dfw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
                dfw.to_csv(str(today)+'_'+user+'.csv',index=False)
            if log == 'no' or log == 'n' or log == 'nop' or log == 'nope':
                print('')
        
            
        if color_dtb[fd_msk] == 'green':
            par_green_cal = cal_dtb[fd_msk][0]*qnt/density_dtb[fd_msk][0]
            temp_top = top-par_green_cal
            temp_green = temp_top-yellow-red-green
            if temp_top< (top_yellow+top_red):
                temp_red = temp_top-top_green
            else: temp_red = top_red
            #temp_red = min(top_red,(top_red+temp_green))
            if temp_top< (top_yellow) and temp_green>=0:
                temp_yellow = temp_top-temp_green
            if temp_top< (top_yellow) and temp_green<0:
                temp_yellow = temp_top
            else: temp_yellow = top_yellow
            temp_yellow = min(top_yellow,(temp_yellow+temp_red))
            if core[usr_msk][4]=='eng':
                print(str(par_green_cal)+' '+str(color_dtb[fd_msk][0])+' Kcal')
                print('You would still have '+str(temp_red)+' red Kcal, '+str(temp_yellow)+' yellow Kcal, and '+str(temp_green)+' green Kcal left, for a total of ', str(temp_top)+' Kcal')
                print('')
                print('Would you like to log this food?')
            if core[usr_msk][4]=='ita':
                print(str(par_green_cal)+' Kcal verdi')
                print('Avresti ancora '+str(temp_red)+' Kcal rosse, '+str(temp_yellow)+' Kcal gialle, e '+str(temp_green)+' Kcal verdi rimaste, per un totale di ', str(temp_top)+' Kcal')
                print('')
                print('Vuoi loggare questo cibo?')
            if core[usr_msk][4]=='esp':
                print(str(par_yellow_cal)+' Kcal vierdes')
                print('Dejarian todavia '+str(temp_red)+' Kcal rojas, '+str(temp_yellow)+' Kcal amarillas, y '+str(temp_green)+' Kcal vierdes, para un total de ', str(temp_top)+' Kcal')
                print('')
                print('Quieres salvar este ingrediente?')
            log = input('')
            log=check(log,core[usr_msk][4])
            print('')
            if log == 'y' or log == 'yes' or log == 'si' or log == 's' or log == 'yep' or log == 'eja':
                top,top_red,top_yellow,top_green,green=temp_top,temp_red,temp_yellow,temp_green,green+par_green_cal
                dfr = pd.read_csv(str(today)+'_'+user+'.csv',sep=",", header=None)
                full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal= np.array(dfr[0][1:]).astype(float), np.array(dfr[1][1:]).astype(float), np.array(dfr[2][1:]).astype(float), np.array(dfr[3][1:]).astype(float), np.array(dfr[4][1:]).astype(float), np.array(dfr[5][1:]).astype(float), np.array(dfr[6][1:]).astype(float), np.array(dfr[7][1:]), np.array(dfr[8][1:]).astype(float), np.array(dfr[9][1:]), np.array(dfr[10][1:])
                full_top, full_top_red, full_top_yellow, full_top_green, full_red, full_yellow, full_green, full_ingr, full_cal, full_color, full_meal=np.append(full_top,top), np.append(full_top_red,top_red), np.append(full_top_yellow,top_yellow), np.append(full_top_green,top_green), np.append(full_red,red), np.append(full_yellow,yellow), np.append(full_green,green), np.append(full_ingr,str(fd)), np.append(full_cal,par_green_cal), np.append(full_color,str(color_dtb[fd_msk][0])),np.append(full_meal,str(ml))
                dfw = pd.DataFrame({'top': [full_top], 'red_left': [full_top_red], 'yellow_left': [full_top_yellow], 'green_left': [full_top_green], 'red': [full_red], 'yellow': [full_yellow], 'green': [full_green], 'ingredients':[full_ingr], 'calories':[full_cal], 'color':[full_color], 'meal':[full_meal]})
                dfw.to_csv(str(today)+'_'+user+'.csv',index=False)
                print('')
            if log == 'no' or log == 'n' or log == 'nop' or log == 'nope':
                print('')
                
        if core[usr_msk][4]=='eng':
            print('Would you like to log other food?')
        if core[usr_msk][4]=='ita':
            print('Vorresti aggiungere altro cibo?')
        if core[usr_msk][4]=='eng':
            print('Quieres agregar otros ingredientes?')
        other=input('')
        other=check(other,core[usr_msk][4])
        print('')
        if other  == 'y' or other == 'yes' or other == 'si' or other == 's' or other == 'yep' or other == 'eja':
            x=1
        if other == 'no' or other == 'n' or other == 'nop' or other == 'nope':
            x=0
    
    left(temp_top,temp_red,temp_yellow,red,yellow,green,core[usr_msk][4])
    return(top,top_red,top_yellow,top_green,red,yellow,green)








