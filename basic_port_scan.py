#########################
#                       #
#  **Basic_Port_Scan**  #       
#  Gabriel de Jesus     #
#   Date:21/03/2021     #
#  Version:0.0.1 beta   #
#                       #   
#########################
import socket
class PortScan:
        client_socket = None

        def __init__(self,ip):

                self.ip_target = ip

        def connect_and_scan(self):
                important_port_list = [21,22,23,25,53,80,110,123,443]
                list_corespondence = {20:'ftp',22:'ssh',23:'telnet',25:'smtp',53:'udpdns',80:'http',110:'pop3',123:'ntp',443:'htt$
                print('PORTA STATE   SERVICE')

                for porta in important_port_list: 
                        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                        client_socket.settimeout(2)

                        code_recev = client_socket.connect_ex((self.ip_target,porta)) 

                        if code_recev == 0: #PORTA ABERTA


                                print(porta,'\033[32m'+'  OPEN'+'\033[0:0m    ',list_corespondence[porta])


if __name__ == '__main__':
        ip_or_domain = input('Alvo: ')
        ps = PortScan(ip_or_domain)
        ps.connect_and_scan()

