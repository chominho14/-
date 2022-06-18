input_num=int(input())

line=0 # 라인 수
max_num=0 # 최댓 값

# 입력 값에 따른 라인 수와 최댓 값 구하기
while input_num>max_num:
    line+=1
    max_num+=line

# 입력 값 라인의 최댓 값에서 입력 값을 빼서 차이를 변수에 저장
gap=max_num-input_num
if line%2==0: # 짝수 일때
    top=line-gap
    bot=gap+1
else: # 홀수 일때
    top=gap+1
    bot=line-gap
print('{0}/{1}'.format(top,bot))