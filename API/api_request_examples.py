#importo a biblioteca
import requests

#utilizo o get para pegar algo com o jsonplaceholder
response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)

#utilizo o get para postar algo com o jsonplaceholder
response = requests.post("https://jsonplaceholder.typicode.com/posts", data =  {"title":"foo", "body":"bar", "userId":1})

print(response.status_code)

#utilizo o get para mudar algo com o jsonplaceholder
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data =  {"title":"foo", "body":"bar", "userId":1})

print(response.status_code)

#utilizo o get para remover algo com o jsonplaceholder
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)

#utilizo o get para acessar um filme
response = requests.get("http://www.omdbapi.com/?apikey=2e450dcb&t=titanic")

print(response.status_code)
print(response.json())