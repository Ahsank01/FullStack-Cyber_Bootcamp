#!/usr/bin/env python3

'''
Perform the math calculation stated by the server on the numbers (that's right, numbers) given by the server. 
possible maths are add, subtract, multiply, or divide. multiply 8 and 4. divide 8 by 4. add 8 and 4. subtract 8 from 4. 
send, rounded, to 8 places to the right of the decimal (0.00000001) if there is a decimal. 
Send whole numbers as they appear. 1, 1.05000000, 0.10000008 and the server will respond with a flag. nc listen.runcode.ninja 9001
'''

#!/usr/bin/env python3

# Import 'sys' module to process command line arguments
import sys
# Import 'socket' module to make network connections
import socket


def main():
    # Variables for connection info
    HOST = sys.argv[1]
    # Convert the second argumment to a number. All 'argv' elements are strings
    PORT = int(sys.argv[2])

    # Create a socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connect to the host and port provided on the command line
        s.connect((HOST, PORT))

        # Capture the data sent by the server
        prompt = s.recv(1024).decode().strip()
        # We only need the second line of text
        prompt = prompt.split('\n')[-1]
        # Uncomment next line to see the prompt from sent by the server
        print(prompt)

        # Get the words and numbers from the prompt
        words = prompt.split()
        # Grab the parts of the prompt we need
        operation = words[0]
        operand1 = words[1]
        # Get the last number without the exclamation point(!)
        operand2 = words[3]
        operand2 = operand2[:-1]

        if operation == 'add':
            answer = int(operand1) + int(operand2)
        if operation == 'subtract':
            answer = int(operand2) - int(operand1)
        if operation == 'multiply':
            answer = int(operand1) * int(operand2)
        if operation == 'divide':
            answer = int(operand1) / int(operand2)
            # Round the number to 8 places
            # https://docs.python.org/3/library/functions.html#round
            answer = round(answer, 8)
            # Pad the number with zeroes, if necessary
            # https://docs.python.org/3.4/library/string.html#format-string-syntax
            answer = f'{answer:.8f}'

        # Convert number to string and add newline character
        answer = str(answer) + '\n'
        # Uncomment next line to see the answer being sent to the server
        print(answer)

        # Send the answer to the server
        s.send(answer.encode())

        # Receive the flag
        flag = s.recv(1024).decode().strip()
        print(flag)


if __name__ == '__main__':
    main()