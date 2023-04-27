import mailbox
from pprint import pprint

# Replace with the path to your mbox file
mbox_file = '/Users/band/Documents/Github//openaiLab/workbench//oaiExpt001.mbox'
print(mbox_file)
# Open the mbox file
mbox = mailbox.mbox(mbox_file)

# Iterate over messages in the mbox file
def parseMbox(mbox_file):
    for message in mbox:
        # Get the message from and subject
        print(f"From: {message['from']}")
        subject = message['subject']
        print(f"Subject: {subject}")

        # Get the message body
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=True)
                    print(f"text/plain body: {body}")
        else:
            body = message.get_payload(decode=True)
            pprint(body)
        print("\n")

def main():
    parseMbox(mbox)
 
if __name__ == "__main__":
    exit(main())
