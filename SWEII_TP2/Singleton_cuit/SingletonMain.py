from SingletonPersonal import SingletonPersonal
from SingletonVideoDigital import SingletonVideoDigital

personal1 = SingletonPersonal()
personal2 = SingletonPersonal()

videodigital1 = SingletonVideoDigital()
videodigital2 = SingletonVideoDigital()

print('Singleton Personal:')
print(personal1 is personal2)

print('Singleton Video Digital:')
print(videodigital1 is videodigital1) # Si devuelven true, es porque ambas variables son de la misma instancia

print('La empresa ' + personal1.getid() + ' tiene cuit: ' + personal1.getCuit())
print('La empresa ' + videodigital1.getid() + ' tiene cuit: ' + videodigital1.getCuit())