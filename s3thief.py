import boto3
from argparse import ArgumentParser

# This script requires you setup the AWS Secret Key in your environment
parser = ArgumentParser(description='Connect to an Amazon S3 instance, list out buckets & their files, then download them all!')
parser.add_argument('--download', '-d', action="store_true", help='Download all the things! (Make sure you have a lot of HDD space!)')
parser.add_argument('--verbose', '-v', action="store_true", help='Verbose output.')
parser.add_argument('--output', '-o', help='Output directory (aka, where do you want the data stored?).')

# Parse arguments
args = parser.parse_args()
parser.set_defaults(output="/tmp")

all_buckets = []
all_files = []
total_file_count = 0

# Connect to S3
s3 = boto3.resource('s3')

# Captures all buckets the API key has access to in an array
for bucket in s3.buckets.all():
    if args.verbose:
        print("[+] Bucket: " + bucket.name)
    all_buckets.append(bucket.name)

print("[+] Discovered " + str(len(all_buckets)) + " buckets available.")

# Print out file names within bucket (bucket name is specified)
conn = boto3.client('s3')
for bucket in all_buckets:
    try:
        for key in conn.list_objects(Bucket=bucket)['Contents']:
            if args.verbose:
                print("[!] " + bucket + ": " + key['Key'])
            all_files.append(key)
            # Download files found if variable set
            filename = key['Key']
            filename_save = str(filename).replace("/", "_")
            print filename_save
            if args.download:
                try:
                    s3.Bucket(bucket).download_file(filename, args.output + filename_save)
                except TypeError:
                    print("skipping...")
        print("[+]        Bucket: " + bucket + " has " + str(len(all_files)) + " files available.")
        total_file_count = total_file_count + len(all_files)
        all_files = []
    except KeyError:
        print("[-]        Bucket: " + bucket + " No Files in bucket.")

print("[+] Found " + str(total_file_count) + " files in the available buckets.")

