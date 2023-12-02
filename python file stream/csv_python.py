file_stream = open('some_data.csv', encoding='utf-8')
for line in file_stream.readlines():
    dados = line.split(",")
    if dados[0] == "Nome":
        continue
    print('Nome:', dados[0])
    print('Idade:', dados[1])
    print('Cidade:', dados[2])
    print("####################################################################################")