import flask
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify, send_file, abort
from .vk_callback_data import docs as vk_docs
from .vk_callback_data import tools as vk_tools

import traceback

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