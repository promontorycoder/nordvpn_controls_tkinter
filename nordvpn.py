#! /usr/bin/env python3

# Import necessary python modules
from tkinter import *
import os
import time

# Establish GUI
root = Tk()

# Define GUI
root.geometry('800x500')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("NordVPN")

# Add Label for GUI window
Label(root, text = "NordVPN Controls",
    font = 'arial 16 bold', bg='gray7', fg='lime green').pack()


def vpn_status():
    nord_stat = "nordvpn status"
    os.system(nord_stat)
    

def vpn_settings():
    nord_set = "nordvpn settings"
    os.system(nord_set)
    
    
def vpn_protocol_udp():
    nordvpn_protocol_udp = "nordvpn set protocol udp"
    os.system(nordvpn_protocol_udp)
    
    
def vpn_protocol_tcp():
    nordvpn_protocol_tcp = "nordvpn set protocol tcp"
    os.system(nordvpn_protocol_tcp)
    
    
def vpn_ks_on():
    nord_ks_on = "nordvpn set killswitch enabled"
    os.system(nord_ks_on)
    
    
def vpn_ks_off():
    nord_ks_off = "nordvpn set killswitch disabled"
    os.system(nord_ks_off)
    
    
def vpn_cybsec_off():
    nordvpn_cybersec_off = "nordvpn set cybersec disabled"
    os.system(nordvpn_cybersec_off)
    
    
def vpn_cybsec_on():
    nordvpn_cybersec_on = "nordvpn set cybersec enabled"
    os.system(nordvpn_cybersec_on)
    
    
def vpn_obsf_off():
    nordvpn_obfuscate_off = "nordvpn set obfuscate disabled"
    os.system(nordvpn_obfuscate_off)
    
    
def vpn_obsf_on():
    nordvpn_obfuscate_on = "nordvpn set obfuscate enabled"
    os.system(nordvpn_obfuscate_on)
    
    
def vpn_notify_off():
    nordvpn_notify_off = "nordvpn set notify disabled"
    os.system(nordvpn_notify_off)
    
    
def vpn_notify_on():
    nordvpn_notify_on = "nordvpn set notify enabled"
    os.system(nordvpn_notify_on)
    
    
def vpn_ac_off():
    nordvpn_ac_off = "nordvpn set autoconnect disabled"
    os.system(nordvpn_ac_off)
    
    
def vpn_ac_on():
    nordvpn_ac_on = "nordvpn set autoconnect enabled"
    os.system(nordvpn_ac_on)
    
def vpn_c():
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
    
    vpn_settings()
    vpn_status()
    
        
def vpn_c_us():
    nord_conn_us = "nordvpn c us"
    os.system(nord_conn_us)
    
    
def vpn_c_chicago():
    nord_conn_chicago = "nordvpn c chicago"
    os.system(nord_conn_chicago)
    
    
def vpn_c_new_york():
    nord_conn_new_york = "nordvpn c new_york"
    os.system(nord_conn_new_york)
    
    
def vpn_c_miami():
    nord_conn_miami = "nordvpn c miami"
    os.system(nord_conn_miami)
    

def vpn_c_canada():
    nord_conn_ca = "nordvpn c canada"
    os.system(nord_conn_ca)
    

def vpn_c_france():
    nord_conn_france = "nordvpn c france"
    os.system(nord_conn_france)
    
    
def vpn_c_germany():
    nord_conn_germany = "nordvpn c germany"
    os.system(nord_conn_germany)
    
    
def vpn_c_uk():
    nord_conn_uk = "nordvpn c uk"
    os.system(nord_conn_uk)

    
def vpn_disconnect():
    nord_ks_off = "nordvpn set killswitch disabled"
    nordvpn_ac_off = "nordvpn set autoconnect disabled"
    nordvpn_whitelist_off = "nordvpn whitelist remove port 8080"
    nord_conn_off = "nordvpn d"
    nord_rate = "nordvpn rate 5"
    
    os.system(nord_ks_off)
    time.sleep(2)
    os.system(nordvpn_ac_off)
    time.sleep(2)
    os.system(nordvpn_whitelist_off)
    time.sleep(2)
    os.system(nord_conn_off)
    time.sleep(2)
    os.system(nord_rate)
    time.sleep(1)
    
    vpn_settings()
    vpn_status()
    
    
def vpn_wl_on():
    nordvpn_whitelist = "nordvpn whitelist add port 8080"
    os.system(nordvpn_whitelist)
    
    
def vpn_wl_off():
    nordvpn_whitelist_off = "nordvpn whitelist remove port 8080"
    os.system(nordvpn_whitelist_off)
    

def clear_terminal():
    clear = "clear"
    os.system(clear)
    
def Exit():
    exit()

B1 = Button(root, font = 'arial 10 bold', text = "VPN Status", 
    padx=2, bg='cyan', command=vpn_status).place(x=60, y=50)
    
