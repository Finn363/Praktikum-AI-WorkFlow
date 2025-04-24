menikah(david, amy).
menikah(jack, karen).
menikah(john, susan).

orangtua(david, liza).
orangtua(amy, liza).
orangtua(david, john).
orangtua(amy, john).
orangtua(jack, ray).
orangtua(karen, ray).
orangtua(john, peter).
orangtua(susan, peter).
orangtua(john, mary).
orangtua(susan, mary).

pria(david).
pria(jack).
pria(john).
pria(ray).
pria(peter).

wanita(amy).
wanita(karen).
wanita(susan).
wanita(liza).
wanita(mary).

ayah(X, Y) :-pria(X), orangtua(X, Y).
ibu(X, Y) :-wanita(X), orangtua(X, Y).
saudara_kandung(X, Y) :-orangtua(Z, Y), orangtua(Z, Y), X \= Y.
kakek(X, Y) :-pria(X), orangtua(X, Z), orangtua(Z, Y).
nenek(X, Y) :-wanita(X), orangtua(X, Z), orangtua(Z, Y).
cucu(X, Y) :-orangtua(Y, Z), orangtua(Z, X).



