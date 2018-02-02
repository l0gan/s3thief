# s3thief
Written by Kirk Hayes (@l0gan)

This script requires you setup the AWS Secret Key in your environment
Ensure you have a file under ~/.aws for each of the following:

#### ~/.aws/credentials:
``` 
[default]
aws_access_key_id = <ACCESS KEY>
aws_secret_access_key = <ACCESS SECRET KEY>
```
#### ~/.aws/config
```
[default]
region=us-east-1
```

### Requirements:
``` pip install boto3 ```

### Use:
```
usage: s3thief.py [-h] [--download] [--verbose] [--output OUTPUT]

Connect to an Amazon S3 instance, list out buckets & their files, then
download them all!

optional arguments:
  -h, --help            show this help message and exit
  --download, -d        Download all the things! (Make sure you have a lot of
                        HDD space!)
  --verbose, -v         Verbose output.
  --output OUTPUT, -o OUTPUT
                        Output directory (aka, where do you want the data
                        stored?).
```



