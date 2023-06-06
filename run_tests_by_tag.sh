
source ./credentials_local.sh


BROWSER=CHROME


robot \
--pythonpath=. \
--variable=BROWSER:${BROWSER} \
-L debug \
--include=$1 \
./tests
