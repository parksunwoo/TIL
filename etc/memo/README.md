# TIL
사소하지만 깨알팁

- 서버상에서 구글 드라이브 파일을 다운로드 받고싶을 떄, 보통 pretrain model을 다운로드 받을때 URL 확인법 <br>
```bash
$ wget --no-check-certificate -r 'https://docs.google.com/uc?export=download&id=FILEID' -O FILENAME
$ wget --no-check-certificate -r 'https://drive.google.com/uc?export=download&id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ' -O craft_mlt_25k.pth
```

- 특정조건의 파일 삭제시
```bash
$ find . -type f -name "h*" -exec rm {} \; 
```

- 특정 명령어 계속 반복시 (1초 간격)
```bash
$ while true; do python run.py -w 5 -f 64 -l ko; sleep 1; done;
```

- 현재 디렉토리 내에 있는 파일의 개수 확인
```bash
$ ls -l | grep ^- | wc -l
```

- 현재 디렉토리 내에 있는 디렉토리 개수
```bash
$ ls -l | grep ^d | wc -l
```


