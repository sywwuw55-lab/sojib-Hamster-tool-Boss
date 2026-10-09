# 🐹 HAMSTER TOOL

> 🔥 নতুন হলে চিন্তার কিছু নেই — নিচের commands একসাথে copy করে Termux-এ paste করুন।
>
> 😈 Setup করুন এবং নিজের/অনুমতিপ্রাপ্ত network-এ ব্যবহার করুন।

## 🚀 INSTALL

pkg update -y && pkg upgrade -y
pkg install root-repo unstable-repo -y
pkg update -y
pkg install python git tsu iw wpa-supplicant pixiewps -y
git clone https://github.com/Rem01Gaming/OneShot-Termux.git
git clone https://github.com/sywwuw55-lab/sojib-Hamster-tool-Boss.git
cd sojib-Hamster-tool-Boss
chmod +x rabbit
cp rabbit /data/data/com.termux/files/usr/bin/rabbit
rabbit
