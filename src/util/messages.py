from colorama import init, Fore

init(autoreset=True)

def success(*args):
    if len(args) == 0:
        print(f'{Fore.GREEN}[SUCCESS]: {args[0]}')
    else:
        print(f'{Fore.GREEN}[SUCCESS]:')

    for msg in args:
        print(f'{Fore.YELLOW}  > {msg}')
