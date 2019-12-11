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


## 만화로 배우는 리눅스 시스템 관리2
- 정기적인 작업을 자동으로 처리하고 싶어
    - 리눅스는 예약 녹화처럼 지정한 시각에 명령어를 자동 실행하는 crond라는 서비스가 있고 crontab은 crond로 실행하고 싶은 멍령어와 실행 시각을 관리하는 명령어
    - crontab -e로 cronjob을 설정하면 임의 명령어 열을 지정 시간에 정기적으로 실행가능
    - cronjob은 crontab 명령어를 실행하는 사용자 권한으로 동작함
    - MAILTO=메일 주소 라는 열을 추가하면 그 이후의 cronjob 출력 내용이 메일로 보내짐(MTA를 설정해둬야 함)
    
- 키 인증으로 안전하게 로그인하고 싶어
    - ssh나 scp의 인증방식에는 암호 인증 이외에도 더욱 안전한 키 인증 방식이 있음
    - 키 인증을 하려면 미리 공개키와 비밀키의 쌍을 작성하고 공개키를 인증 대상 서버에 등록해야 함
    - 비밀키는 패스프레이즈를 아는 사람만 사용 가능
    
- 정시 처리로 자동으로 scp 하고 싶어
    - 패스프레이즈 없는 비밀키를 사용하면 자동으로 키 인증 가능함 (자동인증)
    - 안전하도록 자동인증용 키 쌍은 인증 후 할 수 있는 일을 가능한 제한하기 (일반 작업에만 쓰고 로그인용으로 사용하지 않기)
    - cronjob으로 scp한다면 자동 인증용 비밀키를 -i 옵션으로 지정해서 키 인증하거나 공개키라면 실행할 scp 명령어 내용에 대응하는 서버 쪽 명령어열을
      command = "명령어열" 형식으로 설정하기
      
- 여러 서버에 있는 파일을 효율적으로 수집하고 싶어
    - 자동 인증으로 scp하려면 다운로드 허가 대신에 업로드를 허가하는 쪽이 비교적 안전
    - 키워드는 "처리 크기는 작게" "처리 사이에는 느슨한 결합으로" 커다란 문제는 일단 작은 문제로 쪼개서 생각하기
    - 여러 서버가 관련된 처리는 각각의 서버 단위에서 처리가 가능한 완료되도록 하면 서버끼리 통신하는걸 최소한으로 줄일 수 있음

- 조건에 해당하는 로그 줄 수를 집계하고 싶어
    - wc 명령어를 사용하면 입력한 내용 문자수나 줄 수를 카운트 가능. 특히 줄 수를 세는 wc -l은 자주 사용함
    - 아파치 로그를 날짜로 추출하려면 grep의 정규 표현식을 사용하면 좋음
    - bash 스크립트는 $((계산식))으로 간단한 계산이 가능. 변수와 조합하면 집계에서도 사용 가능
    
- 여러 텍스트 파일을 일괄 편집하고 싶어
    - 셸 스크립트에서 텍스트를 자동 편집하고 싶을 때 sed를 사용
    - sed 로 문자열을 일괄 치환하려면 sed -e "s/치환전/치환후/" 지정
    - 셸 스크립트에서 기존 파일을 편집해서 덮어쓰기를 할 때는 주의가 필요. 일단 다른 파일명으로 변경해두고 원래 파일 위치에 출력하는 등으로 같은 파일을 하나의 처리에서
    읽고 쓰지 않도록 해야 함

- 표기 방법이 일정하지 않은 문구를 한꺼번에 치환하고 싶어
    - vim 검색이나 칯환에서는 확장 정규 표현식을 사용할 때 \v 뒤에 정규 표현식을 작성함
    - sed로 치환할 때 확장 정규 표현식을 사용하려면 GNU sed는 -r 옵션, BSD sed는 -E 옵션을 지정함
    - 정규 표현식은 치환후 지정에 \번호를 써서 (와) 로 감싼 치환전 내용을 치환후 내용에 인용 가능 (역참조)
    
- 정규 표현식 패턴 지정을 좀 더 간단히 만들고 싶어
    - 치환 대상이 한 줄 안에 두 번 이상 나올 때 모두 치환하려면 g 플래그를 지정하기
    - 치환 대상의 대소문자 차이를 무시하고 싶다면 i 플래그를 지정하기
    - 열거한 여러 문자나 문자 범위에 포함된 문자 하나를 치환하고 싶다면 브래킷 표현(대괄호로 안에 문자나 문자 범위를 나열함)을 사용하기
    
- 정규 표현식 패턴 지정을 더 간단히
    - 브래킷 표현과 +와 *를 조합해서 특정 종류 문자만 연속된 문자열을 표현 가능
    - 브래킷 표현의 여는 대괄호 바로 뒤에 ^을 쓰면 블라켓 표현의 부정형이 됨. 어떤 글자가 등장하지 않는 걸 안다면 블라켓 표현의 부정형을 사용함
    - ^을 사용하면 줄 시작에만 있는 치환 대상을 치환 가능함
    - $를 사용하면 줄 끝에만 있는 치환 대상을 치환 가능함
        
