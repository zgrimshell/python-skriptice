import math

#n je broj kugli koji se moze izvuci iz prvog bubanja
#r broj kugli koje se izvlace
#t broj kugli koje treba pogoditi
#c je broj kuglica u drugom bubnju
n = 39
r = 5
c = 5
f = math.factorial 
d = f(n) / f(r) / f(n-r) #broj kombinacija u prvom bubnju
a = d * c
print "Sanse za jackpot su jedan naprema", a

print "Sanse za 5 su jedan naprema", a/(f(r)/f(r)*(c-1))

print "Sanse za 4 + 1 su jedan naprema", a/(f(r)/f(r-1)/f(r-(r-1))*(n-r))

print "Sanse za 4 su jedan naprema",  a/(f(r)/f(r-1)/f(1)*(n-r)*(c-1))

print "Sanse za 3 + 1 su jedan naprema", a/(f(r)/f(r-2)/f(r-(r-2))*f(n-r)/f(2)/f(n-r-2))

print "Sanse za 3 su jedan naprema", a/(f(r)/f(r-2)/f(r-(r-2))*f(n-r)/f(2)/f(n-r-2)*(c-1))

print "Sanse za 2 + 1 su jedan naprema", a/(f(r)/f(r-3)/f(r-(r-3))*f(n-r)/f(3)/f(n-r-3))

print "Sanse za 1 + 1 su jedan naprema", a/(f(r)/f(r-4)/f(r-(r-4))*f(n-r)/f(4)/f(n-r-4))

print "Sanse za 0 + 1 su jedan naprema", a/(f(r)/f(r-5)/f(r-(r-5))*f(n-r)/f(5)/f(n-r-5))
