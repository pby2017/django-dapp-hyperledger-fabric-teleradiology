# 2018-2-myMIMS

[git 처음일 때 - 원격 저장소와 로컬저장소 연결]
1. git config --global user.name "name"
2. git config --global user.email "email"
3. git init
4. git remote add origin https://github.com/pby2017/2018-2-myMIMS.git
5. git pull

[git bash 사용할 때 - git bash, ubuntu linux 환경]
1. git add *
2. git commit -m "commit example"
3. git push origin master (-> branch 이름이 master인 원격 저장소로 push 한다, master 말고 본인 브랜치로 push를 하자.)

[git source tree 처음일 때 - 원격 저장소와 로컬저장소 연결]
1. 깃 원격 저장소 복제
2. 저장소 - 깃플로우 - 저장소 초기화 - 확인
3. 브랜치 develop 체크된 것 확인
4. 저장소 - 깃플로우 - 새기능시작 - 이름 입력 - 확인
5. 브랜치 새기능이름 체크

[git source tree 원격 저장소에 push 하기]
1. 변경 파일 스테이지 올리기
2. 커밋 메시지 입력 후 커밋하기
3. 푸시하기
4. github 사이트에서 new pull request 하기 (from : push 한 브랜치, to : 병합할 브랜치)

[개발환경]
1. python 3.6.5

[install library - pip install]
1. Django                   2.1.3
2. django-unixdatetimefield 0.1.6
3. lazy-object-proxy        1.3.1
4. mysql-connector-python   8.0.13 (Mysql을 설치할 때 설치 선택옵션이다, pip로 따로 설치해도 된다)
5. mysqlclient              1.3.14
6. Pillow                   5.3.0
7. pytz                     2018.7
8. requests                 2.21.0

이외 기타(자동으로 설치되거나 오류해결할 때 설치함) 
astroid                  2.0.4  
autopep8                 1.4.3  
certifi                  2018.11  
chardet                  3.0.4  
colorama                 0.4.0  
idna                     2.8  
isort                    4.3.4  
mccabe                   0.6.1  
pip                      18.1  
pycodestyle              2.4.0  
pylint                   2.1.1  
setuptools               39.0.1  
six                      1.11.0  
typed-ast                1.1.0  
urllib3                  1.24.1  
wrapt                    1.10.11  

[install software]
1. git (https://git-scm.com/)
2. VScode (https://code.visualstudio.com/)
3. Mysql (https://dev.mysql.com/downloads/windows/installer/8.0.html)
4. sourcetree (https://www.sourcetreeapp.com/)

[process]
1. start project name myMIMS
2. add git flow (master, developer, feature) in sourcetree app
3. add django app name mapping
4. add image list page in mapping django app
5. add image detail page in mapping django app
6. connect image detail page and hyperledger fabric
7. change database sqlite3 to mysql
