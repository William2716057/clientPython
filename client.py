import socket

def send_message(message, target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((target_ip, target_port))
        sock.sendall(message.encode())
        print("Message sent successfully.")

    except Exception as e:
        print(f"Error occurred while sending message: {e}")

    finally:
        sock.close()

if __name__ == "__main__":
    target_ip = "<receiver_ip>" # Adjust IP here
    target_port = 9999

    message = "This is a message from the sender!"

    send_message(message, target_ip, target_port)
