# python-1-2024 Benoit


De volgorde van bewerkingen in Python (en andere programmeertalen) wordt bepaald door de operator precedence (prioriteit van operatoren) en associativiteit. Hier is een overzicht van de volgorde waarin bewerkingen worden uitgevoerd in Python, van hoogste naar laagste prioriteit:

Haakjes: () – Expressies tussen haakjes worden eerst geëvalueerd.

Exponentiatie: ** – Machtverheffen wordt daarna gedaan.

+x, -x, ~x: Eenheidsbewerkingen, zoals positief of negatief maken, en bitwijziging.

Vermenigvuldigen, delen, modulo en vloer-deling: *, /, //, %

Optellen en aftrekken: +, -

Bitshift: <<, >>

Bitwise AND: &

Bitwise XOR: ^

Bitwise OR: |

Vergelijkingsoperatoren: ==, !=, >, >=, <, <=, is, is not, in, not in

Booleaanse NOT: not

Booleaanse AND: and

Booleaanse OR: or


Operatoren met dezelfde prioriteit worden geëvalueerd op basis van hun associativiteit, die meestal linksassociatief is (behalve exponentiatie, die rechtsassociatief is). Haakjes kunnen altijd worden gebruikt om de volgorde te veranderen.
