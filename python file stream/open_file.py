#open cria uma conexão entre dois arquivos
#enconding faz que o arqui vo seja lido da forma convencional, com acentos e carácteres especiais
file_stream = open('texto.txt', encoding='utf-8')

#read faz que o arquivo seja lido
meu_texto = file_stream.read()

print(meu_texto)

#close fecha a conexão entre dois arquivos
file_stream.close()

#mode faz que possamos escrever dentro do arquivo
#'a' faz que o que escrevermos seja salvo dentro do arquivo sem que o que estava no arquivo seja apagado, o 'w' faz que o que estava no arquivo seja deletado
file_stream = open('meu_texto.txt', mode= 'a', encoding='utf-8')

#write faz que um determinado texto seja colocado no arquivo
file_stream.write("A agora consigo salvar informações em arquivos usando o python!")

file_stream.close()