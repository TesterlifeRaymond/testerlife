#!/usr/bin/env python3
from app import app
from app import db
db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
