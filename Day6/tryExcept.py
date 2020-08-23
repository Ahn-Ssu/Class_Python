
try:
    f = open('foo.txt', 'w')
    # 오류 강제 발생시키기!  
    raise NotImplementedError # -> 꼭 구현해야하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용 
    pass
except:
    print("실패실패")
finally:
    f.close()


# Exception Custom
class myError(Exception):
    pass

def sayNick(nick):
    if nick == '바보':
        raise myError()
    print(nick)