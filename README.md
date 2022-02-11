# S3-keyword-notifier
Get notified everytime a file with a defined keyword is uploaded to an AWS S3 bucket through a Lambda function

# Supported files

.html, .txt, .json, .odt

# Lambda-S3-keyword-notifier project

This project contains source code and supporting files for buiding the serveless application.

This project includes the following files and folders:

  - src - Code for the application's Lambda function.
  - events - Invocation events that you can use to invoke the function.
  - policies - Policy defining the permissions needed.
    
This application is triggered when a new file is uploaded in a specified bucket.Then, the event is sent to the Lambda function containing a specified keyword and verified emails adresses. The Lambda function will read the new object and looking for the specified keyword inside the object.If the keyword is found, the Lambda function will invoke the AWS SES to send a friendly email to the subscriber.

# Email template

The email template sent is defined inside the Lambda function. The email header mentions the specified keyword, and the body mentions the bucket name. The email received will look like as the following:

    A new <your_keyword> file has been uploaded
    Email Source
    Email Destination
    Date
    Hi there!,

    A new file with the <your_keyword> keyword has just been uploaded in your <bucket_name> bucket!

    Have a Lovely day!

Feel free to configure the content of the email. For instance, more details can be pulled from the Event such as AWS Region, sourceIPAddress, or the userIdentity.

# Author

aissa-laribi <aissalaribi@yahoo.fr> (Aissa Laribi)

Please report bugs and suggestions at the issue tracker!

# Contributing to this project

Feel free to submit a pull request or drop me an email.

# License

The code is made available under the MIT license.




