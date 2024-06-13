import pywhatkit as pwk
import time

def whats():
    # Define the message and contacts
    message = "Hello, this is a test message from the automation."
    contacts = ["+918888795246", "+916485745775"]  # Replace with the actual phone numbers including the country code

    # Function to send message
    def send_whatsapp_message(contact, message):
        try:
            # Schedule the message to be sent in 1 minute from now
            pwk.sendwhatmsg(contact, message, time.localtime().tm_hour, (time.localtime().tm_min + 1))
            time.sleep(60)  # Waiting to ensure the message is sent before sending the next one
        except Exception as e:
            print(f"An error occurred: {e}")

    for contact in contacts:
        send_whatsapp_message(contact, message)


    print("Messages sent successfully!")
    
while True:
    whats()
    time.sleep(7200) # Waiting for two hour the message 
