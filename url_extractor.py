class URLExtractor:
    def __init__(self, url):
        self._url = self.clean_url(url)

    def clean_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
        
    def validate_url(self):
        if not self._url:
            raise ValueError("A URL esta vazia")
        
    def __str__(self):
        return self._url
    
    def get_base_url(self):
        index_interrogation = self._url.find('?')
        url_base = self._url[0:index_interrogation]
        return url_base
    
    def get_parameter_url(self):
        index_interrogation = self._url.find('?')
        url_parameter = self._url[index_interrogation+1:]
        return url_parameter
    
    def get_parameter_value(self, search_parameter):
        index_searched_parameter = self.get_parameter_url().find(search_parameter)
        index_value = index_searched_parameter + len(search_parameter) + 1
        index_concat = self.get_parameter_url().find('&', index_value)
        
        if index_concat == -1:
            value = self.get_parameter_url()[index_value:]
        else:
            value = self.get_parameter_url()[index_value:index_concat]

        return value
