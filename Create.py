import os, sys,time, platform
os.system('clear') 
print('\033[0m [💸] \033[92m Follow Our WhatsApp channel For More Updates 𝐓𝐎𝐇𝐈𝐃 𝐓𝐄𝐂𝐇🥰✨') 
time.sleep(3)
os.system('xdg-open https://whatsapp.com/channel/0029VaGyP933bbVC7G0x0i2T')
print('\n\033[0m [\033[92m✓\033[97m] \033[92m Checking For Updates ....\n') 

bit = platform.architecture()[0]
if bit == '64bit':
    import Safeum
elif bit == '32bit':
    print("\033[0m\033[91m Sorry Your Device Is 32bit, This Tool 32bit Not Sported, Only For \033[92m64Bit\033[0m ]");exit() 
 
