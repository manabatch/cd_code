
DFA = {
    'i': set('n'),
    'n': set('t'),
    't': None
}

def main():
    ip = input("Enter identifier or int keyword: ")
    print(f'Transitions for {ip}')
    c, n = 0, len(ip)
    for lemme in ip:
        c += 1
        if lemme not in DFA.keys():
            print(ip[c-1:], '->', 'Identifier')
            break
        cur = DFA[lemme]
        if cur is None and c == n:
            print(lemme, '->', 'Keyword')
        else:
            print(lemme, '->', cur)

if __name__ == "__main__":
    exit(main() or 0)
