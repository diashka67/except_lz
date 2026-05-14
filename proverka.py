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
        

    def check_header(self, expected_columns, expected_type):
        try:
            actual_columns = list(self.df.columns)
            missing_columns = [col for col in expected_columns if col not in actual_columns]
            if missing_columns:
                raise ValueError(f"Несоответствие структуры данных. Отсутствуют столбцы: {missing_columns}")
            errors = []
            for col in expected_columns:
                actual_type = str(self.df[col].dtype)
                if actual_type != expected_type:
                    errors.append(f"В столбце '{col}' тип данных не соответствует ожидаемому. "
                        f"Ожидается: {expected_type}, Фактически: {actual_type}")  
            if errors:
                raise ValueError("\n".join(errors))
    
            print('Заголовок корректен')
        except AttributeError:
            print('Файл не был открыт')
        except ValueError as e:
            print(f'Ошибка в заголовке: {e}')


