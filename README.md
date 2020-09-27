# mm (MissingModules)
## Инструмент для работы с недостающими модулями в питоне.

Не знаю, есть ли уже такое, но... 
Вы когда-нибудь ставили понравившийся проект на питоне с гитхаба, который оказывался без удобного файлика requirements.txt, или в котором отсутствовали рекомендации по установке необходиммых для работы модулей?
Я да, и не раз. Каждый раз приходилось эмпирическим путем ставить нужные модули, до тех пор пока питон не переставал ругаться на что-либо отсутствующее.
После очередной победы над такой ситуацией решил автоматизировать процесс, написав такую небольшую утилиту.

Пользоваться очень легко. Повторю собственно -h (--help) скрипта.
Достаточно набрать
> python mm.py -f <python_filename>

И скрипт выведет готовую команду для pip с нужными модулями.

Чтобы сформировать файл requirements.txt на будущее достаточно добавить аргумент -r (--requirements):
> python mm.py -f <python_filename> -r

 В качестве зависимости есть файл modules.csv, он нужен чтобы переставлять названия модулей для pip. Иначе он некоторые модули из-за разности названий не воспримет и выдаст ошибку, что такого модуля не существует. По мере необходимости список модулей в файле будет пополняться, но вы можете предлагать и сами какие пожелаете. 
 
 ### ТУ_значит_ДУ, или что нужно сделать:
* Рефакторинг кода. Конечно это замечательно, что все по функциям засунул, но размер это не сократило, и с названиями переменных есть косяки.

* Добавить опции с обработкой нескольких файлов (и даже по маске!), с установкой зависимостей прям из скрипта.

* Расширенный функционал с версионированием модулей, и уже непосредственная работа для всех ленивых кто не создает файл requirements.txt у себя в проектах (тут небольшая загвоздка в логике работы, что установленные модули нельзя добавить в файл).

* Когда-нибудь перевести эту всю кипу текста на английский, потому что не все знают русский (но очень лень, думаю его хватит в хелпе скрипта, и вообще учите русский, на крайний есть гуглопереводчик).
