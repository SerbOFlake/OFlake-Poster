# OFlake Poster
OFlake Poster — это инструмент для автоматизации постинга в Telegram. Он позволяет отправлять сообщения в каналы Telegram на основе шаблонов с использованием плейсхолдеров

# Установка

### Установка

1. Убедитесь что установлен Python 3.6 или выше
2. Установите необходимые зависимости:
  ```bash
  pip install python-telegram-bot
  ```
3. Скачайте репозиторий OFlake Poster и распакуйте его.\
   Ну или отклонируйте:
     ```bash
     git clone https://github.com/SerbOFlake/OFlake-Poster.git
     ```
### Настройка
Для ленивых был собран OOBE инструмент, запустите его при помощи:
```bash
python oobe.py
```
Первым делом будет предложенно вести токен бота, вводим его\
![изображение](https://github.com/user-attachments/assets/3ffb6c05-c2c9-4a9d-aa2d-25311a87d16e)\
Потом нужно ввести имя канала:
> [!WARNING]
> Не ID (будет предложенно потом)\
> Здесь вводится имя канала для добавления в конфигурацию, т.е. желательны простые названия и без пробелов\

![изображение](https://github.com/user-attachments/assets/0dac05e5-28f0-42a6-b54f-893e19227178)

Теперь нужно получить ID канала\
Для получения можно использовать:
  1. Моддовые клиента Телеграм на Android\
     Условный AyuGram изначально ввыводит ID каналов
  2. Использование веб версии\
     Строка веб версии содержит ID канала, переходим на канал и ещем это значение (Оно разное у всех)\
     ![Безымянный](https://github.com/user-attachments/assets/af928d72-c6ad-4c82-8d76-9430413661c0)
     > Значение должно быть отрицательным для ввода

Затем вводим значение сюда:\
![изображение](https://github.com/user-attachments/assets/86e8a690-a76e-4a28-9398-10a093ae9ae6)\
Готово!\
У вас опять появится\
![изображение](https://github.com/user-attachments/assets/0cf44f38-3c69-49d9-919b-8ed4cdee01fa)\
Если нужно добавляйте ещё каналы, если нет оставте пустую строку и нажмите Enter\
![изображение](https://github.com/user-attachments/assets/510fb08f-70c1-424c-bef0-e6eda0f4a541)
> [!TIP] 
> OOBE законченно, вы молодцы!

#### Ручная настройка
Теперь настройка вручную\
Создайте в корневой папке приложения файл ``` config.ini ```
Вставте в него следующие содержимое
```ini
[secure]
token = Here you tokenff
oobe = false

[channels]
test = -1002271321808
```
```token``` - заменить на свой токен бота\
```oobe``` - поставить в true\
В ```[channels]``` добавлять свои каналы

### Создание шаблонов (sample)
Теперь осталось дело за малым, создать свой шаблон\
Переходим в папку ```samples```
И создадим файл test.txt\
Добавим в него условно:
```
Example
Dynamic text: {$dyntext}

👻 By : https://github.com/SerbOFlake/OFlake-Poster
```
Всё что в не ```{$}``` является статическим текстом, а что в них является плейсхолдером (он же заполнитель)\
Сохраните файл

### Использование постера
Переходим к сладкому
#### Автоматизация
Представим ситуацию\
Вы очень такой общительный человек\
И хотите когда каждый раз вы используйте команду
```bash
make
```
было сообщение в группе единомышленников\
Создайте ```makefile```:
```makefile
# Переменные
CHANNEL = test
PLACEHOLDER = "I compiled something"
TEMPLATE = test.txt

# Цель для отправки сообщения
post:
	@echo "Отправка сообщения в канал $(CHANNEL)..."
	@python cli.poster.py --channel $(CHANNEL) --sample $(TEMPLATE) \
		+dyntext "$(PLACEHOLDER)" \
	@echo "Сообщение отправлено!"

# Цель для очистки (если необходимо)
clean:
	@echo "Очистка..."

# Цель по умолчанию
.PHONY: post clean
```
Теперь при
```bash
make post
```
будет сообщение в нашем канале о том что бы что-то скомпилировали\
А если нужно чисто CLI то вот
```bash
python cli.poster.py --channel test --sample test.txt +dyntext "Я молодец!"
```
#### Ручной ввод
Запускаем постер:
```bash
python poster.py
```
Появится:\
![изображение](https://github.com/user-attachments/assets/07f34d76-f04f-4a50-acf2-b69e05277a0a)\
Здесь нужно ввести наш канал (Название, не ID)
> [!NOTE]
> Название которые мы задавали в конфигурацию

Теперь нам нужно указать на шаблон (sample):\
![изображение](https://github.com/user-attachments/assets/9435c72e-4ad0-41a0-b9a4-a6a6c46dc58b)\
В нашем случае ```test.txt```
Появится следующие строки:\
![изображение](https://github.com/user-attachments/assets/748f7a15-f656-4752-a6fa-d91294d73a76)\
До ```🪵 Available placeholders: dyntext``` идёт содержимое шаблона для понимания где что\
В ```🪵 Available placeholders: dyntext``` нам показывают какие плейсхолдеры есть\
В 
```
🪵 Enter placeholder: dyntext
🪵 Enter content:
```
Выберается плейсхолдер по очереди и нам предлагают написать что туда написать\
Для переноса строк используйте ```\n```
Вводим условно:\
![изображение](https://github.com/user-attachments/assets/1fd1864f-329b-4ea7-acb1-422b6e92f78e)\
Вывод в консоль будет следующим:\
![sss](https://github.com/user-attachments/assets/81f2ccfe-ecf5-4d9e-8255-4e7199fafcb6)\
А в канале будет следующий:\
![изображение](https://github.com/user-attachments/assets/3a64cfb4-6235-400d-8986-c539b6477f15)
