# 풀이 2

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
t = t2 - t1 if t2 > t1 else t2-t1+24*60*60
h = t//60//60
m = t//60 % 60
s = t%60
print("%02d:%02d:%02d" % (h, m, s))# 형식을 지정함으로 코드를 짧게 적을 수 있다

# 풀이 1
# 정답은 맞지만 너무 길고 오래걸리는 코드이다.

# now_h, now_m, now_s = list(map(int, input().split(':')))
# throw_h, throw_m, throw_s = list(map(int, input().split(":")))

# now_all = now_h*3600 + now_m*60 + now_s
# throw_all = throw_h*3600 + throw_m*60 + throw_s

# day = 24*60*60

# def s_time(s):
#     h = s//3600
#     m = (s%3600)//60
#     s = (s%3600)%60
    
#     if h < 10:
#         hh="0"+str(h)
#     else:
#         hh = str(h)
#     if m < 10:
#         mm = "0"+str(m)
#     else:
#         mm = str(m)
#     if s < 10:
#         ss = "0"+str(s)  
#     else:
#         ss = str(s)    
#     return [hh,mm,ss]

# if now_all >= throw_all:
#     wait_all = day - now_all + throw_all
#     time = s_time(wait_all)
#     print(f'{time[0]}:{time[1]}:{time[2]}')  
# else:
#     wait_all = throw_all - now_all
#     time = s_time(wait_all)
#     print(f'{time[0]}:{time[1]}:{time[2]}')