import csv
import random


header =['Табельный номер',
         'ФИО',
         'Пол',
         'Год рождения',
         'Год начала работы в компании',
         'Подразделение',
         'Должность',
         'Оклад',
         'Количество выполненных проектов']
    
count_string = random.randint(1000,1100)#генерация количество строк
count = int(count_string/2)

#списки значений
tabNumber = list()
fullname = list()
gender = list()
birth = list()
year_job = list()
service = list()
job_title = list()
salary = list()
project = list()


#варианты строковых значений

first_name_man = ('Сергей','Андрей','Николай','Максим','Никита',
                  'Семен','Степан','Александр','Петр','Данил','Григорий')
last_name_man = ('Викторов','Смирнов','Иванов','Петров','Макеев',
                 'Воронцов','Романов','Лукин','Степанов','Воробьев','Романов')
middle_name_man = ('Сергеевич','Викторович','Николаевич','Андреевич','Петрович',
                   'Александрович','Денисович','Львович','Никитич','Дмитриевич','Владимирович')

first_name_woman = ('Ольга','Алена','Анастасия','Лариса','Анна',
                    'Елизовета','Юлия','Дарья','Маргарита','Татьяна','Светлана')
last_name_woman = ('Викторова','Смирнова','Иванова','Петрова','Макеева',
                   'Романова','Кольцова','Ямщикова','Сатдинова','Николаева','Воронцова')
middle_name_woman = ('Сергеевна','Викторовна','Николаевна','Андреевна','Петровна',
                     'Александровна','Владимировна','Ивановна','Данииловна','Григорьевна','Олеговна')

department = ('Канцелярия','Секретариат','Служба делопроизводства',
              'Отдел охраны труда','Служба упревления персоналом',
              'Отдел организации труда','Бухгалтерия','Служба управления персоналом',
              'Финансовое подразделение','Отдел внешнеэкономических связей',
              'Склады готовой продукции и материалов','Планово-экономический отдел',
              'Служба стандартизации','Юридическая служба','Отдел кадров',
              'Служба безопасности','Вычислительный центр')

job_rank = ('Директор','Начальник','Менеджер','Заместитель директора',
        'Офис-менержер','Секретарь','Руководитель','Главный инженер','Инженер')



number = random.sample(range(1, 1500), count_string)#генерациия уникальных табельных номеров
#добавление таб.номера в отдельный список
for num in number:
    tabNumber.append(num)

for i in range(count):

    #генерация ФИО
    fullname_man =(random.choice(last_name_man) + " "
                    + random.choice(first_name_man) + " "
                    + random.choice(middle_name_man))
    fullname.append(fullname_man)
    fullname_woman = (random.choice(last_name_woman) + " "
                      + random.choice(first_name_woman) + " "
                      + random.choice(middle_name_woman))
    fullname.append(fullname_woman)

    #генерация пола
    gender.append('муж.')
    gender.append('жен.')

for i in range(count*2):

    year = random.randint(1967,2000)#генерация года рождения
    birth.append(year)#добавление в список
    
    job = random.randint(2015,2022)#генерация начала работы
    year_job.append(job)#добавление в список

    depar = random.choice(department)#генерация подразделения
    service.append(depar)#добавление в список

    rank = random.choice(job_rank)#генерация должности
    job_title.append(rank)#добавление в список

    size_salary = random.randint(20000,65000)#генерация оклада
    salary.append(size_salary)#добавление в список

    count_project = random.randint(1,30)#генерация проектов
    project.append(count_project)#добавление в список
    

#запись данных в csv файл
with open('file.csv','w', newline='') as f:
    write = csv.DictWriter(f, fieldnames = header)
    write.writeheader()
    for i in range(count*2): 
        write.writerow({'Табельный номер': tabNumber[i], 'ФИО': fullname[i],
                        'Пол': gender[i], 'Год рождения': birth[i],
                        'Год начала работы в компании': year_job[i],
                        'Подразделение': service[i],'Должность': job_title[i],
                        'Оклад': salary[i],'Количество выполненных проектов': project[i]})


