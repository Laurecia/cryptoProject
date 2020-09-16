
#!/usr/bin/env python3
import sys
from Crypto.Publickey import RSA
#generer la cle
key = RSA.generate(1024)
#exporter la cle dans d'autres variables
k = key.exportkey("PEM")
p = key.publickey().exportkey("PEM")
#ecrire les cles dansx des fichiers peem
with open ("private.PEM","w")as kf:
         kf.write(p.decode())
         kf.close()
with open ("public.PEM","w")as pf:
           pf.write(p.decode())
           pf.close()

#encrypter
if(len(sys.argv) > 2):
       fichier = sys.argv[1]
else :
       fichier = input("le fichier a crypter:");
fo = open(fichier,"rb")
text = fo.read()
d_encrypt = key.publickey().encrypt(text,32)
#ecriture du fichier a encrypter
fo = open(fichier + "crypt","wb")
fo.write(d_encrypt[0])
fo.close()
  