- 오래된 파일을 찾아서 지우고 싶어
    - 오래 파일이나 새로운 파일을 찾으려면 find 명령어를 사용함. 지정 방법은 find 검색 대상 -ctime 최종 갱신일 범위
    - 최종 갱신일 지정은 우선 기준이 되는 과거 날짜까지의 일수를 정함 (1개월 전이라면 30. 1년 전이라면 365 등) 그보다 과거(오래된 파일)을 검색한다면 +, 미래(새로운 파일)를 검색한다면 -를 추가
    - find 명령어로 찾은 모든 파일을 for 반복문에서 사용할 수 있음
    - 오늘부터 출발해서 지정한 날짜만큼 시간을 거슬러 올라가잖아? 목적 일(기준이 되는 날)에 도착했으면 거기서부터 과거 방향으로(시간을 거스른다면) 오래된 파일을 찾으러 가는 거면 +
        반대로 오늘(미래 방향)로 돌아가서 새로운 파일을 찾는다면 -!
        
- 좀 더 복잡한 조건으로 파일을 찾고 싶어
    - 파일명으로 파일을 검색하려면 -name을 사용
    - 검색조건1 -and 검색 조건2라고 쓰면 두 검색 조건 양쪽을 만족하는 파일이 검색됨
    - 검색조건1 -or 검색 조건2라고 쓰면 두 검색 조건 양쪽 또는 어느 한쪽을 만족하는 파일이 검색됨
    - 검색 조건은 3개 이상 조합할 수 있음. 조건 우선순위를 지정하려면 \(와 \)으로 감쌈
    -  -ctime -8 -and -name "*.log" 직전 일주일 전에 변경된 이름이 *.log 로 끝나는 파일
    -  -ctime +30 -and -ctime -60 -and \(-name "*report*" -or -name "*error*" \) 지난달 1개월 사이에 변경된, 이름에 report 또는 error를 포함한 파일
    -  -name "*.tar.gz" -or \( -ctime +7 -and -name ".log" \) 이름이 .tar.gz 로 끝나는 파일 또는 1주일보다 이전에 변경된 이름이 .log로 끝나는 파일
    
- 디스크가 가득 차기 전에 파일을 삭제하고 싶어
```shell script
#!/bin/bash
free_size=$(df /data/backup | \ 
  sed -r -e "s/[^ ]+ +[^ ]+ +[^ ]+ +([^ ]+).+/\1/" | \
  tail -n 1)
required_size=$((10 * 100 * 1000))

if [ $free_size -lt $required_size ]
then
  files=$(find /data/backup -ctime +30)
  for file in $files
  do 
    rm "$file"
  done
fi    
```  

- 이전 명령어가 성공하면 다음도 실행하고 싶어
    - 프로그램을 소스에서 빌드 후 설치하기
        ./configure --prefix=$HOME/local/ && make && make install
    - 최신 정보에 따라 패키지를 갱신하기
        sudo apt-get update && sudo apt-get upgrade && sudo apt-get clean
    - 일반 명령어 나열이나 파이프라인은 도중에 명령어 실행에 실패하더라도 모든 명령어가 실행됨
    - &&로 묶인 명령어를 나열한 AND 리스트는 도중에 명령어 실행에 실패하면 그 이후의 명령어를 실행하지 않음
    - AND 리스트로 가능한 건 if문으로도 가능함. AND 리스트는 어떤 명령어 실행에 성공하면 다음 명령어를 실행한다는 정해진 용도에 대응하는 편의 문법.
    
- 이전 명령어가 실패하면 다음을 실행하고 싶어
    - ||로 명령어를 나열한 OR 리스트는 명령어 실행에 실패하면 다음 명령어를 실행함
    - OR 리스트는 성공할 떄까지 나열한 명령어를 순서대로 실행하는(실패하면 다음 안을 시험하는 사용방법이 대다수)
    - 이런 처리에 실패하면 차선책으로 단계적으로 전환하는 걸 폴백이라고 함

- 부모 디렉토리로 일일이 돌아가는 조작을 생략하고 싶어
```shell script
remove_files(){
  files=$(find ./ -name "*.bak")
  for file in $files
  do
    rm $file
  done
}    

for dir in logs data users
do
  (cd $dir && remove_files)
done     
```     
    - ; 구분자 리스트나 AND 리스트 같은 형태의 명령어열을 소괄호() 로 감싸면 그 내용은 다른 셸(서브셸)로 실행됨
    - cd 명령어를 사용할 때는 cd 와 이어진 처리를 서브셸로 실행하면 매번 원래 디렉터리로 돌아가지 않아도 됨
    - 서브셸 안에 복잡한 처리를 하려면 처리를 함수로 정의해서 서브셸에서 그 함수를 실행하면 됨
    
- 3패턴 이상을 사용하고 싶어
    - hostname 명령어를 사용하면 그 컴퓨터의 호스트명을 알 수 있음
    - 명령어 실행 결과나 변숫값에 대해 A와 같다면, B와 같다면, C와 같다면처럼 경우로 나뉘는 조건 분기는 case 문으로 작성하면 좋음

