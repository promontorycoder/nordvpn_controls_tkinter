nordvpn.py

Program name: NordVPN Controls
Program Creator: promontorycoder

Purpose of Program: 
    Control of NordVPN application in Ubuntu 20.04 via tkinter GUI and python
            
    Creator used to help with python and tkinter learning.

Credits:
    NordVPN - Author has paid NordVPN account at time of program creation
    OpenVPN        

________________________________________________________________________________

REQUIREMENTS FOR UBUNTU 20.04
________________________________________________________________________________

python3
    sudo apt-get install -y python3
    
tkinter
    sudo apt-get install -y python3-tk 

________________________________________________________________________________

GIT CLONE LINK
________________________________________________________________________________

# To git clone into the repository folder, enter the following command into 
# Terminal after navigating from within Terminal to the folder you'd like the
# program folder to be cloned to.

git clone https://github.com/promontorycoder/random_word_list_tkinter.git
________________________________________________________________________________

INSTALLATION INSTRUCTIONS FOR UBUNTU 20.04
________________________________________________________________________________

Step 1: Acquire program files
    Copy files via git clone or other method to chosen install folder

Step 2: Make program files executable
    Open gnome-terminal and navigate to folder with downloaded program files
    Enter the following commands into gnome-terminal:
        chmod +x nordvpn.py
        chmod +x nordvpn.sh
        chmod +x nordvpn_start.desktop
        
Step 2: Edit files to reflect your directory structure
    Open nordvpn.sh into text editor and change line 2 file path to match your
    file structure
    Save and exit file
    
    Open nordvpn_start.desktop into text editor and change lines 5, 6 and 7 to 
    match your file structure
    Save and exit file
    
Step 3: Install tkinter if you do not already have it installed.
    Open gnome-terminal and execute the following command:
        sudo apt-get install -y python3-tk
        
Step 4: Copy .desktop file to /usr/share/applications
    Open gnome-terminal and enter the following command:
        sudo cp nordvpn_start.desktop /usr/share/applications

