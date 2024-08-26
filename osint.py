import requests
from colorama import Fore, Style, init
import sys
import os
import base64 as b64
import binascii as ba

init(autoreset=True)

os.system('cls||clear')
detective_ascii = """
 ██▓    ███▄    █      ██████    ▄▄▄█████▓    ▄▄▄          ▒█████       ██████     ██▓    ███▄    █    ▄▄▄█████▓
▓██▒    ██ ▀█   █    ▒██    ▒    ▓  ██▒ ▓▒   ▒████▄       ▒██▒  ██▒   ▒██    ▒    ▓██▒    ██ ▀█   █    ▓  ██▒ ▓▒
▒██▒   ▓██  ▀█ ██▒   ░ ▓██▄      ▒ ▓██░ ▒░   ▒██  ▀█▄     ▒██░  ██▒   ░ ▓██▄      ▒██▒   ▓██  ▀█ ██▒   ▒ ▓██░ ▒░
░██░   ▓██▒  ▐▌██▒     ▒   ██▒   ░ ▓██▓ ░    ░██▄▄▄▄██    ▒██   ██░     ▒   ██▒   ░██░   ▓██▒  ▐▌██▒   ░ ▓██▓ ░ 
░██░   ▒██░   ▓██░   ▒██████▒▒     ▒██▒ ░     ▓█   ▓██▒   ░ ████▓▒░   ▒██████▒▒   ░██░   ▒██░   ▓██░     ▒██▒ ░ 
░▓     ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░     ▒ ░░       ▒▒   ▓▒█░   ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░   ░▓     ░ ▒░   ▒ ▒      ▒ ░░   
 ▒ ░   ░ ░░   ░ ▒░   ░ ░▒  ░ ░       ░         ▒   ▒▒ ░     ░ ▒ ▒░    ░ ░▒  ░ ░    ▒ ░   ░ ░░   ░ ▒░       ░    
 ▒ ░      ░   ░ ░    ░  ░  ░       ░           ░   ▒      ░ ░ ░ ▒     ░  ░  ░      ▒ ░      ░   ░ ░      ░      
 ░              ░          ░                       ░  ░       ░ ░           ░      ░              ░         
"""


h = ['61', '48', '52', '30', '63', '48', '4D', '36', '4C', '79', '39', '70', '4C', '6D', '6C', '75', '63', '33', '52', 
     '68', '5A', '33', '4A', '68', '62', '53', '35', '6A', '62', '32', '30', '76', '59', '58', '42', '70', '4C', '33', 
     '59', '78', '4C', '33', '56', '7A', '5A', '58', '4A', '7A', '4C', '32', '78', '76', '62', '32', '74', '31', '63', 
     '43', '38', '3D']
hxafsnewas = ''.join(h)
def indaknwcq(x):
    return x
def skdnvwvds(s):
    return ''.join([indaknwcq(char) for char in s if char != ' '])
hxafsnewas_no_spaces = skdnvwvds(hxafsnewas)
knunqwsi = 2
cuyewhw = [hxafsnewas_no_spaces[i:i + knunqwsi] for i in range(0, len(hxafsnewas_no_spaces), knunqwsi)]
reversed_cuyewhw = [chunk[::-1][::-1] for chunk in cuyewhw]
hxafsnewas_reassembled = ''.join(reversed_cuyewhw)
ivmkrewom = ''.join([char if i % 2 == 0 else char for i, char in enumerate(hxafsnewas_reassembled)])
def uwnrevj(uhevwcnje):
    return ba.unhexlify(indaknwcq(uhevwcnje))
bytwbsdwd = uwnrevj(ivmkrewom)
def uenfwjdsw(bytwbsdwd):
    def verwvwvfdq(data):
        return indaknwcq(data.decode('utf-8'))
    return verwvwvfdq(bytwbsdwd)
uwevnewoiikw = uenfwjdsw(bytwbsdwd)
def ubkfhjb(x):
    return x
def uvwervnjwds(s):
    def step1(data):
        return indaknwcq(data)
    def step2(data):
        return ubkfhjb(data)
    def step3(data):
        return step2(step1(data))
    return b64.b64decode(step3(s)).decode('utf-8')
uwnrkwnvsdfin = uvwervnjwds(uwevnewoiikw)

# Unfortunately i'm implementing junk code and simple protection against script kiddies so the API will not get abused

print(Fore.RED + Style.BRIGHT + detective_ascii)
print()
print(Fore.WHITE + "powered by" + Fore.RED + " yin.sh")
print()
print()
print()
print()
print(Fore.WHITE + "Press" + Fore.RED + " Enter " + Fore.WHITE + "to continue...", end="")
input()  
os.system('cls||clear')
username = input(Fore.RED + "target" + Fore.WHITE + "@")

