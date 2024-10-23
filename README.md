# C2 Application

## Introduction

The C2 Application consists of a server, client and database.

The client is a GUI application made in python that also works as a system tray application.

The server and database runs in the terminal.

Client GUI:

<img src="images/client_page.png" width="200" height="250">
<img src="images/client_info.png" width="200" height="250">
<img src="images/client_apps.png" width="200" height="250">

Client tray:

<img src="images/tray.png">

## How to Use

### Prerequisites
```
Mariadb: 15.^
Python: 3.8.^
node: 20.^
```
#### Client:
```
cd client/
pip install -r requirements.txt
```
#### Server:
```
cd server/
npm install
```
#### Database:
```
cd database/
mariadb --table < user.sql
mariadb --table < setup.sql
```

### Build
```
cd client/
pyinstaller --add-data "icon.jpg:." main.py
cd dist/main/
./main
```

### Test
```
cd client/
coverage run -m unittest discover -s unittest/tests
coverage report
```

```
cd client/
pylint <file.py>
```

### Run

#### Client:
```
cd client/
python3 main.py
```

#### Server:
```
cd server/
node index.js
```

#### Server GUI:
```
website: localhost:8084
```

## License

MIT License

Copyright (c) [2024] [C2 Application]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.