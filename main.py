from url_extractor import *

url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url_extractor = URLExtractor(url)
print(url_extractor)

quantity = url_extractor.get_parameter_value('quantidade')
print(quantity)