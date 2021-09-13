import flask, traceback
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify, send_file, abort


class vk_docs:  # Fuck you twine!!!
    hostname = 'http://localhost:5050'

    docs_info = {
    "ru": '''<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Как подключить callback</title>
		<style>
			body {
				background-color: #9BC4FF;
			}
			.main{
				margin-left: 20%;
				margin-right: 20%;
				// height: 100%;
				padding-top: 1%;
				padding-bottom: 1%;
				padding-left: 2%;
				padding-right: 3%;
				background-color: #fff;
				border-radius: 10px;
			}
			.code_window {
				padding-top: 0.5%;
				padding-bottom: 0.75%;
				padding-left: 2%;
				padding-right: 3%;
				border-radius: 10px;
				color: #fff;
				background-color: #1E1E1E;
			}
		</style>
	</head>
	<body>
		<div class="main">
			<h1><center>Введение и написание кода</center></h1>
			<p style="margin-left: 50px;">Наш модуль написан для работы с <strong>callback</strong> событиями серверов vk.com и создания ботов на принципе <strong>callback</strong>. Этот метод подходит для нагруженных проектов, которые соединяют в себе несколько ботов, образуя сеть ботов.</p>
			<p style="margin-left: 50px;">Итак, наш модуль имеет следующие классы: <strong>server</strong>, <strong>group</strong>, <strong>vk_event</strong>, <strong>vk_callbackException</strong>. Чтобы вы могли написать бота, вам нужны только <strong>два</strong> из них: <strong>server</strong> и <strong>group</strong>. Перейдём непосрдественно к коду:</p>
			<p style="margin-left: 50px;">Для начала, мы должны создать класс, который наследуется от класса <strong>server</strong> и создадим там метод <strong>event</strong> со следующими аргументами:</p>
			<div style="margin-left: 75px;" class="code_window"><code><pre><font color="#3786D4">import</font> <font color="#E090D0">vk_callback</font>


<font color="#3786D4">class</font> <font color="#3CC77E">bot</font><font color="#B4B4B4">(<font color="#E090D0">vk_callback</font>.server):</font>
    <font color="#3786D4">def</font> event<font color="#B4B4B4">(self, group_obj, Event):</font>
        <font color="#3786D4">pass</font>  <font color="#4BA440"># Сюда будем писать код</font></pre></code></div>
			<p style="margin-left: 50px;"><strong>group_obj</strong> отвечает за объект группы, <strong>Event</strong> - это объект события.</p>
			<p style="margin-left: 50px;">У <strong>group_obj</strong> есть следующие параметры: <strong>id</strong>, <strong>return_str</strong>, <strong>secret_key</strong>. Для разработки бота нам достаточно только <strong>id</strong>, где <strong>id</strong> это id группы.</p>
			<p style="margin-left: 50px;">У <strong>Event</strong> есть следующие параметры: <strong>type</strong>, <strong>object</strong>, <strong>group_id</strong>, <strong>event_id</strong>, <strong>secret</strong> <i>(всё тоже самое, что и в объекте события вк)</i>. Для <strong>object</strong> это словарь с параметрами объекта события.</p>
			<p style="margin-left: 50px;">Проверять секретный ключ нет необходимости, за это отвечает метод класса <strong>confirmation_secret</strong>. Перейдём же к самому интересному... Давайте подключим двух ботов и сделаем для них разные ответы, чтобы отчётливее продемонстрировать возможности ботов:</p>
			<p style="margin-left: 50px;">К нашему методу <strong>event</strong> мы добавим код, который мы хотим реализовать. Далее, мы ниже создаём объект класса <strong>bot</strong> и добавляем туда объекты класса <strong>group</strong>, которые будут являться объектами групп, к которым мы подключили callback. Затем, запускаем нашего бота</p>
			<div style="margin-left: 75px;" class="code_window"><code><pre><font color="#3786D4">import</font> <font color="#E090D0">vk_callback</font>
<font color="#3786D4">import</font> <font color="#E090D0">vk_api</font>
<font color="#3786D4">import</font> <font color="#E090D0">random</font>


<font color="#3786D4">class</font> <font color="#3CC77E">bot</font><font color="#B4B4B4">(<font color="#E090D0">vk_callback</font>.server):</font>
    <font color="#3786D4">def</font> event<font color="#B4B4B4">(self, group_obj, Event):</font>
        <font color="#3CC77E">bot_1</font> = <font color="#E090D0">vk_api</font>.VkApi<font color="#B4B4B4">(token=<font color="#CAA48D">'***'</font>)</font>.get_api<font color="#B4B4B4">()</font>
        <font color="#3CC77E">bot_2</font> = <font color="#E090D0">vk_api</font>.VkApi<font color="#B4B4B4">(token=<font color="#CAA48D">'***'</font>)</font>.get_api<font color="#B4B4B4">()</font>
        <font color="#3786D4">if</font> Event.type == <font color="#CAA48D">'message_new'</font>:
            <font color="#3786D4">if</font> group_obj.id <font color="#3CC77E">==</font> <font color="#AEC68B">12345678</font>:
                <font color="#3CC77E">bot_1</font>.messages.send<font color="#B4B4B4">(peer_id=Event.object[<font color="#CAA48D">'peer_id'</font>], random_id=<font color="#E090D0">random</font>.randint(<font color="#AEC68B">0</font>, <font color="#AEC68B">999999</font>), message=<font color="#CAA48D">'hello'</font>)</font>
            <font color="#3786D4">else</font>:
                <font color="#3CC77E">bot_2</font>.messages.send<font color="#B4B4B4">(peer_id=Event.object[<font color="#CAA48D">'peer_id'</font>], random_id=<font color="#E090D0">random</font>.randint(<font color="#AEC68B">0</font>, <font color="#AEC68B">999999</font>), message=<font color="#CAA48D">'hi'</font>)</font>


<font color="#3CC77E">bot = bot</font><font color="#B4B4B4">(host=<font color="#CAA48D">'website.ru'</font>, groups=[
    <font color="#E090D0">vk_callback</font>.group(<font color="#AEC68B">12345678</font>, return_str=<font color="#CAA48D">"11693324"</font>, secret_key=<font color="#CAA48D">"secret_key_here"</font>),
    <font color="#E090D0">vk_callback</font>.group(<font color="#AEC68B">87654321</font>, return_str=<font color="#CAA48D">"1af47ed9"</font>, secret_key=<font color="#CAA48D">"secret_key_here"</font>)
], port=<font color="#AEC68B">8080</font>)</font>

<font color="#3CC77E">bot</font>.start</font><font color="#B4B4B4">()</font></pre></code></div>
			<h1><center>Как подключить callback</center></h1>
			<p style="margin-left: 50px;">Подключить callback сервер к вашей группе очень просто! Для начала, заходим в <strong>настройки</strong> группы в <strong>раздел "работа с API"</strong>, затем заходим в раздел <strong>callback</strong></p>
			<center><img style="padding: 20px;" src="https://sun9-57.userapi.com/impg/Jogfj3OsY_xyuNEF4M-HEWe3e24cdDk6cRX0AA/Bk3gEoReG6Y.jpg?size=269x376&quality=96&sign=88463dfda09f6aef6e7c528b42cc6ab8&type=album">
			<img style="padding: 20px;" src="https://sun9-62.userapi.com/impg/jcRz3MvCZW_KtVCUxj7h86kw5OZ1bAJr4q8kjA/bCVd8lfNkt8.jpg?size=303x375&quality=96&sign=cc2fe5fd4219949bb1855c732d0cf69c&type=album">
			<img style="padding: 20px;" src="https://sun9-32.userapi.com/impg/kJfCW-DARk8IL_3rLR2rfUM_ppmsIkmBNXbMkg/YoRGtYyKFYQ.jpg?size=837x367&quality=96&sign=c085c3d12d9a91e6e1e97fe5a1d527c8&type=album">
			<img style="padding: 20px;" src="https://sun9-66.userapi.com/impg/XAgcnRlwNLPwTdImYPHDITc6rLqPFfDvAfS21A/Cs3_eTHTUXc.jpg?size=856x723&quality=96&sign=7217365695b56388fb0f066a5bde1938&type=album"></center>
			<p style="margin-left: 50px;">Затем, нам нужно выбрать в настройках события, которые мы будем обрабатывать</p>
			<center><img style="padding: 20px;" src="https://sun9-39.userapi.com/impg/1jaRM-pVQtzr7MrU-R8IEduz0pt_Qw20XpGb4A/uqPbt6mTe0w.jpg?size=281x68&quality=96&sign=37b79a0655b143b07691ef6440b994aa&type=album">
			<img style="padding: 20px;" src="https://sun9-27.userapi.com/impg/4KPpCeQxmyGooGH2IXUQenrDIlTaTJmDby6sLw/QFhsUyZrZoM.jpg?size=810x904&quality=96&sign=375333776cd7dce46e2b7b50e50d0b50&type=album">
			<img style="padding: 20px;" src="https://sun9-61.userapi.com/impg/gIitBJWAJ8hm0Zz-va0pV-wICRSaRmcO6j3mFw/WMEfCBBuBWk.jpg?size=826x896&quality=96&sign=39a95b6ba16934c2d232fbb7443f3c06&type=album"></center>
			<p style="margin-left: 50px;">Отлично! Теперь мы можем приступить к подключению нашего сервера. Для начала, скопируем что должен вернуть при подтверждении бот и его секретный ключ и вставим в код нашей программы, также скинем в объект айди нашей группы.</p>
			<center><img style="padding: 20px;" src="https://sun9-5.userapi.com/impg/z8EQ5KdAsFxYmv9SzlTygkRcTJEoZTxHeL8SKQ/GyGdePFzyl4.jpg?size=539x338&quality=96&sign=a92e7882817f4d5c60c5194918c6cf1c&type=album">
			<img style="padding: 20px;" src="https://sun9-56.userapi.com/impg/niofrtPBSDxNu80iB8zkweRaVaY6bUFlWQBcDg/kZAVR5ptxaE.jpg?size=676x287&quality=96&sign=947319adf34edb353dc0be4d74bed670&type=album"></center>
			<p>Запускаем сервер, в графе адреса заполняем адрес нашего сервера в формате crthst::rpl/айди_группы</p>
			<center><img style="padding: 20px;" src="https://sun9-76.userapi.com/impg/8-l1K1DhDmS_SVAt1W7v2ah3jLzcdoM9Z70ymQ/7qAacDzpVYU.jpg?size=459x140&quality=96&sign=8d4bed4c1f4861a25cf7bb44e6ea2f5d&type=album"></center>
			<p>Жмём <strong>подтвердить</strong>. Поздравляем, бот подключен!</p>
		</div>
	</body>
</html>''',
    "en": '''<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Как подключить callback</title>
		<style>
			body {
				background-color: #9BC4FF;
			}
			.main{
				margin-left: 20%;
				margin-right: 20%;
				// height: 100%;
				padding-top: 1%;
				padding-bottom: 1%;
				padding-left: 2%;
				padding-right: 3%;
				background-color: #fff;
				border-radius: 10px;
			}
			.code_window {
				padding-top: 0.5%;
				padding-bottom: 0.75%;
				padding-left: 2%;
				padding-right: 3%;
				border-radius: 10px;
				color: #fff;
				background-color: #1E1E1E;
			}
		</style>
	</head>
	<body>
		<div class="main">
			<h1><center>Introduction and code writing</center></h1>
			<p style="margin-left: 50px;">Our module is designed to work with server callback events vk.com and creating bots based on <strong>the callback principle</strong>. This method is suitable for loaded projects that combine several bots to form a network of bots.</p>
			<p style="margin-left: 50px;">So, our module has the following classes: <strong>server</strong>, <strong>group</strong>, <strong>vk_event</strong>, <strong>vk_callbackException</strong>. In order for you to write a bot, you only need <strong>two</strong> of them: <strong>server</strong> & <strong>group</strong>. Let's go straight to the code:</p>
			<p style="margin-left: 50px;">First, we need to create a class that inherits from the <strong>server</strong> class and create the <strong>event</strong> method there with the following arguments:</p>
			<div style="margin-left: 75px;" class="code_window"><code><pre><font color="#3786D4">import</font> <font color="#E090D0">vk_callback</font>


<font color="#3786D4">class</font> <font color="#3CC77E">bot</font><font color="#B4B4B4">(<font color="#E090D0">vk_callback</font>.server):</font>
    <font color="#3786D4">def</font> event<font color="#B4B4B4">(self, group_obj, Event):</font>
        <font color="#3786D4">pass</font>  <font color="#4BA440"># Here we will write the code</font></pre></code></div>
			<p style="margin-left: 50px;"><strong>group_obj</strong>  is responsible for the group object, <strong>Event</strong> is the event object.</p>
			<p style="margin-left: 50px;"><strong>group_obj</strong> has the following parameters: <strong>id</strong>, <strong>return_str</strong>, <strong>secret_key</strong>. To develop a bot, we only need an <strong>id</strong>, where <strong>id</strong> is the group id.</p>
			<p style="margin-left: 50px;"><strong>Event</strong> has the following parameters: <strong>type</strong>, <strong>object</strong>, <strong>group_id</strong>, <strong>event_id</strong>, <strong>secret</strong> <i>(all the same as in the vk event object)</i>. For <strong>object</strong>, this is a dictionary with parameters for the event object.</p>
			<p style="margin-left: 50px;">There is no need to check the secret key.The method of the <strong>confirmation_secret</strong> class is responsible for this. Let's move on to the most interesting part... Let's connect two bots and make different responses for them to better demonstrate the capabilities of bots:</p>
			<p style="margin-left: 50px;">To our <strong>event</strong> method, we will add the code that we want to implement. Next, we create an object of the <strong>bot</strong> class below and add objects of the <strong>group</strong>classthere, which will be objects of the groups to which we connected the callback. Then, we launch our bot</p>
			<div style="margin-left: 75px;" class="code_window"><code><pre><font color="#3786D4">import</font> <font color="#E090D0">vk_callback</font>
<font color="#3786D4">import</font> <font color="#E090D0">vk_api</font>
<font color="#3786D4">import</font> <font color="#E090D0">random</font>


<font color="#3786D4">class</font> <font color="#3CC77E">bot</font><font color="#B4B4B4">(<font color="#E090D0">vk_callback</font>.server):</font>
    <font color="#3786D4">def</font> event<font color="#B4B4B4">(self, group_obj, Event):</font>
        <font color="#3CC77E">bot_1</font> = <font color="#E090D0">vk_api</font>.VkApi<font color="#B4B4B4">(token=<font color="#CAA48D">'***'</font>)</font>.get_api<font color="#B4B4B4">()</font>
        <font color="#3CC77E">bot_2</font> = <font color="#E090D0">vk_api</font>.VkApi<font color="#B4B4B4">(token=<font color="#CAA48D">'***'</font>)</font>.get_api<font color="#B4B4B4">()</font>
        <font color="#3786D4">if</font> Event.type == <font color="#CAA48D">'message_new'</font>:
            <font color="#3786D4">if</font> group_obj.id <font color="#3CC77E">==</font> <font color="#AEC68B">12345678</font>:
                <font color="#3CC77E">bot_1</font>.messages.send<font color="#B4B4B4">(peer_id=Event.object[<font color="#CAA48D">'peer_id'</font>], random_id=<font color="#E090D0">random</font>.randint(<font color="#AEC68B">0</font>, <font color="#AEC68B">999999</font>), message=<font color="#CAA48D">'hello'</font>)</font>
            <font color="#3786D4">else</font>:
                <font color="#3CC77E">bot_2</font>.messages.send<font color="#B4B4B4">(peer_id=Event.object[<font color="#CAA48D">'peer_id'</font>], random_id=<font color="#E090D0">random</font>.randint(<font color="#AEC68B">0</font>, <font color="#AEC68B">999999</font>), message=<font color="#CAA48D">'hi'</font>)</font>


<font color="#3CC77E">bot = bot</font><font color="#B4B4B4">(host=<font color="#CAA48D">'website.ru'</font>, groups=[
    <font color="#E090D0">vk_callback</font>.group(<font color="#AEC68B">12345678</font>, return_str=<font color="#CAA48D">"11693324"</font>, secret_key=<font color="#CAA48D">"secret_key_here"</font>),
    <font color="#E090D0">vk_callback</font>.group(<font color="#AEC68B">87654321</font>, return_str=<font color="#CAA48D">"1af47ed9"</font>, secret_key=<font color="#CAA48D">"secret_key_here"</font>)
], port=<font color="#AEC68B">8080</font>)</font>

<font color="#3CC77E">bot</font>.start</font><font color="#B4B4B4">()</font></pre></code></div>
			<h1><center>How to connect callback</center></h1>
			<p style="margin-left: 50px;">Connecting a callback server to your group is very simple! First, go to the <strong>group settings</strong> in the <strong>"API usage"</strong>, section, then go to the <strong>callback</strong> section</p>
			<center><img style="padding: 20px;" src="https://sun9-57.userapi.com/impg/Jogfj3OsY_xyuNEF4M-HEWe3e24cdDk6cRX0AA/Bk3gEoReG6Y.jpg?size=269x376&quality=96&sign=88463dfda09f6aef6e7c528b42cc6ab8&type=album">
			<img style="padding: 20px;" src="https://sun9-62.userapi.com/impg/jcRz3MvCZW_KtVCUxj7h86kw5OZ1bAJr4q8kjA/bCVd8lfNkt8.jpg?size=303x375&quality=96&sign=cc2fe5fd4219949bb1855c732d0cf69c&type=album">
			<img style="padding: 20px;" src="https://sun9-32.userapi.com/impg/kJfCW-DARk8IL_3rLR2rfUM_ppmsIkmBNXbMkg/YoRGtYyKFYQ.jpg?size=837x367&quality=96&sign=c085c3d12d9a91e6e1e97fe5a1d527c8&type=album">
			<img style="padding: 20px;" src="https://sun9-66.userapi.com/impg/XAgcnRlwNLPwTdImYPHDITc6rLqPFfDvAfS21A/Cs3_eTHTUXc.jpg?size=856x723&quality=96&sign=7217365695b56388fb0f066a5bde1938&type=album"></center>
			<p style="margin-left: 50px;">Then, we need to select the events that we will process in the settings</p>
			<center><img style="padding: 20px;" src="https://sun9-39.userapi.com/impg/1jaRM-pVQtzr7MrU-R8IEduz0pt_Qw20XpGb4A/uqPbt6mTe0w.jpg?size=281x68&quality=96&sign=37b79a0655b143b07691ef6440b994aa&type=album">
			<img style="padding: 20px;" src="https://sun9-27.userapi.com/impg/4KPpCeQxmyGooGH2IXUQenrDIlTaTJmDby6sLw/QFhsUyZrZoM.jpg?size=810x904&quality=96&sign=375333776cd7dce46e2b7b50e50d0b50&type=album">
			<img style="padding: 20px;" src="https://sun9-61.userapi.com/impg/gIitBJWAJ8hm0Zz-va0pV-wICRSaRmcO6j3mFw/WMEfCBBuBWk.jpg?size=826x896&quality=96&sign=39a95b6ba16934c2d232fbb7443f3c06&type=album"></center>
			<p style="margin-left: 50px;">Great! Now we can start connecting our server. To begin with, we will copy what the bot should return when confirming and its secret key and paste it into the code of our program, as well as throw it into the ID object of our group.</p>
			<center><img style="padding: 20px;" src="https://sun9-5.userapi.com/impg/z8EQ5KdAsFxYmv9SzlTygkRcTJEoZTxHeL8SKQ/GyGdePFzyl4.jpg?size=539x338&quality=96&sign=a92e7882817f4d5c60c5194918c6cf1c&type=album">
			<img style="padding: 20px;" src="https://sun9-56.userapi.com/impg/niofrtPBSDxNu80iB8zkweRaVaY6bUFlWQBcDg/kZAVR5ptxaE.jpg?size=676x287&quality=96&sign=947319adf34edb353dc0be4d74bed670&type=album"></center>
			<p>Starting the server, in the address column, fill in the address of our server in the format crthst::rpl/group_id</p>
			<center><img style="padding: 20px;" src="https://sun9-76.userapi.com/impg/8-l1K1DhDmS_SVAt1W7v2ah3jLzcdoM9Z70ymQ/7qAacDzpVYU.jpg?size=459x140&quality=96&sign=8d4bed4c1f4861a25cf7bb44e6ea2f5d&type=album"></center>
			<p>Click <strong>confirm</strong>. Congratulations, the bot is connected!</p>
		</div>
	</body>
</html>'''
    }

    for lang in docs_info:
        docs_info[lang] = docs_info[lang].replace('crthst::rpl', hostname)


