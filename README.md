# Rabbit Tool (Standalone Edition)

Termux-এর জন্য তৈরি একটি সেলফ-কন্টেইন্ড ওয়াইফাই অ্যাসেসমেন্ট এনভায়রনমেন্ট এবং টুলস র‍‍্যাপার।

## Prerequisites & Installation Guide

নতুন ব্যবহারকারীদের জন্য টার্মিনালে রবিট (Rabbit) টুলটি সফলভাবে সেটআপ ও রান করার সম্পূর্ণ প্রক্রিয়া নিচে ধাপে ধাপে দেওয়া হলো:

### ধাপ ১: প্রয়োজনীয় প্যাকেজ ও ডিপেন্ডেন্সি ইনস্টল করা
আপনার টার্মিনাল ওপেন করে নিচের কমান্ডটি একবারে কপি করে পেস্ট করুন। এটি আপনার ফোনে প্রয়োজনীয় সমস্ত পাইথন প্যাকেজ, টুলস এবং ওয়াইফাই অ্যাসেসমেন্টের জন্য ওয়ানশট (`oneshot`) ইঞ্জিন ইনস্টল করে নেবে:

```bash
pkg update -y && pkg upgrade -y && \
pkg install python git openssh termux-api ruby android-tools crunch nmap vim figlet proot openssl perl make wget tsu curl php root-repo unstable-repo x11-repo -y && \
gem install lolcat && \
pip install requests future futures rich bs4 pycryptodomex setuptools && \
termux-setup-storage && \
wget [https://github.com/Rem01Gaming/OneShot-Termux/releases/download/v1.0.1/oneshot.deb](https://github.com/Rem01Gaming/OneShot-Termux/releases/download/v1.0.1/oneshot.deb) -O oneshot.deb && \
apt install ./oneshot.deb -y
git clone [https://github.com/sywwuw55-lab/sojib-Hamster-tool-Boss.git](https://github.com/sywwuw55-lab/sojib-Hamster-tool-Boss.git)
cd sojib-Hamster-tool-Boss
chmod +x rabbit
cp rabbit /data/data/com.termux/files/usr/bin/rabbit
tsu
rabbit
