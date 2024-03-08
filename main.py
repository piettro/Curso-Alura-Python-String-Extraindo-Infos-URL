url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

##
url_base = url[0:19]
url_parameter = url[20:]
print(url_base)
print(url_parameter)

##
index_interrogation = url.find('?')
url_base = url[0:index_interrogation]
url_parameter = url[index_interrogation+1:]
print(url_base)
print(url_parameter)

##
search_parameter = 'moedaDestino'
index_searched_parameter = url_parameter.find(search_parameter)
index_value = index_searched_parameter + len(search_parameter) + 1
index_concat = url_parameter.find('&', index_value)

if index_concat == -1:
    value = url_parameter[index_value:]
else:
    value = url_parameter[index_value:index_concat]

print(value)