echo "start fastapi"
host=$1
port=$2
isreload=$3
workernum=$4

# default
host=${host:-0.0.0.0}
port=${port:-8000}
echo host: $host #从yml文件中获取
echo port: $port

if [ ${isreload:-1} ];then
  echo "reload"
  uvicorn --host $host --port $port --reload --log-level info app.run:app
elif [ ${workernum:-4} ];then
  uvicorn --host $host --port $port --workers $workernum  --log-level info app.run:app 
fi


  



