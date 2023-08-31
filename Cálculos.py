from Ecuaciones import *

# Materiales
fc = 21
fy = 420
b = 100
h = 30
fiv = 0.75
pmin =  0.0012

# Datos iniciales Parrilla sup
rs = 5
ds = h-rs
Mnx = 3500
Mny = 3700
Nbsx = 2
Nbsy = 3

# Datos iniciales Parrilla inf
ri = 7.5
di = h-ri
Mpx = 3500
Mpy = 3700
Nbix = 4
Nbiy = 5

# Datos iniciales diseño cortante simple
r = max(rs, ri)
d = h-r
Vux = 115
Vuy = 95

# Acero minimo
Asmin = f_Asmin(pmin, b, h); print("Asmin = %.2f" %Asmin)

#Parrilla superior dir x - Diseño
print(''); print('Parilla superior dir x')
pcalsx = f_pcal(fc, fy, Mnx, b, ds);        print(" pcal  = %.4f" %pcalsx)
Ascalsx = f_Ascal(pcalsx, b, ds);           print(" Ascal = %.2f" %Ascalsx)
Asreqsx = f_Asreq(Ascalsx, Asmin);          print(" Asreq = %.2f" %Asreqsx)
Asbsx = f_Asb(Nbsx);                        print(" Asb   = %.2f" %Asbsx)
Sepsx = f_sep(Asreqsx, Asbsx, b);           print(" Sep   = %.2f" %Sepsx)
dbpsx = f_dbp(Nbsx);                        print(' db en pulg', dbpsx)
Dissx = f_dist(Asreqsx, Asbsx, b, dbpsx);   print(' Ref   = ', Dissx)
Ascolsx = f_Ascol(Asreqsx, Asbsx);          print(" Ascol = %.2f" %Ascolsx)
Mnsx = f_Mn(fc, fy, Ascolsx, b, ds);        print(" Mn    = %.1f" %Mnsx)
ChMnsx = f_ChMn(Mnx,Mnsx);                  print(' Chequeo Mn =', ChMnsx)

#Parrilla superior dir y - Diseño
print(''); print('Parilla superior dir y')
pcalsy = f_pcal(fc, fy, Mny, b, ds);        print(" pcal  = %.4f" %pcalsy)
Ascalsy = f_Ascal(pcalsy, b, ds);           print(" Ascal = %.2f" %Ascalsy)
Asreqsy = f_Asreq(Ascalsy, Asmin);          print(" Asreq = %.2f" %Asreqsy)
Asbsy = f_Asb(Nbsy);                        print(" Asb   = %.2f" %Asbsy)
Sepsy = f_sep(Asreqsy, Asbsy, b);           print(" Sep   = %.2f" %Sepsy)
dbpsy = f_dbp(Nbsy);                        print(' db en pulg', dbpsy)

Dissy = f_dist(Asreqsy, Asbsx, b, dbpsy);    print(' Ref   = ', Dissy)
Ascolsy = f_Ascol(Asreqsy, Asbsy);          print(" Ascol = %.2f" %Ascolsy)
Mnsy = f_Mn(fc, fy, Ascolsy, b, ds);        print(" Mn    = %.1f" %Mnsy)
ChMnsy = f_ChMn(Mny,Mnsy);                  print(' Chequeo Mn = ', ChMnsy)

#Parrilla inferior dir x - Diseño
print(''); print('Parilla inferior dir x')
pcalix = f_pcal(fc, fy, Mpx, b, di);        print(" pcal  = %.4f" %pcalix)
Ascalix = f_Ascal(pcalix, b, di);           print(" Ascal = %.2f" %Ascalix)
Asreqix = f_Asreq(Ascalix, Asmin);          print(" Asreq = %.2f" %Asreqix)
Asbix = f_Asb(Nbix);                        print(" Asb   = %.2f" %Asbix)
Sepix = f_sep(Asreqix, Asbix, b);           print(" Sep   = %.2f" %Sepix)
dbpix = f_dbp(Nbix);                        print(' db en pulg', dbpix)

Disix = f_dist(Asreqix, Asbix, b, dbpix);    print(' Ref   = ', Disix)
Ascolix = f_Ascol(Asreqix, Asbix);          print(" Ascol = %.2f" %Ascolix)
Mnix = f_Mn(fc, fy, Ascolix, b, di);        print(" Mn    = %.1f" %Mnix)
ChMnix = f_ChMn(Mpx,Mnix);                  print(' Chequeo Mn = ', ChMnix)

#Parrilla inferior dir y - Diseño
print(''); print('Parilla inferior dir y')
pcaliy = f_pcal(fc, fy, Mpy, b, di);        print(" pcal  = %.4f" %pcaliy)
Ascaliy = f_Ascal(pcaliy, b, di);           print(" Ascal = %.2f" %Ascaliy)
Asreqiy = f_Asreq(Ascaliy, Asmin);          print(" Asreq = %.2f" %Asreqiy)
Asbiy = f_Asb(Nbiy);                        print(" Asb   = %.2f" %Asbiy)
Sepiy = f_sep(Asreqiy, Asbiy, b);           print(" Sep   = %.2f" %Sepiy)
dbpiy = f_dbp(Nbiy);                        print(' db en pulg', dbpiy)

Disiy = f_dist(Asreqiy, Asbiy, b, dbpiy);    print(' Ref   = ', Disiy)
Ascoliy = f_Ascol(Asreqiy, Asbiy);          print(" Ascol = %.2f" %Ascoliy)
Mniy = f_Mn(fc, fy, Ascoliy, b, di);        print(" Mn    = %.1f" %Mniy)
ChMniy = f_ChMn(Mpy,Mniy);                  print(' Chequeo Mn = ', ChMniy)

#Diseño a cortante
print(''); print('Diseño a cortante')
Vcx = f_Vc(fiv, fc, b, d);                  print(" Vcx = %.1f" %Vcx)
ChVcx = f_ChVc(Vux,Vcx);                   print(' Chequeo cortante = ', ChVcx)

Vcy = f_Vc(fiv, fc, b, d);                  print(" Vcy = %.1f" %Vcy)
ChVcy = f_ChVc(Vux,Vcy);                   print(' Chequeo cortante = ', ChVcy)