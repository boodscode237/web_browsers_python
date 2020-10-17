import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
res.raise_for_status()  # is used to raise an error when it occures
filedld = open('romeoandJ.txt', 'wb')

for file in res.iter_content(100000):
    filedld.write(file)
