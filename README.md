# API implemented by Python, Flask

- Python(3.4.1)
  - Flask
  - SQLAlchemy

## Preparation

```sh
pip install -r requirements.txt
```

## 実行

```sh
python run.py
```

## テスト

```sh
# 全てのtestを実行する
python manage.py test
# 特定のtestを実行する
nosetests -v tests/hoge.py
# pyenv exec nosetests -v tests/hoge.py
```
