# 21600402 전산전자공학부 안수현
# 파이썬 프로그래밍 HW_1 

# 이 코드는 박지현교수님 파이썬 프로그래밍 수업의 과제로 단위 변환 프로그램입니다. 
# 항목은 길이 1) 길이 2) 넓이 3) 무게 4) 온도 5) 속도 6) 데이터양 7) 시간
# - 으로 총 7가지의 항목을 구현했습니다. 

# 프로그램의 가독성을 위해서 추가한 seperator 변수, console 의 출력에서 사용한다. 
seperator = "-"*100
# 각 리스트는 유저가 항목을 선택하고, 세부항목을 보여주기 위하여 사용된다. 
length = ["1. 센티미터(cm)->인치(in)", "2. 센티미터(cm)->미터(m)","3. 인치(in)->센티미터(cm)"]
area =["1. 제곱미터(m^2)->평","2. 제곱미터(m^2)->제곱피트(ft^2)","3. 제곱미터(m^2)->제곱야드(yd^2)"]
weight =["1. 킬로그램(kg)->그램(g)","2. 그램(g)->온스(oz)","3. 킬로그램(kg)->파운드(lb) "]
temp =["1. 섭씨온도('C)->화씨온도('F)","2. 화씨온도('F)->섭씨온도('C)","3.섭씨온도('C)->절대온도(K)"]
speed =["1. 초속(m/s)->시속(km/h)","2. 초속(m/s)->시속(m/h)","3. 시속(km/h)->시속(m/s)"]
data =["1. 메가바이트(MB)->킬로바이트(KB)","2. 메가바이트(MB)->기가바이트(GB)","3.기가바이트(GB)->테라바이트(TB) "]
time = ["1. 초->분","2. 분->시간","3. 시간->초 "]
# categoryList = [length, area, weight, temp, speed, data, time ] 
# 유저에게 어떠한 항목이 있는지 보여주기 위한 categoryLabel이다. 
categoryLabel = "1) 길이 2) 넓이 3) 무게 4) 온도 5) 속도 6) 데이터양 7) 시간"



# UI 제공 : 프로그램 설명
print(seperator)
print("안녕하세요, 단위변환 프로그램입니다 :D \n변환할 단위를 선택하시고 입력을 하시면 변환된 단위로 출력이 됩니다!")
# 지원하는 변환 목록 소개
print("지원 목록은 ",categoryLabel,"입니다.\n"+seperator)



# 사용자로부터 사용할 카테고리를 입력받기 위한 안내 메세지 출력 -> 입력 형식 지정
print("변환하실 값의 항목을 '숫자'로 입력해주세요. \n항목 [ "+categoryLabel+ " ]\n입력 예 : 1")
# 사용자로부터 사용할 카테고리를 입력 받음 
mode = input("입력 : ")



