# Profile-Evaluating
Ця програма розроблена для користувачів соціальної мережі Instagram, які влаштовують конкурси та розіграші на своїх сторінках. Програма надає можливість швидко обрати переможця та перевірити, чи він виконав умови розіграшу(підписки, лайки, коментарі). Програма сама запитує необхідні дані для обробки дані. Щоб запустити процес, достатньо викликати одну функцію.

Вхідні дані програми, які вказуються користувачем, - це логін, пароль та URL-адреса посту, під яким треба буде перевіряти списки людей. Програма буде запитувати в користувача вхідні дані стільки раз, скільки він захоче додавати інформацію та списки людей для превірки. Вихідні дані - це ім'я користувача, якого було визначено, як переможця

Система має два основних великих модулі InstagramAPI.py, в якому знаходиться клас для отримання даних з соціальної мережі, та 
profile_eval.py, в якому знаходиться клас для взаємодії з користувачем та обробки отриманих даних.
Метод _ data_collecting запускає основну роботу програми та починає взаємодію з користувачем. Метод _ set_look_in встановлює масив, з якого буде проводитись пошук переможця. Методи _ add_check_subscriptions, _ add_check_likes, _ add_check_comments добавляють списки імен, серед яких треба буде присутність переможця. Метод _ check_requirements перевіряє чи виконав переможець всі умови. Метод _ return_result друкує обраного переможця для користувача
У модулі get_comments_likes знаходяться дві функції, які знаходять списки людей, які прокоментували і лайкнули конкретний пост. Ці функції також використовують методи з класу InstagramAPI.

Після запуску модуля winner_finder.py ( модуль для початку роботи програми ) з'явиться меню, яку буде пропонувати користувачу зробити дію (встановити дані, серед яких треба буде обирати переможця, встановити дані, на які треба буде перевіряти пререможця або отримати результат). Свій вибір треба подавати у вигляді числа (номер дії, яку хочете зробити). Якщо не встановити дані, з яких треба обирати переможця і попросити програму видати результат, то вона видасть повідомлення про відсутність достатньої кількості інформації та поверне в якості переможця значення -1. Коли встановлюється  значення
_ look_in, то запитується вид даних, які ви хочете встановити в цьому місці (лайки, коментарі, пілписники). Від відповіді будут залежати подальші дії. Коли користувач оприділився з тим, що й куди він хоче додати, то програма запитує в нього логін, пароль і за необхідності URL - адресу конкретного поста. Після накопичення всієї необхідної інформації, яку хоче користувач, починається пошук.

Приклад:

[1] Set a place for searching a winner.

[2] Add a post to check comments.

[3] Add a post to check likes.

[4] Add a profile to check subscriptions

[5] Start searching.

Enter a number of action: 1

Enter a number of data type you want to set(1. likes, 2. comments, 3. subscriptions): 3

Enter your username: LOGIN

Enter your password: PASSWORD

Login success!



[1] Set a place for searching a winner.

[2] Add a post to check comments.

[3] Add a post to check likes.

[4] Add a profile to check subscriptions

[5] Start searching.

Enter a number of action: 2

Enter your username: LOGIN

Enter your password: PASSWORD

Enter an url of your post: URL

Login success!

Login success!



[1] Set a place for searching a winner.

[2] Add a post to check comments.

[3] Add a post to check likes.

[4] Add a profile to check subscriptions

[5] Start searching.

Enter a number of action: 5

Your winner is  WINNER

