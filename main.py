from proverka import Check 
def main():

    file = Check()
    file.open_file()
    
    if file.df is not None:
        file.check_structure()
        file.check_empty()
        file.check_header(["Участники гражданского оборота", "Тип операции", "Сумма операции",
                    "Вид расчета","Место оплаты","Терминал оплаты","Дата оплаты","Время оплаты",
                    "Результат операции", "Cash-back","Сумма cash-back"])  
    else:
        print(" Программа завершена: файл не был открыт")

if __name__ == "__main__":
    main()