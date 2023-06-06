

BROWSER=chrome

robot --variable=BROWSER:$BROWSER -L debug $1
#robot --variable=BROWSER:$BROWSER --loglevel=debug $1