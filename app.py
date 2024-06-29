import pywhatkit as kit
import time

# List of messages to send
messages = [
    "Hello!",
    "How are you doing?",
    "This is an automated message.",
    "Have a great day! It was supposed to be a prank"
]

# WhatsApp number in the format: "+<country_code><number>"
phone_number = "+92 0000000000"

# Send each message with a delay
for message in messages:
    # Adjust the time_delay as needed
    time_delay = 15  # Delay in seconds before sending the next message
    wait_time = time.time() + time_delay
    wait_time_struct = time.localtime(wait_time)
    kit.sendwhatmsg(phone_number, message, wait_time_struct.tm_hour, wait_time_struct.tm_min + 1)  # Adding 1 minute to avoid immediate send
    time.sleep(time_delay)

print("Messages sent successfully.")