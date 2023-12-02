a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#3 aspas é utilizado para que o texto passe de uma linha

a = "Hello, World!"
print(a[1])
#mostra um determinado caractere

a = "Hello, World!"
print(len(a))
#mostra a quantidade de caracteres

txt = "The best things in life are free!"
print("free" in txt)
#define como true ou false se determinada palavra esta em algum texto

txt = "The best things in life are free!"
print("expensive" not in txt)
#define como true ou false se determinada palavra nao esta em algum texto

a = "Hello, World!"
print(a.upper())
#deixa todo o texto em caixa alta

a = "Hello, World!"
print(a.lower())
#deixa todo o texto em caixa baixa

a = " Hello, World! "
print(a.strip())
#remove espaços no inicio e no final do texto

a = "Hello, World!"
print(a.replace("H", "J"))
#substitui uma parte por outra

a = "Hello, World!"
print(a.split(","))
#separa um texto em dois