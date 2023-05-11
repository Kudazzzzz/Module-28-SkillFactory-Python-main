valid_email = "ikud65666@gmail.com"
valid_pass = "ZXc!12345"

invalid_email = 'Qwertybasd333222@gmail.com'
invalid_pass = 'Asd99999'

name = 'Иван'
surname = 'Куд'
region = 'Москва г'
email = 'Siiinusoid@yandex.ru'
password = 'Asd77777'

false_email = '123456'
false_mobile_max = '891178945236'
false_mobile_mini = '8911789452'
false_name_mini = 'А'
name_two_letters = "Он"
thirty_letters = 'Ывавпуппупупупрвапвпвпврипапак'
thirty_one_letters = 'Ывавпуппупупупрвапвпвпврипапакв'

class TestData:
    BASE_URL = 'https://b2c.passport.rt.ru/'

    #Заголовки названий элементов
    FORM_AUTH_MAIL = 'Почта'
    AUTH = 'Авторизация'
    RECOVERY = 'Восстановление пароля'
    CHECK = 'Регистрация'
    VERIFICATION_EMAIL = 'Подтверждение email'
    VERIFICATION_INVALID_EMAIL = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    VERIFICATION_INVALID_NAME = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    ENTRY_VK = 'Войти'
    OK = 'Одноклассники'
    CHOICE_ACCOUNT = 'Вход'
    MM = 'Войти и разрешить'
