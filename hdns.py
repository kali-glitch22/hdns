#!/bin/python3
import dns.resolver, sys
argumentos = sys.argv
red   = "\033[1;31m"
blue  = "\033[1;34m"
cyan  = "\033[1;36m"
green = "\033[0;32m"
reset = "\033[0;0m"
bold  = "\033[;1m"
reverse = "\033[;7m"
branco = "\033[37m"
gray = "\033[0;37m"
orange = "\033[0;49;33m"
yellow = "\033[0;49;93m"

def instruncoes():
    print('-'*47)
    print(yellow, """\n __  __     _____     __   __     ______    
/\ \_\ \   /\  __-.  /\ "-.\ \   /\  ___\   
\ \  __ \  \ \ \/\ \ \ \ \-.  \  \ \___  \  
 \ \_\ \_\  \ \____-  \ \_\\"\_\  \/\_____\ 
  \/_/\/_/   \/____/   \/_/ \/_/   \/_____/ 
                                            \n\n""", reset)

    if 'hH' in argumentos or len(argumentos) != 4:
        print("""    ./hdns.py alvo -w wordlist
        wordlist by:https://gist.github.com/jhaddix/86a06c5dc309d08580a018c66354a056""".capitalize())
if __name__ == "__main__":
    instruncoes()
def main():
    try:
        word = sys.argv[3]
        alvo = sys.argv[1]
    except Exception as e:
        instruncoes()
        print(e)
        exit()
    res = dns.resolver.Resolver()
    arquivo = open(word, "r")
    subdomains = arquivo.read().splitlines()


    for subdomain in subdomains:
        try:
            sub_alvo = subdomain + "." + alvo
            result = res.resolve(sub_alvo, "A")
            for ip in result:
                print(red,sub_alvo, "->",ip,reset)
        except:
            pass
main()
print('-' * 47)