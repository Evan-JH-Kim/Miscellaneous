sample = 0 # 표본 개수
threshold = 10 # 이 값 이상의 비율만 표시
mbti_sample = {} # 표본, {'닉네임': 'MBTI'}
mbti_stat = {} # 통계, {'MBTI': 비율}

with open('mbti_sample.txt', 'rt', encoding='UTF8') as f:
    for line in f.readlines():
        sample += 1
        mbti_sample[line.split()[0]] = line.split()[1]

for mbti in mbti_sample.values():
    mbti_types = [""]
    for alphabets in mbti:
        for i in range(len(mbti_types)):
            mbti_types.append(mbti_types[i] + alphabets)
    mbti_types.remove("")
    for mbti_type in mbti_types:
        mbti_stat[mbti_type] = mbti_stat[mbti_type] + 1 if mbti_type in mbti_stat.keys() else 1
            
for k in mbti_stat.keys():
    mbti_stat[k] = round(mbti_stat[k]*100/sample, 2)

print(str(sample)+"개의 표본으로부터 확고히 검증된 결과입니다!")
for item in sorted(mbti_stat.items(), key=lambda k : k[1], reverse=True):
    if item[1] >= threshold: 
        print(item[0] + ": " + str(item[1]) + "%") 
