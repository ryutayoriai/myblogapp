# Django
for Django

## environment

### requirements

```
pip install -r requirements.txt
```

### postgresql


・インストールとバージョン確認
```
brew install postgresql
postgres --version
```

・postgres起動
```
postgres -D /usr/local/var/postgres
```

・ユーザ作成
```
createuser -P myblogapp
psql -q -c'select * from pg_user' postgres
```

・DB作成
```
createdb myblogapp -O myblogapp
psql -U myblogapp myblogapp
```

・マイグレーション
```
cd (myblogapp配置ディレクトリ)
python manage.py migrate
```

### download source 

```
git clone https://github.com/ryutayoriai/myblogapp.git
```

### create admin user

```
python manage.py createsuperuser
```

### run 

```
python manage.py runserver
```

・サイトへのアクセスは `http://127.0.0.1:8000` 

・管理サイトへのアクセスは `http://127.0.0.1:8000/admim` 

### TODO

1. 設定ファイルをlocalとproductionで切り替える

```
https://qiita.com/okoppe8/items/e60d35f55188c0ab9ecc
```




