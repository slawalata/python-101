from flask import Flask, render_template, request
import boto3, botocore

app = Flask(__name__)

S3_BUCKET = "myapp.upload"
app.config['S3_BUCKET'] = S3_BUCKET
app.config['S3_KEY'] = "AKIAX7KSC7IQ4IFHIT4B"
app.config['S3_SECRET'] = "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"
app.config['S3_LOCATION'] = f'http://s3.amazonaws.com.{S3_BUCKET}/'

s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET'],
    # aws_session_token=app.config['S3_TOKEN']
)


@app.route('/')
def index():
    return render_template(
        's3_index.html',
        imgs_folder="https://s3.amazonaws.com/myapp.imgs"
    )


@app.route('/id_files', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']

        if f.filename == "":
            return "Please select a file"

        # Uncomment to find your file is stored in disk
        # f.save(f.filename)

        file_url = upload_file_to_s3(f, S3_BUCKET)
        # file_url = "None"

        return render_template(
            "success.html",
            file_url=str(file_url)
        )


def upload_file_to_s3(file, bucket_name, acl="public-read"):
    """
    Docs: http://boto3.readthedocs.io/en/latest/guide/s3.html
    """
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type  # Set appropriate content type as per the file
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(app.config["S3_LOCATION"], file.filename)


if __name__ == "__main__":
    app.run()
