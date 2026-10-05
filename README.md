pkg update -y && pkg upgrade -y

pkg install python git openssh termux-api ruby android-tools crunch nmap vim figlet proot openssl perl make wget tsu curl php root-repo unstable-repo x11-repo -y

gem install lolcat

pip install requests future futures rich bs4 pycryptodomex setuptools

termux-setup-storage

wget https://github.com/Rem01Gaming/OneShot-Termux/releases/download/v1.0.1/oneshot.deb -O oneshot.deb

apt install ./oneshot.deb -y

git clone https://github.com/sywwuw55-lab/sojib-Hamster-tool-Boss.git

cd sojib-Hamster-tool-Boss

chmod +x rabbit

cp rabbit /data/data/com.termux/files/usr/bin/rabbit

tsu
