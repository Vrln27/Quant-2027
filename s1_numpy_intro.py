import numpy as np 

prix = np.array([100,102,99,105,103])

print ("prix :", prix)
print ("longueur de prix ;", len(prix))
print ("type :", type(prix))
print ("prix moyen :", np.mean(prix))
print ("prix max :", np.max(prix))
print ("prix min :", np.min(prix))
print("ecart type :", np.std(prix))

rendement = np.diff(prix) / prix [:-1]*100 

print ("rendement % :", rendement )
print ("rendement moyen % :", round(np.mean(rendement), 4))
print ("volatilite des rendement % : ", round(np.std(rendement), 4))
