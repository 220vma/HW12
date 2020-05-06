import json
from os import path

class JsonFile():
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __str__(self):
        return f'Объект класса {self.__class__.__name__} с именем {self.name} и данными {type(self.data)}'

    def writeToFile(self):
        with open(f'{self.name}.json', 'w', encoding='utf-8') as jsonFile:
            jsonFile.write(json.dumps(self.data, ensure_ascii=False))

    def readFromFile(self):
        with open(f'{self.name}.json', 'r', encoding='utf-8') as jsonFile:
            return f'Данные из файла {self.name}.json: {json.load(jsonFile)}'

    def __add__(self, other):
        print(f'...Объединение данных из файлов {self.name}.json и {other.name}.json...')
        try:
            jsonFile1 = open(f'{self.name}.json', 'r', encoding='utf-8')
            jsonFile2 = open(f'{other.name}.json', 'r', encoding='utf-8')
        except FileNotFoundError:
            return '>>>Ошибка с открытием одного из файлов! Перезапишите данные в файлы!<<<'
        jsonFile3 = open('COMBINED.json', 'w+', encoding='utf-8')

        jsonFile3.write(json.dumps((json.load(jsonFile1), json.load(jsonFile2))))
        jsonFile1.close()
        jsonFile2.close()
        jsonFile3.close()

        return '---Объединение успешно!---'

    def relPath(self):
        try:
            return f'Относительный путь к {self.name}.json: ' + path.relpath(f'{self.name}.json', '.')
        except FileNotFoundError:
            return '>>>Файл с данными не существует!<<<'

    def absPath(self):
        try:
            return f'Абсолютный путь к {self.name}.json: ' + path.abspath(f'{self.name}.json')
        except FileNotFoundError:
            return '>>>Файл с данными не существует!<<<'



listJson = JsonFile('list1', [1, 2, 'line'])
dictJson = JsonFile('dict1', {1: 'a', 2: 'b', 3: 'c'})
print(listJson.__str__(), dictJson.__str__(), sep='\n')
listJson.writeToFile()
print(listJson.readFromFile())
dictJson.writeToFile()
print(dictJson.readFromFile())
print(listJson + dictJson)
print(listJson.relPath())
print(dictJson.relPath())
print(listJson.absPath())
print(dictJson.absPath())