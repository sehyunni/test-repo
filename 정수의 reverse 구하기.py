Touched by user2
n=int(input()) #정수 입력받기(int말고 문자열로 취급)
m=n.rstrip("0") #문자열 오른쪽에 있는 0 제거
	
print(m[-1::-1]) #문자열의 가장 끝부터 0번째 인덱스까지 역순으로 출력
