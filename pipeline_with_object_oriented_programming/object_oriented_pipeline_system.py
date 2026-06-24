class Sourcedata:
    def __init__(self,name):
        self.__name = name
        self.__total_records = 0

    def get_name(self):
        return self.__name

    def get_total_records(self):
        return self.__total_records

    def set_add_records(self,qtd):
        self.__total_records += qtd

    def status(self):
        return f'{self.get_name()}: {self.get_total_records()} registros processados'

class FileCSV(Sourcedata):
    def __init__ (self,name, delimiter):
        self.__delimiter = delimiter
        super().__init__(name)

    def status(self):
        return f'{super().status()} | delimitador: {self.__delimiter}'

class APIExternal(Sourcedata):
    def __init__(self,name,request_limit):
        self.__request_limit = request_limit
        super().__init__(name)

    def requests_available(self):
        return self.__request_limit - self.get_total_records()

    def status(self):
        return f'{super().status()} | requisições dispóníveis: {self.requests_available()}'


my_file_csv = FileCSV('usuarios_sistema',';')
my_file_csv.set_add_records(150)
print(my_file_csv.status())
my_api_external = APIExternal('API Clima',1000)
my_api_external.set_add_records(230)
print(my_api_external.status())