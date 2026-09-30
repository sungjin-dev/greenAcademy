students = [{"name": "철수", "score": 85}, {"name": "영희", "score": 55}]

for s in students:
    if s["score"] >= 60:
        result = "합격"

    else :
        result = "재시험"

    print(f"{s['name']}: {result}")


    def calculate_stats(score_list):
        total = sum(score_list)
        avg = total / len(score_list)
        return total, avg

    total, avg = calculate_stats([90,80,100])
    print(f"총점 : {total}, 평균: {avg:.2f}")          # ':' 포맷 지정자(format specifier)

























# total, avg = ...에서 쉼표가 "변수 2개를 만든다"는 뜻이 아니라, 튜플을 분해해서 각각 이름에 연결한다는 뜻이라는 점입니다.

# 1단계: 함수가 튜플 객체 하나를 만든다

# def calculate_stats(scores):
#     total = sum(scores)
#     avg = total / len(scores)
#     return total, avg

# return total, avg는 사실 return (total, avg)와 같다. 쉼표가 튜플을 만드는 것이지, 괄호가 만드는 게 아니에요. 메모리에는 이런 구조가 생깁니다.

# 튜플 객체  ──┬─ [0] ──► int 객체 270
#             └─ [1] ──► float 객체 90.0

# 튜플은 값을 직접 담는 게 아니라, 각 값 객체를 가리키는 참조(포인터)를 담고 있다.


