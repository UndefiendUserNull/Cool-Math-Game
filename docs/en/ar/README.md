<!-- Language: ar -->

# لعبة الرياضة الكول π

اللعبه بتدرب دماغك على عدم استخدام الاله الحاسبه وتحل بدماغك

## مزايا

- **صعوبه متزايده**: اللعبه صعوبتها بتزيد كل ما تجيب اجابه صح
- **نظام حفظ**: الستريك بتاعك بيتحفظ في ملف لما تخلص الجيم
- **الاطوار**: جمع, طرح, ضرب, قسمه, وعشوائي
- **كونسول ملون**: الكونسول مش ابيض واسود بس
- **خفيفه**: اللعبه بالكتير بتستخدم 12.2 ميجا رام

## مطلتبات البناء

- Python 3.x (مستخدمتش اي مكاتب خارجيه الا الان)

## ازاي تبني

### الطريقه 1: "bat/sh"

1. انسخ الريبو: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
2. لمستخدم **ويندوز**, شغل `build.bat`
3. لمستخدم **لينكس**, شغل `build-linux.sh`

### الطريقه 2: "auto-py-to-exe"

1. نزل auto-py-to-exe: `pip install auto-py-to-exe`
2. انسخ الريبو: `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`
3. افتح الcmd جوا فولدر الsrc واكتب `auto-py-to-exe`
4. لما يفتح دوس على Settings
5. دوس على `Import Config From JSON File` واختار `build-config.json` اللي موجود في الفولدر
6. اضرب `CONVERT .PY TO .EXE`

### الطريقه 3: "pyinstaller"

1. نزل : `pip install pyinstaller`.
2. انسخ الريبو : `git clone https://github.com/UndefiendUserNull/Cool-Math-Game`.
3. افتح الcmd جوا "src" وحط الكود ده

   **ويندوز** :

   ```bash
   pyinstaller --noconfirm --onefile --console --icon "..\ico.ico" --name "Cool Math Game" --clean --add-data "game.py;." --add-data "filesHandler.py;." --add-data "colors.py;." --add-data "globals.py;." --add-data "utils.py;." "main.py"
   ```

   **لينكس** :

   ```bash
   pyinstaller --noconfirm --onefile --console --icon="ico.ico" --name="Cool Math Game" --clean --add-data="src/game.py:." --add-data="src/filesHandler.py:." --add-data="src/colors.py:." --add-data="src/globals.py:." --add-data="src/utils.py:." src/main.py
   ```
