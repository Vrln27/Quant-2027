rendement =[0.02,-0.01,0.03,-0.02,0.0015,0.01,-0.005]

def analyse_rendement(rendement):
    moyenne = sum(rendement)/len(rendement)
    pire_rendement = min (rendement)
    nombre_jours_positifs = sum(1 for i in rendement if i>0)

    print(f"le rendement moyen est de :{moyenne*100:.2f}%")
    print(f"le pire rendement est de :{pire_rendement*100:.2f}%")
    print(f"le nombre de jours positifs est de :{nombre_jours_positifs}")

    return moyenne, pire_rendement, nombre_jours_positifs


analyse_rendement(rendement)



