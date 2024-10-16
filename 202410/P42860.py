def solution(name):
    spell_move = 0
    cursor_move = len(name) - 1
    
    for i, spell in enumerate(name):
        spell_move += min(ord(spell)-ord('A'), ord('Z')-ord(spell)+1)
        
        next = i+1
        while next < len(name) and name[next]=='A':
            next += 1 #연속된 A가 끝나고 시작지점
        cursor_move = min(cursor_move, i*2+(len(name)-next), 2*(len(name)-next)+i)
    return spell_move+cursor_move