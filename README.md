# LIBS-PYTHON
Projeto que ura armazena as libs python que eu faço para reuso 

```shell
python -m venv venv
.\venv\Scripts\Activate.ps1 | deactivate
pip freeze > requirements.txt  ## para todos
pip freeze >> requirements.txt
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
pip freeze | xargs pip uninstall -y
```
## BUILD
[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
```shell
##
python -m pip install --upgrade build | py -m pip install --upgrade build
python -m build | py -m build
##
dist/
├── example_package_YOUR_USERNAME_HERE-0.0.1-py3-none-any.whl
└── example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz
##
python -m pip install -f example_package_YOUR_USERNAME_HERE-0.0.1.tar.gz | py -m pip install
```