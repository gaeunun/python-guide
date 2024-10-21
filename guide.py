import streamlit as st  

# 프로그래밍 개념을 정의하는 딕셔너리
python_guide = {     
    "변수와 자료형": {         
        "설명": (             
            "변수는 데이터를 저장하기 위해 사용되며, 자료형은 저장할 수 있는 데이터의 "             
            "형태를 정의합니다.\n\n"             
            "- int: 정수\n"             
            "- float: 실수\n"             
            "- str: 문자열\n"             
            "- bool: 불린(True 또는 False)"         
        ),         
        "예제": "x = 10\nname = 'Alice'"     
    },     
    "조건문": {         
        "설명": (             
            "조건문은 특정 조건이 참인지 거짓인지에 따라 실행할 코드를 정합니다.\n\n"             
            "if 문을 사용하여 조건에 따른 분기를 구현할 수 있습니다."         
        ),         
        "예제": (             
            "x = 10\n"             
            "if x > 0:\n"             
            "    print('양수입니다')\n"             
            "elif x < 0:\n"             
            "    print('음수입니다')\n"             
            "else:\n"             
            "    print('0입니다')"         
        )     
    },     
    "반복문": {         
        "설명": (             
            "반복문은 코드 블록을 여러 번 실행할 때 사용됩니다.\n\n"             
            "for문과 while문이 있습니다."         
        ),         
        "예제": (             
            "for i in range(5):\n"             
            "    print(i)"         
        )     
    },     
    "리스트": {         
        "설명": (             
            "리스트는 여러 값을 저장할 수 있는 데이터 구조입니다.\n\n"             
            "리스트는 대괄호 []를 사용하여 만들며, 인덱스는 0부터 시작합니다."         
        ),         
        "예제": (             
            "fruits = ['사과', '바나나', '체리']\n"             
            "print(fruits[0])  # 사과"         
        )     
    },     
    "함수": {         
        "설명": (             
            "함수는 특정 작업을 수행하는 코드 블록입니다.\n\n"             
            "def 키워드를 사용하여 정의합니다."         
        ),         
        "예제": (             
            "def greet(name):\n"             
            "    return f'안녕하세요, {name}'\n\n"             
            "print(greet('파이썬'))"         
        )     
    },
    "정의": {         
        "설명": (             
            "정의는 코드에서 특정 이름으로 함수를 선언하고, 그 함수가 어떤 작업을 수행할지를 "
            "정의하는 것입니다. 이러한 함수는 나중에 호출하여 사용할 수 있습니다."         
        ),         
        "예제": (             
            "def add(a, b):\n"             
            "    return a + b\n\n"             
            "result = add(5, 3)\n"             
            "print(result)  # 8"         
        )     
    },
    "튜플": {         
        "설명": (             
            "튜플은 여러 값을 저장할 수 있는 데이터 구조로, 변경이 불가능합니다.\n\n"             
            "튜플은 괄호 ()를 사용하여 만들며, 인덱스는 0부터 시작합니다."         
        ),         
        "예제": (             
            "coordinates = (10, 20)\n"             
            "print(coordinates[0])  # 10"         
        )     
    },
    "딕셔너리": {         
        "설명": (             
            "딕셔너리는 키-값 쌍으로 데이터를 저장하는 데이터 구조입니다.\n\n"             
            "딕셔너리는 중괄호 {}를 사용하여 만들며, 키를 통해 값을 조회할 수 있습니다."         
        ),         
        "예제": (             
            "person = {'name': 'Alice', 'age': 25}\n"             
            "print(person['name'])  # Alice"         
        )     
    },
    "집합": {         
        "설명": (             
            "집합은 중복되지 않는 값을 저장하는 데이터 구조입니다.\n\n"             
            "집합은 중괄호 {}를 사용하여 만들며, 수학적 집합 연산을 지원합니다."         
        ),         
        "예제": (             
            "unique_numbers = {1, 2, 2, 3}\n"             
            "print(unique_numbers)  # {1, 2, 3}"         
        )     
    },
    "예외 처리": {         
        "설명": (             
            "예외 처리는 프로그램 실행 중 발생할 수 있는 오류를 처리하는 방법을 말하며,\n"             
            "try, except 문을 사용하여 구현합니다."         
        ),         
        "예제": (             
            "try:\n"             
            "    result = 10 / 0\n"             
            "except ZeroDivisionError:\n"             
            "    print('0으로 나눌 수 없습니다.')"         
        )     
    },
    "모듈": {         
        "설명": (             
            "모듈은 여러 함수나 클래스를 담고 있는 Python 파일입니다.\n"             
            "다른 Python 파일에서 불러와 사용합니다."         
        ),         
        "예제": (             
            "import math\n"             
            "print(math.sqrt(16))  # 4.0"         
        )     
    }
}  

# Streamlit 앱의 제목 
st.title("초보자를 위한 Python 가이드")  

# 사이드바 메뉴 생성 
concept = st.sidebar.selectbox(     
    "관심 있는 Python 개념을 선택하세요:",     
    list(python_guide.keys()) 
)  

# 선택한 개념의 설명 및 예제 출력 
st.header(concept) 
st.write(python_guide[concept]["설명"]) 
st.subheader("예제 코드:") 
st.code(python_guide[concept]["예제"], language='python')