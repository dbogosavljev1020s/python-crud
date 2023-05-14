# Python Flask CRUD sistem
## Pripremanje projekta
1. U PHPMyAdmin napraviti bazu `studenti`
2. Importovati `korisnik .sql` u bazu
3. Smestiti 'generate debug baza sesija 2021-22.py' unutar željenog foldera
4. Pokrenuti CMD i navigovati do foldera u kojem želite da napravite projekat
5. U CMD pokrenuti komandu: `py "generate debug baza sesija 2021-22.py"`
6. Uneti ime projekta (možete ga uneti proizvoljno)
7. Sačekati da se izgradi projekat
8. Zatvoriti CMD
9. Otvorite folder projekta i njega iskopirati `src` folder
10. Pokrenuti 'start_console.bat'
11. Unutar novootvorenog CMD pokrenuti `start_flask_server.bat` i ostaviti da radi u pozadini

## Putanje
`127.0.0.1:5000/register` - Forma za unos podataka o studentu. Na ovoj stranici postoji bazična validacija podataka (Jedinstveni indeks, provera lozinke, vrednost prosečne ocene i broj položenih ispita)<br><br>
`127.0.0.1:5000/login` - Forma za prijavljivanje putem indeksa i lozinke.<br><br>
`127.0.0.1:5000/show_all` - Tabela sa podacima o svim unetim studentima. Ukoliko je korisnik prijavljen, onda mu se daje mogućnost da menja i briše podatke iz baze<br><br>
`127.0.0.1:5000/better_than_average/<average>` - Filtrira studente po minimalnoj prosečnoj oceni<br><br>
`127.0.0.1:5000/logout` - Odjavljuje korisnika<br><br>
`127.0.0.1:5000/update/<indeks>` - Forma za promenu podataka željenog korisnika<br><br>
`127.0.0.1:5000/delete/<indeks>` - Brisanje željenog korisnika iz baze
