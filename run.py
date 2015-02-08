# -*- encoding:utf-8 -*-
''' test init app
`python run.py`
http://localhost:12345
'''
from zip_address import app

if __name__ == "__main__":
    app.debug = True
    # db.create_all(app=app)
    app.run(host="0.0.0.0", port=12345)
