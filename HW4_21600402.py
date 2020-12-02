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

# Q6 연령별과 측정부위, 체온을 받아 그 체온이 정상범위에 있는지, 열이 있는지, 체온 측정이 잘못된 것인지 결과를 return하는 함수
def checkBodytemperature(agegroup, measurespot, bodytemperature):
    #print(agegroup, measurespot, bodytemperature)
    if agegroup == '0-2세' and measurespot == '구강':
        # 해당 popup이 없으면 0-2세와 구강을 매칭한 경우 정상 판정이나 기록은 되지 않으며
        # 무반응으로 보이기 때문에 추가 작성하였습니다. 
        messagebox.showwarning("측정오류", "0-2세의 구강 측정은 불가능합니다.")
        return '측정오류 : 0-2세 구강 판정불가'
    bodytemperaturelow = temperaturerangedict[measurespot][agegroup][0]
    bodytemperaturehigh = temperaturerangedict[measurespot][agegroup][1]
    if bodytemperaturelow <= bodytemperature <= bodytemperaturehigh:
        # 정상체온인 경우 showinfo 함수를 사용하여 결과를 출력 
        messagebox.showinfo("측정 결과", "정상체온입니다.")
        return '정상체온입니다.'
    elif bodytemperature > bodytemperaturehigh:
        # 측정결과 열이 있는 경우 showerror 함수를 이용하여 출력 
        messagebox.showerror("측정 결과", "열이 있습니다.")
        return '열이 있습니다.'
    else:
        # LO 의 경우 showwarning을 통하여 popup info 
        messagebox.showwarning("측정 결과", "체온이 너무 낮거나 체온 측정이 잘못되었습니다.")
        return '체온이 너무 낮거나 체온 측정이 잘못되었습니다.'

"""
21600402 전산전자공학부 안수현 Hw4

해당 주석 위의 코드들은 교수님이 제공해주신 hw3 의 코드 중 몇 가지의 함수를 사용하였음을 밝힙니다. 
checkBodytemperature 함수 외의 변화를 준 내용은 없습니다.
"""

from tkinter import *
from tkinter import messagebox


window = Tk()
window.title("체온 측정 프로그램") # 조건 타이틀에 프로그램 이름을 작성할 것 

# 프로그램 window 크기를 조절하고 위치시키는 함수입니다. 
def centerWindow():
    # 해당 두 변수로 프로그램 윈도우창의 크기를 설정합ㄴ디ㅏ. 
    w = 600
    h = 350

    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    # x,y 값을 스크린의 절반 위치로 잡아 대략적으로 화면의 중간에 위치하여 윈도우창이 나타납니다. 
    x = (sw - 400)/2
    y = (sh- 400)/2
    # 해당 작업을 통해, 가로 세로와 화면에서 나타날 위치를 지정해줍니다. 
    window.geometry('%dx%d+%d+%d'%(w,h,x,y))

# 프로그램 window 배치 및 크기 설정함수
centerWindow()

# window에서 체온측정에 관한 요소들을 배치시킬 '프레임' (조건 : 프레임 사용)
# 또한 프레임에 패딩을 주어 윈도우 창에 달라 붙지 않게 조절 (조건 : 패딩으로 컴포넌트 배치)
frame_F1 = Frame(window, relief="solid",padx=10,pady=10)
frame_F1.grid(row=0, column=0)


#왼쪽, 최상단에 놓일 연령대 선택 라벨 
ageLabel = Label(frame_F1, text="연령대 선택 :",width=15)
ageLabel.grid(row=0,column=0)
#왼쪽,위에서 두번째에 놓일 측정부위 선택 라벨 
areaLabel = Label(frame_F1, text="측정 부위 선택 :",width=15)
areaLabel.grid(row=1,column=0)
#왼쪽, 위에서 세번째에 놓일 체온 입력 라벨 
tempLabel = Label(frame_F1, text="체온 입력 :",width=15)
tempLabel.grid(row=2,column=0)



