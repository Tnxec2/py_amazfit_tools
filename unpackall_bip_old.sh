for line in ./test/bip/meine/*/*.bin; do 
     echo "$line"
     python3 main.py "$line"
done