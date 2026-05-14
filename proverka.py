import pandas as pd

class Check:

    def __init__(self):
        self.df = None

    def open_file(self):
        try:
            name_file = input('Введите имя файла: ')
            if name_file != 'var5.csv':
                raise ValueError('ПЕРЕСМОТРИ НАЗВАНИЕ ФАЙЛА!!!')
            
            self.df = pd.read_csv(name_file)
            print('Файл открыт')
            return True
            
        except (FileNotFoundError, ValueError) as e:
            print(e)  
        except pd.errors.ParserError:
            print("Файл поврежден или имеет неверный формат")
        except Exception:
            print('Не удалось открыть файл')
        
        return False

    def check_empty(self):
        try:
            if self.df.empty: 
                raise pd.errors.EmptyDataError
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
            if actual_columns != expected_columns:
                raise ValueError
            print('Заголовок корректен')
        except AttributeError:
            print('Файл не был открыт')
        except ValueError:
            print('Ошибка в первом ряду: заголовок не соответствует ожидаемому')

    def check_data_types(self):
        if self.df is None:
            print('Файл не был открыт')
            return False
        errors = []

        # Проверка того что с числами
        cols = ['Сумма операции', 'Сумма cash-back']
        existing_cols = [c for c in cols if c in self.df.columns]

        #пытаемся преобразовать значения в выбранных столбцах (existing_cols) датафрейма в числовой тип.
        #параметр errors='coerce' говорит, что значения, которые не могут быть преобразованы в число, должны быть заменены на NaN(не число). 
        #метод .isna().any() проверяет, есть ли хотя бы одно значение NaN в любом из этих столбцов.
        check = self.df[existing_cols].apply(pd.to_numeric, errors='coerce').isna().any()

        # ключ (col) представляет собой название столбца, а значение (has_error) указывает на наличие ошибки. 
        # код итерирует по этим парам, чтобы определить, какие столбцы содержат некорректные данные
        for col, has_error in check.items():
            if has_error:
                errors.append(f'{col} — содержит нечисловые значения')
            else:
                print(f'{col} — все числа корректны')

        # Проверка даты
        try:
            pd.to_datetime(self.df['Дата оплаты'], format='%d-%m-%Y', errors='raise')
            print('Дата оплаты — все норм')
        except:
            errors.append('Дата оплаты — неверный формат')

        # Проверка времени
        try:
            pd.to_datetime(self.df['Время оплаты'], format='%H:%M:%S', errors='raise')
            print('Время оплаты — все норм')
        except:
            errors.append('Время оплаты — неверный формат')

        # Проверка Cash-back
        if 'Cash-back' in self.df.columns:
        # isin проверяет каждую ячейку на наличие да или нет
        # .all() проверяет, чтобы условие выполнилось абсолютно для всех строк.
            if not self.df['Cash-back'].isin(['да', 'нет']).all():
                errors.append('Cash-back — содержит недопустимые значения')

        if errors:
            print('\nНайдены ошибки:')
            for e in errors:
                print(f'- {e}')
            return False
        else:
            return True
