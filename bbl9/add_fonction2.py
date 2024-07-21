import json,os,textwrap ,sqlite3
import datetime,time

current_link=os.getcwd()
image_path=f"{current_link}//files//images//milky-way-8153503_1280.jpg"
"""
connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
curseur = connexion.cursor()
curseur_baiboly = connexion.cursor()
curseur_fihirana1 = connexion.cursor()
curseur_trad = connexion.cursor()

curseur_baiboly.execute('SELECT * FROM Baiboly')
resultats_baiboly=curseur_baiboly.fetchall()
#print(len(resultats_baiboly))

curseur_fihirana1.execute('SELECT * FROM fihirana1')
resultats_fihirana1=curseur_fihirana1.fetchall()
#print(type(resultats_fihirana1[0]))

curseur_fihirana2.execute('SELECT * FROM fihirana2')
resultats_fihirana2=curseur_fihirana2.fetchall()
#print(len(resultats_fihirana2))

curseur_listfhr1.execute('SELECT * FROM list_fihirana1')
resultats_fihirana2=curseur_fihirana2.fetchall()
#print(len(resultats_fihirana2))

curseur_fihirana2.execute('SELECT * FROM list_fihirana2')
resultats_fihirana2=curseur_fihirana2.fetchall()
#print(len(resultats_fihirana2))


#for resultat_baiboly in resultats_baiboly:
#    print()



connexion.close()
"""

historique_dict=dict()
class fihirana_G():
    def fihirana1(fhr,ttr):
        fhi_=''
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur_fihirana1 = connexion.cursor()
        curseur_fihirana1.execute('SELECT * FROM fihirana1')
        resultats_fihirana1=curseur_fihirana1.fetchall()
        connexion.close()
#, encoding='utf-8'
        for resultat_fihirana1 in resultats_fihirana1:
            if (resultat_fihirana1[1])==fhr:
                donnees=resultat_fihirana1
                break
            else:
                pass
        
        try:
            fh=eval(donnees[2])
            fh_ord=donnees[3]
            fh_ord=str(fh_ord).split(", ")
            
            ttr=ttr
            fhi=[]
            for fh_ in fh_ord:
                fhi.append(''.join(fh[fh_]))
            fi='\n'.join(fhi)
            
            fhi_=  f"{ttr}\n\n {fi}" 
        except:pass
        
        return fhi

    def fihirana2(fhr,ttr):
        fhi_=''
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur_fihirana2 = connexion.cursor()
        curseur_fihirana2.execute('SELECT * FROM fihirana2')
        resultats_fihirana2=curseur_fihirana2.fetchall()
        connexion.close()
        for resultat_fihirana2 in resultats_fihirana2:
            if (resultat_fihirana2[1])==fhr:

                donnees=resultat_fihirana2
                break
            else:
                pass
        try:
            fh=eval(donnees[2])
            fh_ord=eval(donnees[3])
            #fh_ord=str(fh_ord).split(", ")
            ttr=ttr
            fhi=[]
            for fh_ in fh_ord:
                fhi.append(''.join(fh[fh_]))
            fi='\n'.join(fhi)
            fhi_=  f"{ttr}\n {fi}" 
        except:pass
        return fhi
 
    def fihirana_fanampiny(fhr,ttr):
        fhi_=''
        #if len(fhr)==1:    
        #    fhr=f"00{fhr}"    
        #elif len(fhr)==2:
        #    fhr=f"0{fhr}"
        #else:
        #    fhr=fhr
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur_fihirana2 = connexion.cursor()
        curseur_fihirana2.execute('SELECT * FROM fihirana_ajout')
        resultats_fihirana2=curseur_fihirana2.fetchall()
        connexion.close()
        donnees=resultats_fihirana2[int(fhr-1)]
        #print(donnees)
        #
        #for resultat_fihirana2 in resultats_fihirana2:
        #    if (resultat_fihirana2[1])==fhr:
        #        donnees=resultat_fihirana2
        #        break
        #    else:
        #        pass
        try:
            fh=eval(donnees[2])
            fh_ord=eval(donnees[3])
            #fh_ord=str(fh_ord).split(", ")
            ttr=ttr
            fhi=[]
            for fh_ in fh_ord:
                fhi.append(''.join(fh[fh_]))
            fi='\n\n'.join(fhi)
            fhi_=  f"{ttr}\n {fi}" 
        except:pass
        return fhi

    def fihirana_1_get_lohateny(inn):
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur_fihirana1 = connexion.cursor()
        curseur_fihirana1.execute('SELECT * FROM list_fihirana1')
        resultats_get_fihirana1=curseur_fihirana1.fetchall()
        connexion.close()
        for resultat_get_fihirana2 in resultats_get_fihirana1:
            if (resultat_get_fihirana2[1])==inn:
                tte=resultat_get_fihirana2
                break
            else:
                tte=['', '', '', '']
        return tte

    def fihirana_2_get_lohateny(self):
        pass

    def fihirana1_get(inn):
        tte=['', '', '', '','Vide']
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur_fihirana1 = connexion.cursor()
        curseur_fihirana1.execute('SELECT * FROM list_fihirana1')
        resultats_get_fihirana1=curseur_fihirana1.fetchall()
        connexion.close()
        try:
            for resultat_get_fihirana1 in resultats_get_fihirana1:
                if (resultat_get_fihirana1[1])==int(inn):
                    tte=resultat_get_fihirana1
                    break
        except:pass
        return tte

    def fihirana2_get(inn):
        tte=['', '', '', '','--']
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur_fihirana2 = connexion.cursor()
        curseur_fihirana2.execute('SELECT * FROM list_fihirana2')
        resultats_get_fihirana2=curseur_fihirana2.fetchall()
        connexion.close()
        try:
            for resultat_get_fihirana2 in resultats_get_fihirana2:

                if (resultat_get_fihirana2[1])==int(inn):
                    tte=resultat_get_fihirana2
                    break
                
        except:pass
        return tte

    def fihiranaf_get(titre):
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur.execute('SELECT * FROM list_fihirana_ajout')
        resultats_fihirana2=curseur.fetchall()
        connexion.close()
        titreSplit = titre.split(" ")
        print(titreSplit)
        if titre !="":
            #return [listtitre for listtitre in resultats_fihirana2 if titre.lower() in str(listtitre[4]).lower()]
            for resultat_fihirana2 in resultats_fihirana2:
                if str(resultat_fihirana2[4]).lower().startswith(titre.lower()):
                    #print(resultat_fihirana2[4],titre)
                    #resultSplit=resultat_fihirana2[4].split(' (')
                    #print(resultSplit[1])
        
                    
                    #print(resultat_fihirana2[0])
                    return resultat_fihirana2[4],resultat_fihirana2[0],resultat_fihirana2[2]
                # if resultat_fihirana2[4]!='':
                #     resultSplit=resultat_fihirana2[4].split(' (')
                #     print(resultSplit)
                #     if str(resultSplit[1]).lower().startswith(titre.lower()):
                #         return resultat_fihirana2[4],resultat_fihirana2[0],resultat_fihirana2[2]
