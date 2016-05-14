# Java

## Class

### StringBuffer
StringBuffer를 쓰는 이유.  
String클래는 불변객체이기때문에subString(), trin() 등 메소드를 사용해서 가공할 때마다 계속해서 새로운 객체를 생성하여 반환한다.  
따라서 원래 String객체는 가지고 있는 문자열이 변경되지 않으며 여전히 사용가능한 채로 남든다.
이렇게 가비지가 생긴다.
아래의 예제를 보자.  

아래의 코드 처럼 반복문을 을 100번 더하는 코드가 있다.
``` java
        String str="";
        for(int i = 0; i < 100; i++){
            str = str + "*";
        }
        System.out.println(str);
```
100번 하는것과 같다.  
StringBuffer를 이용해서 해보자.
``` java       
        // StringBuffer클래스를 만든다.
        StringBuffer sb = new StringBuffer();
        for(int i = 0; i < 100; i++){
            // append()메소드를 통해서 문자열을 더한다.
            sb.append("*");
        }
        // 마무리는 toString
        String str6 = sb.toString();
        System.out.println(str6);
```
우리는 여기서 두 개의 코드를 봤다.  
두개의 코드는 보기에는 비슷 할 지 모르지만 성능(속도)면에서 많은 차이가 난다.
StringBuffer을 사용하자.
