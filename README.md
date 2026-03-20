[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tKFkieDb)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23006675)
﻿# DAFE1000-oblig-template

<Replace with full name and OsloMet email address>
<Rajaa El fajli  raelf6164@oslomet.no>


forklaring for oppgaven:
vi har funksjonen:
f(x) = e^-x/4 arctan(x)

vi har:
arctan(x) = tan^-1(x)


jeg skal bruke produktregelen og få den deriverte:
f'(x) = e^-x/4(1/1+x^2 - 1/4 arctan(x))
f'(x) = e^-x/4.1/1+x^2 - 1/4 e ^-x/4. arctan(x)
faktoriserer:
f'(x) = e^-x/4(1/1+x^2-1/4arctan(x))

finne et toppunkt:
et toppunkt skjer når den deriverte er lik 0
f'(x) = 0 
siden e^-x/4 >0 må:
1/1+x^2 -1/4 arctan(x)=0
ganger med 4:
4/1+x^2 -arctan(x)=0
omskriver til :
arctan(x) - 4/x^2+1 =0
løse ligningen :
denne ligningen kan ikke løses eksakt så derfor finner vi løsning numerisk 
x_topp = 1.690708
y_topp = 0.679322 # på terminalen i python 

f(x) = ca 1.6907
f(1.6907) = 0.6793

Toppunktet er :
(1.6907, 0.6793)

Dette er  et toppunkt fordi før punktet f'(x) >0 funksjonen øker og etter punktet f'(x) <0 funksjonen minker ( se på bildet inni eksamples mappe).


