print('Program Menghitung Luas dan Keliling lingkaran')
print('===============================================')
r = float (input('masukan jari-jari : '))
pi = 3.14
diameter = 2 * r
luas = pi * r * r
keliling = pi * diameter
print('\nLuasnya =', str("%.2f" % luas))
print('Kelilingnya =', str("%.2f" % keliling))
