🚀 Rabbit & Termux Tool Installation

📌 ধাপ ১: Termux Update & Upgrade

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

📌 ধাপ ৭: Rabbit Folder-এ প্রবেশ

cd sojib-Hamster-tool-Boss

📌 ধাপ ৮: Execute Permission দেওয়া

chmod +x rabbit

📌 ধাপ ৯: Rabbit Command Install

cp rabbit /data/data/com.termux/files/usr/bin/rabbit

📌 ধাপ ১০: Rabbit Tool চালু করা

rabbit

---

💚 প্রতিটি ধাপের কমান্ড আলাদাভাবে Copy করে Termux-এ Paste করুন।

⚠️ নোট: একই Repository আগে Clone করা থাকলে "git clone" কমান্ডে error আসতে পারে।
