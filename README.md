## Nobø API kommandoer
Programmet noboG00.py benyttes sammen med Nobø HUB og en Raspberry Pi i samme nettverk som HUB.

noboG00.py er et svært forenkelt python3-program for å kjøre API kommandoer som er listet opp i Nobø-dokument:\
https://www.glendimplex.no/media/15655/nobo-hub-api-v-1-1-integration-for-advanced-users.pdf

noboG00.py lister ut informasjon fra Nobø HUB med kommando G00.
Programmet kan modifiseres til å sende andre kommandoer.

Programmet kjøres fra kommando-linje (CLI) i Raspberry Pi:\
python3 noboG00.py

eksempel_utskrift.txt viser et eksempel på resultat fra programkjøring. Inneholder en sone, en ukeprofil (i tilegg til default) og en ovn.\
yyyyyyyyyyyy er HUB serienummer\
xxxxxxxxxxxx er objekt serienummer (f.eks ovn)

noboG00.py har ingen feilhåndteringsmekanismer og kan defor gi "heng"-situasjoner i gitte tilfeller.

Denne programvaren brukes på eget ansvar og utgiver av denne programvaren tar ikke noe ansvar for eventuell skade som kan skje på ved bruk av programvaren.

IMPORTANT\
This software is not officially supported or endorsed by Glen Dimplex Nordic AS, and program supplier is not an official partner of Glen Dimplex Nordic as.
