# Welcome to the Outreach Tool!

Before you start, please note that this is a python script! Please visit this link to download Python so that you can run the tool:  
https://www.python.org/downloads/

Once everything is set, you can run the program by typing 'python outreach_tool.py' into your terminal.  

This tool is used to **automatically send emails** out using the **SMTP library** and **Gmail!** 

⚠️ **Gmail's daily limit is 500 emails per day**

There is also a **5 second buffer** between each email sent to not overload servers and prevent spam emails being sent out. Please respect these settings!

## Quick Guide

Here's a quick walkthrough to help you get started with the tool.

### App Password Setup

First, you'll need to set up a Gmail inbox with 2FA and get an app password. Please visit the link below for more instructions:  
https://support.google.com/accounts/answer/185833?hl=en

*It's recommended that you create a separate Gmail inbox for this.*

### What You'll Be Prompted For:

1. the email you want to send from
2. an app password (you can get this by setting up 2FA, and then getting the app password)
3. the email subject
4. the content of the email (preferably in HTML form)
5. the name of the signature
6. the maximum number of emails to send (1-499)
7. filepath to the JSON file containing contacts to send emails to

## JSON Format

Your JSON file should contain at least the following fields:

{  
    "Name": "Jane Doe",  
    "Email": "janedoe@example.com"  
}

## Util Scripts

There are three python scripts in Util that can help you clean up data.

1. **clean_json.py** will take in a JSON file and extract only the **First name**, **Last name**, and **Email** parameters into a specified output file that contains only **Name** and **Email**.
2. **process_text.py** takes in a block of text with four parameters (name, location, email, phone) and writes it to a json. This script is pretty niche, and you shouldn't need to use this.
3. **remove_duplicates.py** takes in a JSON file and removes duplicate items based off the **Name** parameter within a JSON file into a specified output file.

*Please note that 1 and 3 require an input **AND** an output JSON file!*

If you have any issues or questions, either message me on Slack or open a Github issue!