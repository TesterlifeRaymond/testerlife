#!/usr/bin/env python3
from interface import app
from interface.auth import auth


app.register_blueprint(auth, url_prefix='/auth')  # auth module blueprint 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

