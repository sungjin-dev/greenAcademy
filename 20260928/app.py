from member import member_config 
import session


class MemberService:
    def __init__(self):
        self.members = {}
        self.init_database()

    def sign_up(self):

        uid = input('input your new member ID')

        session.signinedMemberId ==


userInputNum = str(input("원하는 숫자를 입력하시오"))

if session.getSigninedMemberId() == '':
    return  


if userInputNum == member_config.SING_UP :
    self.sign_up()


제어문 및 함수('def')정의

조건문 반복문




# print("박성진")

# myName = "박성진"

# name = "성적 관리 대시보드" #str

# user_count = 25  #int

# print(f"{myName}가(이) 만든 {name}는 {user_count}째이다")


# scores = [90, 80, 100]

# scores.append(95)

# print(scores)


# user = "admin"

# if user == "admin":
#     print("관리자님 안녕하세요")

# else :
#     print("일반 사용자입니다")



# tasks = ["대시보드 UI 기획", "데이터베이스 연동", "사용자 테스트 진행"]

# print("오늘 할 일 목록")

# for task in tasks: 
#     print(task)


# # 중복이 포함된 리스트
# original_list = [1, 2, 2, 3, 4, 4, 5]

# # 1. set으로 바꿔서 중복 제거
# unique_set = set(original_list)

# # 2. 다시 리스트로 변환
# unique_list = list(unique_set)

# print(unique_list)  # 출력 결과: [1, 2, 3, 4, 5] (순서는 무작위로 섞일 수 있음)
# 보통은 이 과정을 한 줄로 줄여서 list(set(original_list)) 형태

# set은 "값(Value)은 없고 '키(Key)'만 존재하는 딕셔너리

# dict.fromkeys() -> 원래 순서를 유지하면서 중복만 제거