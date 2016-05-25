# SQL

## SQL(Strucured Query Laguage)
> 관계형 데이터 베이스(RDBMS)  
> 데이터베이스에 접근하고, 다루기 위한 언어.  
> ANSI표준  

## SQL_SYNTAX
> 대소문자를 구분하지 않는다. 
> SQL이 끝나면 마지막에 세미콜론 쓴다.  

- `SELECT` DATA를 조회 할 때  
- `UPDATE` DATA를 수정 할 때  
- `DELETE` DATA를 삭제 할 때  
- `INSERT INTO`  DATA를 추가 할 때
- `CREATE DATABASE` DATABASE를 새로 만들 때  
- `ALTER TABLE` TABLE이나 DATABASE의 구조를 수정 할 때  
- `DROP TABLE` TABLE를 삭제 할 때  
- `CREATE TABLE` TABLE를 생성 할 때  
- `DROP INDEX` INDEX를 삭제 할 때  

## SELECT
SELECT문을 이용해서 DATABASE의 자료를 조회 해서 결과를 받는다.  
```SQL
SELECT  COLUMN_NAME
FROM    TABLE_NAME;
```

## INSERT INTO Statement
> 테이블의 한 행 입력
> 두 가지 형식이 있다
```SQL
INSERT INTO TABLE_NAME
VAlLES (value1,value2,value3,value1,...);
```
```SQL
INSERT INTO TABLE_NAME (COLUMN1,COLUMN2,COLUMN3,...)
VAULES (value1,value2,value3,value1,...);

```
## SELECT DISTINCT
조회되는 결과 중 중복된 값들을 제거해서 가져온다.
```SQL
SELECT DISTINCT 
    COLUNM_NAME1
  , COLUNM_NAME2
FROM 
    TABLE_NAME;
```

## WHERE
원하는 조건에 맞는 DATA만 추출 할 때
```SQL
/* COLUNM_NAME1의 값이 'HJ'인 것만 조회 */
SELECT  COLUNM_NAME1, COLUNM_NAME2
FROM    TABLE_NAME
WHERE   COLUNM_NAME1 = 'HJ';
```
WHERE에 사용 할 수 있는 비교연산자
```
=       같다
<>      같지 않다 ( != )
>       크다 
<       작다
>=      같거나 크다
<=      같거나 작다
BETWEEN A와B의 교집합
LIKE    포함되는 값
IN      한 개 이상의 값을 넣을 수 있다.
```

## AND & OR Operators
> WHERE절에서 조건이 2개 이상 일 때 사용한다. 
  
`AND`연산자 : A와 B가 TRUE일 때
```SQL
/* COLUNM_NAME1의 값이 '가'이고 
COLUNM_NAME2의 값이 '나'인 DATA를 조회 */
SELECT  *
FROM    TABLE_NAME
WHERE   COLUNM_NAME1 = '가'
AND     COLUNM_NAME2 =  '나'
```
`OR`연산자 : A와 B 중 하나라도 TRUE일 때
```SQL
/* COLUNM_NAME1의 값이 '가'이거나
COLUNM_NAME2의 값이 '나'인 DATA를 조회 */
SELECT  *
FROM    TABLE_NAME
WHERE   COLUNM_NAME1 = '가'
OR      COLUNM_NAME2 = '나'
```


## ORDER BY
조회한 DATA를 정렬하는 기준

```SQL
SELECT
     COLUNM_NAME1  
   , COLUNM_NAME2
FROM
     TABLE
ORDER BY
     COLUNM_NAME1 ASC -- 오름차순 정렬
   , COLUNM_NAME2 DESC ; -- 내림차순 정렬

```
## INSERT INTO Statement
> 테이블의 한 행 입력
> 두 가지 형식이 있다
```SQL
INSERT INTO TABLE_NAME
VAlLES (value1,value2,value3,value1,...);
```
```SQL
INSERT INTO TABLE_NAME (COLUMN1,COLUMN2,COLUMN3,...)
VAULES (value1,value2,value3,value1,...);
```







