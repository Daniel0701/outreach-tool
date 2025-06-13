Hello! Welcome to the Outreach Tool! This tool is used to automatically send emails out using the SMTP library and Gmail! The daily limit is 500 emails per day, and there is a 5 second buffer between each email sent to not overload servers and not be labelled as spam.

This is a quick guide to helping you get used to the tool.

First and foremost, the program will prompt you for information:
- the email you want to send from
- an app password (you can get this by setting up 2FA, and then getting the app password)
- the email subject
- the content of the email (preferably in HTML form)
- the name of the signature
- the maximum number of emails to send (1-499)
- filepath to the json containing contact names to send to

Note: the json should at least contain a "Name" parameter as well as an "Email" parameter to get the name and email. 