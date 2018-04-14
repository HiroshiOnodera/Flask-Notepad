# Flask-Sample-Notepad

## 実行手順

### 設定ファイル修正

    config/config.dfgファイルのSQLALCHEMY_DATABASE_URIに、SQLiteのパスを記載

    例）Windows
    SQLALCHEMY_DATABASE_URI="sqlite:///C:\\Users\\name\\Flask_notepad\\notepad.db"

### PowerShell

#### 1.仮想環境構築

    python -m venv .\

#### 2.仮想環境起動

    \Scripts\activate

#### 3.ライブラリインストール

    pip install -r requrement.txt

#### 4. 環境変数設定

    $env:FLASK_APP="main.py"

#### 5. SQLite初期化

    flask initdb

#### 6. ユーザ登録

    flask useradd your@mail.com password

#### 7. 起動

    flask run

下記のURLにアクセス
<http://localhost:5000>