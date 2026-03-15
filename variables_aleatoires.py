import numpy as np 

# donnees du probleme 

rendement = np.array([0.04,0.00,-0.02])
probabilite_A = np.array([0.4,0.4,0.20])
probabilite_B = np.array([0.2,0.3,0.5])

# rendement et B  
rendement_A = rendement * probabilite_A
rendement_B = rendement * probabilite_B

# esperance A
esperance_a = np.sum(rendement*probabilite_A)

# esperance B
esperance_b = np.sum(rendement*probabilite_B)

# volatilite 
volatilite_a = np.sum(probabilite_A*(rendement-esperance_a)**2)
volatilite_b = np.sum(probabilite_B*(rendement-esperance_b)**2)


#ecart type
ecart_type_a = np.sqrt(volatilite_a)
ecart_type_b = np.sqrt(volatilite_b)


# affichage 

print ( " quelle action choisir ? " )
print (f"A : rendement : {esperance_a*100:.2f}%, volatilite : {ecart_type_a*100:.2f}%")
print (f"B : rendement : {esperance_b*100:.2f}%, volatilite : {ecart_type_b*100:.2f}%")




