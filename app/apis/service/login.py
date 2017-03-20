
""" auth apis file """

import json
from flask_restful import reqparse, fields
from ...util.result.result import BaseResource
from ...model import db, User


RESULT = {
    'result': fields.String,
    'message': fields.String,
    'response': fields.Nested(fields.String)
}


class Login(BaseResource):
    """ Login apis class model """

    def __init__(self):
        """ init class model """
        super(Login, self).__init__()
        self.parse = reqparse.RequestParser()
        self.date_base = db.session
        self.parse.add_argument('username', type=str, required=True, help='请输入用户名')
        self.parse.add_argument('password', type=str, required=True, help='请输入登录密码')

    def get(self):
        """用户登录"""
        args = self.parse.parse_args()
        user = self.date_base.query(User).filter_by(username=args.get('username')).first()

        if user and user.confirm_password(args.get('password')) is True:
            self.base_res.set_res(
                'result': 'success',
                'messages': 
                )
        return json.dumps(dict(
                code='200',
                message='failed',
                username=user.username,
                auth=user.identity
            ))
