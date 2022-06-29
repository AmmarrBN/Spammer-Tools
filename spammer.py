#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import os,sys,time,requests,json,random
from colorama import Fore,init,Back

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
W2="\033[1;0m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"
localtime=time.asctime(time.localtime(time.time()))

def logo():
    os.system("clear")
    print (f"""
{putih}                  ╭──────────────────────────────────╮
{putih}                  │   Copyright By Ammar Executed    │
{putih}╭─────────────────┴──────────────────────────────────┴───────────────╮
{putih}│                                                                    │
{putih}│{R} ██████████████████████  {Y}•{biru}⟩ {W}Creator {R}:{W} AmmarrBN                      │
{W}│{R} ██████████████████████  {Y}•{biru}⟩ {W}Githubb {R}:{W} github.com/AmmarrBN           │
{W}│ ██████████████████████  {Y}•{biru}⟩{W} Powered Executed Team                   │
{W}│ ██████████████████████ --|/-\|/-\|\033[1;0m\033[1;41mBrutal Spammer Tools\033[1;0m{putih}|/-\|/-\|\-- │
{putih}│                                                                    │
{putih}╰─────────────────┬───────────────────────────────────┬──────────────╯
{putih}                  │ Waktu {R}:{Y}  {localtime}{W} │
{putih}                  ╰─────────────────┬─────────────────╯
{putih}              ┌─────────────────────┴─────────────────────┐
{putih}              │ Version {R}:{G} 2.08 {B}||{W} Info {R}:{W} Dont Remove {R}Code{W} │
{putih}              └───────────────────────────────────────────┘
{putih}                    {G}Gunakam Dengan Bijak Ya Sluur ツ
{putih}    ┌────┬──────────────────────────────────┬────────┬───────────────┐
{putih}    │ NO │          Menu Tools              │ Status │      Info     │\033[1;0m
{putih}    ├────┼──────────────────────────────────┼────────┼───────────────┤
{W2}    │ {putih}{R}00 {W2}│{putih}{R}         Exited Tools{W2}             │{putih}{ungu}  null  {W2}│{putih} {R} Keluar Tools {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 01{W2} │{putih}        Spam Sms Tools            {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}    Massive    {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 02{W2} │{putih}        Spam Sms Tools            {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}   Unlimited   {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 03{W2} │{putih}        Spam Sms Tools            {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}    Brutall    {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 04{W2} │{putih}        Spam Call Tools           {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}     Delay     {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 05{W2} │{putih}      Spam Call Unlimited         {W2}│{putih}{G} OFLINE {W2}│{putih}{Y}   Perbaikan   {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 06{W2} │{putih}        Spam-WhatsApp             {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}    Massive    {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 07{W2} │{putih}        Spam-WhatsApp             {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}   Unlimited   {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 08{W2} │{putih}        Spam-WhatsApp             {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}    Brutall    {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 09{W2} │{putih}       Spam Sms,Call,Wa           {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}    Normall    {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 10{W2} │{putih}       Spam Sms,Call,Wa           {W2}│{putih}{G} ONLINE {W2}│{putih}{Y}    Brutall    {W2}│
{W2}    │    ├──────────────────────────────────┼────────┼───────────────┤
{W2}    │{putih}{biru} 11{W2} │{putih}       Informasi+Credit           {W2}│{putih}{ungu}  null  {W2}│{putih}{Y}  Info Tools   {W2}│
{W2}    └────┴──────────────────────────────────┴────────┴───────────────┘""")
    bre=input(f"{W}Pilih Menu {biru}00-11 {R}:{G} ")
    if bre == "0" or bre == "00":
        print(f"{W}[{R}!{W}] Exited With Program{abu}....")
        sys.exit("")
    if bre == "1" or bre == "01":
        os.system("git clone https://github.com/AmmarrBN/Massive_Sms")
        os.system("cd Massive_Sms")
    if bre == "2" or bre == "02":
        os.system("git clone https://github.com/AmmarrBN/Sms-Unli && cd Sms-Unli && python taekyung.py")
    
logo()
