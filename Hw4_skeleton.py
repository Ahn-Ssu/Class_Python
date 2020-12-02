from tkinter import *


window = Tk()
window.title("체온 측정 프로그램")

def centerWindow():
    w = 500
    h = 200

    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = (sw - 400)/2
    y = (sh- 400)/2
    window.geometry('%dx%d+%d+%d'%(w,h,x,y))
centerWindow()

# window에서 좌우로 구분하여 배치할수 있는 요소들을 배치하기 위해서 F1이라는 이름으로 프레임을 하나 만듬 
frame_F1 = Frame(window, relief="solid",padx=10,pady=10)
frame_F1.grid(row=0, column=0)

# # F1 프레임을 좌우로 구분하기 위해서 프레임 내에서 프레임을 좌|우, 2개로 나누어서 생성함 
# f1_lhs = Frame(frame_F1, relief="solid", padx=1, pady=1, width=20)
# f1_lhs.grid(row=0, column=0)

# f1_rhs = Frame(frame_F1, relief="solid", padx=1, pady=1)
# f1_rhs.grid(row=0, column=1)


#왼쪽에 놓일 라벨과 랜덤 생성 버튼 
ageLabel = Label(frame_F1, text="연령대 선택 :",width=20)
ageLabel.grid(row=0,column=0)

areaLabel = Label(frame_F1, text="측정 부위 선택 :",width=20)
areaLabel.grid(row=1,column=0)

tempLabel = Label(frame_F1, text="체온 입력 :",width=20)
tempLabel.grid(row=2,column=0)



#오른쪽에 놓일 라벨과 결과 확인 버튼 
agegetter = StringVar(value="11-65세")
age0radio = Radiobutton(frame_F1, text="0-2세", value="0-2세", variable=agegetter, width=7).grid(row=0,column=1)
age3radio = Radiobutton(frame_F1, text="3-10세", value="3-10세", variable=agegetter, width=7).grid(row=0,column=2)
age3radio = Radiobutton(frame_F1, text="11-65세", value="11-65세", variable=agegetter, width=7).grid(row=0,column=3)
age3radio = Radiobutton(frame_F1, text="65세 이상", value="65세 이상", variable=agegetter, width=7).grid(row=0,column=4)

areagetter = StringVar(value="귀")
area1Radio = Radiobutton(frame_F1, text="구강 ", value="구강", variable=areagetter, width=7).grid(row=1,column=1)
area2Radio = Radiobutton(frame_F1, text="귀", value="귀", variable=areagetter, width=7).grid(row=1,column=2)
area3Radio = Radiobutton(frame_F1, text="항문", value="항문", variable=areagetter, width=7).grid(row=1,column=3)
area4Radio = Radiobutton(frame_F1, text="겨드랑이", value="겨드랑이", variable=areagetter, width=7).grid(row=1,column=4)

strgetter = StringVar(value="36.5")
tempTextBox = Entry(frame_F1,textvariable=strgetter,width=10).grid(row=2,column=1)


randomButton = Button(frame_F1, text="자동 입력(랜덤)")
randomButton.grid(row=3,column=0,columnspan=2)

submitButton = Button(frame_F1, text="결과확인")
submitButton.grid(row=3,column=2)

window.mainloop()


print('출입자의 체온을 기록합니다.....') # Q1 프로그램에 대한 안내문구

# 측정부위별, 연령대별 정상체온 범위 
temperaturerangedict = {'구강': {'0-2세':(0, 0), '3-10세':(35.5, 37.5), '11-65세':(36.4, 37.6), '65세 이상':(35.8, 36.9)},
                        '귀':{'0-2세':(36.4, 38.0), '3-10세': (36.1, 37.8), '11-65세': (35.9, 37.6), '65세 이상': (35.8, 37.5)},
                        '항문': {'0-2세':(36.6, 38.0), '3-10세': (36.6, 38.0), '11-65세': (37.0, 38.1), '65세 이상': (36.2, 37.3)},
                        '겨드랑이': {'0-2세':(34.7, 37.3), '3-10세': (35.9, 36.7), '11-65세': (35.2, 36.9), '65세 이상': (35.6, 36.3)}
                        }
agegrouplist = ['0-2세', '3-10세', '11-65세', '65세 이상'] # 연령대 목록 

