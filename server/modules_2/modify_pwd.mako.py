# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1502268956.3273702
_enable_loop = True
_template_filename = 'htdocs/modify_pwd.mako'
_template_uri = 'modify_pwd.mako'
_source_encoding = 'utf-8'
_exports = ['add_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'root.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        password_title = context.get('password_title', UNDEFINED)
        username_title = context.get('username_title', UNDEFINED)
        newpassword_title = context.get('newpassword_title', UNDEFINED)
        submit_text = context.get('submit_text', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="header">\n    <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n</div>\n<div class="registration_form" class="block">\n    <form method="post" class="login form">\n        <table>\n            <tr>\n                <td>')
        __M_writer(str(username_title))
        __M_writer('</td>\n                <td><input type="text" name="username"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(password_title))
        __M_writer('</td>\n                <td><input type="password" name="password"/></td>\n            </tr>\n            <tr>\n                <td>')
        __M_writer(str(newpassword_title))
        __M_writer('</td>\n                <td><input type="password" name="newpassword"/></td>\n            </tr>\n            <tr>\n               <td><input type="submit" name="form.commit"\n                        value="')
        __M_writer(str(submit_text))
        __M_writer('"/></td>\n            </tr>\n        </table>\n    </form>\n</div>\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_add_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script type="text/javascript">\n        $(document).ready(function() {\n            bookie.login.init();\n        });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "modify_pwd.mako", "source_encoding": "utf-8", "filename": "htdocs/modify_pwd.mako", "line_map": {"36": 1, "37": 4, "38": 4, "39": 10, "40": 10, "41": 14, "42": 14, "43": 20, "44": 20, "45": 32, "51": 26, "55": 26, "27": 0, "61": 55}}
__M_END_METADATA
"""
