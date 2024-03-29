### 📌 Summary

2022.03~ 2022.11

#### 팀프로젝트, NI:KEY (신조어 기반 스마트 키보드) - 백엔드 부분 

하나의 앱 안에 맞춤법 검사기, 신조어 사전, 클립보드 기능을 통합했기 때문에 개별적으로 앱들을 설치하지 않아도 되는 스마트 키보드 앱입니다.    
업무, 채팅 시 화면 이동이나 앱 전환으로 인한 번거로움 최소화하고 이해하지 못한 신조어를 편하게 검색할 수 있는 공간 형성했습니다.

- 주요 기능

신조어 사전:
사용자에게 신뢰도 있는 정보를 제공하기 위해 수많은 단어의 뜻, 예문, 연관어들을 직접 선별하여 신조어 사전 구축
방송에서 사용되거나 커뮤니티 상에서 신조어를 제일 많이 접한다는 자료를 참고하여 직접 신조어 데이터(단어 명, 단어 뜻, 예문, 연관어)를 수집 혹은 제작하여 가공했기에 사용자들에게 실용성 보장
신조어에 대한 구체적인 예시들을 제공하면 남녀노소 누구나 쉽고 정확하게 단어를 사용할 수 있음. 이와 같은 이유로 사용자들이 신조어 사전을 믿고 사용

맞춤법 검사:
기존 스마트 키보드들은 맞춤법 검사 시 신조어 인식불가
하지만 본 프로젝트에서는 신조어도 문제없이 인식하여 맞춤법 검사 진행
맞춤법이 틀린 부분은 “맞춤법” 빨간색으로, 띄어쓰기가 필요한 부분은 “띄어쓰기” 파란색,
신조어로 인식한 단어는 “신조어의심” 보라색으로 표현 
텍스트 자료 수정, 메신저 소통 등 다양한 상황에서 적절한 맞춤법 결과를 보여줌으로써 원활한
의사소통이 가능하며,  맞춤법 검사를 통해 사회적 체면은 물론 언어 수준 향상까지 가능 

![nikey](https://user-images.githubusercontent.com/71927533/199383073-219f9df9-e5e3-4635-acdc-4288b170b2dd.PNG)

- 차별성

![차별성](https://user-images.githubusercontent.com/71927533/199383979-130f45ff-822e-4b19-8325-f065c4c47c25.PNG)


- 팀원 소개 및 역할

PM, SA, Backend, 기획 총괄

![image](https://user-images.githubusercontent.com/71927533/199383538-82bfaf0f-8939-499b-a58b-970801f469b7.png)


### 📊 Background

- 추진 배경

2020년 국민의 언어 의식 조사 결과
유행어나 신조어의 의미를 몰라서 곤란함을 겪은 경험 43.1%[1]
신문, 텔레비전에서 나오는 말의 의미를 몰라 곤란했던 경험 36.3%[1]
맞춤법을 신경 쓰고 보고서나 이력서를 작성하는 사람 67%[2]
성인 남녀의 60%가 한글 표기에 어려움을 느끼고 있다고 응답하고, 한글 표기 중에서도 맞춤법과 띄어쓰기가 가장 어렵다는 의견이 많았음[3]


- 타겟 고객

![image](https://user-images.githubusercontent.com/71927533/199383804-caec3ecd-86ba-41b0-b74e-ea8f7e6c9f1b.png)


### 👍 Expected Results

- 기대효과 및 활용 분야

앱을 통해 불필요한 웹 브라우저 이동 시간을 절약하고 알맞은 단어 사용을 도와줌으로써 자신의 의사를 정확하게 표현하는 의사소통이 가능함

신조어가 끊임없이 생겨나므로 그 데이터들을 추가하여 제공하면 사용자들에게 트렌드를 읽을 수 있도록 도울 수 있고 기존의 사용자들도 앱을 오랫동안 사용할 수 있게 유도
신규 사용자 또한 같은 이유로 앱을 설치하도록 유도

네이버에서도 오픈 사전이라는 명목 하에 사전이 있지만 표준 사전이 없기 때문에 
본 프로젝트의 신조어 사전이 표준 신조어 사전이 될 수 있음

표준 신조어 사전이 제작된다면 본 프로젝트에서 직접 수집한 신조어를 특허로 등록할 수 있음 또한 이 앱을 더욱 발전시켜 신조어 커뮤니티를 만들면 사용자가 직접 신조어를 제작할 수 있도록 참여를 유도하여 사용 유저들을 유치할 수 있음



### 🛠️ Technology Stack

- Mobile App: Kotlin(Android)
- Web: Python, JavaScript
- Server: AWS EC2
- DB: AWS RDS(MariaDB)



### Design
- Figma
[웹사이트 초안](https://www.figma.com/file/cP74X2L2XI18MCsXvV3S7a/%EC%9C%A0%ED%82%A4%EC%A6%88?node-id=1740%3A2)
