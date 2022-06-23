# 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다.
# 다음과 같이 a, b 변수를 선언한 후 a의 두 번째 요솟값을 변경하면 b 값은 어떻게 될까?
# 그리고 이런 결과가 오는 이유에 대해 설명해 보자.

# >>> a = b = [1, 2, 3]
# >>> a[1] = 4
# >>> print(b)

# A) b 값은 [1,4,3]이 된다. 그 이유는 리스트는 주소 참조이며 a와 b가 가리키는 주소가 동일하기 때문이다.