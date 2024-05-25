## [📕 회원 관리 웹 애플리케이션 요구사항](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%95%20%ED%9A%8C%EC%9B%90%C2%A0%EA%B4%80%EB%A6%AC%C2%A0%EC%9B%B9%C2%A0%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%C2%A0%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD-1)

### [📗 회원 정보](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20%ED%9A%8C%EC%9B%90%C2%A0%EC%A0%95%EB%B3%B4-1)

이름 : username

나이 : age

### [📗 기능 요구사항](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20%EA%B8%B0%EB%8A%A5%20%EC%9A%94%EA%B5%AC%EC%82%AC%ED%95%AD-1)

- 회원 저장
- 회원 목록 조회

**[Member] - 회원 도메인 모델**

```java
package hello.servlet.domain.member;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class Member {
    
    private Long id;
    private String username;
    private int age;

    public Member() {
    }
    
    public Member(String username, int age) {
        this.username = username;
        this.age = age;
    }
}
```

>> id는 Member를 회원 저장소에 저장하면 회원 저장소가 할당한다.

**[MemberRepository] - 회원 저장소**

```java
package hello.servlet.domain.member;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
* 동시성 문제가 고려되어 있지 않음, 실무에서는 ConcurrentHashMap, AtomicLong 사용 고려
*/
public class MemberRepository {
    
    private static Map<Long, Member> store = new HashMap<>(); //static 사용
    private static long sequence = 0L; //static 사용
    
    private static final MemberRepository instance = new MemberRepository();
    
    public static MemberRepository getInstance() {
	    return instance;
    }
    
    private MemberRepository() {
    }
    
    public Member save(Member member) {
        member.setId(++sequence);
        store.put(member.getId(), member);
        return member;
    }
    
    public Member findById(Long id) {
	    return store.get(id);
    }
    
    public List<Member> findAll() {
  	  return new ArrayList<>(store.values());
    }
    
    public void clearStore() {
		store.clear();
    }
}
```

>> 싱글톤 패턴은 객체를 단 하나만 생성해서 공유해야 하므로 생성자를 private 접근자로 막아둔다.

**[회원 저장소 테스트 코드]**

```java
package hello.servlet.domain.member;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import java.util.List;
import static org.assertj.core.api.Assertions.*;

class MemberRepositoryTest {
    
    MemberRepository memberRepository = MemberRepository.getInstance();
    
    @AfterEach // 다음 테스트에 영향을 주지 않도록 저장소 초기화
    void afterEach() {
	    memberRepository.clearStore();
    }
    
    @Test
    void save() {
        //given
        Member member = new Member("hello", 20);
        
        //when
        Member savedMember = memberRepository.save(member);
        
        //then
        Member findMember = memberRepository.findById(savedMember.getId());
        assertThat(findMember).isEqualTo(savedMember);
    }
    
    @Test
    void findAll() {
        //given
        Member member1 = new Member("member1", 20);
        Member member2 = new Member("member2", 30);
        
        memberRepository.save(member1);
        memberRepository.save(member2);
        
        //when
        List<Member> result = memberRepository.findAll();
        
        //then
        assertThat(result.size()).isEqualTo(2);
        assertThat(result).contains(member1, member2);
    }
}
```

## [📕 서블릿으로 회원 관리 웹 애플리케이션 만들기](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%95%20%EC%84%9C%EB%B8%94%EB%A6%BF%EC%9C%BC%EB%A1%9C%20%ED%9A%8C%EC%9B%90%20%EA%B4%80%EB%A6%AC%20%EC%9B%B9%20%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0-1)

### [📗 [MemberFormServlet] - 회원 등록 폼](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20%5BMemberFormServlet%5D%20-%20%ED%9A%8C%EC%9B%90%20%EB%93%B1%EB%A1%9D%20%ED%8F%BC-1)

