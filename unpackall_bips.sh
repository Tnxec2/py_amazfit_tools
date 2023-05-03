for line in ./test/bips/zepp/*/*.bin; do 
     echo "$line"
     python main.py "$line"
done