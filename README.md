## Проект мобильных автотестов на приложение Wikipedia

<!-- Описание -->

## :open_book: Описание
В проекте представлены примеры мобильной автоматизации тестирования на Python. 
<p>Реализован параметризированный запуск тестов на эмуляторе, реальном устройстве и ферме browserstack
<p>Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео, etc). 
<p>В тестах шаги отображены в виде лямбда-степов через with allure.step
<p>Также по факту прохождения теста отправляется уведомление с результатами в Telegram.
<p>Реализована интеграция с Allure TestOps.

## :heavy_check_mark: Кратко
- [x] Кастомный локальный запуск с использованием `Android Studio` или `Browserstack`
- [x] Удаленный запуск с использованием `Jenkins` и `Browserstack`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Интеграция с `Allure TestOps`
- [x] Отправка результатов тестирования в `Telegram`

<!-- Технологии -->

## :gear: Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/android_studio.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/appium.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/browserstack.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
<!--   <code><img width="5%" title="Jira" src="images/logo/jira.png"></code> -->
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

## :heavy_check_mark: Что проверяют тесты

- [x] Работу поиска
- [x] Сохранение результатов поиска
- [x] Заголовки onboardind screen
- [x] Добавление языка
- [x] Удаление языка 


<!-- Jenkins -->

## <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/003_t1me0ver_python_wikipedia_app/)

Для запуска тестов из Jenkins:
Нажмите кнопку "Собрать сейчас"

<p><img src="images/screenshots/Jenkins-1.png" alt="Jenkins"/></p>

<!-- Browserstack -->

### <img width="5%" title="Browserstack" src="images/logo/browserstack.png"> Запуск проекта в [Browserstack](https://app-automate.browserstack.com/dashboard/v2/builds/65244ceb48f2f2b65acc631d3c24a9359e0e63dc/sessions/4e836aedbcf9a24ccb8eecd0677bca5a6b5b00fb)
##### После запуска сборки в Jenkins, тесты начинают проходить удаленно через Browserstack. Где в реальном времени можно следить за прохождением теста через логи.

<p><img src="images/screenshots/Browserstack-1.png" alt="Browserstack"/></p>

<!-- Локальный запуск -->

## :computer: Локальный запуск 

Для локального запуска:
1. Склонируйте репозиторий
2. Установите Poetry `poetry install`
3. Откройте проект в PyCharm, установите интерпретатор
4. Запустите BrowserStack
   - Получите ваш username, access key и загрузите apk из папки resources для получения app id
6. Установите Android Studio и Appium
   - Запустите Appim Server
   - Запустите в Android Studio эмуляцию устройства
   - Введите в командной строке `adb devices` для проверки, что устройство доступно
7. Создайте `env` файлы по образцам в папке проекта:
    - `config.browserstack.env` с вашими данными
9. Запустите тесты в PyCharm через командную строку: 
```bash
env -S "context=browserstack" pytest . --alluredir allure-results/
```
10. Проверьте статус запуска в BrowserStack

### :heavy_plus_sign: Параметры сборки

> - env -S "context=browserstack" - запуск через browserstack
> - env -S "context=real" запуск на реально подклченном устройстве
> - env -S "context=emulation" запуск через эмулятор

Обязательно создавать env файлы по образцу из проекта

<!-- Отчеты -->

## :bar_chart: Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке: 
```bash
allure serve 
```

### <img width="3%" title="Allure" src="images/logo/allure_report.png"> Allure

#### Примеры отображения тестов

<img src="images/screenshots/Allure-1.png" alt="Allure"/>

### <img width="2.5%" title="Telegram" src="images/logo/tg.png"> Telegram

Настроена отправка отчета в Telegram

<img src="images/screenshots/Telegramm-1.png" alt="Telegram"/>

<!-- Allure TestOps -->

## :briefcase: Проект интегрирован с Allure TestOps 

#### Автоматически собраны тест-кейсы

<img src="images/screenshots/Allure-2.png" alt="Allure TestOps"/>

#### Представлены дашборды аналитики

<img src="images/screenshots/Allure-3.png" alt="Allure TestOps"/>
