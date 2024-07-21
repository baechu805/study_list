import streamlit as st

st.title("Study list")

with st.expander('Linux 기본 명령어'):
	st.text('ls : 현재 디렉토리의 모든 파일 및 폴더를 기본 형식으로 보여줌\n'
            'cd : 디렉토리를 변경\n'
            'cd .. : 현재 디렉토리의 상위 폴더로 이동\n'
            'pwd : 현재 작업 중인 디렉토리의 경로를 표시\n'
            'mkdir : 새로운 디렉토리(폴더)를 생성\n'
            'touch : 새로운 빈 파일을 생성\n'
            'chmod : 파일이나 디렉토리의 권한을 변경\n'
            'grep : 파일 내용 중에서 지정된 패턴이나 문자열을 검색하여 그 결과를 출력\n')

with st.expander('Git 명령어'):
    st.text('git status : 파일 상태 확인\n'
            'git init : .git 하위 디렉토리 생성\n'
            'git add <파일명> :커밋에 단일 파일의 변경 사항을 포함\n'
            'git commit -m "커밋 메시지 : 커밋 생성\n'
            'git clone <https:.. URL> : 기존 소스 코드 다운로드/복제\n'
            'git push -u < remote > <브랜치이름> : 새 브랜치를 원격 저장소로 push\n'
            'git pull : 원격 저장소의 변경 내용이 현재 디렉토리에 가져와지고(fetch) 병합(merge)됨\n'
            'git branch <브랜치이름> : 새 브랜치 생성 (local로 만듦)\n'
            'git checkout -b <브랜치이름> : 브랜치 생성 & 이동\n')
