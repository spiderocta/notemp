import boto3
import requests 


session = boto3.Session(
    aws_access_key_id ='<your aws_access_key_id>'
    aws_secret_access_key = '<your aws_secret_access_key>'
)

s3 = session.resource('s3')

url = 'https://images.theconversation.com/files/2927/original/Screen_shot_2011-08-15_at_2.02.22_PM.jpg'

request = requests.get(url)

if request.status_code == 200:
    #upload
    file_content = request.content
    #object = s3.object('<the bucket name>', '<the name of the file>')
    object = s3.object('<dev-bucket>', 'catMeme.jpg')
    result = object.put(Body=file_content)
else :
    #throw an error 
    print('error occured while fetching the resource. status {}'.format(request.status_code))