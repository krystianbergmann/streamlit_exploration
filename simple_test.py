import streamlit as st
# Importujemy bibliotekę Streamlit i nadajemy jej skrót "st"

st.title("Dodawanie dwóch liczb")
# Wyświetlamy tytuł aplikacji na górze strony

a = st.number_input("Pierwsza liczba", value=0)
# Tworzymy pole do wpisania pierwszej liczby
# Wartość wpisana przez użytkownika trafi§a do zmiennej 'a'

b = st.number_input("Druga liczba", value=0)
# Tworzymy pole do wpisania drugiej liczby
# Wartość wpisana przez użytkownika trafia do zmiennej 'b'

wynik = a + b
# Dodajemy dwie liczby zapisane w zmiennych 'a' i 'b'
# Wynik dodawania zapisujemy do zmiennej 'wynik'

st.write("Wynik:", wynik)
# Wyświetlamy tekst "Wynik:" oraz obliczoną wartość na stronie