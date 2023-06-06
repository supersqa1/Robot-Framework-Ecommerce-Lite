
BROWSER=CHROME

python3 -m robot --pythonpath=. --variable=BROWSER:${BROWSER} --include=$1 tests