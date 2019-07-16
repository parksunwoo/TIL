# TIL
사소하지만 깨알팁

- 서버상에서 구글 드라이브 파일을 다운로드 받고싶을 떄, 보통 pretrain model을 다운로드 받을때 URL 확인법
wget --no-check-certificate -r 'https://docs.google.com/uc?export=download&id=FILEID' -O FILENAME
wget --no-check-certificate -r 'https://drive.google.com/uc?export=download&id=1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ' -O craft_mlt_25k.pth

