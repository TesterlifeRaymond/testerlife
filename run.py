#!/usr/bin/env python3
from interface import app
from interface import db
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
