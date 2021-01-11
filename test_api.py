from requests import put, get, delete

# put('http://127.0.0.1:5000/book1', data={'name': 'The Slight Edge'}).json()
# print(get('http://localhost:5000/book1').json())
print(delete('http://127.0.0.1:5000/book1'))