- 사원 번호 첫 글자로 처리를 나누고 싶어
    - case 문으로 추상적인 선택지를 정의하려면 와일드카드(*와 ?)를 사용함
    - case 문은 구체적인 선택지(상세한 조건)일수록 앞쪽에, 추상도가 높은 선택지(유연한 조건)일수록 뒤쪽에 두기
    - case 문 선택지는 | 로 여러 패턴을 나열 가능함. 판별 후 처리가 같은 선택지는 | 로 나열해서 하나로 묶는게 좋음
    
- 같은 처리를 1시간마다 반복 실행하고 싶어
    - 단순히 같은 처리를 반복해서 실행하고 싶다면 while 반복 사용. while 반복은 조건을 만족하는 동안 처리를 반복해서 실행함
    - 셸 스크립트에서 웹페이지에 접속하려면 curl 명령어를 사용
    - 반복 처리를 천천히 진행하려면 반복마다 sleep 명령어로 처리를 일시 정지시킴
    
- 명령어 출력을 파이프라인으로 받고 싶어
```shell script
#!/bin/bash
log=$1
if [ "$1" = "" ]
then 
    tempfile=$(mktemp)
    while read line
    do
      echo "$line" >> $tempfile
    done
    log=$tempfile
fi

cat $log | cut -d " " -f 7 | sort | uniq -c | sort -r | head -n 10 > ./top.txt
cat $log | cut -d " " -f 7 | sort | uniq -c | sort -r | head -n 10 > ./bottom.txt

if [  "$tempfile" != "" ]
then
    rm $tempfile
fi
```     
  - while 반복을 쓰면 실패할 때까지 같은 명령어를 몇 번이고 반복실행가능
  - 파이프라인으로 표준 입력에 넘긴 내용은 while 반복으로 read 명령어를 반복 실행하면 읽어 들일 수 있음 (이걸 임시 파일에 저장하면 일반 파일처럼 취급 가능)
  - 임시 파일은 mktemp 명령어로 작성함 (사용이 끝난 임시 파일은 잘 삭제할 것)
  
- 스페이스가 들어있는 파일명도 반복 처리에 쓰고 싶어
    - for 반복은 처리 대상에 공백 문자가 섞여 있으면 기대한 대로 동작하지 않을 수도 있음
    - while과 read로 반복문을 사용하면 각종 입력을 한 줄씩 확실하게 처리 가능
    - 어떤 이름의 파일이 올지 알 수 없다면 for 반복보다 while과 read를 사용하는 쪽이 안전
    
- 키보드 입력을 받고 싶어
    - 키보드 입력은 read 명령어로 읽을 수 있음
    - read 명령어를 단독으로 실행하면 키보드 입력을 대기하는 상태가 되어서 enter를 입력할 때까지 입력된 내용을 읽을 수 있음
    - read 명령어로 입력을 대기할 때 read -p "입력하세요>" name처럼 해서 입력을 요구하는 프롬프트를 표시하면 좋음

- 키보드 입력을 확인해서 다시 입력받고 싶어
```shell script
#!/bin/bash
given_args=0
on_arg_given(){
  given_args=$(($given_args + 1))
}

while getopts l:f:u:i:q:g:p:b:c:s: OPT; do
    case $OPT in
      l) last_name="$OPTARG"; last_name_given=yes; on_arg_given;;
      f) first_name="$OPTARG"; first_name_given=yes; on_arg_given;;

    esac
done

input(){
  [ "$last_name_given" = "" ] && read -p " 성은?> " last_name
  [ "$first_name_given" = "" ] && read -p " 이름은?> " first_name
}

confirm(){

}

if [$given_args -lt 10]; then
    while true; do
      input; confirm
      if [  "$yesno" != "yes" ]; then continue; else break; fi
    done
fi
```
 
- 명령어의 모든 출력을 파일로 저장하고 싶어
    - 명령어나 스크립트의 정보 출구는 표준 출력 (1번) 과 표준 에러 출력(2번) 두 가지가 있음
    - 리다이렉트를 사용하면 표준 출력(1> 또는 >)과 표준 에러 출력(2>) 각자 따로따로 출력할 곳을 변경 가능
    - "출력 번호 >& 출력 대상 번호"라고 쓰면 특수한 리다이렉트가 되어서 두 출력을 하나로 합칠 수 있음
      1> /path/to/file 2>&1 이라고 적으면 표준 출력이 파일에 리다이렉트되고, 표준 에러 출력도 표준 출력과 같은 출력 대상에 리다이렉트 됨
      
- 사용자 작성용 명령어 차이를 파악하고 싶어
    - 기본적으로 useradd를 사용(드물게 adduser 밖에 사용할 수 없는 경우도 있음)
    - 실행하기 전에 --help로 사용법을 확인할 것!
    - 기대와 다른 상태로 사용자가 작성되었다면 userdel로 삭제(드물게 rmuser 밖에 사용할 수 없는 경우도 있음)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
      
      
          
    
    
    
    
    
    
    
    
      
  
  
  
  
  
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
        
        
        
    




















        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      
      
      
      












    
    
    
    
    
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    












      

















