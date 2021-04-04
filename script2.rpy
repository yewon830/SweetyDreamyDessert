# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
 



# The game starts here.

##플레이어케릭터
define player_name = "플레이어이름"
define na = Character("player_name",dynamic = True, color="#e5aaae")

define f = Character("친구")
define m = Character("엄마")

label start:
    "당신의 이름을 입력해주세요."
    $player_name = renpy.input("내 이름은")##화면에 내 이름은 나오고 다음칸에 입력받는 칸이 나온다.
    na "내 이름은 [player_name]"##p는 위에 선언한 케릭터고, 대화창에 변수값을 나오게 할려면 [변수명]으로 사용한다.
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    na "이제 이 학교를 떠날 때가 왔다."
    scene bg room




    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

   

    f "야, 너 다음주에 전학간다며? 부럽다.. 나도 너 따라 가고 싶다."
    na "이 학교에 붙어 있을 이유가 하나도 없다."
    f "그래서, 어디 학교로 가는데?"
    na "그건...들어도 모를텐데?"
    f "아 됐고, 빨리 말해봐."
    na "....."
    na "국휘고등학교."

    #여기서 배경 바뀌고 국휘고 사진 나옴
    f "엥? 진짜 처음 들어보네?"
    na "내가 말해도 모를거라 했잖아..."

    #여기서 배경 집으로 바뀌고 회색
    "과거, 약 한 달 전"
    na "엄마, 나 전학가고 싶어요."
    m "무슨 소리야. 무슨 문제라도 있니?"
    na "여기 학교 분위기 너무 안좋아요. 애들 막 야자 째고 그런다니까요."
    m "어머, 정말?"
    na "막 대놓고 담배냄새 풍기고... 진짜 여기서 공부 못하겠어요. 그래서 제..."
    m "세상에. 엄마가 분위기 좋은 학교를 알아봐줄게."
    na "네? 아뇨 제가 알..."
    m "우리 딸이 공부를 못한다는데 엄마가 알아봐줘야지!!"

    "현재"
    na "미남없는 학교에 왜다니냐."

    "그렇다. 나는 학교에 잘생긴 남자가 단 한 명도 없기 때문에 엄마에게 거짓말을 하고 학교를 옮기게 된 것이다."
    na "잘생긴게 밥 먹여준다."
    # This ends the game.

    return
