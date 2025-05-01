import hashlib
import time
import os
import shutil

try:
    import colorama
    colorama.init(autoreset=True)
    
    C_BRIGHT_YELLOW = colorama.Style.BRIGHT + colorama.Fore.YELLOW
    C_BRIGHT_GREEN = colorama.Style.BRIGHT + colorama.Fore.GREEN
    C_CYAN = colorama.Fore.CYAN 
    C_BRIGHT_WHITE = colorama.Style.BRIGHT + colorama.Fore.WHITE
    C_BRIGHT_RED = colorama.Style.BRIGHT + colorama.Fore.RED
    C_DARK_RED = colorama.Fore.RED 
    C_BRIGHT_MAGENTA = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
    C_BRIGHT_BLUE = colorama.Style.BRIGHT + colorama.Fore.BLUE
    C_WHITE = colorama.Fore.WHITE
    C_GREEN = colorama.Fore.GREEN 
    C_RED = colorama.Fore.RED 
    C_YELLOW = colorama.Fore.YELLOW 
    C_RESET = colorama.Style.RESET_ALL
except ImportError:
    print("Error: 'colorama' library not found.")
    print("Please install it using: pip install colorama")
    C_BRIGHT_YELLOW = C_BRIGHT_GREEN = C_CYAN = C_BRIGHT_WHITE = C_BRIGHT_RED = ""
    C_DARK_RED = C_BRIGHT_MAGENTA = C_BRIGHT_BLUE = C_WHITE = C_GREEN = C_RED = ""
    C_YELLOW = C_RESET = ""
    
    



def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    
    try:
        
        width = shutil.get_terminal_size().columns
        return max(width, 60) 
    except OSError:
        return 80 

def center_text(text, width):
    
    import re
    plain_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
    return text.center(width + len(text) - len(plain_text))


def print_separator(full_width, percent=75, color=C_BRIGHT_YELLOW):
    
    separator_char = "-="
    
    target_len = int(full_width * (percent / 100.0))
    
    if target_len % 2 != 0:
        target_len -= 1
    target_len = max(2, target_len) 

    separator = (separator_char * (target_len // len(separator_char)))
    
    if len(separator) < target_len:
         separator += separator_char[0]

    print(center_text(color + separator + C_RESET, full_width))

MR_PROGRAMM_ART = [
    "▓▓   ▓▓  ▓▓▓▓         ▓▓▓▓    ▓▓▓▓     ▓▓▓    ▓▓▓▓   ▓▓▓▓     ▓▓▓   ▓▓   ▓▓  ▓▓   ▓▓",
    "▓▓▓ ▓▓▓  ▓▓  ▓▓       ▓▓  ▓▓  ▓▓  ▓   ▓▓ ▓▓  ▓▓      ▓▓  ▓   ▓▓ ▓▓  ▓▓▓ ▓▓▓  ▓▓▓ ▓▓▓",
    "▓  ▓  ▓  ▓▓▓▓    ▓▓   ▓▓▓▓    ▓▓▓▓    ▓   ▓  ▓  ▓▓▓  ▓▓▓▓    ▓▓▓▓▓  ▓  ▓  ▓  ▓  ▓  ▓",
    "▓     ▓  ▓   ▓        ▓       ▓   ▓   ▓▓ ▓▓  ▓▓   ▓  ▓   ▓   ▓   ▓  ▓     ▓  ▓     ▓",
    "▓▓   ▓▓  ▓    ▓       ▓       ▓    ▓   ▓▓▓    ▓▓▓▓   ▓    ▓  ▓   ▓  ▓▓   ▓▓  ▓▓   ▓▓"  
]


HASH_ALGORITHMS = [
    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
    'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512',
    'blake2b', 'blake2s'
]

def identify_hash(password, target_hash):
    password_bytes = password.encode('utf-8')
    target_hash_lower = target_hash.lower()

    for algo_name in HASH_ALGORITHMS:
        try:
            hasher = hashlib.new(algo_name)
            hasher.update(password_bytes)
            calculated_hash = hasher.hexdigest()
            if calculated_hash == target_hash_lower:
                return algo_name.upper() 
        except Exception:
            continue 
    return None



def display_title(width):
    
    clear_console()
    print_separator(width, percent=75, color=C_BRIGHT_YELLOW) 
    print() 

    
    for line in MR_PROGRAMM_ART:
         
         print(C_BRIGHT_GREEN + center_text(line, width) + C_RESET)

    print() 

    
    combined_title_line = (
        C_CYAN + "HASH ANALYZER" + C_RESET +
        C_BRIGHT_WHITE + " version " +
        C_DARK_RED + "[" + C_BRIGHT_RED + " 1.1 " + C_DARK_RED + "]" + C_RESET
    )

    
    print(center_text(combined_title_line, width))

    print() 
    print_separator(width, percent=75, color=C_BRIGHT_YELLOW) 
    time.sleep(1.25)
    print("\n\n") 


def main():
    
    while True:
        width = get_terminal_width()
        display_title(width)

        
        try:
            print(C_CYAN + "Please input Password:      " + C_RESET, end='')
            password = input(C_BRIGHT_WHITE)

            print(C_BRIGHT_GREEN + "Please input HASH data:     " + C_RESET, end='')
            hash_input = input(C_BRIGHT_RED)
            time.sleep(1)

        except EOFError:
            print("\nExiting.")
            break
        except KeyboardInterrupt:
             print("\nExiting.")
             break


        print("\n") 

        
        base_text = C_BRIGHT_MAGENTA + "Calculating possible " + C_BRIGHT_YELLOW + "HASH" + C_BRIGHT_MAGENTA + " possibilities"
        print(base_text, end='', flush=True)

        
        dots = ""
        for i in range(1, 4):
            dots = "." * i
            
            print(f"\r{base_text}{C_BRIGHT_MAGENTA}{dots}{' ' * (3 - len(dots))}", end='', flush=True)
            time.sleep(0.4)
        print() 

        found_algo = identify_hash(password, hash_input)

        
        if found_algo:
            print(C_GREEN + "HASH" + C_BRIGHT_YELLOW + " has been discovered!" + C_RESET)
            time.sleep(1.25)
            clear_console()
            time.sleep(0.5)

            print(f"{C_CYAN}Password{C_BRIGHT_WHITE}: {C_BRIGHT_BLUE}{password}{C_RESET}")
            print(f"{C_BRIGHT_YELLOW}HASH    {C_BRIGHT_WHITE}: {C_BRIGHT_BLUE}{hash_input}{C_RESET}") 
            print()

            
            print(f"{C_BRIGHT_WHITE}[[" +
                  f"{C_WHITE} This has been discovered to be using the " +
                  f"{C_BRIGHT_WHITE}- {C_BRIGHT_GREEN}{found_algo}{C_BRIGHT_WHITE} - " +
                  f"{C_WHITE}hashing {C_BRIGHT_YELLOW}method{C_BRIGHT_RED}" + 
                  f"{C_BRIGHT_WHITE} ]]{C_RESET}") 

        else:
            print(f"{C_RED}NO possible {C_BRIGHT_YELLOW}HASH{C_RED} was discovered.{C_RESET}")

        
        print("\n\n\n") 
        try:
            input(C_BRIGHT_WHITE + "Press enter to continue..." + C_RESET)
        except EOFError:
            print("\nExiting.")
            break
        except KeyboardInterrupt:
             print("\nExiting.")
             break
        
if __name__ == "__main__":
    main()