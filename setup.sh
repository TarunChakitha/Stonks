for data in $(cat urls)
do
url=$(echo $data | cut -d',' -f1)
code=$(echo $data | cut -d',' -f2)
filename=${code%?}
filename=$(echo "${filename:1}" | head -c -1)

echo "from stocks import Stocks

url = $url
code = $code

mc = Stocks(url=url,company=code)
mc.getData()" > companies/"$filename".py
done

echo "
setup complete.
"