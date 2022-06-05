for line in ./test/bips/zepp/*/*.bin; do 
     echo "$line"
     python3 main.py "$line"
done