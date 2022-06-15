for line in ./test/bip/edited/*/*.bin; do 
     echo "$line"
     python3 main.py "$line"
done