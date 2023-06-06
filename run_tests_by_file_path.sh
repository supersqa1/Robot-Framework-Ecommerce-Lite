

source ./credentials_local.sh

BROWSER=chrome


robot \
--pythonpath=. \
--variable=BROWSER:${BROWSER} \
-L debug \
$1
