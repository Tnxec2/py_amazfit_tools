for line in ./test/bip/*.bin; do 
     echo "$line"
     python3 main.py --old "$line"
done