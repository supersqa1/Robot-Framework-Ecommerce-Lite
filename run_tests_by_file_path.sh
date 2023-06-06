

BROWSER=chrome
CREDENTIALS_VARIABLE_FILE=./variables_credentials_local.py

robot \
--pythonpath=. \
--variable=BROWSER:${BROWSER} \
--variablefile=${CREDENTIALS_VARIABLE_FILE} \
-L debug \
$1
