bigger(gajah, kuda).
bigger(kuda, keledai).
bigger(keledai, anjing).
bigger(keledai, monyet).

is_bigger(X,Y) :- bigger(X, Y).
is_bigger(X,Y) :- bigger(X, Z), is_bigger(Z,Y).