def validateInput(ainputlist): # Q3 입력이 유효한지 검증하는 함수
    if len(ainputlist) != 3: # Q3-c, d 입력값 갯수 검증 
        return '항목의 갯수가 맞지 않습니다. 2개의 , 로 구분된 3개의 항목이 있어야 합니다.' # Q3-e 잘못된 입력이면 메세지 리턴

    if not ainputlist[0].strip() in agegrouplist: # Q3-a 연령대
        return '연령대는 ' + str(agegrouplist) + ' 중 하나여야 합니다.' # Q3-e 잘못된 입력이면 메세지 리턴

    if not ainputlist[1].strip() in temperaturerangedict.keys(): # Q3-a 측정부위 
        return '측정 부위는 ' + str(list(temperaturerangedict.keys())) + ' 중 하나여야 합니다.' # Q3-e 잘못된 입력이면 메세지 리턴

    try:
        bodytemp = float(ainputlist[2]) # Q3-b 체온은 소수점을 포함한 양의 숫자
        if bodytemp < 0:
            return '체온은 양의 숫자 (소수점 이하 숫자 포함 가능) 여야 합니다.' # Q3-e 잘못된 입력이면 메세지 리턴
    except:
        return '체온은 양의 숫자 (소수점 이하 숫자 포함 가능) 여야 합니다.' # Q3-e 잘못된 입력이면 메세지 리턴

    return True # Q3-e 정상 입력이면 True 리턴

while True: # Q5
    # Q2 사용자로부터 연령대, 측정부위, 체온을 받는다.
 
    userinput = input('\n연령대('+str(agegrouplist)+' 중 하나), \n측정부위('+str(list(temperaturerangedict.keys()))+' 중 하나), \n체온을 , 를 이용하여 순서대로 입력하세요: ')
    userinputlist = userinput.split(',')
    message = validateInput(userinputlist) # Q4 3번 함수를 이용, 2번 입력을 검증
    if message==True:
        break
    else: # Q5 잘못된 입력일 경우 3번 함수에서 받은 메세지를 출력하고 제대로 된 입력을 받을 때까지 계속 2~4번 수행
        print(message)

# Q6 연령별과 측정부위, 체온을 받아 그 체온이 정상범위에 있는지, 열이 있는지, 체온 측정이 잘못된 것인지 결과를 return하는 함수
def checkBodytemperature(agegroup, measurespot, bodytemperature):
    #print(agegroup, measurespot, bodytemperature)
    if agegroup == '0-2세' and measurespot == '구강':
        return '측정오류'
    bodytemperaturelow = temperaturerangedict[measurespot][agegroup][0]
    bodytemperaturehigh = temperaturerangedict[measurespot][agegroup][1]
    if bodytemperaturelow <= bodytemperature <= bodytemperaturehigh:
        return '정상체온입니다.'
    elif bodytemperature > bodytemperaturehigh:
        return '열이 있습니다.'
    else:
        return '체온이 너무 낮거나 체온 측정이 잘못되었습니다.'

# Q7 6번 함수를 이용, 체온이 정상인지 확인
checkmessage = checkBodytemperature(userinputlist[0].strip(), userinputlist[1].strip(), float(userinputlist[2]))
from datetime import datetime
timestamp = datetime.now()
# Q7 결과 메세지를 확인한 날짜, 시간과 함께 출력
print(timestamp, checkmessage)
print()

# Q8 랜덤하게 입력값을 만드는 함수를 정의
def randomInput():
    import random
    rgroup = random.choice(agegrouplist)
    rspot = random.choice(list(temperaturerangedict.keys()))
    rerror = random.uniform(0, 1)
    if rerror < 0.3: # Q8-c 랜덤 생성 시 체온에 오류값 (음수)이 30% 확률로 랜덤하게 들어가도록 하라
        rtemperature = random.uniform(-18, 0)
    else:
        rtemperature = random.uniform(34, 39) # 34.7 ~ 38.1
    return [rgroup, rspot, rtemperature]

resultlist = list()
for i in range(10): # Q9 10개의 랜덤 입력값
    result = dict() # Q9 결과를 딕셔너리 형태로 만들어 저장
    rinput = randomInput()
    result['연령별'] = rinput[0]
    result['측정부위'] = rinput[1]
    result['체온'] = rinput[2]
    message = validateInput(rinput)
    if message==True:
        checkmessage = checkBodytemperature(rinput[0], rinput[1], rinput[2])
        result['정상여부'] = checkmessage
    else: # Q9-b 체온에 잘못된 입력값이 있는 경우 6번 함수 실행하지 말고 바로 '정상여부'에 '측정오류'라고 저장
        result['정상여부'] = '측정오류'
    result['측정일시'] = str(datetime.now())
        
    resultlist.append(result) # Q9-c 총 10개의 결과를 하나의 리스트 변수에 저장
    
print('\n체온값 검증 자동 테스트 10회......\n') 
print(resultlist) # Q10 9번 결과를 출력