```java
package hello.servlet.web.servlet;

import hello.servlet.domain.member.MemberRepository;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "memberFormServlet", urlPatterns = "/servlet/members/newform")
public class MemberFormServlet extends HttpServlet {
    
	private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {
        
        response.setContentType("text/html");
        response.setCharacterEncoding("utf-8");
        
        PrintWriter w = response.getWriter();
        w.write("<!DOCTYPE html>\n" +
                "<html>\n" +
                "<head>\n" +
                " <meta charset=\"UTF-8\">\n" +
                " <title>Title</title>\n" +
                "</head>\n" +
                "<body>\n" +
                "<form action=\"/servlet/members/save\" method=\"post\">\n" +
                " username: <input type=\"text\" name=\"username\" />\n" +
                " age: <input type=\"text\" name=\"age\" />\n" +
                " <button type=\"submit\">전송</button>\n" +
                "</form>\n" +
                "</body>\n" +
                "</html>\n");
    }
}
```

>> MemberFormServlet은 단순하게 회원 정보를 입력할 수 있는 HTML Form을 만들어서 응답한다. 자바 코드로 HTML을 제공해야 하므로 쉽지 않은 작업이다.

### [📗 [MemberSaveServlet] - 회원 저장](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%5BMemberSaveServlet%5D%C2%A0-%20%ED%9A%8C%EC%9B%90%20%EC%A0%80%EC%9E%A5-1)

```java
package hello.servlet.web.servlet;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "memberSaveServlet", urlPatterns = "/servlet/members/save")
public class MemberSaveServlet extends HttpServlet {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {
        
        System.out.println("MemberSaveServlet.service");
        String username = request.getParameter("username");
        int age = Integer.parseInt(request.getParameter("age"));
        
        Member member = new Member(username, age);
        System.out.println("member = " + member);
        memberRepository.save(member);
        
        response.setContentType("text/html");
        response.setCharacterEncoding("utf-8");
        
        PrintWriter w = response.getWriter();
        w.write("<html>\n" +
                "<head>\n" +
                " <meta charset=\"UTF-8\">\n" +
                "</head>\n" +
                "<body>\n" +
                "성공\n" +
                "<ul>\n" +
                " <li>id="+member.getId()+"</li>\n" +
                " <li>username="+member.getUsername()+"</li>\n" +
                " <li>age="+member.getAge()+"</li>\n" +
                "</ul>\n" +
                "<a href=\"/index.html\">메인</a>\n" +
                "</body>\n" +
                "</html>");
    }
}
```

MemberSaveServlet은 다음 순서로 동작한다.

1. 파라미터를 조회해서 Member 객체를 만든다.
2. Member 객체를 MemberRepository를 통해서 저장한다.
3. Member 객체를 사용해서 결과 화면용 HTML을 동적으로 만들어서 응답한다.

### [📗 [MemberListServlet] - 회원 목록](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%5BMemberListServlet%5D%C2%A0-%20%ED%9A%8C%EC%9B%90%20%EB%AA%A9%EB%A1%9D-1)

```java
package hello.servlet.web.servlet;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

@WebServlet(name = "memberListServlet", urlPatterns = "/servlet/members")
public class MemberListServlet extends HttpServlet {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {
        
        response.setContentType("text/html");
        response.setCharacterEncoding("utf-8");
        
        List<Member> members = memberRepository.findAll();
        
        PrintWriter w = response.getWriter();
        w.write("<html>");
        w.write("<head>");
        w.write(" <meta charset=\"UTF-8\">");
        w.write(" <title>Title</title>");
        w.write("</head>");
        w.write("<body>");
        w.write("<a href=\"/index.html\">메인</a>");
        w.write("<table>");
        w.write(" <thead>");
        w.write(" <th>id</th>");
        w.write(" <th>username</th>");
        w.write(" <th>age</th>");
        w.write(" </thead>");
        w.write(" <tbody>");
        
/*
        w.write(" <tr>");
        w.write(" <td>1</td>");
        w.write(" <td>userA</td>");
        w.write(" <td>10</td>");
        w.write(" </tr>");
*/
        
        for (Member member : members) {
            w.write(" <tr>");
            w.write(" <td>" + member.getId() + "</td>");
            w.write(" <td>" + member.getUsername() + "</td>");
            w.write(" <td>" + member.getAge() + "</td>");
            w.write(" </tr>");
        }
        
        w.write(" </tbody>");
        w.write("</table>");
        w.write("</body>");
        w.write("</html>");
    }
}
```

