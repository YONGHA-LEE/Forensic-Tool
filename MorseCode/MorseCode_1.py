message = '- .... . .--. .- ... ... .-- --- .-. -.. ..-. --- .-. - .... .. ... .-.. . ...- . .-.. .. ... .-- . .-.. .-.. -.. --- -. .'

morsecode = {
    '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd',
    '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h',
    '..' : 'i', '.---' : 'j', '-.-' : 'k', '.-..' : 'l',
    '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p',
    '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't',
    '..-' : 'u', '...-' : 'v', '.--' : 'w', '-..-' : 'x',
    '-.--' : 'y', '--..' : 'z', '.----' : '1', '..---' : '2',
    '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6',
    '--...' : '7', '---..' : '8', '----.' : '9', '-----' : '0',
    '--..--' : ',', '---...' : ':', '..--..' : '?', '.----.' : "'",
    '-....-' : '-', '-..-.' : '/' 
    }

def decrypt(message):
    result = ''

    for c in message.split(' '):    # 공백 기준으로 split
        if c in morsecode.keys():
            result += morsecode[c]
    
    return result

if __name__ == '__main__':
    result = decrypt(message)
    print(result)
