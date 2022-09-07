# Для создания своих уведомлений через код
# pip install plyer

import os
import platform

from plyer import notification


def notify(message, title):
    if platform.system() == 'Darwin':
        os.system("osascript -e 'display notification \"{}\" with title \"{}\"'".format(message, title))
    else:
        notification.notify(
            title=title,
            message=message,
            app_icon='python.ico')


if __name__ == "__main__":
    notify('ПОБЕДА', 'Всё работает!!!')
