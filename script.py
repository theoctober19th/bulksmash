#!/usr/bin/python3
import os
from config import MESSAGE_INTERVAL
from exceptions import MessageFileNotFound
import subprocess
import csv
import time

def is_valid_number(number):
    number = number.strip()
    return len(number) == 10

def _get_numbers():
    numbers_csv_path = os.path.join(os.path.dirname(__file__), 'contacts.csv')
    invalid_numbes_csv_path = os.path.join(os.path.dirname(__file__), 'invalid_numbers.csv')
    valid_numbers = []
    with open(numbers_csv_path) as csv_file, open(invalid_numbes_csv_path, "w") as invalid_numbers_file:
        reader = csv.DictReader(csv_file)
        writer = csv.DictWriter(invalid_numbers_file, [
            'name', 'number'
        ])
        writer.writeheader()
        for row in reader:
            if is_valid_number(row["number"]):
                number = row['number']
                valid_numbers.append(number.strip())
            else:
                #number is invalid
                print("Invalid number {} for {}\n".format(row['number'],  row['name']))
                writer.writerow(row)
    return valid_numbers


def _format_number_with_code(number):
    return number

def _load_message():
    try:
        message_path = os.path.join(os.path.dirname(__file__), 'message.txt')
        message = ""
        with open(message_path) as message_file:
            message = message_file.read()
        return "'{}'".format(message)
    except:
        raise MessageFileNotFound()

def send_message(message, number):
    command = [
        'adb',
        'shell',
        'service',
        'call',
        'isms',
        '7',
        'i32',
        '2',
        's16',
        'com.android.messaging',
        's16',
        _format_number_with_code(number),
        's16',
        'null',
        's16',
        message,
        's16',
        'null',
        's16',
        'null'
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    print("Sending message to: {}".format(number))
    process.wait()

def main():
    numbers = _get_numbers()
    message = _load_message()
    for number in numbers:
        send_message(message, number)
        time.sleep(MESSAGE_INTERVAL)
    print("Sent messages to {} recepients.".format(len(numbers)))


if __name__ == "__main__":
    main()
