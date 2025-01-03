from re import search
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.adult_mode = bool(adult_mode)

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, nickname):
        return any(user.nickname == nickname for user in self.users)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname:
                if user.password == hash(password):
                    self.current_user = user
                    return
                print("Неверный логин или пароль")
                return
        print("Пользователь не найден или пароль неверный")

    def register(self, nickname, password, age):

        if nickname in self:
            print(f"Пользователь {nickname} уже существует")
            return

        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None
            print(f"Выход пользователя {self.current_user.nickname} выполнен успешно")
        else:
            print("Сейчас никто не залогинен, операция невозможна")

    def add(self, *args):
        for new_video in args:
            for video in self.videos:
                if video.title == new_video.title:
                    print("Видео с таким названием уже существует")
                    return
            self.videos.append(new_video)

    def get_videos(self, search_word):
        search_word = search_word.lower()
        found_videos = []
        for video in self.videos:
            if search_word in video.title.lower():
                found_videos.append(video.title)
        return found_videos

    def watch_video(self, video_title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        if self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for video in self.videos:
            if video.title == video_title:
                for i in range(1, video.duration + 1):
                    print(i, end=' ', flush=True)
                    time.sleep(1)
                print("Конец видео", flush=True)
                return

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')