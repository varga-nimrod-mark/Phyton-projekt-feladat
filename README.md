# Phyton-projekt-feladat
======================================================
Videó Képkocka Kinyerő v0.1.0
======================================================

LEÍRÁS
A program egy megadott videófájlból (pl. mp4) adott időközönként képkockákat 
ment ki egy mappába a megadott formátumban. A kimentett képek felbontása a 
felhasználó által testreszabható(a bemeneti videó felbontásánál csak kissebb méret adható meg).

======================================================
FUTTATÁSHOZ SZÜKSÉGES FELTÉTELEK
======================================================

1. Python telepítés: A program futtatásához Python 3.x környezet szükséges.
2. OpenCV könyvtár: A videó- és képfeldolgozást a cv2 modul végzi, amelyet 
   futtatás előtt telepíteni kell. 

   Telepítése a parancssorban (Command Prompt / Terminal):
   pip install opencv-python

======================================================
BEMENETI ADATOK ÉS PARAMÉTEREK BEÁLLÍTÁSA
======================================================

Mivel a program nem parancssori argumentumokat használ, a futtatás előtt 
a kód elején található "#==================== Input's_&_Outputs ====================" 
szekcióban kell megadni a megfelelő adatokat a változóknál:

* video_path
  - A feldolgozandó videófájl pontos elérési útja (pl. "C:\...\test_video.mp4").
  - Fontos, hogy a fájl valóban létezzen ezen a helyen, különben hibaüzenetet ad!

* debug
  - Értéke True vagy False lehet.
  - Ha False (alapértelmezett): A program elvégzi a képkockák kimentését a háttérben.
  - Ha True: A program bekapcsolja a hibakereső (debug) módot. Kiírja a videó 
    információit a konzolra, megjeleníti a feldolgozott videót egy ablakban, de 
    ilyenkor NEM menti le a képeket, igy tesztelhető a program a cél mappa tele "szemetelése" nélkül.
    A lejátszás a 'q' billentyű megnyomásával megszakítható.

* fsps (Frames Saved Per Second)
  - Egy egész szám, amely megadja, hogy egy másodpercnyi videóanyagból 
    hány darab képkockát mentsen le a program (pl. 2).

* fajl_formatum_nyers
  - Az itt megadott formátumban kerülnek a képek lementésre, a kódsor az alábbi formátumokat támogatja:
    jpg, jpeg, jpe, png, webp, bmp, dib, tif, tiff, jp2, hdr, pic, sr, ras, ppm, pnm,
    amenyiben ezektől eltér a megadott formátum a program hibaüzenetet ad!

* save_path
  - A mappa pontos elérési útja, ahová a program a képeket fogja menteni 
    (pl. "C:\...\farme's").
  - FONTOS: A mappának már léteznie kell a program indítása előtt, különben hibaüzenetet ad!

* size
  - A kimentett képek felbontása (szélesség, magasság) formátumban, pl. [640, 640].
  - Csak két pozitív egész szám adható meg.
  - A megadott méret nem lehet nagyobb, mint az eredeti videó felbontása 
    (csak kicsinyítés vagy azonos méret engedélyezett).

Mentett képek elnevezése
A "#-------------------- Saved_File_Name --------------------" szekción bellül kerül megadásra (kb.: 58.sor+-2) a lementendő kép elnevezése
a "fajlnev" változón bellül lehet megadni.
  - FONTOS: a változóban megadott szövegnek alábbi módon kell végződnie: .{fajl_formatum} különben a program nem fut le. 
  - Példa a helyes elnevezésre: fajlnev = f"mentésinév.{fajl_formatum}"

======================================================
FUTTATÁS
======================================================

1. Nyisd meg a .py kiterjesztésű kódot egy kódszerkesztőben (pl. VS Code, Notepad++).
2. Állítsd be a saját elérési útjaidat a `video_path` és `save_path` változóknál.
3. Mentsd el a fájlt
4. Futtasd a programot a parancssorból:
   python video_frame_saver.py
