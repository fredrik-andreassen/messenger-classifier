# Messenger-klassifiserer


## Avhengigheter
#### Norsk data
For optimal utfilterering av systemgenererte meldinger, må Messenger-språket ditt være norsk. Andre språk gjenkjennes ikke av de regulære uttrykkene som filtrerer ut slike meldinger.

Eksempelutdrag fra rå samtaledata med norsk språk:
```json
    {
      "sender_name": "person6",
      "timestamp_ms": 1626285208702,
      "content": "Videochatten er avsluttet.",
      "call_duration": 47,
      "type": "Call",
      "is_unsent": false
    },
    {
      "sender_name": "person3",
      "timestamp_ms": 1626285173388,
      "content": "person3 ble med i videochatten.",
      "type": "Generic",
      "is_unsent": false
    },
    {
      "sender_name": "person4",
      "timestamp_ms": 1626285164904,
      "content": "Du ble med i videochatten.",
      "type": "Generic",
      "is_unsent": false
    }
```
#### NLTK
Meldinger tokeniseres med NLTK.
`pip install nltk`

#### NLTK-data
Pakke nødvendig for tokenisering kan lastes ned via Python-interpreten.
```python
import nltk
nltk.download('punkt')
```
[Offisiell veilednig](https://www.nltk.org/data.html)


## Hvordan legge til Messenger-data
#### Last ned din Facebook-informasjon
`Innstillinger og personvern > Innstillinger > Din Facebook-infomrasjon > Last ned informasjonen din`

![Skjermdump fra Facebook](readme_pictures/skjermdump-facebook.png)

Velg datoperiode "Siden starten" for å sikre mest mulig data, mediekvalitet "Lav", format "JSON" og "Opprett fil".
Datapakken kan lastes ned under fanen "Tilgjengelige kopier" når den er klar. Noen ganger kan dataen opprettes i to filer.
#### Flytt meldingsdata inn i prosjektet
Flytt mappen `inbox` som ligger i kopien du lastet ned, inn i rotmappen til dette prosjektet.

## Hvordan kjøre
`python main.py`

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
Exit with input '/q'.

>>> hei på deg! hvordan har du det?
Features: contains(hei): True
Predicted class: person1

>>> Hva skal dere i helgen, gutter?
Features: contains(gutter): True,  contains(helgen): True
Predicted class: person2

Input: _
```
#### Kommandoer
Ved å starte input på skråstrek (/) tolkes input som en kommando.
* `/exit`: Avslutter
* `/reset`: Starter på nytt
* `/clear`: Tømmer terminalen med `clear`/`cls`
* `/dist`: Viser meldingsfordeling for valgt samtale
