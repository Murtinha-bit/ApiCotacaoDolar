import requests
import sqlite3
conn = sqlite3.connect("D:\Murta Faculdade\bdcotacoes.db")
cursor= conn.cursor()

url = 'https://api.hgbrasil.com/finance?format=json-cors&key=31d91ff4'
resposta = requests.get(url)
print(resposta.status_code)
if (resposta.status_code == 200):
    json = resposta.json()
    print(json['results']['currencies']['USD']['buy'])
    print(json['results']['currencies']['EUR']['buy'])
else:
    print("Não foi possivel conseguir sua requisição")
cursor.execute("insert into moedas (Dolar, Euro) values ('json['results']['currencies']['USD']['buy']','json['results']['currencies']['EUR']['buy']')")
conn.commit()
cursor.execute("select * from moedas")
conn.close()