#age radiobutton을 한 그룹으로 묶기 위한 StringVar() instance agegetter 
#해당 변수를 radiobutton variable 필드의 값으로 주어 한 그룹으로 묶는다.
agegetter = StringVar()

# 각각 연령대 radibutton이다. 각 text와 변수는 동일하며, grid에서 통일성을 주기 위하여 width를 통일하였다. 
age0radio = Radiobutton(frame_F1, text="0-2세", value="0-2세", variable=agegetter, width=10)
age1radio = Radiobutton(frame_F1, text="3-10세", value="3-10세", variable=agegetter, width=10)
age2radio = Radiobutton(frame_F1, text="11-65세", value="11-65세", variable=agegetter, width=10)
age3radio = Radiobutton(frame_F1, text="65세 이상", value="65세 이상", variable=agegetter, width=10)
# 또한 RadioButton().grid() 로 바로 frame에 올리지 않고 instance를 생성하였다.
# 이는 나중에 clearAll 함수(정상입력시 모든 선택 해제), randomSampling을 위하여 instance를 만든 후, 해당 객체를 grid로 올렸다. 
age0radio.grid(row=0,column=1)
age1radio.grid(row=0,column=2)
age2radio.grid(row=0,column=3)
age3radio.grid(row=0,column=4) 


#agegetter와 동일한 수행을 하는 areagetter이다.
#측정부위 radiobutton를 한 그룹으로 두어, 택 1의 기능을 구현
areagetter = StringVar()
area1Radio = Radiobutton(frame_F1, text="구강 ", value="구강", variable=areagetter, width=10)
area2Radio = Radiobutton(frame_F1, text="귀", value="귀", variable=areagetter, width=10)
area3Radio = Radiobutton(frame_F1, text="항문", value="항문", variable=areagetter, width=10)
area4Radio = Radiobutton(frame_F1, text="겨드랑이", value="겨드랑이", variable=areagetter, width=10)
area1Radio.grid(row=1,column=1)
area2Radio.grid(row=1,column=2)
area3Radio.grid(row=1,column=3)
area4Radio.grid(row=1,column=4)

# tempGetter는 Radio 그룹에는 해당되지는 않지만 이후 textvariable, 내부 텍스트 값을 변환 시킬때 사용된다.
# 1) randomSampling, 2) 정상입력의 value 비우기
tempGetter = StringVar()
# 입력 컨포넌트들의 세로위치를 맞추기 위한 width 값 조절 
tempTextBox = Entry(frame_F1,textvariable=tempGetter,width=17)
tempTextBox.grid(row=2,column=1,columnspan=2)

# 해당함수는 랜덤 생성 버튼의 command 를 수행하는 함수이다.
# hw3 코드에서 구현된 randomInput을 통해 샘플 값을 랜덤으로 생성하고, 생성된 값에 따라 
# 연령대 라디오 선택, 측정 환부 라디오 선택, 체온 값 입력을 수행한다. 
def randomSet():
    # randomInput 함수를 사용하여 randomSample을 하나 생성한다. 
    # 이때 랜덤 값은 연령대 중 하나, 측정부의 중 하나, 오류가 섞이는 온도가 생성된다. 
    randomSample = randomInput()

    # 생성된 연령대에 맞게 라디오 버튼의 전환을 수행한다. 
    # randomSmaple[0]는 연령대에 관한 정보를 가지고 있다. 
    if(randomSample[0]=="0-2세"):
        age0radio.invoke() # age0radio는 value가 0-2세이다. 
    elif(randomSample[0]=="3-10세"):
        age1radio.invoke() # age1radio는 value가 3-10세이다.
    elif(randomSample[0]=="11-65세"):
        age2radio.invoke() # age2radio는 value가 11-65세이다.
    elif(randomSample[0]=="65세 이상"):
        age3radio.invoke() # 65세이상이당 


    # 생성된 측정부위에 맞게 해당 라디오 그룹의 선택을 수행함
    # randomSample[1]은 측정부위에 관한 정보를 가지고 있음 
    if(randomSample[1]=="구강"):
        area1Radio.invoke() # 1radio는 value가 구강이다.
    elif(randomSample[1]=="귀"):
        area2Radio.invoke() # 2radio는 value가 귀이다.
    elif(randomSample[1]=="항문"):
        area3Radio.invoke() # 3radio는 value가 ㅎㅁ이다.
    elif(randomSample[1]=="겨드랑이"):
        area4Radio.invoke() # 4radio는 value가 겨드랑이다.

    # 이전에 StringVar() instance로 생성한 tempGetter의 값을 랜덤 생성한 값으로 바꾸어 
    # 온도 설정을 수행한다. 
    tempGetter.set(round(randomSample[2],2))

