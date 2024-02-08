import socket
import threading

# Connection Data
host = '127.0.0.1'
port = 44444

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Sending Nickname
client.send(nickname.encode('ascii'))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive and decrypt message from server
            message = client.recv(1024)
            decrypted_message = message.decode('ascii')
            print(decrypted_message)
        except:
            # Close Connection When Error
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        # Ввод и отправка зашифрованного сообщения
        message = '{}: {}'.format(nickname, input(''))
        encrypted_message = message.encode('ascii')
        client.send(encrypted_message)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