class vk_tools:  # Fuck you PyPl!!!
    def repl_to_dict(args):
        # print(args)
        data = dict()
        for arg in args:
            data[arg] = args[arg]
        # print(data)
        return data


app = Flask(__name__)


class vk_callbackException(Exception):
    pass


class vk_event:
    def __init__(self, type, object, group_id, event_id, secret):
        self.type = type
        self.object = object
        self.group_id = group_id
        self.event_id = event_id
        self.secret = secret


class group:
    def __init__(self, id: int, return_str: str, secret_key: str):
        self.id = id
        self.return_str = return_str
        self.secret_key = secret_key


class server:
    def __init__(self, host: str, groups=[], port=False):
        self.host = host
        self.port = port
        self.groups = [Group for Group in groups if type(Group) is group]
        
        if len(self.groups) == 0:
            raise vk_callbackException('groups given null')
        self.group_dict = dict()
        for Group in groups:
            self.group_dict[Group.id] = Group
    
    def confirmation_secret(self, group_obj, Event):
        if Event.secret != group_obj.secret_key:
            return "Invalid secret key"
        elif Event.type == 'confirmation':
            self.event(group_obj, Event)
            return 'ok'
            return group_obj.return_str
    
    def event(self, group_obj, Event):
        return group_obj.return_str
    
    def start(self, print_serverInfo=print, show_documentation=True, default_lang='ru'):
        global app
        if default_lang not in vk_docs.docs_info:
            default_lang = 'en'
        flask.print = print_serverInfo
        if self.port is None:
            vk_docs.hostname = self.host
        else:
            vk_docs.hostname = f"http://{self.host}:{self.port}"
        
        @app.route('/', methods=['GET', 'POST'])
        def get_docs_dl():
            return redirect('/documentation/%s' % default_lang)
        
        @app.route('/documentation', methods=['GET', 'POST'])
        def get_docs_dl_doc():
            return redirect('/documentation/%s' % default_lang)
        
        @app.route('/documentation/<lang>', methods=['GET', 'POST'])
        def get_docs(lang):
            if not(show_documentation):
                return abort(404)
            
            if lang not in vk_docs.docs_info:
                return redirect('/documentation/%s' % default_lang)
            else:
                return vk_docs.docs_info[lang]
        
        @app.route('/<group_id>', methods=['GET', 'POST'])
        def upload_event(group_id):
            try:
                if int(group_id) in self.group_dict:
                    POST_DATA = request.json
                    # print(POST_DATA)
                    if 'event_id' in vk_tools.repl_to_dict(POST_DATA) and 'secret' in vk_tools.repl_to_dict(POST_DATA):
                        if 'object' in POST_DATA:
                            event_object = vk_event(
                                type=POST_DATA['type'],
                                object=POST_DATA['object'],
                                group_id=POST_DATA['group_id'],
                                event_id=POST_DATA['event_id'],
                                secret=POST_DATA['secret']
                            )
                        else:
                            event_object = vk_event(
                                type=POST_DATA['type'],
                                object=None,
                                group_id=POST_DATA['group_id'],
                                event_id=POST_DATA['event_id'],
                                secret=POST_DATA['secret']
                            )
                        return self.confirmation_secret(self.group_dict[int(group_id)], Event=event_object)
                    else:
                        return "It's request not from vk.com, go away!"
                else:
                    return "<strong>Unknown group</strong>"
            except:
                return f"<strong>{traceback.format_exc()}</strong>"
        
        if self.port is None:
            return app.run(host=self.host)
        else:
            return app.run(host=self.host, port=self.port)