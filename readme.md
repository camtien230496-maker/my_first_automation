
==== Automation Testing Framework =====

Technologies
- Python
- Selenium WebDriver
- PyTest
- Page Object Model

Features
- Login test scenarios
- Positive & negative test cases
- Reusable page objects
- HTML test report

How to run tests
pytest -m smoke --html=report/report.html


=====  PUSH CODE ========
git init
git remote origin https://github.com/camtien230496-maker/my_first_automation
git branch -M main
git status
git add .
git status
git config --global user.email "camtien230496@gmail.com"
git config --global user.name "TienChau"
git commit -m "22012026"
git push


====== TAO VENV =======
python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install -upgrade pip
pip install selenium pytest
pip install requests
pip install pytest-html

==> run test:
pytest .\test_login01.py

====== API =======
@pytest.mark.api TRƯỚC CLASS
========RUN API TEST=========
pytest -m api -s




