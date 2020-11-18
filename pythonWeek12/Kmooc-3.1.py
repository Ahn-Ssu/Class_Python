#연습하기 2번
def findTeacher(sub):
    subjects = {
        '김경미':['수학','과학'],
        '최영희':['영어','수학'],
        '강동원':'영어',
        '정필수':['사회','역사'],
        '박희수':'국어',
        '이승철':['수학','과학'],
    }

    teacher = []
    for key in subjects.keys():
        if sub in subjects[key]:
            teacher.append(key)

    return teacher

sub = input("과목을 입력하시오: ")
print(findTeacher(sub))

            