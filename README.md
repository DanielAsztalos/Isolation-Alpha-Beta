# Isolation Console Game

## A játék lényege
A játékot két játékos játsza ('1' - játékos, '2' - számítógép). Kezdetben a két játékos egy 7x7-es táblán kell elhelyezze a saját bábuját. Ezután egymás után váltakozva léptethetik a bábuikat függőleges, vízszintes vagy átlós irányokba a szabadon levő területekre ('_'). Ezekbe az irányokba a következő akadályig vagy a tábla széléig léphet a játékos. Azokra a területekre amiket elhagyott egy-egy játékos már nem lehet lépni ('X'), így a játék folyamán egyre fogynak a szabad területek. Minden játékos arra törekszik, hogy úgy lépjen, hogy az ellenfélnek elfogyjanak a lehetséges lépései. Az a játékos veszít, akinek hamarabb fogynak el a lehetséges lépései, nem léphet már semmilyen irányba.

## A program leírása
A program az Isolation játék konzolra írt verziója. A program a konzolba írja ki minden lépés után a tábla aktuális állapotát.

Jelölések:

'_' - üres mezők

'X' - már látott mezők

'1' / '2' - a játékosok aktuális pozíciói

Mindig amikor az 1-es játékoson van a sor, a konzolba kiíródik azoknak a területeknek a pozíciói, ahova a játékos léphet, előttük egy sorszámmal. Ezután a konzolban megjelenik egy kérdés, hogy a játékos melyik területre szeretne továbblépni. Ide a játékos meg kell adja a lehettsége lépései közül kiválasztott lépés listabeli sorszámát, majd az Enter gomb leütésével hagyja jóvá a lépést.

A számítógép (2-es játékos) az Alpha-Beta Pruning algoritmus alapján dönti el, hogy mi számára az optimális lépés, ez alatt pedig a konzolra a "Computer is thinking..." felirat kerül. Az algoritmus által használt heurisztikus függvény az 2-es és a 1-es játékosok lehetséges lépéseinek a különbségét számolja ki, úgy, hogy a szám pozitív legyen ha a számítógépnek van több lépés lehetősége, negatív, ha a játékosnak, illetve 0 különben. Ebben a játékban ez egy elég jó heurisztikus függvénynek bizonyúlt. 

## A program futtatása
A program <b>python 3.6</b> verzióban íródott. 

Meghívás:
```
python isolation.py [args]
```

A program a következő argumentumokat használ, amelyek közül egyet kell megadni:

-d \<N\> - a számítógép N mélységig menjen le az alpha-beta pruning algoritmussal

-t \<N\> - a számítógép N másodpercig "gondolkozhat"