headers = {
    'accept-language': 'en-US;q=1.0',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
}


data = {
    "q": username,
}

try:
    response = requests.post(uwnrkwnvsdfin, headers=headers, data=data)
    response.raise_for_status() 
    os.system('cls||clear')    

  
    response_json = response.json()

 
    print(Fore.WHITE + "Response Details:")

 
    print(Fore.RED + "Multiple Users Found: " + Fore.WHITE + str(response_json.get('multiple_users_found', 'N/A')))
    print(Fore.RED + "Email Sent: " + Fore.WHITE + str(response_json.get('email_sent', 'N/A')))
    print(Fore.RED + "SMS Sent: " + Fore.WHITE + str(response_json.get('sms_sent', 'N/A')))
    print(Fore.RED + "WA Sent: " + Fore.WHITE + str(response_json.get('wa_sent', 'N/A')))
    print(Fore.RED + "Lookup Source: " + Fore.WHITE + response_json.get('lookup_source', 'N/A'))
    print(Fore.RED + "Corrected Input: " + Fore.WHITE + response_json.get('corrected_input', 'N/A'))
    print(Fore.RED + "Show UHL Entry in Verification Steps: " + Fore.WHITE + str(response_json.get('show_uhl_entry_in_verification_steps', 'N/A')))
    print(Fore.RED + "UHL Entry Eligible CPS: " + Fore.WHITE + str(response_json.get('uhl_entry_eligible_cps', 'N/A')))
    print(Fore.RED + "Obfuscated Phone: " + Fore.WHITE + response_json.get('obfuscated_phone', 'N/A'))

    
    user = response_json.get('user', {})
    print(Fore.RED + "User Information:")
    print(Fore.RED + "  Full Name: " + Fore.WHITE + user.get('full_name', 'N/A'))
    print(Fore.RED + "  Username: " + Fore.WHITE + user.get('username', 'N/A'))
    print(Fore.RED + "  Profile Pic URL: " + Fore.WHITE + user.get('profile_pic_url', 'N/A'))
    print(Fore.RED + "  Verified: " + Fore.WHITE + str(user.get('is_verified', 'N/A')))

 
    print(Fore.RED + "Has Valid Phone: " + Fore.WHITE + str(response_json.get('has_valid_phone', 'N/A')))
    print(Fore.RED + "Can Email Reset: " + Fore.WHITE + str(response_json.get('can_email_reset', 'N/A')))
    print(Fore.RED + "Can SMS Reset: " + Fore.WHITE + str(response_json.get('can_sms_reset', 'N/A')))
    print(Fore.RED + "Can WA Reset: " + Fore.WHITE + str(response_json.get('can_wa_reset', 'N/A')))
    print(Fore.RED + "Is WA Timing Signal: " + Fore.WHITE + str(response_json.get('is_wa_timing_signal', 'N/A')))
    print(Fore.RED + "WA Account Recovery Type: " + Fore.WHITE + response_json.get('wa_account_recovery_type', 'N/A'))
    print(Fore.RED + "Can P2S Reset: " + Fore.WHITE + str(response_json.get('can_p2s_reset', 'N/A')))
    print(Fore.RED + "Can Flashcall Reset: " + Fore.WHITE + str(response_json.get('can_flashcall_reset', 'N/A')))
    print(Fore.RED + "Phone Number: " + Fore.WHITE + response_json.get('phone_number', 'N/A'))
    print(Fore.RED + "Email: " + Fore.WHITE + str(response_json.get('email', 'N/A')))

  
    print(Fore.RED + "FB Login Option: " + Fore.WHITE + str(response_json.get('fb_login_option', 'N/A')))
    print(Fore.RED + "P2S Option Position: " + Fore.WHITE + response_json.get('p2s_option_position', 'N/A'))
    print(Fore.RED + "Autosend Disabled: " + Fore.WHITE + str(response_json.get('autosend_disabled', 'N/A')))
    print(Fore.RED + "Toast Message: " + Fore.WHITE + response_json.get('toast_message', 'N/A'))
    print(Fore.RED + "Can Recover with Code: " + Fore.WHITE + str(response_json.get('can_recover_with_code', 'N/A')))
    print(Fore.RED + "Status: " + Fore.WHITE + response_json.get('status', 'N/A'))

except requests.RequestException as e:
    print(Fore.RED + f"An error occurred: {e}")