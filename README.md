# CNC Metalworking Augustus, sajt v2

## Šta je u paketu

- Gotov sajt, 40 HTML strana na pet jezika: engleski je podrazumevani (root), nemački `/de/`, poljski `/pl/`, češki `/cs/`, srpski `/sr/`.
- `assets/css/style.css` (jedan CSS za ceo sajt), `assets/js/main.js` (mobilni meni), `assets/img/` (sve slike smanjene: ukupno 1,3 MB umesto 86 MB).
- `sitemap.xml`, `robots.txt`, `favicon.ico`.
- `build.py` + `i18n_extra.py` (opciono): Python skripta koja generiše sve strane iz tekstova (en i sr su u `build.py`, de/pl/cs u `i18n_extra.py`). Ako menjaš tekst na više strana odjednom, lakše je izmeniti u `build.py` i pokrenuti `python3 build.py` nego ručno menjati 40 fajlova. Ako ti to ne treba, slobodno menjaj HTML direktno.

## Struktura URL-ova

| EN | DE | PL | CZ | SR |
|---|---|---|---|---|
| `/index.html` | `/de/index.html` | `/pl/index.html` | `/cs/index.html` | `/sr/index.html` |
| `/products/` | `/de/produkte/` | `/pl/produkty/` | `/cs/produkty/` | `/sr/proizvodi/` |
| `/products/window-opener.html` | `/de/produkte/fensteroeffner.html` | `/pl/produkty/otwieracz-okien.html` | `/cs/produkty/otvirac-oken.html` | `/sr/proizvodi/otvarac-prozora.html` |
| `/products/door-opener.html` | `/de/produkte/tueroeffner.html` | `/pl/produkty/otwieracz-drzwi.html` | `/cs/produkty/otvirac-dveri.html` | `/sr/proizvodi/otvarac-vrata.html` |
| `/products/replacement-cylinder.html` | `/de/produkte/ersatzzylinder.html` | `/pl/produkty/cylinder-zapasowy.html` | `/cs/produkty/nahradni-valec.html` | `/sr/proizvodi/rezervni-cilindar.html` |
| `/services/` | `/de/leistungen/` | `/pl/uslugi/` | `/cs/sluzby/` | `/sr/usluge/` |
| `/about/` | `/de/ueber-uns/` | `/pl/o-nas/` | `/cs/o-nas/` | `/sr/o-nama/` |
| `/contact/` | `/de/kontakt/` | `/pl/kontakt/` | `/cs/kontakt/` | `/sr/kontakt/` |

Svi folderi sa `/` imaju `index.html` unutra. Prevodi na nemački, poljski i češki su urađeni pažljivo, ali pre puštanja neka ih pročita neko kome je to maternji jezik (npr. kupci iz Poljske ili Češke), da se uhvati eventualna sitnica.

Svaka strana ima `hreflang` linkove ka svojim verzijama na ostalim jezicima, pa Google zna da su to iste strane. Linkovi su relativni, radi i lokalno (Live Server) i na hostingu.

## Pre puštanja, obavezno

1. **Domen u kodu.** U `build.py` na vrhu je `DOMAIN = "https://www.cncaugustus.com"`. Ako domen bude drugačiji, promeni i pokreni build, ili nađi/zameni u svim HTML fajlovima i u `sitemap.xml` i `robots.txt`.
2. **Kontakt forma.** Forma šalje na Formspree (besplatno do 50 poruka mesečno, dovoljno). Napravi nalog na formspree.io, dodaj formu, dobićeš ID tipa `xabcdefg`. Zameni `REPLACE_WITH_FORM_ID` u svih pet kontakt strana (najlakše u `build.py` pa pokreni build). Poruke stižu na info@cncaugustus.com. Alternativa ako hosting bude Netlify: dodaj `netlify` atribut na `<form>` i obriši `action`.
3. **Katalog.** Sve strane linkuju `downloads/catalogue-2027.pdf`. Katalog (`catalogue-2027.pdf`) je već u folderu `downloads/`. Kad se katalog menja, zameni fajl pod istim imenom.
4. **Slike.** Već su obrađene. Ako se dodaju nove: max 1600 px širine, JPG 80% kvalitet, nikad PNG od 5 MB.

## Posle puštanja

- Google Search Console: dodaj domen, pošalji `sitemap.xml`.
- Google Analytics ili Tag Manager: ubaci kod u `<head>` svih strana (u `build.py` funkcija `head()` je jedno mesto za to). Bez ovoga se ne mogu pratiti oglasi.
- Google Business Profile za firmu (besplatno, pojavljuje se na mapi).

## Šta je promenjeno u odnosu na prvu verziju

- Pet jezika: engleski podrazumevan, pa nemački, poljski, češki i srpski. Prevod se više ne radi JavaScriptom, svaka jezička verzija je posebna strana koju Google indeksira.
- Video izbačen. Hero je sada fotografija proizvoda na tamnoj pozadini.
- Dizajn: tamno plava iz logotipa za header, hero, sekcije i footer; svetlo siva za ostale sekcije; bela samo za kartice. Fontovi Montserrat (naslovi, isti kao u katalogu), IBM Plex Sans (tekst) i IBM Plex Mono (brojevi i specifikacije).
- Novi tekstovi na obe verzije, pisani za B2B kupce (distributeri, proizvođači staklenika), bez šablonskog teksta.
- Naslovi strana, meta opisi, Open Graph tagovi, favicon, sitemap, robots.
- Kontakt forma sa poljima koja prodaji trebaju (firma, zemlja, tema, količina). Telefon i mejl su klikabilni.
- Jedan CSS i jedan JS umesto po jedan za svaku stranu. Font Awesome izbačen, ikonice su inline SVG.
- Ispravljene greške: `data-in18n`, dupli ključ `text_efikasnost`, `prducts.js`, `lang="en"` na srpskim stranama, placeholder koordinate u mapi.
