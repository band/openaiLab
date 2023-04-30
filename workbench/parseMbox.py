import mailbox
import re

# Replace with the path to an mbox file
mbox_file = '/Users/band/Documents/Github//openaiLab/workbench//oaiExpt001.mbox'
print(mbox_file)

# Iterate over messages in the mbox file
def parseMbox(mbox_file):
    # open the mbox file
    mbox = mailbox.mbox(mbox_file)
    for message in mbox:
        # Get message from and subject
        print(f"From: {message['from']}")
        subject = message['subject']
        print(f"Subject: {subject}")
        # Get the message body
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True).decode("utf-8")
                    if match := re.search(r'On.*wrote:', body, flags=re.DOTALL):
                        msg = body[:match.start()].split("-- \r\nYou ",1)[0]
                    else:
                        msg = body.split("-- \r\nYou ",1)[0]
                    print(f"text/plain body: {msg}")
        else:
            body = message.get_payload(decode=True).decode("utf-8")
            if match := re.search(r'On.*wrote:', body, flags=re.DOTALL):
                msg = body[:match.start()].split("-- \r\nYou ",1)[0]
            else:
                msg = body.split("-- \r\nYou ",1)[0]
            print(f"body: {msg}")
        print("----------\n")

def main():
    parseMbox(mbox_file)
 
if __name__ == "__main__":
    exit(main())
