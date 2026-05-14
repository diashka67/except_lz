import pandas as pd

class Check:

    def __init__(self):
        self.df = None  #пока пусто, потом будет наш открытый файл

    def open_file(self): #проверяем открытие файла
        try:
            name_file = input('введите имя файла:')
            if name_file != 'var5.csv':
                raise ValueError('ПЕРЕСМОТРИ НАЗВАНИЕ ФАЙЛА!!!')
            
            self.df = pd.read_csv(name_file)
            print('Файл открыт')
            
        except (FileNotFoundError, ValueError) as e:
            print(e)  
        except pd.errors.ParserError:
            print("Файл поврежден или имеет неверный формат")
        except Exception:
            print('Не удалось открыть файл')


    def check_empty(self):
        try:
            if self.df.empty: 
                raise pd.errors.EmptyDataError # ошибка пандаса, когда файл пустой
            print('Файл содержит данные')
        except AttributeError:
            print('Файл не был открыт')
        except ValueError:
            print('Файл пуст')

    def check_structure(self):
        try:
            if not isinstance(self.df, pd.DataFrame):  
                raise TypeError
            print('Структура файла правильная')
        except AttributeError:
            print('Файл не был открыт')
        except TypeError:
            print('Неправильная структура файла: ожидается таблица')
        

    def check_header(self, expected_columns):
        try:
            actual_columns = list(self.df.columns)
            if not all(col in actual_columns for col in expected_columns):
                missing_columns = [col for col in expected_columns if col not in actual_columns]
                raise ValueError(f"Несоответствие структуры данных. Отсутствуют столбцы: {missing_columns}")
            print('Заголовок корректен')
        except AttributeError:
            print('Файл не был открыт')
        except ValueError as e:
            print('Ошибка в заголовке: {e}')


