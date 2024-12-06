De `str`-klasse in Python heeft een groot aantal methoden die je kunt gebruiken om tekst te manipuleren en analyseren.
Hier zijn enkele van de belangrijkste methodes gegroepeerd op basis van hun functionaliteit:

### 1. **Controleren op eigenschappen**

- **`str.isalpha()`**: Controleert of de string alleen alfabetische tekens bevat.
- **`str.isdigit()`**: Controleert of de string alleen cijfers bevat.
- **`str.isalnum()`**: Controleert of de string alleen alfanumerieke tekens bevat.
- **`str.isspace()`**: Controleert of de string alleen spaties, tabs of nieuwe regels bevat.
- **`str.islower()`**: Controleert of alle letters kleine letters zijn.
- **`str.isupper()`**: Controleert of alle letters hoofdletters zijn.

---

### 2. **Converteren van tekst**

- **`str.lower()`**: Converteert alle tekens naar kleine letters.
- **`str.upper()`**: Converteert alle tekens naar hoofdletters.
- **`str.capitalize()`**: Maakt het eerste teken van de string een hoofdletter.
- **`str.title()`**: Maakt elk woord in de string een hoofdletter aan het begin.
- **`str.swapcase()`**: Wisselt hoofdletters en kleine letters om.

---

### 3. **Zoeken en vervangen**

- **`str.find(sub)`**: Geeft de eerste index van een substring terug (of `-1` als deze niet wordt gevonden).
- **`str.index(sub)`**: Zoals `find()`, maar genereert een fout als de substring niet wordt gevonden.
- **`str.replace(old, new)`**: Vervangt alle gevallen van een substring door een andere substring.
- **`str.count(sub)`**: Telt hoe vaak een substring voorkomt.
- **`str.startswith(prefix)`**: Controleert of de string begint met een bepaalde substring.
- **`str.endswith(suffix)`**: Controleert of de string eindigt met een bepaalde substring.

---

### 4. **Splitsen en samenvoegen**

- **`str.split(sep)`**: Splitst een string op een scheidingsteken en retourneert een lijst.
- **`str.rsplit(sep)`**: Zoals `split()`, maar begint aan het einde.
- **`str.join(iterable)`**: Verbindt een iterable met een string als scheidingsteken.
- **`str.partition(sep)`**: Splitst de string in drie delen: vóór, het scheidingsteken, en na.
- **`str.rpartition(sep)`**: Zoals `partition()`, maar begint aan het einde.

---

### 5. **Aanpassen van witruimte**

- **`str.strip(chars)`**: Verwijdert voor- en achteraan opgegeven tekens (standaard witruimte).
- **`str.lstrip(chars)`**: Verwijdert tekens aan de linkerkant.
- **`str.rstrip(chars)`**: Verwijdert tekens aan de rechterkant.

---

### 6. **Formatteren**

- **`str.format()`**: Gebruikt placeholders om tekst te formatteren.
- **`str.zfill(width)`**: Voegt nullen toe aan het begin van de string totdat deze de opgegeven breedte bereikt.
- **`str.center(width)`**: Centreert de string in een veld van opgegeven breedte.
- **`str.ljust(width)`**: Links-uitlijnen van de string in een veld van opgegeven breedte.
- **`str.rjust(width)`**: Rechts-uitlijnen van de string in een veld van opgegeven breedte.

---

### 7. **Codering en Decodering**

- **`str.encode(encoding)`**: Encodeert de string naar bytes.
- **`bytes.decode(encoding)`**: Decodeert bytes terug naar een string.

Wil je een specifieke methode in detail uitgelegd hebben?