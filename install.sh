#!/bin/bash
#creation de daemon 
USERNAME=$( logname )

TO_CRYPT="/home/$USERNAME/cryptoProject/toCrypt"
CRYPTED="/home/$USERNAME/cryptoProject/crypted"
TO_DECRYPT="/home/$USERNAME/cryptoProject/toDecrypt"
DECRYPTED="/home/$USERNAME/cryptoProject/toDecrypt"

CHEMIN_SH="/usr/bin"

mkdir -p TO_CRYPT
mkdir -p CRYPTED
mkdir -p TO_DECRYPT
mkdir -p DECRYPTED

sudo cp service.sh $CHEMIN_SH

printf "%s\n" "[unit]" "" "[service]" "" "[install]" ""