# 입력들이 모두 정상인 경우, validation을 수행한 뒤 다음 입력을 받기 위하여 
# 선택된 라디오와, 모든 입력들을 지우는 함수이다. 
def clearAll():

    # 연령대 라디오를 모두 선택되지 않은 상태로 바꾼다.
    age0radio.deselect()
    age1radio.deselect()
    age2radio.deselect()
    age3radio.deselect()
    
    # 측정부위 라디오버튼을 모두 선택되지 않은 상태로 전환한다.
    area1Radio.deselect()
    area2Radio.deselect()
    area3Radio.deselect()
    area4Radio.deselect()

    # tempGetter 의 textvalue를 "" (null) 값으로 전환한다. 
    tempGetter.set("")


#결과확인 버튼을 눌렀을때 연결된 command를 수행하는 함수이다. 
# 각각의 radio와 text에서 값을 추출하여 list를 만든뒤, hw3에서 구현된 validate check를 수행한다. 
# 해당 수행이 정상적으로 이루어지지 않은 경우엔 어떤 입력에러가 있었는지 popup을 수행한다. 
# 정상적으로 이루어진 경우 온도를 체크하고, 정상체온인 경우에는 해당 결과를 타임스탬프와 함께 기록을 수행한다. 
def checkOne():
    # 각각의 var_instance에서 Radio와 Text에서 연령대, 측정부위, 체온을 얻어내 list로 만든다. 
    userinput = [agegetter.get(),areagetter.get(),tempGetter.get()]
    
    # 만들어진 list를 validateInput에 제공하여 정상 입력이 이루어졌는지 체크한다. 
    message = validateInput(userinput)

    # 리턴된 메세지가 True 인 경우 입력값이 모두 올바르게 입력된 상황이다. 
    # 해당 상황의 경우 checkBodytemperature 함수를 수행하여 해당 조건이 고열인지, 정상체온인지, LO인지 체크한다. 
    if message==True:
        resultmessage = checkBodytemperature(userinput[0],userinput[1],float(userinput[2]))
        # 측정결과 값을 기록하기 위해서 resultmessage를 리스트에 추가한다. 
        userinput.append(resultmessage) 
        # 측정결과를 기록하기 위하여 record 함수에 결과 값이 추가된 userinput을 제공한다. 
        record(userinput)
        # 입력이 정상인 경우, 다음 입력을 받기 위하여 clearAll 함수를 통해 모든 선택 값들을 초기화 한다. 
        clearAll()
    # 입력값이 올바르게 입력되지 않아 에러메세지와 함께 리턴된 경우
    # 해당 메세지를 popup으로 제공하여 어떤 입력 오류인지 안내한다. 
    else :
        messagebox.showinfo("입력 오류", message)    


# 입력을 자동으로 랜덤으로 생성하는 버튼이다. 해당 버튼을 누르면 randomSet 함수를 호출하여 동작을 수행한다. 
randomButton = Button(frame_F1, text="자동 입력(랜덤)", command=randomSet)
randomButton.grid(row=3,column=0,columnspan=3,pady=5)

# 선택(생성)된 결과를 확인하는 버튼이다. 해당 버튼을 클릭하면 checkOne 함수를 호출하여 입력값이 정상인지 여부를 수행한다. 
submitButton = Button(frame_F1, text="결과확인", command=checkOne)
submitButton.grid(row=3,column=3,pady=5)