'''     
    def fihirana1_nd_scren(fhr):
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
#, encoding='utf-8'
        with open((f"{chm_fihirana1}\\{fhr}.json"), "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        fh=donnees
        fh_ord=fh['ord']
        fhi=[]
        
        for fh_ in fh_ord:
            fi=''.join(fh[fh_])
            fhi.append(fi)
        return fhi
    
    def fihirana2_nd_scren(fhr):
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
#, encoding='utf-8'
        with open((f"{chm_fihirana2}\\{fhr}.json"), "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        fh=donnees
        fh_ord=fh['ord']
        fhi=[]
        
        for fh_ in fh_ord:
            fi=''.join(fh[fh_])
            fhi.append(fi)
        return fhi
'''
    

class baiboly_G():
    def trad(inn,lng):
        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur_trad = connexion.cursor()
        curseur_trad.execute('SELECT * FROM trad')
        resultats_trad=curseur_trad.fetchall()
        connexion.close()
        for resultat_trad in resultats_trad:
            #print(type(resultat_trad[1]))
            if str(resultat_trad[1])==str(inn):
                tte=resultat_trad
                break
            else:
                tte=['', '', '', '']
        
        return tte,tte[2]

    def baiboly(b):
        baiboly=b.split(' ')
        #print(baiboly[0])

        connexion = sqlite3.connect(f"{current_link}//files//db_out.sqlite3")
        curseur = connexion.cursor()
        curseur_baiboly = connexion.cursor()
        curseur_baiboly.execute('SELECT * FROM Baiboly')
        resultats_baiboly=curseur_baiboly.fetchall()
        connexion.close()

        
        #with open(f"{chm_baiboly}\\{baiboly_G.trad(baiboly[0],1)}.json", "r", encoding='utf-8') as fichier:
        #    donnees = json.load(fichier)
        baiboly_trad=baiboly_G.trad(baiboly[0],1)
        #print(baiboly_trad[1])
        for resultat_baiboly in resultats_baiboly:
            if (resultat_baiboly[1])==baiboly_trad[1]:
                donnees=resultat_baiboly
                break
            else:
                tte=['', '', '', '']
                
        bb_chpt_=eval(donnees[2])
        bb_chpt=bb_chpt_[f"Chapitre {baiboly[1]}"]
        bb_v=baiboly[3]
        bb_vr=bb_v.split(',')
        
        if len(bb_vr)==1:
            bb_vrs=bb_vr[0].split('-')
            #print(f"bb_vrs({bb_vrs})")
            if len(bb_vrs)==1:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs[0])-1])
                bbl2=''
                bbl3=''
            else:
                bbl1= ''.join(bb_chpt[int(bb_vrs[0])-1:int(bb_vrs[1])])
                bbl2=''
                bbl3=''
                #bbl=f'" {bbl_} "'

        elif len(bb_vr)==2:
            bb_vrs1=bb_vr[0].split('-')
            bb_vrs2=bb_vr[1].split('-')
            #print(f"bb_vrs({bb_vrs})")
            if len(bb_vrs1)==1 and len(bb_vrs2)==1:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
                bbl3=''
            elif len(bb_vrs1)==2 and len(bb_vrs2)==1:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
                bbl3=''
            elif len(bb_vrs1)==1 and len(bb_vrs2)==2:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
                bbl3=''
            elif len(bb_vrs1)==2 and len(bb_vrs2)==2:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
                bbl3=''
            
            else:
                bbl1=''
                bbl2=''
                bbl3=''

        return bbl1,bbl2

