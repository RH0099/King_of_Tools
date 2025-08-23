
pkg update && pkg upgrade -y

pkg install python nmap git termux-api -y

pip install mitmproxy

pkg instoll python -y

pkg instoll python3 -y

pkg install dsniff -y 

pkg install arp-scan -y 

pkg instoll git -y

pkg instoll nmap -y

git clone https://github.com/RH0099/Natwark_scan-MITM_tools.git

clear

cd Natwark_scan-MITM_tools

python3 Advance_MITM.py
