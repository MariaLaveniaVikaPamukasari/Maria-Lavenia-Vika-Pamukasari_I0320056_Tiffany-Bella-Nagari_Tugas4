# Menentukan beberapa keluaran dari operator bitwise

x = 4
y = 11
print('nilai :',x,'binary :',format(x,'08b'))
print('nilai :',y,'binary :',format(y,'08b'))

# bitwise OR
a = x | y
print('\nSoal a')
print('x | y')
print('--------OR--------')
print('nilai :',a,'binary :',format(a,'08b'))
# bitwise right shift
b = x >> y
print('\nSoal b')
print('x >> y')
print('--------(>>)--------')
print('nilai :',b,'binary :',format(b,'08b'))
# bitwise XOR
c = x ^ y
print('\nSoal c')
print('x ^ y')
print('--------(^)--------')
print('nilai :',c,'binary :',format(c,'08b'))
# bitwise NOT
d = ~x
print('\nSoal d')
print('~x')
print('--------(~)--------')
print('nilai :',d,'binary :',format(d,'08b'))
# bitwise AND
e = y & x
print('\nSoal e')
print('y & x')
print('--------(&)--------')
print('nilai :',e,'binary :',format(e,'08b'))

