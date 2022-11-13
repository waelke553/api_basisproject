# api_basisproject

Voor dit project heb ik gekozen om rond het thema hashing the werken.
Hierbij is mijn inspiratie gekomen uit een programma/plug-in op google chrome. Waarbij je per site je wachtwoorden kunt encrypteren. En via 1 key-wachtwoord de geencrypteerde wachtwoorden kunt decrypteren.


# Project inhoud

Maar bij mijn project heb ik gekozen dat een user zijn wachtwoord per site kan encrypteren via een key-wachtwoord. Dat hij mee geeft met de api en als de user zijn wachtwoord wilt decrypteren. Moet hij de juiste key-wachtwoord meegeven. En dan pas zal het echte wachtwoord voor die website worden gedecrypteerd.

Daarnaast heb ik ook voor mijn api gekozen voor een deel "PATH" parameters te gebruiken. Maar grotendeels zijn "Query" parameters. Zodaning dat ik controle erop kan voeren.

Ook heb ik een json file structuur aangemaakt om aan te tonen dat ik de leerstof die ik heb geleerd kon toepassen op dit project.

Voor deze api heb ik ook een front-end aan gekoppeld om de api makkelijker te gebruiken. Ook heb ik gebruik gemaakt van gitlab om mijn html website te hosten. (Zie foto)

![Front-end page](./img/front-end-page.png)


# Python libraries

Python libraries die ik heb gebruikt voor dit project zie je hieronder.

1. Cryptography
2. Json
3. Os
4. Fastapi
5. Pydantic

"Cryptograpy" heb ik gebruikt om strings te encrypteren en dycrepteren. "Json" gebruik ik om een json file te lezen en te schrijven. "Os" is gebruikt om een file aan te maken op het systeem zou het nog niet bestaan. "Fastapi" is gebruikt om een api aan te maken. "Pydantic" heb ik gebruikt om classes aan te maken met het basemodel.



# Soorten API's

Voor dit project hebt ik 2 'GET' api's waarvan eentje je de websites terug geeft van de user. En de tweede zal je het geencrypteerde wachtwoord geven als je de juiste key wachtwoord meegeeft.

Als laatste heb ik ook een 'POST' api die je kan gebruiken om een nieuwe user met een webiste en wachtwoord en key wachtwoord kan meegeven. En mijn python code zal voor jou het opslaan in een json file.

## Foto's

### Postman foto's

![1-get-fout](./img/1_fout_geen_user_gevonden.png)

![1-get-inorde](./img/1_inorde.png)

![2-get-fout](./img/2_get_key_verkeerd.png)

![2-get-inorde](./img/2_get_inorde.png)

![3-post-fout](./img/3_post_foutmelding_wachtwoord_query.png)

![3-post-inorde](./img/3_post_inorde.png)

### Front-end foto's

![front-end-api-calls-fout](./img/front-end-api-calls.png)

![front-end-api-calls-inorde](./img/front-end-api-calls-inorde.png)


# Algemene eisen & Documentatie (+65%) [Wat de leerling denk dat goed is gegaan]
## Algemeen

- [x] 1 API in een GitHub repository
- [x] 1 front-end in een GitHub repository
- [x] Beschrijving van het gekozen thema, je API en je front-end + link naar hosted API, link naar front-end GitHub repository en link naar hosted front-end op GitHub README.md
- [x] Aantoonbare werking totale API door screenshots van Postman requests op GitHub README.md
- [x] Volledige OpenAPI docs screenshot(s) op GitHub README.md

## REST API

- [x] Minstens 2 GET endpoints 
- [x] Minstens 1 POST endpoint met class(es)
- [x] Maximaal gebruik van validaties. Gebruik van response model wanneer aangewezen.
- [x] Logisch gebruik van path parameters, query parameters en body

## Deploying 

- [x] Docker container voor de API, welke automatisch door GitHub Actions opgebouwd wordt
- [x] Deployment van de API container op Okteto Cloud via Docker Compose

## Front-end

- [x] Een simpele front-end, minstens op basis van AlpineJS (Heb hier meerderheid javascript geschreven. Maar ik heb wel AlphineJS gebruikt voor sommige delen om aan te tonen dat ik het heb gebruikt.)
- [x] Deployment van de front-end

## Suggesties voor bijkomende componenten

- [x] Stijlgeving op de front-end (+5%)
- [ ] Interactie van je API met een andere externe service, API of databank (+15%)
- [ ] Eigen inspiratie… (+?%)


# URL Links

Github Repository: Hier zit u op
Github Repository voor front-end: [GitHub Repo - Front-end Link](https://github.com/waelke553/api_basisproject_website)
Hosted API: [Okteto - Hosted API Link](https://hashing-service-waelke553.cloud.okteto.net)
Hosted front-end: [Github - Hosted Front-end Link](https://hashing-service-waelke553.cloud.okteto.net)


Bijkomende commentaar, aanvullingen, enz:

Bij mijn front-end kan je zien dat als je de input fields invult. Dat je gewoon de link met blote ogen kan zien. Ook als is je wachtwoord met bolletjes is dit niet bij de link.

Dus type NIET je gebruikte passwoorden!