MemberListServlet은 다음 순서로 동작한다.

1. memberRepository.findAll() 을 통해 모든 회원을 조회한다.
2. 회원 목록 HTML을 for 루프를 통해서 회원 수 만큼 동적으로 생성하고 응답한다.

### [📗 템플릿 엔진으로...](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%ED%85%9C%ED%94%8C%EB%A6%BF%20%EC%97%94%EC%A7%84%EC%9C%BC%EB%A1%9C...-1)

서블릿 덕분에 동적으로 원하는 HTML을 마음껏 만들 수 있다.

정적인 HTML 문서라면 화면이 계속 달라지는 회원의 저장 결과라던가, 회원 목록 같은 동적인 HTML을 만드는 일은 불가능 할 것이다.

그런데, 코드에서 보듯이 이것은 매우 복잡하고 비효율 적이다. 자바 코드로 HTML을 만들어 내는 것 보다 차라리 HTML 문서에 동적으로 변경해야 하는 부분만 자바 코드를 넣을 수 있다면 더 편리할 것이다. 

이것이 바로 템플릿 엔진이 나온 이유이다. 템플릿 엔진을 사용하면 HTML 문서에서 필요한 곳만 코드를 적용해서 동적으로 변경할 수 있다. 대표적인 템플릿 엔진에는 JSP, Thymeleaf, Freemarker, Velocity등이 있다. 

## [📕 JSP로 회원 관리 웹 애플리케이션 만들기](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%95%20JSP%EB%A1%9C%20%ED%9A%8C%EC%9B%90%20%EA%B4%80%EB%A6%AC%20%EC%9B%B9%20%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%20%EB%A7%8C%EB%93%A4%EA%B8%B0-1)

### [📗 JSP 라이브러리 추가](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20JSP%20%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC%20%EC%B6%94%EA%B0%80-1)

**[build.gradle]**

```java
//JSP 추가 시작
implementation 'org.apache.tomcat.embed:tomcat-embed-jasper'
implementation 'javax.servlet:jstl'
//JSP 추가 끝
```

### [📗 [new-form.jsp] - 회원 등록 폼 JSP](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20%5Bnew-form.jsp%5D%20-%20%ED%9A%8C%EC%9B%90%20%EB%93%B1%EB%A1%9D%20%ED%8F%BC%20JSP-1)

```xml
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
	<title>Title</title>
</head>
<body>
    
<form action="/jsp/members/save.jsp" method="post">
    username: <input type="text" name="username" />
    age: <input type="text" name="age" />
    <button type="submit">전송</button>
</form>
    
</body>
</html>
```

<%@ page contentType="text/html;charset=UTF-8" language="java" %> 

첫 줄은 JSP문서라는 뜻이다. JSP 문서는 이렇게 시작해야 한다. 

회원 등록 폼 JSP를 보면 첫 줄을 제외하고는 완전히 HTML와 똑같다. 

JSP는 서버 내부에서 서블릿으로 변환되는데, 이전에 작성한 MemberFormServlet과 거의 비슷한 모습으로 변환된다.

### [📗 [save.jsp] - 회원 저장 JSP](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%5B%08save.jsp%5D%C2%A0-%20%ED%9A%8C%EC%9B%90%20%EC%A0%80%EC%9E%A5%20JSP-1)

