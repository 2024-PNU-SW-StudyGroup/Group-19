# 챕터 2 마무리
API : 프로그램 간 데이터를 전달하기 위한 규칙
HTTP : 웹에서 데이터를 주고받기 위한 프로토콜
JSON : API에서 자주 사용되는 데이터 전달 포맷
XML : 전통적으로 사용되는 데이터 포맷

## 주요 메서드
json.dumps() - 파이썬 객체를 JSON 문자열로 변환

json.loads() - JSON문자열을 파이썬 문자열로 변환

pandas.read_json() - JSON 문자열을 판다스 시리즈나 df로 변환

xml.etree.ElementTree.fromstring() - XML문자열 분석 -> xml.etree.ElementTree 객체 반환

xml.etree.ElementTree.Element.findtext() - 지정한 태그 이름과 맞는 '첫번째' 자식 반환
xml.etree.ElementTree.Element.findall() - 지정한 태그 이름과 맞는 모든 자식 반환

requests.get() - HTTP GET 방식으로 URL 호출 -> requests.Response 객체 반환

requests.Response.json() - 응답으로 온 JSON문자열을 파이썬 객체로 변환하여 반환

# 챕터 3 - 불필요한 데이터 삭제하기
데이터 정제, 데이터 랭글링, 데이터 먼징 과정을 통해 불필요한 데이터를 삭제할 수 있다.
보통 이는 Pandas dataFrame을 활용하여 수행됨.

loc 메서드+슬라이싱 을 통해 원하는 항목을 포함한 새 df를 생성할 수 있음.

drop() 메서드  - pd.df의 행이나 열을 삭제할 수 있는 메서드. 삭제하려는 열이나 행을 선택하고 axis=1 세팅을 활용하여 열을 삭제할 수 있음.
특히 inplace 매개변수를 True로 설정하면 현재 선택한 df에 수정된 내용을 덮어쓰기 할 수 있다.

### <열 삭제>

dropna() 메서드 - 판다스는 비어있는 값을 NaN으로 표시한다 -> dropna는 axis변수를 1로 설정함으로써 df에서 NaN이 포함된 열을 삭제한다.
해당 메서드에 how 매개변수를 'all'로 지정하면 '모든 값이 NaN인 열' 만 삭제한다.

### <행 삭제>

열 삭제때와 마찬가지로 똑같이 drop() 메서드 사용 가능 -> ns_book.drop([0,1]) 과 같이 인덱스 슬라이스를 설정함으로써 지정한 행을 삭제할 수 있다.

### 중복된 행 찾기

duplicated() 메서드 - 중복된 행 중에서 처음 행을 제외한 나머지 행은 True로 그 외는 False 반환. -> True가 떴다? = 중복. (df내의 모든 열을 기준으로 찾음)

특정 value들을 기준으로 중복된 행이 있는지 찾으려면 -> subset 매개변수 설정 -> ex) book.duplicated(subset=['도서명', '저자'])

duplicated()메서드의 keep 매개변수를 False로 지정하면 중복된 모든 행을 True로 표시함.

### 그룹별로 모으기
groupby() 메서드 - 해당 메서드의 by 매개변수에는 행을 합칠때 기준이 되는 열을 지정함. 해당 메서드는 기본적으로 지정된 열에 NaN이 있으면 해당 열을 삭제함 
그러나 NaN을 삭제하면 '대출권수' 같은 value에 영햐을 끼치므로 dropna 매개변수를 'False'로 지정함으로써 막을 수 있음.

예를 들어 '대출권수' 같은 영역은 일반적으로 합이나 평균을 요구함 -> sum()사용

### 원본 데이터 업데이트
duplicated()메서드를 활용하여 중복된 행을 True로 표시한 불리언 배열을 반전 -> ~ 연산자 활용 -> copy메서드 활용하여 복사

<원본 데이터프레임 인덱스 설정> - 
set_index()메서드 활용 -> inplace 매개변수를 True로 지정하여 새로운 df를 반환하지 않고 기존 df를 수정할 수 있음.

<업데이트하기 : update() 메서드> - 다른 df를 활용하여 원본 df를 업데이트 할때 사용함. ex) book3.update(loan_count)

## 해당 장 최종 복습을 위해서는 page 179의 일괄 처리 함수를 설정하는 과정을 복습하자.

