
__version__ = "0.1.0"
__author__="Varga Nimród Márk"


import cv2
import os
#==================== Input's_&_Outputs ====================
video_path = r"C:\Users\Felhasznalo\Desktop\pyton projekt\VIDEÓ\test_video.mp4" #video elérési utvonala
debug = bool(False) #Videó megtekintése feldologzás közben T/F
fsps = 2 # Frame saved per second (mentett képek per másodperc)
fajl_formatum_nyers = "png" #Kimeneti fájl formátum (png, jpg, jpeg,)
save_path = r"C:\Users\Felhasznalo\Desktop\pyton projekt\farme's" #képek mentési helye
size = [640, 640] # mentett képek mérete (szélesség, magasság)

#==================== Video_Processing ====================
frame_szamlalo = 0
mentett_kepek = 0
fajl_formatum = fajl_formatum_nyers.lower()
tamogatott_formatumok = ["jpg", "jpeg", "jpe","png","webp","bmp", "dib","tif", "tiff","jp2","hdr", "pic","sr", "ras", "ppm", "pnm"]
cap = cv2.VideoCapture(video_path)
video_fps = cap.get(cv2.CAP_PROP_FPS)
video_cime = os.path.splitext(os.path.basename(video_path))[0]
lepeskoz_framekben = int(video_fps * fsps)
orig_szelesseg = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
orig_magassag = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
if not cap.isOpened():
    print("Hiba: Nem sikerült megnyitni a videót. Ellenőrizd, hogy a fájl létezik-e az adott útvonalon!")
    print("Vagy a megadott fájl nem feldolgozható formátumban van.")
elif video_fps == 0:
    print("Hiba: Nem sikerült beolvasni a videó FPS számát.")

elif not os.path.exists(save_path):
    print('Hiba: Nem sikerült megnyitni a mappát. Ellenőrizd, hogy a mentési mappa létezik-e az adott útvonalon!')

elif not (isinstance(size, (tuple, list)) and len(size) == 2 and isinstance(size[0], int) and isinstance(size[1], int) and size[0] > 0 and size[1] > 0):

    print(f"Hiba: A 'size' változó értéke érvénytelen! Jelenlegi érték: {size}")
    print("Két pozitív, egész számot adj meg pl.: (1280, 720).")

elif size[0] > orig_szelesseg or size[1] > orig_magassag:
    print(f"Hiba: A megadott méret {size} nagyobb, mint a videó maximális felbontása ({orig_szelesseg}x{orig_magassag})!")
    print("A sikeres feldolgozáshoz az eredetinél kisebb vagy azzal megegyező felbontást kell megadnod.")
elif fajl_formatum not in tamogatott_formatumok:
    print(f"Hiba: A megadott formátum ({fajl_formatum}) nem kép formátum vagy nem támogatott formátum!")
else:
    print("Videó sikeresen betöltve! Kezdődik a feldolgozás...")
    while True:
        ret, frame = cap.read()

        if not ret:
                   print(f"Kész! Összesen {mentett_kepek} db képkocka lett kimentve a(z) '{save_path}' mappába.")
                   print("Videó feldolgozása sikeresen lezárult...")
                   print("Program Vége...")
                   break

        frame_resize = cv2.resize(frame, size)
        #-------------------- Saved_File_Name --------------------
        fajlnev = f"{video_cime}_frame_{mentett_kepek:03d}.{fajl_formatum}"
        #---------------------------------------------------------

        teljes_eleresi_ut = os.path.join(save_path, fajlnev)
        if debug == False and frame_szamlalo%lepeskoz_framekben==0:
            cv2.imwrite(teljes_eleresi_ut, frame_resize)
            mentett_kepek += 1
        
        frame_szamlalo += 1
         
#==================== Debug ====================
    if debug == True:
       print (f"Video címe: {video_cime}")
       print (f"Video elérési utvonala: {video_path}")
       print (f"Video mentési útvonala: {save_path}")
       print (f"Video képkockáinak eredeti mérete: {orig_szelesseg}X{orig_magassag}")
       print (f"Video képkockáinak új mérete: {size[0]}X{size[1]}")
       print (f"Mentett képek per másodperc: {fsps}")
       print(f"Video fps értéke: {video_fps}")
       print (f"Minden {lepeskoz_framekben}. képkockát mentjük le")
       print(f"Video bemeneti mentési formátuma: {fajl_formatum_nyers}")
       print(f"Video feldolgozott mentési formátuma: {fajl_formatum}")           
       cv2.imshow('Feldolgozott_videó', frame_resize)
       if cv2.waitKey(25) & 0xFF == ord('q'):
         print("Feldolgozás megszakítva a felhasználó által.")
         cv2.destroyAllWindows()   

cap.release()
cv2.destroyAllWindows()