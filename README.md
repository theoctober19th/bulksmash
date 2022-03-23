# bulksmash
A bulk SMS sender written in Python that sends a message to large number of receptionist using an Android phone connected to the computer.

## Prerequisite
1. Android Phone
2. USB Cable
3. Computer
4. Android Debug Bridge (`adb`)
5. Device drivers for the android phones

## Instructions
1. Clone the repository
2. Fill the file `contacts.csv` with the list of numbers to send the SMS to.
3. Write the desired message in `message.txt` file.
4. Change relevant configurations in `config.py` file.
5. Connect the Android phone to the computer and turn on the USB debugging mode.
6. Run the script using `python3 script.py`