#튜플은 변경 불가능한 데이터 셋 
#변경

#튜플 선언시 주의할 점 
emptyTuple = () 
testTuple = (1,2,3)
oneSizeTuple = (1,) # 튜플의 길이가 하나인 경우, 반드시 콤마로 구분을 해야함 

#튜플 검색 메소드 
oneSizeTuple.count(1) # 안쪽에 전달한 인자가 몇개 있는가?
testTuple.index(2) # 2의 좌표좀 
testTuple.index(2,1) # 2를 검색하는데 위치는 1번 부터 