```xml
<%@ page import="hello.servlet.domain.member.MemberRepository" %>
<%@ page import="hello.servlet.domain.member.Member" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    // request, response 사용 가능
    MemberRepository memberRepository = MemberRepository.getInstance();
    System.out.println("save.jsp");
    String username = request.getParameter("username");
    int age = Integer.parseInt(request.getParameter("age"));
    Member member = new Member(username, age);
    System.out.println("member = " + member);
    memberRepository.save(member);
%>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
성공
<ul>
	<li>id=<%=member.getId()%></li>	
	<li>username=<%=member.getUsername()%></li>
	<li>age=<%=member.getAge()%></li>
</ul>
<a href="/index.html">메인</a>
</body>
</html>
```

**<%@ page import="hello.servlet.domain.member.MemberRepository" %>** : 자바의 import 문과 같다.

**<% ~~ %>** : 이 부분에는 자바 코드를 입력할 수 있다.

**<%= ~~ %>** : 이 부분에서는 자바 코드를 출력할 수 있다.

### [📗 [members.jsp] - 회원 목록 JSP](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%5B%08members.jsp%5D%C2%A0-%20%ED%9A%8C%EC%9B%90%20%EB%AA%A9%EB%A1%9D%20JSP-1)

```xml
<%@ page import="java.util.List" %>
<%@ page import="hello.servlet.domain.member.MemberRepository" %>
<%@ page import="hello.servlet.domain.member.Member" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%
    MemberRepository memberRepository = MemberRepository.getInstance();
    List<Member> members = memberRepository.findAll();
%>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="/index.html">메인</a>
<table>
    <thead>
    <th>id</th>
    <th>username</th>
    <th>age</th>
    </thead>
    <tbody>
<%
    for (Member member : members) {
        out.write(" <tr>");
        out.write(" <td>" + member.getId() + "</td>");
        out.write(" <td>" + member.getUsername() + "</td>");
        out.write(" <td>" + member.getAge() + "</td>");
        out.write(" </tr>");
    }
%>
	</tbody>
</table>
    
</body>
</html>
```

### [📗 서블릿과 JSP의 한계](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B8%94%EB%A6%BF%EA%B3%BC%20JSP%EC%9D%98%20%ED%95%9C%EA%B3%84-1)

- 서블릿은 뷰(View)화면을 위한 HTML을 만드는 작업이 자바 코드에 섞여서 지저분하고 복잡하다.
- JSP를 사용한 덕분에 뷰를 생성하는 HTML 작업을 깔끔하게 가져가고, 중간중간 동적으로 변경이 필요한 부분에만 자바 코드를 적용했다. 그런데 이렇게 해도 해결되지 않는 몇가지 고민이 남는다.
- 회원 저장 JSP : 코드의 상위 절반은 회원을 저장하기 위한 비즈니스 로직이고, 나머지 하위 절반만 결과를 HTML로 보여주기 위한 뷰 영역이다. 회원 목록의 경우에도 마찬가지다.
- 코드를 잘 보면, JAVA 코드, 데이터를 조회하는 리포지토리 등등 다양한 코드가 모두 JSP에 노출되어 있다. **JSP가 너무 많은 역할을 한다.** 이렇게 작은 프로젝트도 벌써 머리가 아파오는데, 수백 수천줄이 넘어가는 JSP를 떠올려보면 정말 지옥과 같을 것이다.

### [📗 MVC 패턴의 등장](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20MVC%20%ED%8C%A8%ED%84%B4%EC%9D%98%20%EB%93%B1%EC%9E%A5-1)

> **비즈니스 로직은 서블릿 처럼 다른곳에서 처리하고, JSP는 목적에 맞게 HTML로 화면(View)을 그리는 일에 집중하도록 하자. 과거 개발자들에게도 비슷한 고민이 있었고, 그래서 MVC 패턴이 등장했다.**

## [📕 MVC 패턴](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%95%20MVC%20%ED%8C%A8%ED%84%B4-1)

### [📗 개요](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%EA%B0%9C%EC%9A%94-1)

#### **MVC 패턴 이전**

