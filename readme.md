# I should definitely slay the dragon, right?

Sami Malmsten

# Pelin idea ja tavoite
Pelin idea on valita oma reitti pelin läpi.
Pelin tavoite on yrittää saada kaikki 16 loppua pelaamalla peliä monta kertaa ja kokeilemalla kaikkia toimintoja. 

# Tiedostot
Classes tiedostossa luokat Player, Room ja Item. Room luokasta on tehty joka huoneelle oma aliluokka
Main tiedostossa on pääohjelma, pelaaja olio, pelaajan kaikki toiminnot, pelin tallenus ja lataus, pelin loppu ja huoneiden luominen.
Rooms tiedostossa on huoneiden oliot ja funktio huoneiden luomiselle pelin aikana.
User_info tiedostossa kysytään pelaajan nimi ja ikä kun pelin aloittaa ensimmäistä kertaa. Jos pelaaja on alle 12, peliä ei voi aloittaa.
Ending_texts tiedostossa on kaikki pelin loput funktiossa.

# main.py tiedosto
Tiedoston alussa tehdään alku esineet ja ensimmäinen huone.
Pelin alussa katsotaan onko tallennus olemassa ja ladataan tiedot jos on. Jos save.json on tyhjä kysytään pelaajan nimi ja ikä.
Sitten funktio jossa While loopilla käydään läpi pelaajan toiminnot pelin aikana ja se palauttaa pelin pelin lopun jos huone palauttaa lopun.
Joka loopin alussa peli tallennetaan kutsumalla save_game funktiota.
Jos pelin pääsee läpi, loopin jälkeen tulostaa pelin lopun ja muokkaa tallenusta jotta seuraava pelikerta ei ala viimeisestä huoneesta.

# classes.py
Kaikki pelin luokat.
# rooms.py
Funktio joka luo huoneen, huoneen esineet ja huoneen toiminnot. Funktio palauttaa luodun huoneen ja pelin lopun.
# user_info.py
Funktio joka kysyy pelaan iän ja nimen. Jos pelaajan ikä alle 12, peli sammuu.
# ending_texts.py
Funktio joka tulostaa pelin lopun ja lisää sen listaan, jos sitä ei ole saatu vielä.

# Kestävän kehityksen aiheet
Ei nälkää.
Yhteistyö ja kumppanuus.
Pelissä pitää selvittää ruoka kriisi yksin tai yhteistyössä muiden kanssa.
