echo "===========Good Locality============"
gcc -O0 -o good good.c
time ./good

echo "===========Bad Locality============="
gcc -O0 -o bad bad.c
time ./bad

rm good bad