class export_files():
    def export_out_file(fl):
        with open(f"{current_link}\\files\\dependances\\scrn1_out.json", "w") as f:
            json.dump(fl,f,indent=4, ensure_ascii= False, sort_keys=False)

        pass

    def ajout_historique(fl,ntr):
        a=time.asctime()
        a=a.split(' ')
        filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
        #historique_dict[filtr]=fl
        with open(f"{current_link}\\files\\dependances\\Historique.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
            dt[filtr]=ntr,fl

        with open(f"{current_link}\\files\\dependances\\Historique.json", "w",encoding='utf-8') as f:
            json.dump(dt,f,indent=4, ensure_ascii= False, sort_keys=False)

        pass

    def sauvegarde_param():
        pass
'''
class Save_file():
    def __init__(self,out_fl,fl,ntr):
        self.export_out_file(out_fl)
        self.ajout_historique(fl,ntr)

    def export_out_file(self,out_fl):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        #print(out_fl['type'], out_fl['titre'], out_fl['content'], type(out_fl['ord_diff']))
        j_dt=json.dumps(out_fl)
        curseur.execute('INSERT OR REPLACE INTO scrn1_out(type, titre, content, ord_diff) VALUES (?, ?, ?, ?)', (out_fl['type'], out_fl['titre'], j_dt, out_fl['ord_diff']))
        connexion.commit()
        connexion.close()
    
    def ajout_historique(self,fl,ntr):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        a=time.asctime()
        a=a.split(' ')
        #filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
        #print(fl,ntr, filtr)
        curseur.execute('INSERT OR REPLACE INTO Historique(jour, date, heure, type, content) VALUES (?, ?, ?, ?, ?)', (a[0], a[2], a[3], ntr, fl))
        connexion.commit()
        connexion.close()


flii={'type': 'FIHIRANA', 'titre': ' MANGINA, MANGINA ', 'content': ["1\nMangina, mangina\nHenoy fa injao \n'Lay Tompo irina \nMiteny aminao \n", 'Henoy fa miteny \nAm-ponao izao \nMiteny, mifona \nFa tia anao \n', '2\nMangina, mangina \nFeo mamy tokoa \nMitory hafaliana \n‘Njao re ao am-po \n', 'Ekeko ry Tompo \nMangina aho izao \nMangina ny foko \nHihaino Anao \n'], 'ord_diff': 4}

#Save_file(flii,'','')
reqq='1Chroniques'
connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
curseur = connexion.cursor()
curseur.execute("SELECT Content_file FROM Baiboly WHERE Bible = ?",reqq)
result=curseur.fetchone()
'''
#print((result))
#result=result[0]
#result=str(result).split(', ')
#print(type(result))
#print(result)
#print(type(fl))
#Save_file('file','baiboly')

#f=fihirana_G.fihirana_fanampiny(1,"f")
#b=baiboly_G.baiboly("Genesisy 10 : 10,25")
#print((f))

# texte_modifie_1 = textwrap.fill("\n".join(mots), width=max_caracteres_par_ligne_1)

# print(texte_modifie_1)
# texte_modifie_1_= textwrap.wrap(texte_modifie_1,width=200)
# print(texte_modifie_1_)

# texte_modifie_2 =textwrap.wrap(phrases, width=int(bbl_cntt[1]))
# print(type(texte_modifie_2))