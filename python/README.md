# TIL
Today I Learned

- 가상환경 라이브러리 -venv   
    - 파이썬3에서는 venv 라이브러리가 기본 제공
    
```bash
$ python3 -m venv ./myvenv      # 가상환경 디렉토리 생성
$ source ./myvenv/bin/activate  # 맥/리눅스 가상환경 활성화
$ pip install <package>         # 가상환경 안에서 개발
$ deactivate                    # 현재 가상환경 비활성 
```
    
    - 파이썬3 명령어로 생성한 가상환경이므로 pip로 실행해도 무관함 
    - virtualenv : 파이썬3에서는 굳이 사용할 필요없음, 파이썬2에서 사용하기위함
    












