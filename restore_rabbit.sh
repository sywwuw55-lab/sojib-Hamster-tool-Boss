#!/bin/bash
echo "[*] Restoring RABBIT tool to current secure state..."

# ১. লোকাল ডিভাইস আইডি কনফার্ম করা
if [ ! -f ~/.device_id ]; then
    echo "RABBIT-$(cat /proc/sys/kernel/random/uuid | cut -d'-' -f1 | tr '[:lower:]' '[:upper:]')" > ~/.device_id
fi

# ২. মেইন স্ক্রিপ্ট তৈরি করা (HOME এক্সপোর্ট সহ)
cat << 'INNER_EOF' > rabbit
#!/bin/bash
DEVICE_ID_FILE="/data/data/com.termux/files/home/.device_id"
BLOCKLIST_FILE="/data/data/com.termux/files/home/blocklist.txt"

if [ -f "$DEVICE_ID_FILE" ]; then
    DEVICE_ID=$(cat "$DEVICE_ID_FILE")
else
    DEVICE_ID="RABBIT-$(cat /proc/sys/kernel/random/uuid | cut -d'-' -f1 | tr '[:lower:]' '[:upper:]')"
    echo "$DEVICE_ID" > "$DEVICE_ID_FILE"
fi

if [ -f "$BLOCKLIST_FILE" ]; then
    if grep -q "$DEVICE_ID" "$BLOCKLIST_FILE"; then
        echo "============================================================"
        echo " [X] ACCESS DENIED! Your device ($DEVICE_ID) is BLOCKED by Admin."
        echo "============================================================"
        exit 1
    fi
fi

# ব্যানার শো করা
clear
echo "=========================================================="
echo "[!] INITIALIZING SECURE HACKING ENVIRONMENT..."
echo "[!] TARGET: WIRELESS VULNERABILITY ASSESSMENT"
echo "[!] Your Device Unique Code: $DEVICE_ID"
echo "=========================================================="
echo ""
echo "       (\\__/)   "
echo "       (=\\'.\\'=)   "
echo "       (\")_(\")   "
echo ""
echo "  ██╗  ██╗ █████╗ ███╗   ███╗███████╗████████╗███████╗██████╗ "
echo "  ██║  ██║██╔══██╗████╗ ████║██╔════╝╚══██╔══╝██╔════╝██╔══██╗"
echo "  ███████║███████║██╔████╔██║███████╗   ██║   █████╗  ██████╔╝"
echo "  ██╔══██║██╔══██║██║╚██╔╝██║╚════██║   ██║   ██╔══╝  ██╔══██╗"
echo "  ██║  ██║██║  ██║██║ ╚═╝ ██║███████║   ██║   ███████╗██║  ██║"
echo "  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝"
echo ""
echo "[!] WARNING: FOR AUTHORIZED TESTING ONLY [!]"
echo "=========================================================="
echo ""
echo "[*] Summoning Magic Power... SUCCESS"
echo "[*] Granting Root & Network Permissions... SUCCESS"
echo "[*] LAUNCHING ONESHOT MAGIC ENGINE..."
echo ""

# রুট পারমিশনে সঠিক HOME এবং PATH সেট করে oneshot রান করা
su -c "export HOME=/data/data/com.termux/files/home; export PATH=\$PATH:/data/data/com.termux/files/usr/bin; /data/data/com.termux/files/usr/bin/oneshot -i wlan0 -K"
INNER_EOF

# ৩. পারমিশন ঠিক করা এবং বাইনারিতে লিংক করা
chmod +x rabbit
cp rabbit /data/data/com.termux/files/usr/bin/rabbit
chmod +x /data/data/com.termux/files/usr/bin/rabbit

echo "[+] RESTORATION COMPLETED SUCCESSFULLY! Type 'rabbit' to run."
