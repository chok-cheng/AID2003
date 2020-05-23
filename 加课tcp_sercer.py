#创建一个简单的tcp服务器
from socket import *
host='127.0.0.1'
prot=12345
ADDR=(host,prot)
sockfd=socket()
#设置套接字选项，允许重用地址
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(5)

while True:
    client_sock,addr=sockfd.accept()
    print('Client connect from ',addr)
    while True:
        data=client_sock.recv(1024)
        print(data)
        if data.strip()==b'quit':
            break
        print(data.decode())
        send_data=input('>')+'\r\n'
        client_sock.send(send_data.encode())
    client_sock.close()
sockfd.close()

#可重用的TCP服务器
#可以接收一个客户端的连接
#如果客户端发送quit 结束通信 断开连接
#可以继续等待下一个客户端连接
