# Script lavet af Frank Simens 28.09.2020
# Prøvet og testet af mig.
# Kontakt frank@simens.dk
#
# Slet apt cache
sudo apt clean
# opdater apt
sudo apt update

# Hent onlyoffice
wget http://download.onlyoffice.com/install/opensource-install.sh
# Installer Onlyoffice
sudo bash opensource-install.sh -ims false
# Installer timeshift til backup af system Chromium som Internet browser 
# Terminator som terminal Hardinfo som systeminfo Scribus som Illustrator eller MS Publisher gimp i stedet for Photoshop 
# Gnome Tweaks og Grub Customizer for at redigere Gnome og Grub 
# Gparted for at Redigere hardiske. Inkscape som tegneprogramm Bluefish for programmering 
# MyPaint som tegneprogram i stedet for paint. 
sudo apt install -y timeshift vlc chromium-browser terminator hardinfo scribus gimp gnome-tweaks grub-customizer gparted inkscape bluefish mypaint

# Updater Systemet
sudo apt update
# Opgrader Systemet
sudo apt -y upgrade

# Import AnyDesk GPG key for signing APT packages.


wget -qO - https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo apt-key add -

# Then add AnyDesk repository content to your Ubuntu system.

echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list


# Finally update apt cache and install the latest release of AnyDesk on Ubuntu 20.04/18.04 Linux.

sudo apt update
sudo apt install anydesk

# Slet firefox og thunderbird
sudo apt remove firefox gnome-terminal thunderbird
