import socket 
import optparse
import threading
import time

def logo_co(toll):
    print("")
    print(f"\033[1;37m████████╗██╗████████╗░█████╗░███╗░░██╗")
    print(f"\033[1;37m╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗░██║")
    print(f"\033[1;37m░░░██║░░░██║░░░██║░░░███████║██╔██╗██║")
    print(f"\033[1;37m░░░██║░░░██║░░░██║░░░██╔══██║██║╚████║")
    print(f"\033[1;37m░░░██║░░░██║░░░██║░░░██║░░██║██║░╚███║")
    print(f"\033[1;37m░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝")
    print("---------------------------------------")
    print(f"      Welcome to {toll}\n\n")


logo_co("Ports Scanner Tool")

class PortScanner:
    
    def get_user_inputs(self):
        object_parser = optparse.OptionParser()
        object_parser.add_option("--ip",dest="ip_target",help="Enter Target IP or Domain")
        object_parser.add_option("--range1",dest="range1",help="Enter the start port")
        object_parser.add_option("--range2",dest="range2",help="Enter the end port")
        (user_input, argument) = object_parser.parse_args()

        if not user_input.ip_target:
            object_parser.error("[-] Specify an Target IP please, -h for help")
        elif not user_input.range1:
            object_parser.error("[-] Specify an range1 please, -h for help")
        elif not user_input.range2:
            object_parser.error("[-] Specify an range2 please, -h for help")
        
        return user_input

    banner = "\nStarting Port Scan..."
    for char in banner:
        print(char, end="", flush=True)
        time.sleep(0.04)

    def scan_single_port(self,ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        connect = sock.connect_ex((ip, port))
        if connect == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown"

            print(f"[+] port: {port:<4} is open | service: {service}")
        

            sock.close()

    def Threads_scan(self, ip, start, end):
        threads = []
        print("\n---------------------------------------")
        for port in range(start, end +1):
            t = threading.Thread(target=self.scan_single_port, args=(ip, port))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
        print("Scanning finished! ")
        

object1 = PortScanner()
user_input = object1.get_user_inputs()

start = int(user_input.range1)
end = int(user_input.range2)
object1.Threads_scan(user_input.ip_target, start, end)
