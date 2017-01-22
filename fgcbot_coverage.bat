coverage run -m unittest discover fgcbot.test

coverage report --omit="*test*,*__init__*"

pause