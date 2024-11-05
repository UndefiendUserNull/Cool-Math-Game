<!-- Language: ar -->

# لعبة الرياضة الكول π

اللعبة بتدرب دماغك على عدم استخدام الالة الحاسبة وتحل بدماغك

## مزايا

- **صعوبة متزايده**: اللعبة صعوبتها بتزيد كل ما تجيب اجابة صح
- **نظام حفظ**: الستريك بتاعك بيتحفظ في ملف لما تخلص الجيم
- **الاطوار**: جمع, طرح, ضرب, قسمة, عشوائي, وفيثاغورث
- **كونسول ملون**: الكونسول مش ابيض واسود بس
- **خفيفه**: اللعبه بالكتير بتستخدم 12.2 ميجا رام

## متطلبات البناء

- Python 3.x (مستخدمتش اي مكاتب خارجية الى الان)
- Pyinstaller

## ازاي تبني

### الطريقة 1: "bat/sh"

1. انسخ الريبو `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
2. لمستخدم **ويندوز**, شغل `build.bat`
3. لمستخدم **لينكس**, شغل `build-linux.sh`

### الطريقة 2: "auto-py-to-exe"

1. نزل auto-py-to-exe: `pip install auto-py-to-exe`
2. انسخ الريبو: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
3. افتح الcmd جوا فولدر الsrc واكتب `auto-py-to-exe`
4. لما يفتح دوس على Settings
5. دوس على `Import Config From JSON File` واختار `build-config.json` اللي موجود في الفولدر
6. اضرب `CONVERT .PY TO .EXE`

### الطريقة 3: "pyinstaller"

1. نزل : `pip install pyinstaller`
2. انسخ الريبو : `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
3. افتح الcmd جوا "src" وحط الكود ده

   **ويندوز** :

   ```bash
   pyinstaller --noconfirm --onefile --console --name --icon "./ico.ico" "Cool Math Game" --add-data "colors.py;." --add-data "filesHandler.py;." --add-data "game.py;." --add-data "geometryGame.py;." --add-data "globals.py;." --add-data "main.py;." --add-data "utils.py;."  "src\main.py"
   ```

   **لينكس** :

   ```bash
   pyinstaller --noconfirm --onefile --console --name "Cool Math Game" --add-data "colors.py:." --add-data "filesHandler.py:." --add-data "game.py:." --add-data "geometryGame.py:." --add-data "globals.py:." --add-data "main.py:." --add-data "utils.py:." "main.py"
   ```

# صور

![صوره واحد](https://i.imgur.com/a7iSmvW.png?raw=true "صوره")
![صوره اتنين](https://i.imgur.com/ZQvIrIh.png?raw=true "صوره اتنين")
![صوره تلاته](https://i.imgur.com/Agr8bJ3.png?raw=true "صوره تلاته")
