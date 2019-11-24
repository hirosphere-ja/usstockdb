プロジェクト名
usstockdb       ⇒ 米国株式データベース

アプリケーション名
usstockmarket   ⇒ 米国株式市場一覧
  model Market
usstocklist     ⇒ 米国株式銘柄一覧
usstockdividend ⇒ 米国株式現金配当

python manage.py startapp usstockmarket

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

python manage.py createsuperuser