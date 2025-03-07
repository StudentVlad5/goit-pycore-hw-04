'''
Завдання 1

У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

Вимоги до завдання:
Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.


Рекомендації для виконання:
Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.

Критерії оцінювання:
Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:
total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

Очікуваний результат:

Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
'''
from termcolor import colored
path = "./salary_file.txt" 

def total_salary(path):
    total = 0
    average = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as f:
            salary = f.readlines()
            for i in salary:
                i = i.strip()
                if not i:
                    continue 
                try:
                    name, salary_str = i.split(',')
                    salary_val = int(salary_str)
                    if salary_val < 0:
                        print(f"{colored("Check the salary value for the employee:",'yellow')} {colored(name,'red')}")
                        continue
                    else:
                        total += salary_val
                        count += 1
                except ValueError:
                    print(f"{colored("Check the salary value for the employee:","yellow")} {colored(name,'red')}")
                    continue
            if count == 0:
                print("No valid salary data found.")
                return total, average 

            average = round(total / count, 2)
            print(f"{colored("The total amount of wages:",'cyan')} {colored(total,'green')}, {colored("Average salary:", "cyan")} {colored(average, 'green')}, {colored("Current employees:", "cyan")} {colored(count, 'green')}")
            return total, average
    except FileNotFoundError:
        print('File not found')
        return total, average
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return total, average
    
total_salary(path)