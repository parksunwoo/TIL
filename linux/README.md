# TIL
Today I Learned

- 리눅스 기본명령어   
폴더복사 : cp -r 원본폴더 목적지폴더  
폴더이동 : mv 원본폴더 목적지폴더  
폴더삭제 : rm -rf 폴더  

## 만화로 배우는 리눅스 시스템 관리
- vim 치트시트 https://vim.rtorr.com/lang/ko
 
- 폴더에서 파일을 찾을때
```shell script
$grep -r "검색하고 싶은 문자열" /home/docs
```

- 파일 내용을 대문자 소문자 차이를 무시하고 검색
```shell script
$grep -r -i "yameno tarou" 디렉터리 경로
```

- 파일 내용을 대문자 소문자 차이를 무시하고 정규 표현식으로 검색
```shell script
$grep -r -i -E "((야메노 *(타로)|yameno +tarou)" 디렉터리 경로
```

- vim에서도 복사 & 붙이기 & 되돌리기를 하고싶어 (yank)
    - 선택 시작위치까지 커서를 옮기고 V 키를 눌러 영역선택. 범위를 정했으면 Y 키를 누르고 클립보드에 복사
        붙이고 싶은장소 이동 후 SHIFT + P , 1,0, SHIFT + P 의 경우 10번 붙여넣기
        
    - vim 에서 되돌리기는 U, 되돌리기의 되살리기는 Ctrl + R

- 다른 화면도 보면서 작업하고 싶어 화면분할
    - 현재화면을 가로분할 Ctrl + B, "
    - 현재화면을 세로분할 Ctrl + B, %
    - 화면 포커스 이동 Ctrl + B, 상 하 좌 우 

- SSH 넘어서 명령어를 하나만 실행하기
```shell script
$ ssh mint@server /scripts/do_backup.sh
```

- 서버에서 서버에 파일을 복사하기/ 복사원본 서버명과 서버경로 복사 대상 서버명과 서버 경로
```shell script
$ scp mint@server1:/data/file mint@server2:/backup
```

- 시스템 과부하를 파악하고 싶어 (top)
    - load average >= CPU 코어수가 되면 과부하 상태
    - CPU 사용률과 CPU 시간 양쪽이 큰 프로세스는 과부하 원인의 가능성이 높음
    - 과부하 원인인 프로세스는 kill 명령어로 종료함
    
- service 명령어
```shell script
$ sudo service apache2 restart
```   
    - load average 가 높아도 CPU는 과부하 상태가 아닐 수도 있다
    - 빈 메모리가 부족하면 -> 스왑(디스크 I/O)이 자주발생 -> CPU 처리가 쌓임 -> load average가 높아져서 시스템 반응이 나빠짐
    - 스왑량이 급격히 증가한다면 주의가 필요
    
- 로그 파일에서 필요한 줄만 뽑고 싶어 (파이프라인)
```shell script
$ grep "/retro" access.log | grep -v "/live" | less
```   
    
- 작업 절차를 자동화하고 싶어 (셀 스크립트)
    - bash용 셸 스크립트를 작성하려면 텍스트 파일 첫 줄에 #!/bin/bash 라고 적고 두 번째 줄 이후는 자동 실행하고 싶은 셸 명령어를 작성
    - 셸 스크립트는 chmod +x 파일명으로 실행 권한을 설정
    - 명령어가 이상이 생겨서 그 시점에서 스크립트 실행을 중단하고 싶을 떈 if [$? != 0]; then exit; fi 라고 적는다
    
- 같은 문자열을 스크립트에서 재사용하고 싶어(셸 변수)
    - 터미널이나 셸 스크립트에서 변수명=문자열 이라고 작성하면 오른쪽 문자열이 값이고 왼쪽에 있는 게 이름인 변수가 정의됨
    - 그 이후는 $변수명 또는 ${변수명} 으로 그 값과 동일하게 사용가능
    - 유지 보수하기 쉽도록 변수명은 변수에 저장될 내용을 잘 설명하는 이름을 사   
    
- 작업 환경과 상태를 정해서 스크립트를 실행하고 싶어(환경변수)
    - HOME : 현재 사용자의 홈 디렉토리 경로
    - PWD : 현재 디렉토리 경로
    - EDITOR : 정해진 텍스트 에디터 경로
    - PAGER : 정해진 페이지 경로
    - USER : 현재 사용자의 사용자명
    - GROUP : 현재 사용자의 그룹명
    - HOSTNAME : 머신의 호스트명

- 로그 파일에서 필요한 줄만 뽑고 싶어 (cut)
```shell script
$ cat /var/log/apache2/access.log | grep -v "/live" | cut -d " " -f 7 | less
```   

- 같은 내용의 줄을 세어보고 싶어 (sort와 uniq)
```shell script
#! /bin/bash
log=/var/log/apache2/access.log
count = 10
echo "접속수가 많은 ${count}개 페이지:"
cat $log | grep -v "/live" | cut -d " " -f 7 | sort | uniq -c | sort -r | head -n $count 
```   

- CSV 파일을 열의 내용에 따라 정렬하고 싶어 (sort와 리다이렉트)
```shell script
$ cat item.csv | cut -d "," -f 1-3 | sort -t "," -k 3 -n > ./items-sorted.csv
$ echo "12345, 추가항목, 0" >> ./items-sorted.csv
```   

- 명령줄 지정으로 작업 내용을 바꾸고 싶어 (명령줄 인수)
```shell script
$ script.sh -s filename1 -t filename2

    #! /bin/bash
    while getopts s:t: OPT
    do
      case $OPT in
        s) source="$OPTARG" ;;
        t) target="$OPTARG" ;;
      esac
    done
```   

- 명령어 이상 종료에 대응하고 싶어(종료상태)
    - $? 으로 직전에 실행한 명령어 종료 상태를 참조 가능
    - $? 값은 명령어가 정상 종료하면 0, 이상 종료하면 0 이외의 값이 됨
    - exit에 인수로 숫자를 지정하면 셸 스크립트의 종료 상태가 됨
    - if로 종료 상태를 참조하면 명령어가 정상 종료했는지에 따라 조건 분기가 가능
    
- 같은 처리를 반복해서 실행하고 싶어(for)
```shell script
    for filename in readmine.log
    do
      ./create-restart/sh $filename
    done
```   

- 공통 처리를 계속 재사용하고 싶어(셸 함수)
```shell script
#! /bin/bash

main(){
  report marketing.log mail-$(today).csv /shared/marketing/reports
  report system.log $(today).csv /shared/system/mail-reports
}

report(){
  source=$1
  report=$2
  outdir=$3
  ./analyze_mail_log.sh $source $report
}

today(){
  date +%Y-%m-%d
}

main
```   












    
    
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












      

















