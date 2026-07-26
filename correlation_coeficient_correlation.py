import numpy as np 
# données 

x = np.array ([4, -2, 1, -1, 3])
y = np.array ([3, -1, 2, -2, 1])

# calculs des moyennes 
e_x = np.mean(x)
e_y = np.mean(y)

#calculs de la correlation et du coefficient de correlation
cov_xy = np.cov(x,y,bias=True)[0,1]
corr_xy = np.corrcoef(x,y)[0,1]

# Affichage des resultats 

print(f"la moyenne de X est : {e_x} et celle de Y est : {e_y}")
print(f"la covariance des deux actifs est : {cov_xy} et leur coefficient de correlation est : {corr_xy :.2f}")