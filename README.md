# notemp
python script that uses the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) package to communicate with AWS. it will download any image from the internet using the requests package, save it in memory, 
and then upload it directly to a given s3 bucket using  your Access key ID and the Secret Key that you configured.

## keys configurations 
you have to configure `your Access key ID and the Secret Key` in this section : 

```python 
session = boto3.Session(
    aws_access_key_id ='<your aws_access_key_id>'
    aws_secret_access_key = '<your aws_secret_access_key>'
)
```
and the `image url` in this section :

```python 
url = '<image url>'
```

and of course your bucket name and let your dog choose a name for the file 

```python 
object = s3.object('<the bucket name>', '<the name of the file>')
```

## usage 

to use the script first you need to install the required modules you can find them in the `requirements.txt` and to do that just run 

``` 
pip3 install -r requirements.txt
```

after this you can run the code directly using the following command 

```
python3 code.py
```