![](https://blog.kakaocdn.net/dn/bpeb09/btsiOfZqOoj/aKlE8GFRI7zuNzL2EkQK91/img.png)

- **너무 많은 역할**  
    하나의 서블릿이나 JSP만으로 비즈니스 로직과 뷰 렌더링까지 모두 처리하게 되면, 너무 많은 역할을 하게 되고, 결과적으로 유지보수가 어려워진다. 비즈니스 로직을 호출하는 부분에 변경이 발생해도 해당 코드를 손대야 하고, UI를 변경할 일이 있어도 비즈니스 로직이 함께 있는 해당 파일을 수정해야 한다.
- **변경의 라이프 사이클**  
    사실 이게 정말 중요한데, 진짜 문제는 둘 사이에 변경의 라이프 사이클이 다르다는 점이다. 예를 들어서 UI 를 일부 수정하는 일과 비즈니스 로직을 수정하는 일은 각각 다르게 발생할 가능성이 매우 높고 대부분 서로에게 영향을 주지 않는다. 이렇게 변경의 라이프 사이클이 다른 부분을 하나의 코드로 관리하는 것은 유지보수하기 좋지 않다.
- **기능 특화**  
    특히 JSP 같은 뷰 템플릿은 화면을 렌더링 하는데 최적화 되어 있기 때문에 이 부분의 업무만 담당하는 것이 가장 효과적이다.

### [📗 Model View Controller (MVC) 패턴](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20Model%20View%20Controller%20(MVC)%20%ED%8C%A8%ED%84%B4-1)

MVC 패턴은 지금까지 학습한 것 처럼 하나의 서블릿이나, JSP로 처리하던 것을 컨트롤러(Controller)와 뷰(View)라는 영역으로 서로 역할을 나눈 것을 말한다. 

웹 애플리케이션은 보통 이 MVC 패턴을 사용한다. 

- **Controller** : HTTP 요청을 받아서 파라미터를 검증하고, 비즈니스 로직을 실행한다. 그리고 뷰에 전달할 결과 데이터를 조회해서 모델에 담는다. 
- **Model** : 뷰에 출력할 데이터를 담아둔다. 뷰가 필요한 데이터를 모두 모델에 담아서 전달해주는 덕분에 뷰는 비즈니스 로직이나 데이터 접근을 몰라도 되고, 화면을 렌더링 하는 일에 집중할 수 있다. 
- **View** : 모델에 담겨있는 데이터를 사용해서 화면을 그리는 일에 집중한다. 여기서는 HTML을 생성하는 부분을 말한다.

### [📗 MVC 패턴 1](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20MVC%20%ED%8C%A8%ED%84%B4%201-1)

![](https://blog.kakaocdn.net/dn/bVGowR/btsivOPYMcs/7PKsEzPK7qdHePawp6taJ1/img.png)

컨트롤러에 비즈니스 로직을 둘 수도 있지만, 이렇게 되면 컨트롤러가 너무 많은 역할을 담당한다. 그래서 일반적으로 비즈니스 로직은 서비스(Service)라는 계층을 별도로 만들어서 처리한다. 그리고 컨트롤러는 비즈니스 로직이 있는 서비스를 호출하는 역할만 담당한다. 

참고로 비즈니스 로직을 변경하면 비즈니스 로직을 호출하는 컨트롤러의 코드도 변경될 수 있다. 앞에서는 이해를 돕기 위해 비즈니스 로직을 호출한다는 표현보다는, 비즈니스 로직이라 설명했다.

### [📗 MVC 패턴 2](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0MVC%20%ED%8C%A8%ED%84%B4%202-1)

![](https://blog.kakaocdn.net/dn/RhfgN/btsiBKGbNyV/rTgv9akU7MTCJXKicL1d9k/img.png)

1. 클라이언트가 서버에 요청을 보내고 컨트롤러를 호출한다.
2. 컨트롤러는 클라이언트의 요청을 검증하고 서비스나 리포지토리에 접근한다. 서비스나 리포지토리는 비즈니스 로직을 실행한다.
3. 컨트롤러는 서비스나 리포지토리에서 얻은 결과를 모델에 전달한다.
4. 컨트롤러는 뷰 로직을 호출한다.
5. 뷰 로직은 모델의 데이터를 참조하여 응답을 생성한다.
6. 클라이언트가 서버로부터 응답을 받는다.

## [📕 MVC 패턴 적용](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%95%20MVC%20%ED%8C%A8%ED%84%B4%20%EC%A0%81%EC%9A%A9-1)

> **서블릿을 컨트롤러로 사용하고, JSP를 뷰로 사용해서 MVC 패턴을 적용  
> Model은 HttpServletRequest 객체를 사용한다.   
> request는 내부에 데이터 저장소를 가지고 있는데  
> request.setAttribute() , request.getAttribute() 를 사용하면 데이터를 보관하고, 조회할 수 있다.**

### [📗 회원 등록](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%20%ED%9A%8C%EC%9B%90%20%EB%93%B1%EB%A1%9D-1)

#### **[MvcMemberFormServlet] - 컨트롤러**

```java
package hello.servlet.web.servletmvc;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "mvcMemberFormServlet", urlPatterns = "/servlet-mvc/members/
new-form")
public class MvcMemberFormServlet extends HttpServlet {
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        String viewPath = "/WEB-INF/views/new-form.jsp";
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

**dispatcher.forward()** : 다른 서블릿이나 JSP로 이동할 수 있는 기능이다. 서버 내부에서 다시 호출이 발생한다.  
  

/WEB-INF 이 경로안에 JSP가 있으면 외부에서 직접 JSP를 호출할 수 없다. 우리가 기대하는 것은 항상 컨트롤러를 통해서 JSP를 호출하는 것이다.  
  
redirect vs. forward 리다이렉트는 실제 클라이언트(웹 브라우저)에 응답이 나갔다가, 클라이언트가 redirect 경로로 다시 요청한다. 따라서 클라이언트가 인지할 수 있고, URL 경로도 실제로 변경된다. 반면에 포워드는 서버 내부에서 일어나는 호출이기 때문에 클라이언트가 전혀 인지하지 못한다.

#### **[new-form.jsp] - 뷰**

```xml
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
    
<!-- 상대경로 사용, [현재 URL이 속한 계층 경로 + /save] -->
<form action="save" method="post">
	username: <input type="text" name="username" />
	age: <input type="text" name="age" />
	<button type="submit">전송</button>
</form>
    
</body>
</html>
```

여기서 form의 action을 보면 절대 경로(로 시작)이 아니라 상대경로(로 시작X)하는 것을 확인할 수 있다. 

이렇게 상대경로를 사용하면 폼 전송시 현재 URL이 속한 계층 경로 + save가 호출된다.

### [📗 회원 저장](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%ED%9A%8C%EC%9B%90%20%EC%A0%80%EC%9E%A5-1)

#### **[MvcMemberSaveServlet] - 컨트롤러**

```java
package hello.servlet.web.servletmvc;
import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(name = "mvcMemberSaveServlet", urlPatterns = "/servlet-mvc/members/
save")
public class MvcMemberSaveServlet extends HttpServlet {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        String username = request.getParameter("username");
        int age = Integer.parseInt(request.getParameter("age"));
        Member member = new Member(username, age);
        System.out.println("member = " + member);
        memberRepository.save(member);
        
        //Model에 데이터를 보관한다.
        request.setAttribute("member", member);
        
        String viewPath = "/WEB-INF/views/save-result.jsp";
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

- HttpServletRequest를 Model로 사용한다.
- request가 제공하는 setAttribute() 를 사용하면 request 객체에 데이터를 보관해서 뷰에 전달할 수 있다.
- 뷰는 request.getAttribute() 를 사용해서 데이터를 꺼내면 된다.

#### **[save-result.jsp] - 뷰**

```xml
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
	<meta charset="UTF-8">
</head>
<body>
성공
<ul>
    <li>id=${member.id}</li>
    <li>username=${member.username}</li>
    <li>age=${member.age}</li>
</ul>
<a href="/index.html">메인</a>
</body>
</html>
```

- <%= request.getAttribute("member")%> 로 모델에 저장한 member 객체를 꺼낼 수 있지만, 너무 복잡해진다.
- JSP는 **${} 문법**을 제공하는데, 이 문법을 사용하면 request의 attribute에 담긴 데이터를 편리하게 조회할 수 있다.

### [📗 회원 목록](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%97%C2%A0%ED%9A%8C%EC%9B%90%20%EB%AA%A9%EB%A1%9D-1)

#### **[MvcMemberListServlet] - 컨트롤러**

```java
package hello.servlet.web.servletmvc;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet(name = "mvcMemberListServlet", urlPatterns = "/servlet-mvc/
members")
public class MvcMemberListServlet extends HttpServlet {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("MvcMemberListServlet.service");
        List<Member> members = memberRepository.findAll();
        
        request.setAttribute("members", members);
        
        String viewPath = "/WEB-INF/views/members.jsp";
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

#### **[members.jsp] - 뷰**

```xml
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<a href="/index.html">메인</a>
<table>
    <thead>
    <th>id</th>
    <th>username</th>
    <th>age</th>
    </thead>
    <tbody>
    <c:forEach var="item" items="${members}">
        <tr>
            <td>${item.id}</td>
            <td>${item.username}</td>
            <td>${item.age}</td>
        </tr>
    </c:forEach>
    </tbody>
</table>
    
</body>
</html>
```

**jstl** : Java 코드를 바로 사용하지 않고 HTML 태그(<>) 형태로 직관적인 코딩을 지원하는 라이브러리

<%@ taglib prefix="c" uri="[http://java.sun.com/jsp/jstl/core](http://java.sun.com/jsp/jstl/core)"%>

## [📕 MVC 패턴의 한계](https://repeater2487.tistory.com/116?category=1116968#%F0%9F%93%95%20MVC%20%ED%8C%A8%ED%84%B4%EC%9D%98%20%ED%95%9C%EA%B3%84-1)

#### **포워드 중복**

View로 이동하는 코드가 항상 중복 호출되어야 한다. 물론 이 부분을 메서드로 공통화해도 되지만 해당 메서드도 항상 직접 호출해야 한다.

```java
RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
dispatcher.forward(request, response);
```

#### **ViewPath에 중복**

String viewPath = "/WEB-INF/views/new-form.jsp";

prefix: /WEB-INF/views/ suffix: .jsp 만약 jsp가 아닌 thymeleaf 같은 다른 뷰로 변경한다면 전체 코드를 다 변경해야 한다.

#### **사용하지 않는 코드**

다음 코드를 사용할 때도 있고, 사용하지 않을 때도 있다. 특히 response는 현재 코드에서 사용되지 않는다.

그리고 이런 HttpServletRequest , HttpServletResponse 를 사용하는 코드는 테스트 케이스를 작성하기도 어렵다.  
  

#### **공통 처리가 어렵다**

기능이 복잡해질수록 컨트롤러에서 공통으로 처리해야 하는 부분이 점점 더 많이 증가할 것이다. 단순히 공통 기능을 메서드로 뽑으면 될 것 같지만, 결과적으로 해당 메서드를 항상 호출해야 하고, 실수로 호출하지 않으면 문제가 될 것이다. 그리고 호출하는 것 자체도 중복이다.

> **이 문제를 해결하려면 컨트롤러 호출 전에 먼저 공통 기능을 처리해야 한다. 소위 수문장 역할을 하는 기능이 필요하다. 프론트 컨트롤러(Front Controller) 패턴을 도입하면 이런 문제를 깔끔하게 해결할 수 있다. (입구를 하나로!) 스프링 MVC의 핵심도 바로 이 프론트 컨트롤러에 있다.**