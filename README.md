🚀 Rabbit & Termux Tool Installation

📌 ধাপ ১: Termux Update

pkg update -y && pkg upgrade -y

📌 ধাপ ২: Repository Install

pkg install root-repo unstable-repo -y

📌 ধাপ ৩: Package Update

pkg update -y

📌 ধাপ ৪: প্রয়োজনীয় Package Install

pkg install python git tsu iw wpa-supplicant pixiewps -y

📌 ধাপ ৫: OneShot Repository Clone

git clone https://github.com/Rem01Gaming/OneShot-Termux.git

📌 ধাপ ৬: Rabbit Tool Repository Clone

git clone https://github.com/sywwuw55-lab/sojib-Hamster-tool-Boss.git

📌 ধাপ ৭: Tool Folder-এ প্রবেশ

cd sojib-Hamster-tool-Boss

📌 ধাপ ৮: Execute Permission দিন

chmod +x rabbit

📌 ধাপ ৯: Rabbit Command Install

cp rabbit /data/data/com.termux/files/usr/bin/rabbit

📌 ধাপ ১০: Rabbit চালু করুন

rabbit

---

💚 প্রতিটি কমান্ড আলাদাভাবে কপি করুন এবং Termux-এ পেস্ট করুন।

⚠️ কোনো কমান্ড চালানোর আগে সেটির কাজ বুঝে নিন।
