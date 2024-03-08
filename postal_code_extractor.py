import re

address = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
search = pattern.search(address)

if search:
    postal_code = search.group()
    print(postal_code)

cpf = "718.457.190-85"

pattern = re.compile("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}")
search = pattern.search(address)

if search:
    postal_code = search.group()
    print(postal_code)