# 입력값이 잘못되었거나, 카테고리 번호내에 없는 경우의 처리 
# 정수로 변환해 검사를 시행 
if (not mode.isdecimal()) or (int(mode)<1 or int(mode)>7 ):
    # 입력된 값을 보여주면서, 무엇이 잘못되었는지 설명 
    print(seperator)
    print("!!!입력 값 :", mode, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
    # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
    input("\n프로그램을 종료합니다. (확인 = 엔터)")

 # categoryList = [length, area, weight, temp, speed, data, time ] 
# 입력값이 멀쩡한 경우에 대한 수행 
else:
    # 입력 값을 정수 값으로 변환 
    mode =int(mode)
    print(seperator)
    
    # 입력된 첫번째 항목에 따라 각각 다른 세부항목을 출력합니다.
    # 항목 1 : 길이
    if mode == 1 :
        # 입력받은 항목 출력
        print("선택하신 항목은 길이 입니다. 변환 기능은 아래와 같습니다.")
        print(length)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
        # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdecimal()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+length[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :# 센티미터(cm)->인치(in)
                    print("입력하신", inputValue,"센티미터(cm) -> 인치(in) 변환 값 =",round(inputValue*0.39370,2))
                elif modeType == 2 :# 센티미터(cm)->미터(m)
                    print("입력하신", inputValue,"센티미터(cm) -> 미터(m) 변환 값 =",round(inputValue*0.01,2))
                elif modeType == 3 :# 인치(in)->센티미터(cm)
                    print("입력하신", inputValue,"센티미터(cm) -> 인치(in) 변환 값 =",round(inputValue/0.39370,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")
    # 항목 2 : 넓이    
    elif mode == 2 :    
        print("선택하신 항목은 넓이 입니다. 변환 기능은 아래와 같습니다.")
        print(area)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
        # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdecimal()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+area[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :# "제곱미터(m^2)->평" 
                    print("입력하신", inputValue,"제곱미터(m^2)->평 변환 값 =",round(inputValue*3.305785,2))
                elif modeType == 2 :# "제곱미터(m^2)->제곱피트(ft^2)"
                    print("입력하신", inputValue,"제곱미터(m^2)->제곱피트(ft^2) 변환 값 =",round(inputValue*10.76391,2))
                elif modeType == 3 :# "제곱미터(m^2)->제곱야드(yd^2)"
                    print("입력하신", inputValue,"제곱미터(m^2)->제곱야드(yd^2) 변환 값 =",round(inputValue*1.19599,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")
    # 항목 3 : 무게
    elif mode == 3 :
        print("선택하신 항목은 무게 입니다. 변환 기능은 아래와 같습니다.")
        print(weight)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
        # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdecimal()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+weight[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :# 킬로그램(kg)->그램(g)
                    print("입력하신", inputValue,"킬로그램(kg)->그램(g) 변환 값 =",round(inputValue*1000,2))
                elif modeType == 2 :# "그램(g)->온스(oz)"
                    print("입력하신", inputValue,"그램(g)->온스(oz) 변환 값 =",round(inputValue*0.035274,2))
                elif modeType == 3 :# "킬로그램(kg)->파운드(lb)"
                    print("입력하신", inputValue,"킬로그램(kg)->파운드(lb) 변환 값 =",round(inputValue*2.204623,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")
    # 항목 4 : 온도
    elif mode == 4 :
        print("선택하신 항목은 온도 입니다. 변환 기능은 아래와 같습니다.")
        print(temp)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
        # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdecimal()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+temp[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :#  섭씨온도('C)->화씨온도('F)
                    print("입력하신", inputValue,"섭씨온도('C)->화씨온도('F) 변환 값 =",round(inputValue*1.8 + 32,2))
                elif modeType == 2 :# 화씨온도('F)->섭씨온도('C)
                    print("입력하신", inputValue,"화씨온도('F)->섭씨온도('C) 변환 값 =",round(inputValue/1.8 - 32,2))
                elif modeType == 3 :# 섭씨온도('C)->절대온도(K)
                    print("입력하신", inputValue,"섭씨온도('C)->절대온도(K) 변환 값 =",round(inputValue-273.15,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")
    # 항목 5 : 속도
    elif mode == 5 :
        print("선택하신 항목은 속도 입니다. 변환 기능은 아래와 같습니다.")
        print(speed)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
        # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdecimal()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+speed[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :#  초속(m/s)->시속(km/h)
                    print("입력하신", inputValue,"초속(m/s)->시속(km/h) 변환 값 =",round(inputValue*3.6,2))
                elif modeType == 2 :# 초속(m/s)->시속(m/h)
                    print("입력하신", inputValue,"초속(m/s)->시속(m/h) 변환 값 =",round(inputValue*3600,2))
                elif modeType == 3 :# 시속(km/h)->시속(m/s)
                    print("입력하신", inputValue,"시속(km/h)->시속(m/s) 변환 값 =",round(inputValue*0.277778,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")
    # 항목 6 : 데이터양
    elif mode == 6 :
        print("선택하신 항목은 데이터양 입니다. 변환 기능은 아래와 같습니다.")
        print(data)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
         # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdecimal()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+data[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :#  메가바이트(MB)->킬로바이트(KB)
                    print("입력하신", inputValue,"메가바이트(MB)->킬로바이트(KB) 변환 값 =",round(inputValue*1024,2))
                elif modeType == 2 :# 메가바이트(MB)->기가바이트(GB)
                    print("입력하신", inputValue,"메가바이트(MB)->기가바이트(GB) 변환 값 =",round(inputValue*0.000977,2))
                elif modeType == 3 :# 기가바이트(GB)->테라바이트(TB)
                    print("입력하신", inputValue,"기가바이트(GB)->테라바이트(TB) 변환 값 =",round(inputValue*0.000977,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")
    # 항목 7 : 시간
    elif mode == 7 :
        print("선택하신 항목은 시간 입니다. 변환 기능은 아래와 같습니다.")
        print(time)
        # 세부항목 수행을 위한 입력을 받는 코드
        modeType = input("선택(숫자로 입력) : ")
        # 세부항목의 갯수가 3개이기 때문에 1,2,3 이외의 값은 유효하지 않음
        # 유효값 범위로 들어왔을때의 수행하는 if-than 문  
        if (not modeType.isdigit()) or (int(modeType)<1 or int(modeType)>3):
            print(seperator)
            print("!!!입력 값 :", modeType, " 해당 하는 목록의 번호를 입력하지 않으셨습니다.!!!")
            # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
            input("\n프로그램을 종료합니다. (확인 = 엔터)")
        else:
            print(seperator)
            modeType = int (modeType)
            # 입력한 세부항목 재확인 
            # print("입력하신 세부항목은",length[modeType-1])
            inputValue = input("변환할 양의정수 값만 입력해주세요! 현재 모드 --> "+time[modeType-1]+"\n입력 :")
            if inputValue.isdigit() and int(inputValue) > 0 :
                inputValue = int(inputValue)
                if modeType == 1 :#  초->분
                    print("입력하신", inputValue,"초->분 변환 값 =",round(inputValue/60,2))
                elif modeType == 2 :# 분->시간 
                    print("입력하신", inputValue,"분->시간  변환 값 =",round(inputValue/60,2))
                elif modeType == 3 :# 시간->초
                    print("입력하신", inputValue,"시간->초 변환 값 =",round(inputValue*360,2))
                print(seperator)
            else:
                print("!!!입력 값 :", inputValue, " 양수를 입력하지 않았습니다!!!")
                # 프로그램이 바로 끝나는 것이 아닌, 종료함을 알리고 엔터를 입력받기 전까지 콘솔에 보임
                input("\n프로그램을 종료합니다. (확인 = 엔터)")