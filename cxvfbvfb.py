import requests
response = requests.get('https://en.wikipedia.org/wiki/Main_Page')
print(response.content)



import requests
response = requests.get('https://coinmarketcap.com/')
response_text = response.text
response_parse = response_text.split('<span>')
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        print(parse_elem_1)