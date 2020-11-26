#! /usr/bin/env python3

# Import necessary python modules
from tkinter import *
import os
import time

# Establish GUI
root = Tk()

# Define GUI
root.geometry('1000x950')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("NordVPN")

# Add Label for GUI window
Label(root, text = "NordVPN Controls",
    font = 'arial 16 bold', bg='gray7', fg='lime green').pack()


def clear_output():

    text_output_window.delete(1.0, END)


def get_info(arg):

    print(text_output_window.get("1.0", "current lineend"))


def vpn_status():
   
    clear_output()
    
    f = os.popen('nordvpn status')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    

def vpn_settings():
        
    clear_output()
    
    f = os.popen('nordvpn settings')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_protocol_udp():
       
    f = os.popen('nordvpn set protocol udp')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_protocol_tcp():
        
    f = os.popen('nordvpn set protocol tcp')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_ks_on():

    f = os.popen("nordvpn set killswitch enabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_ks_off():
    
    f = os.popen('nordvpn set killswitch disabled')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
   
    
def vpn_cybsec_off():
    
    f = os.popen("nordvpn set cybersec disabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_cybsec_on():
    
    f = os.popen('nordvpn set cybersec enabled')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_obsf_off():

    f = os.popen('nordvpn set obfuscate disabled')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_obsf_on():
    
    f = os.popen("nordvpn set obfuscate enabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_notify_off():
    
    f = os.popen("nordvpn set notify disabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_notify_on():

    f = os.popen("nordvpn set notify enabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_ac_off():
    
    f = os.popen("nordvpn set autoconnect disabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_ac_on():

    f = os.popen("nordvpn set autoconnect enabled")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_c():
    
    clear_output()
    
    vpn_c_us()
    time.sleep(2)
    
    vpn_ks_on()
    time.sleep(2)
    
    vpn_ac_on()
    time.sleep(2)
    
    vpn_wl_on()
    time.sleep(1)
    
    vpn_cybsec_off()
    time.sleep(1)
    
    f = os.popen('nordvpn status')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_c_us():
    
    clear_output()
    
    f = os.popen("nordvpn c us")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_c_chicago():

    clear_output()
    
    f = os.popen("nordvpn c chicago")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_c_new_york():
    
    clear_output()
    
    f = os.popen("nordvpn c new_york")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_c_miami():
    
    clear_output()

    f = os.popen("nordvpn c miami")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    

def vpn_c_canada():
    
    clear_output()
    
    f = os.popen("nordvpn c canada")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    

def vpn_c_uk():
    
    clear_output()
    
    f = os.popen("nordvpn c uk")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    

def vpn_d():
    
    clear_output()
    
    f = os.popen("nordvpn d")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    

def vpn_rate():
    
    f = os.popen("nordvpn rate 5")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)

    
def vpn_disconnect():

    clear_output()
    
    vpn_ks_off()
    time.sleep(2)
    
    vpn_ac_off()
    time.sleep(2)
    
    vpn_wl_off()
    time.sleep(2)
    
    vpn_d()
    time.sleep(2)
    
    vpn_rate()
    time.sleep(1)
    
    g = os.popen('nordvpn settings')
    for line in g:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    f = os.popen('nordvpn status')
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_wl_on():

    f = os.popen("nordvpn whitelist add port 8080")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
    
def vpn_wl_off():
    
    f = os.popen("nordvpn whitelist remove port 8080")
    for line in f:
        line = line.strip()
        if line:
            text_output_window.insert("end", line + '\n')
    text_output_window.bind("<Return>", get_info)
    
   
def Exit():
    exit()


# Create Buttons
B1 = Button(root, font = 'arial 10 bold', text = "VPN Status", 
    padx=2, bg='cyan', command=vpn_status).place(x=60, y=170)
    
B2 = Button(root, font = 'arial 10 bold', text = "VPN Settings", 
    padx=2, bg='cyan', command=vpn_settings).place(x=60, y=210)

    
B3 = Button(root, font = 'arial 10 bold', text = "VPN Protocol UDP", 
    padx=2, bg='plum1', command=vpn_protocol_udp).place(x=500, y=50)
    
B4 = Button(root, font = 'arial 10 bold', text = "VPN Protocol TCP", 
    padx=2, bg='plum1', command=vpn_protocol_tcp).place(x=500, y=90)

    
B5 = Button(root, font = 'arial 10 bold', text = "Killswitch Disable", 
    padx=2, bg='MediumOrchid1', command=vpn_ks_off).place(x=350, y=130)

B6 = Button(root, font = 'arial 10 bold', text = "Killswitch Enable", 
    padx=2, bg='MediumOrchid1', command=vpn_ks_on).place(x=350, y=170)

    
B7 = Button(root, font = 'arial 10 bold', text = "CyberSec Disable", 
    padx=2, bg='MediumOrchid1', command=vpn_cybsec_off).place(x=500, y=130)

B8 = Button(root, font = 'arial 10 bold', text = "CyberSec Enable", 
    padx=2, bg='MediumOrchid1', command=vpn_cybsec_on).place(x=500, y=170)


B9 = Button(root, font = 'arial 10 bold', text = "Obfuscate Off", 
    padx=2, bg='purple1', command=vpn_obsf_off).place(x=350, y=210)

B10 = Button(root, font = 'arial 10 bold', text = "Obfuscate On", 
    padx=2, bg='purple1', command=vpn_obsf_on).place(x=350, y=250)


B11 = Button(root, font = 'arial 10 bold', text = "Notifications Off", 
    padx=2, bg='purple1', command=vpn_notify_off).place(x=500, y=210)

B12 = Button(root, font = 'arial 10 bold', text = "Notificaions On", 
    padx=2, bg='purple1', command=vpn_notify_on).place(x=500, y=250)


B13 = Button(root, font = 'arial 10 bold', text = "Auto-Connect Off", 
    padx=2, bg='plum1', command=vpn_ac_off).place(x=350, y=50)

B14 = Button(root, font = 'arial 10 bold', text = "Auto-Connect On", 
    padx=2, bg='plum1', command=vpn_ac_on).place(x=350, y=90)


B15 = Button(root, font = 'arial 10 bold', text = "Quick Connect", 
    padx=2, bg='violet red', command=vpn_c).place(x=60, y=130)

B16 = Button(root, font = 'arial 10 bold', text = "Connect - USA", 
    padx=2, bg='PaleGreen2', command=vpn_c_us).place(x=200, y=50)

B17 = Button(root, font = 'arial 10 bold', text = "Connect - Chicago", 
    padx=2, bg='PaleGreen2', command=vpn_c_chicago).place(x=200, y=90)

B18 = Button(root, font = 'arial 10 bold', text = "Connect - New York", 
    padx=2, bg='PaleGreen2', command=vpn_c_new_york).place(x=200, y=130)

B19 = Button(root, font = 'arial 10 bold', text = "Connect - Miami", 
    padx=2, bg='PaleGreen2', command=vpn_c_miami).place(x=200, y=170)
    
B20 = Button(root, font = 'arial 10 bold', text = "Connect - Canada", 
    padx=2, bg='yellow2', command=vpn_c_canada).place(x=200, y=210)

B23 = Button(root, font = 'arial 10 bold', text = "Connect - UK", 
    padx=2, bg='yellow2', command=vpn_c_uk).place(x=200, y=250)
    
        
B24 = Button(root, font = 'arial 10 bold', text = "Disconnect VPN", 
    padx=2, bg='orange red', command=vpn_disconnect).place(x=60, y=90)

    
B25 = Button(root, font = 'arial 10 bold', text = "Remove Port 8080 Whitelist", 
    padx=2, bg='ghost white', command=vpn_wl_off).place(x=650,
        y=50)
    
B26 = Button(root, font = 'arial 10 bold', text = "Add Port 8080 Whitelist", 
    padx=2, bg='floral white', command=vpn_wl_on).place(x=650, 
        y=90)

        
B27 = Button(root, font = 'arial 10 bold', text = 'EXIT', 
    command = Exit, bg = 'firebrick3', padx=2, pady=1).place(x=60, y=50)
    

# Create tkinter text output widget
text_output_window = Text(root, height=30, width=100, borderwidth=1, 
    relief='ridge', bg='gray7', fg='lime green')
text_output_window.place(x=50, y=400)

# Create scrollbar for text output widget
scrollbar = Scrollbar(root)
scrollbar.place(x=900, y=650)

# Configure commands for scrollbar and tie to text widget
text_output_window.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_output_window.yview, bg='gray7', 
    activebackground='lime green', highlightcolor='lime green', width=15)
    
    
root.mainloop()

