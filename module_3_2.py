def send_email(massage, recipient, sender="university.help@gmail.com"):
    check_progression = True
    while True:
        if "@" not in sender or "@" not in recipient:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            check_progression = False
            break
        else:
            if sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'):
                if recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net'):
                    break
                else:
                    print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                    check_progression = False
                    break
            else:
                print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
                check_progression = False
                break
    while check_progression:
        if recipient == sender:
            print("Нельзя отправить письмо самому себе!")
            break
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
            break
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            break




send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