from tkinter.scrolledtext import *
# 측정 결과를 저장하기위한 2번 프레임 
# 해당 프레임은 window에서 두번째 칸에 위치한다. 
frame_F2 = Frame(window, relief="solid",padx=10,pady=5)
frame_F2.grid(row=1, column=0)

# ScrolledText가 어떤 역할인지 나타내기 위한 라벨
# 해당 라벨은 recordText 위에 위치하여 유저에게 안내를 수행한다. 
saveLabel = Label(frame_F2, text="측정기록")
saveLabel.grid(row=0,column=0)

# 측정결과가 기록되는 ScrolledText
recordText = ScrolledText(frame_F2,width=70,height = 10)
recordText.grid(row=1,column=0,columnspan=4)

# 결과가 저장될때 총 recordText에 임시로 얼마나 저장이 되어있는지 기록하기 위한 변수 
saveCount = 0 

# 정상입력인 경우 recordText에 기록하기 위함 
def record(sourceList):
    # saveCount를 공유하기 위한 global 선언
    global saveCount

    # 측정시간을 같이 기록하기 위한 datetime import 
    from datetime import datetime
    # 저장 순서에 맞게 측정시간을 맨 앞으로 배치한다. 
    sourceList.insert(0,str(datetime.now()))
    # str으로 기록을 하기 위하여 join(list)를 수행하며, 매 측정 결과를 가독성 있게 구분하기 위하여 줄바꿈을 수행한다. 
    savedStr = ', '.join(sourceList) + "\n"
    # 마지막으로 기록된 위치에 기록을 추가한다. 
    recordText.insert(END, savedStr)
    # 추가된 기록을 세기 위하여 saveCount를 1 증가 시킨다. 
    saveCount+= 1

# saveButton을 기록된 결과들을 저장하는 함수이다. 
def save():
    # saveCount로 현재 몇건이 저장되어 있는지 알기위하여 static으로 변수를 받아온다. 
    global saveCount
    # 아무것도 기록되지 않은 상태에서 저장하기 버튼을 누른 경우 저장 동작을 리젝하는 if 문이다.
    if saveCount<1:
        # 아무것도 저장되지 않은 경우 에러메세지와 함께 저장된 기록이 없다는 안내를 하고 함수를 종료한다. 
        messagebox.showerror("저장실패", "저장된 기록이 없습니다")
        return
    
    # 파일을 저장하는 경로와 이름을 직접 설정하기 위한 filedialog, asksaveasfile 이당 
    from tkinter.filedialog import asksaveasfile
    # 결과 값을 str으로 저장하므로 쓰기모드와, 텍스트 파일로 저장을 한다. 
    f = asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # 저장을 수행하지 않고 취소를 누른 경우 아무것도 수행하지 않고 함수를 종료한다. 
        return

    # f instance에서 name이 저장이 된 Path를 가지고 있으므로 그를 알려주기위하여 str으로 받아온다. 
    path = f.name
    # get 함수를 통해 여태까지 쓰인 기록을 str으로 받아온다. 
    text2save = str(recordText.get(1.0, END)) 
    # 설정된 Path와 이름으로 스트링을 텍스트 파일로 기록을 수행한다. 
    f.write(text2save)
    f.close() # f.close()

    # 파일을 정상적으로 저장한 후 popup을 통해 저장이 성공했음 알린다.
    # 내용으로는 어떤 Path에 저장이 되었는지 알려주며, 몇건이 저장이 되었는지 알려준다. 
    messagebox.showinfo("저장성공", path+"에"+str(saveCount)+"건 저장 되었습니다.")
    # 저장이 된 기록들은 scroll text에서 제거를 수행한다. 
    recordText.delete(1.0,END)
    # 동시에, 임시로 남아있는 기록이 없으므로 saveCount도 0으로 만든다. 
    saveCount=0
    
# 기록된 결과를 저장하기 위한 saveButton. 
saveButton = Button(frame_F2, text="저장하기", command=save)
saveButton.grid(row=2,column=0,columnspan=4,pady=5)

# window창을 계속 유지하는 코드 
window.mainloop()
