# Messenger-prosjekter

## Klassifiserer
### Avhengigheter
##### NLTK
`pip install nltk`
##### NLTK-data
Manglende datapakker vises ved kjøring.
[Offisiell veilednig](https://www.nltk.org/data.html)

### Hvordan legge til Messenger-data
##### Last ned din Facebook-informasjon
`Innstillinger og personvern > Innstillinger > Din Facebook-infomrasjon > Last ned informasjonen din`
![Skjermdump fra Facebook](readme_pictures/skjermdump-facebook.png)
Velg datoperiode "Siden starten" for å sikre mest mulig data, mediekvalitet "lav", format "JSON" og "Opprett fil".
Datapakken kan lastes ned under fanen "Tilgjengelige kopier" når den er klar.
##### Flytt meldingsdata inn i prosjektet
Flytt mappen `inbox` som ligger i kopien du lastet ned, inn i rotmappen til dette prosjektet.

### Hvordan kjøre
`python classifier.py`

Hver mappe i `inbox` representerer en samtale i Messenger. Kopier mappenavnet til ønsket samtale og lim inn i programmet ved forspørsel.

Trekkgenerering kan ta litt tid avhengig av samtalens lengde.

```
Conversation: samtalenavn_xxxxx
Loading messages...
Cleaning messages...

 MESSAGE DISTRIBUTION (11 participants)
 person1:   22.654 %   (23984)
 person2:   14.745 %   (15611)
 person3:    7.044 %   (7457)
 person4:    4.609 %   (4880)
 person5:    3.723 %   (3942)
 person6:   15.094 %   (15980)
 person7:   20.592 %   (21801)
 person8:    7.823 %   (8282)
 person9:    3.273 %   (3465)
person10:    0.434 %   (460)
person11:    0.008 %   (8)

Generating features...
Training classifier...

Ready!
Exit with input 'q'.

Input: hei på deg! hvordan har du det?
Features: contains(hei): True
Predicted class: person1

Input: Hva skal dere i helgen, gutter?
Features: contains(gutter): True,  contains(helgen): True
Predicted class: person2

Input: _
```
