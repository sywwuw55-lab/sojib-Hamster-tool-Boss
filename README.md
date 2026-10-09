# 🚀 Rabbit & Termux Tool Installation

### 📌 ধাপ ১: Termux Update & Upgrade

```bash
pkg update -y && pkg upgrade -y
```

### 📌 ধাপ ২: Repository Install

```bash
pkg install root-repo unstable-repo -y
```

### 📌 ধাপ ৩: Package Update

```bash
pkg update -y
```

### 📌 ধাপ ৪: প্রয়োজনীয় Package Install

```bash
pkg install python git tsu iw wpa-supplicant pixiewps -y
```

### 📌 ধাপ ৫: OneShot Repository Clone

```bash
git clone https://github.com/Rem01Gaming/OneShot-Termux.git
```

### 📌 ধাপ ৬: Rabbit Tool Repository Clone

```bash
git clone https://github.com/sywwuw55-lab/sojib-Hamster-tool-Boss.git
```

### 📌 ধাপ ৭: Rabbit Folder-এ প্রবেশ

```bash
cd sojib-Hamster-tool-Boss
```

### 📌 ধাপ ৮: Execute Permission দেওয়া

```bash
chmod +x rabbit
```

### 📌 ধাপ ৯: Rabbit Command Install

```bash
cp rabbit /data/data/com.termux/files/usr/bin/rabbit
```

### 📌 ধাপ ১০: Rabbit Tool চালু করা

```bash
rabbit
```

---
💚 প্রতিটি ধাপের কমান্ড আলাদাভাবে কপি করে Termux-এ চালান।
