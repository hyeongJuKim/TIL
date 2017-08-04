# MariaDB

DataBase 생성
```MYSQL
CREATE DATABASE {dataBaseName} DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

SHOW DATABASES;
```

User 생성
```SQL
CREATE USER '{userID}'@'%' identified by '{passWord}' ;
```

User 권한주기
```SQL
GREANT ALL PRIVILEGES ON {dataBaseName}.{tableName} TO '{userName}'@'%'; 

USE {DATABASE NAME};
```

USER 조회
```SQL
SELECT HOST, USER, PASSWORD, 
  FROM MYSQL.USER;
```

USER 삭제
```SQL
DROP USER '{userName}'@'{serverName}';

-- local인 경우 '%'로 한다.
DROP USER '{userName}'@'{serverName}';
```