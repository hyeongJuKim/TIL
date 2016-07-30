# Branch

현재 버젼의 소스와 각종 정보들을 담고있다.
(가지치기)

커밋하면 Git은 현 Staging Area에 있는 데이터의 스냅샷에 대한 포인터, 저자나 커밋 메시지 같은 메타데이터, 이전 커밋에 대한 포인터 등을 포함하는 커밋 개체(커밋 Object)를 저장한다. 이전 커밋 포인터가 있어서 현재 커밋이 무엇을 기준으로 바뀌었는지를 알 수 있다. 최초 커밋을 제외한 나머지 커밋은 이전 커밋 포인터가 적어도 하나씩 있고 브랜치를 합친 Merge 커밋 같은 경우에는 이전 커밋 포인터가 여러 개 있다.  

### 새 브랜치 생성하기 
그럼 새로운 브랜치를 따보자
```
$ git branch {branchName}
```
새로 만든 브랜치도 지금 작업하고 있던 마지막 커밋을 가리킨다.  
아직까지 master 브랜치를 가리키고 있다.
  
`git log --oneline --decirate` 옵션을 사용해서 브랜치가 어떤 커밋을 키리키는지 확인해보자.  
HEAD가 master 브랜치를 가리키고 있을것이다.
### 브랜치 이동하기
`git checout {branchName}` 명령으로 다른 브랜치로 이동해보자.
```
$ git checout {branchName}
```

자 이제 다시 커밋을 해보자.  
```
$ git vim test.rb
$ get commit -a -m 'made a change'
```
  
### 기존 브랜치를 다른 브랜치에 덮어쓰기
```
$ git status
$ git branch -f 대상브랜치 [위치]  (ex. git branch -f master HEAD)
$ git checkout master 
```