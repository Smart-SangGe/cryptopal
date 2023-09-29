base64 --decode 7.txt > encrypted7.bin
openssl enc -d -aes-128-ecb -K $(echo -n "YELLOW SUBMARINE" | xxd -p) -in encrypted7.bin -out decrypted7.txt
cat decrypted7.txt