B2 = Button(root, font = 'arial 10 bold', text = "VPN Settings", 
    padx=2, bg='cyan', command=vpn_settings).place(x=60, y=90)

    
B3 = Button(root, font = 'arial 10 bold', text = "VPN Protocol UDP", 
    padx=2, bg='plum1', command=vpn_protocol_udp).place(x=600, y=50)
    
B4 = Button(root, font = 'arial 10 bold', text = "VPN Protocol TCP", 
    padx=2, bg='plum1', command=vpn_protocol_tcp).place(x=600, y=90)

    
B5 = Button(root, font = 'arial 10 bold', text = "Killswitch Disable", 
    padx=2, bg='SkyBlue2', command=vpn_ks_off).place(x=400, y=170)

B6 = Button(root, font = 'arial 10 bold', text = "Killswitch Enable", 
    padx=2, bg='SkyBlue2', command=vpn_ks_on).place(x=400, y=210)

    
B7 = Button(root, font = 'arial 10 bold', text = "CyberSec Disable", 
    padx=2, bg='plum2', command=vpn_cybsec_off).place(x=600, y=170)

B8 = Button(root, font = 'arial 10 bold', text = "CyberSec Enable", 
    padx=2, bg='plum2', command=vpn_cybsec_on).place(x=600, y=210)


B9 = Button(root, font = 'arial 10 bold', text = "Obfuscate Off", 
    padx=2, bg='SkyBlue3', command=vpn_obsf_off).place(x=400, y=290)

B10 = Button(root, font = 'arial 10 bold', text = "Obfuscate On", 
    padx=2, bg='SkyBlue3', command=vpn_obsf_on).place(x=400, y=330)


B11 = Button(root, font = 'arial 10 bold', text = "Notifications Off", 
    padx=2, bg='plum3', command=vpn_notify_off).place(x=600, y=290)

B12 = Button(root, font = 'arial 10 bold', text = "Notificaions On", 
    padx=2, bg='plum3', command=vpn_notify_on).place(x=600, y=330)


B13 = Button(root, font = 'arial 10 bold', text = "Auto-Connect Off", 
    padx=2, bg='SkyBlue1', command=vpn_ac_off).place(x=400, y=50)

B14 = Button(root, font = 'arial 10 bold', text = "Auto-Connect On", 
    padx=2, bg='SkyBlue1', command=vpn_ac_on).place(x=400, y=90)


B15 = Button(root, font = 'arial 10 bold', text = "Quick Connect", 
    padx=2, bg='violet red', command=vpn_c).place(x=200, y=50)

B16 = Button(root, font = 'arial 10 bold', text = "Connect - USA", 
    padx=2, bg='PaleGreen2', command=vpn_c_us).place(x=200, y=90)

B17 = Button(root, font = 'arial 10 bold', text = "Connect - Chicago", 
    padx=2, bg='PaleGreen2', command=vpn_c_chicago).place(x=200, y=130)

B18 = Button(root, font = 'arial 10 bold', text = "Connect - New York", 
    padx=2, bg='PaleGreen2', command=vpn_c_new_york).place(x=200, y=170)

B19 = Button(root, font = 'arial 10 bold', text = "Connect - Miami", 
    padx=2, bg='PaleGreen2', command=vpn_c_miami).place(x=200, y=210)
    
B20 = Button(root, font = 'arial 10 bold', text = "Connect - Canada", 
    padx=2, bg='yellow2', command=vpn_c_canada).place(x=200, y=250)

B21 = Button(root, font = 'arial 10 bold', text = "Connect - France", 
    padx=2, bg='yellow2', command=vpn_c_france).place(x=200, y=290)

B22 = Button(root, font = 'arial 10 bold', text = "Connect - Germany", 
    padx=2, bg='yellow2', command=vpn_c_germany).place(x=200, y=330)
    
B23 = Button(root, font = 'arial 10 bold', text = "Connect - UK", 
    padx=2, bg='yellow2', command=vpn_c_uk).place(x=200, y=370)
    
        
B24 = Button(root, font = 'arial 10 bold', text = "Disconnect VPN", 
    padx=2, bg='orange red', command=vpn_disconnect).place(x=60, y=410)

    
B25 = Button(root, font = 'arial 10 bold', text = "Remove Port 8080 Whitelist", 
    padx=2, bg='ghost white', command=vpn_wl_off).place(x=600,
        y=410)
    
B26 = Button(root, font = 'arial 10 bold', text = "Add Port 8080 Whitelist", 
    padx=2, bg='floral white', command=vpn_wl_on).place(x=600, 
        y=450)

        
B27 = Button(root, font = 'arial 10 bold', text = 'EXIT PROGRAM', width=18, 
    command = Exit, bg = 'firebrick3', padx=2, pady=1).place(x=60, y=450)
    

B28 = Button(root, font = 'arial 10 bold', text = 'Clear Terminal', 
    padx=2, bg='lime green', command=clear_terminal).place(x=400, y=450)    
    
root.mainloop()

