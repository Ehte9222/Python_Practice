import pywhatkit as kit
import time

messages = [
    "Hello!",
    "How are you doing?",
    "This is an automated message.",
    "Have a great day! It was supposed to be a prank"
]
phone_number = "+92 0000000000"
for message in messages:
    time_delay = 15  
    wait_time = time.time() + time_delay
    wait_time_struct = time.localtime(wait_time)
    kit.sendwhatmsg(phone_number, message, wait_time_struct.tm_hour, wait_time_struct.tm_min + 1) 
    time.sleep(time_delay)

print("Messages sent successfully.")