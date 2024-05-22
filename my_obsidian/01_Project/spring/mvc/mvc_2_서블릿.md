## [📕 프로젝트 생성](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%95%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%EC%83%9D%EC%84%B1-1)

### [📗 프로젝트 환경](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20%ED%99%98%EA%B2%BD-1)

- Project : Gradle
- Language : Java
- Spring Boot : 2.7.12
- Packaging : War
- Java : 11
- Dependencies : Spring Web, Lombok
  - **Spring Web**  
     Build web, including RESTful, applications using Spring MVC. Uses Apache Tomcat as the default embedded container. **-> 톰캣 서버를 내장하여 별도의 서버 없이 웹 어플리케이션 실행 가능**
  - **Lombok**  
     Java annotation library which helps to reduce boilerplate code.   
     -> Boilerplate code란 getter, setter와 같이 **여러 곳에서 꼭 필요한 기능으로 반복적으로 사용되는 코드**로  
     Lombok을 사용하면 annotation을 사용하여 getter와 setter를 작성하지 않아도 사용할 수 있다.

### [📗 Jar vs War](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20Jar%20vs%20War-1)

Jar와 War 모두 자바 클래스 패키징 확장자로 프로젝트를 배포할 때 사용  
Jar는 JDK(Java Development Kit)에 포함된 JRE(Java Runtime Environment)만 있으면 실행 가능  
War는 웹 어플리케이션 전용 패키징으로 WEB-INF, META-INF로 사전 정의된 구조를 사용하여 War를 실행하기 위해서는 웹 서버 또는 WAS가 필요함

**[build.gradle]**

```java
plugins {
	id 'java'
	id 'war'
	id 'org.springframework.boot' version '2.7.12'
	id 'io.spring.dependency-management' version '1.0.15.RELEASE'
}

group = 'hello'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '11'

configurations {
	compileOnly {
		extendsFrom annotationProcessor
	}
}

repositories {
	mavenCentral()
}

dependencies {
	implementation 'org.springframework.boot:spring-boot-starter-web'
	compileOnly 'org.projectlombok:lombok'
	annotationProcessor 'org.projectlombok:lombok'
	providedRuntime 'org.springframework.boot:spring-boot-starter-tomcat'
	testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

tasks.named('test') {
	useJUnitPlatform()
}
```

## [📕 Hello 서블릿](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%95%20Hello%20%EC%84%9C%EB%B8%94%EB%A6%BF-1)

### [📗 스프링 부트 서블릿 환경 구성](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%EC%8A%A4%ED%94%84%EB%A7%81%20%EB%B6%80%ED%8A%B8%20%EC%84%9C%EB%B8%94%EB%A6%BF%20%ED%99%98%EA%B2%BD%20%EA%B5%AC%EC%84%B1-1)

**@ServletComponentScan** : 스프링 부트는 서블릿을 직접 등록해서 사용할 수 있음

**[hello.servlet.ServletApplication]**

```java
package hello.servlet;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@ServletComponentScan //서블릿 자동 등록
@SpringBootApplication
public class ServletApplication {

	public static void main(String[] args) {
		SpringApplication.run(ServletApplication.class, args);
	}

}
```

### [📗 서블릿 등록하기](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B8%94%EB%A6%BF%20%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0-1)

실제 동작하는 서블릿 코드

**[hello.servlet.basic.HelloServlet]**

```java
package hello.servlet.basic;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/*
@WebServlet 서블릿 애노테이션
  name: 서블릿 이름
  urlPatterns: URL 매핑
*/
@WebServlet(name = "helloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {

    // 서블릿이 호출되면 service 메소드가 실행됨
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        System.out.println("HelloServlet.service");
        System.out.println("request = " + request);
        System.out.println("response = " + response);

        String username = request.getParameter("username");
        System.out.println("username = " + username);

        response.setContentType("text/plain");
        response.setCharacterEncoding("utf-8");
        response.getWriter().write("hello " + username);

    }
}
```

**@WebServlet** : 서블릿 annotation

- name : 서블릿 이름
- urlPatterns : URL 매핑

HTTP 요청을 통해 매핑된 URL이 호출되면 서블릿 컨테이너는 다음 메서드를 실행한다.

protected void service(HttpServletRequest request, HttpServletResponse response)

**콘솔 실행결과**

```shell
HelloServlet.service
request = org.apache.catalina.connector.RequestFacade@5e4e72
response = org.apache.catalina.connector.ResponseFacade@37d112b6
username = world
```

### [📗 서블릿 컨테이너 동작 방식 설명](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B8%94%EB%A6%BF%20%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88%20%EB%8F%99%EC%9E%91%20%EB%B0%A9%EC%8B%9D%20%EC%84%A4%EB%AA%85-1)

#### **내장 톰캣 서버 생성**

![](https://blog.kakaocdn.net/dn/M2KQA/btsivgZjICR/KCBP3ZQTMDFJFVMXzKyiX0/img.png)

1. 스프링 부트는 내장 톰캣 서버를 실행한다.
2. 내장 톰캣 서버는 서블릿 컨테이너에서 helloServlet을 생성한다.

#### **HTTP 요청, HTTP 응답 메시지**

![](https://blog.kakaocdn.net/dn/B3Tat/btsiFNBJ2Gh/VkGyuKHRm5oZKKXum76P5K/img.png)

웹 브라우저는 다음과 같은 요청 메시지를 웹 애플리케이션 서버에 전송한다.

#### **웹 애플리케이션 서버의 요청 응답 구조**

![](https://blog.kakaocdn.net/dn/ZBcEq/btsivRLMZPY/PSLSMl1z9Hnh0mS3VQ1jjK/img.png)

1. 웹 애플리케이션 서버는 HTTP 요청 메시지를 기반으로 request, response 객체를 만들고 helloServlet을 실행한다.
2. helloServlet에서는 response 객체를 변경한다.
3. 웹 애플리케이션 서버는 변경된 response 객체 정보로 HTTP 응답을 생성하여 웹 브라우저에 전송한다.

## [📕 HttpServletRequest](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%95%20%08HttpServletRequest-1)

### [📗 HttpServletRequest - 개요](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HttpServletRequest%20-%20%EA%B0%9C%EC%9A%94-1)

#### **HttpServletRequest 역할**

HTTP 요청 메시지를 개발자가 직접 파싱해서 사용해도 되지만, 매우 불편할 것이다.

서블릿은 개발자가 HTTP 요청 메시지를 편리하게 사용할 수 있도록 개발자 대신에 HTTP 요청 메시지를 파싱한다.

그리고 그 결과를 **HttpServletRequest** 객체에 담아서 제공한다.

#### **HTTP 요청 메시지**

```shell
POST /save HTTP/1.1
Host: localhost:8080
Content-Type: application/x-www-form-urlencoded
username=minhyeok&age=29
```

- START LINE (POST)
  - HTTP 메소드
  - URL
  - 쿼리 스트링
  - 스키마, 프로토콜
- 헤더 (Host, Content-Type)
  - 헤더 조회
- 바디 (username=minhyeok&age=29)
  - form 파라미터 형식 조회
  - message body 데이터 직접 조회

**HttpServletRequest** 객체는 여러 가지 부가기능도 함께 제공한다.

#### **임시 저장소 기능**

해당 HTTP 요청이 시작부터 끝날 때까지 유지되는 임시 저장소 기능

- 저장 : request.setAttribute(name, value)
- 조회 : request.getAttribute(name)

#### **세션 관리 기능**

request.getSession(create: true)

### [📗 HttpServletRequest - 기본 사용법](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HttpServletRequest%20-%20%EA%B8%B0%EB%B3%B8%20%EC%82%AC%EC%9A%A9%EB%B2%95-1)

**[RequestHeaderServlet]  
**

```java
package hello.servlet.basic.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import java.io.IOException;

//http://localhost:8080/request-header?username=hello
@WebServlet(name = "requestHeaderServlet", urlPatterns = "/request-header")
public class RequestHeaderServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response)
    throws ServletException, IOException {

        printStartLine(request);
        printHeaders(request);
        printHeaderUtils(request);
        printEtc(request);

        response.getWriter().write("ok");
    }
}
```

**[start-line 정보]**

```java
//start line 정보
private void printStartLine(HttpServletRequest request) {
    System.out.println("--- REQUEST-LINE - start ---");

    System.out.println("request.getMethod() = " + request.getMethod()); //GET
    System.out.println("request.getProtocal() = " + request.getProtocol()); //HTTP/1.1
    System.out.println("request.getScheme() = " + request.getScheme()); //http
    // http://localhost:8080/request-header
    System.out.println("request.getRequestURL() = " + request.getRequestURL());
    // /request-test
    System.out.println("request.getRequestURI() = " + request.getRequestURI());
    //username=hi
    System.out.println("request.getQueryString() = " + request.getQueryString());
    System.out.println("request.isSecure() = " + request.isSecure()); //https 사용 유무
    System.out.println("--- REQUEST-LINE - end ---");
    System.out.println();
}
```

**결과**

```shell
--- REQUEST-LINE - start ---
request.getMethod() = GET
request.getProtocal() = HTTP/1.1
request.getScheme() = http
request.getRequestURL() = http://localhost:8080/request-header
request.getRequestURI() = /request-header
request.getQueryString() = username=hello
request.isSecure() = false
--- REQUEST-LINE - end ---
```

**[헤더 정보]**

```java
//Header 모든 정보
private void printHeaders(HttpServletRequest request) {
    System.out.println("--- Headers - start ---");

/*  예전방식
    Enumeration<String> headerNames = request.getHeaderNames();
    while (headerNames.hasMoreElements()) {
    String headerName = headerNames.nextElement();
    System.out.println(headerName + ": " + request.getHeader(headerName));
    }
*/

    request.getHeaderNames().asIterator().forEachRemaining(headerName -> System.out.println(headerName + ":" + request.getHeader(headerName)));
    System.out.println("--- Headers - end ---");
    System.out.println();
}
```

**결과**

```shell
--- Headers - start ---
host: localhost:8080
connection: keep-alive
cache-control: max-age=0
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36
(KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/
webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
sec-fetch-site: none
sec-fetch-mode: navigate
sec-fetch-user: ?1
sec-fetch-dest: document
accept-encoding: gzip, deflate, br
accept-language: ko,en-US;q=0.9,en;q=0.8,ko-KR;q=0.7
--- Headers - end ---
```

**[Header 편리한 조회]**

```java
//Header 편리한 조회
private void printHeaderUtils(HttpServletRequest request) {
    System.out.println("--- Header 편의 조회 start ---");
    System.out.println("[Host 편의 조회]");
    System.out.println("request.getServerName() = " + request.getServerName()); //Host 헤더
    System.out.println("request.getServerPort() = " + request.getServerPort()); //Host 헤더
    System.out.println();

    System.out.println("[Accept-Language 편의 조회]");
    request.getLocales().asIterator()
    .forEachRemaining(locale -> System.out.println("locale = " + locale));
    System.out.println("request.getLocale() = " + request.getLocale());
    System.out.println();

    System.out.println("[cookie 편의 조회]");
    if (request.getCookies() != null) {
    	for (Cookie cookie : request.getCookies()) {
		    System.out.println(cookie.getName() + ": " + cookie.getValue());
	    }
    }
    System.out.println();
    System.out.println("[Content 편의 조회]");
    System.out.println("request.getContentType() = " + request.getContentType());
    System.out.println("request.getContentLength() = " + request.getContentLength());
    System.out.println("request.getCharacterEncoding() = " + request.getCharacterEncoding());
    System.out.println("--- Header 편의 조회 end ---");
    System.out.println();
}
```

**결과**

```shell
--- Header 편의 조회 start ---
[Host 편의 조회]
request.getServerName() = localhost
request.getServerPort() = 8080
[Accept-Language 편의 조회]
locale = ko
locale = en_US
locale = en
locale = ko_KR
request.getLocale() = ko
[cookie 편의 조회]
[Content 편의 조회]
request.getContentType() = null
request.getContentLength() = -1
request.getCharacterEncoding() = UTF-8
--- Header 편의 조회 end ---
```

**[기타 정보] - HTTP 메시지의 정보는 아님**

```java
//기타 정보
private void printEtc(HttpServletRequest request) {
    System.out.println("--- 기타 조회 start ---");
    System.out.println("[Remote 정보]");
    System.out.println("request.getRemoteHost() = " + request.getRemoteHost()); //
    System.out.println("request.getRemoteAddr() = " + request.getRemoteAddr()); //
    System.out.println("request.getRemotePort() = " + request.getRemotePort()); //
    System.out.println();

    System.out.println("[Local 정보]");
    System.out.println("request.getLocalName() = " + request.getLocalName()); //
    System.out.println("request.getLocalAddr() = " + request.getLocalAddr()); //
    System.out.println("request.getLocalPort() = " + request.getLocalPort()); //\

    System.out.println("--- 기타 조회 end ---");
    System.out.println();
}
```

**결과**

```shell
--- 기타 조회 start ---
[Remote 정보]
request.getRemoteHost() = 0:0:0:0:0:0:0:1
request.getRemoteAddr() = 0:0:0:0:0:0:0:1
request.getRemotePort() = 54305
[Local 정보]
request.getLocalName() = localhost
request.getLocalAddr() = 0:0:0:0:0:0:0:1
request.getLocalPort() = 8080
--- 기타 조회 end ---
```

> > 로컬에서 테스트하면 IPv6 정보가 나오는데, IPv4 정보를 보고 싶으면 다음 옵션을 VM options에 넣어주면 된다.

-Djava.net.preferIPv4Stack=true

## [📕 HTTP 요청 데이터](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%95%20%08HTTP%20%EC%9A%94%EC%B2%AD%20%EB%8D%B0%EC%9D%B4%ED%84%B0-1)

### [📗 HTTP 요청 데이터 - 개요](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HTTP%20%EC%9A%94%EC%B2%AD%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20%EA%B0%9C%EC%9A%94-1)

> **HTTP 요청 메시지를 통하여 클라이언트에서 서버로 데이터를 전달하는 방법**

- **GET** - 쿼리 파라미터 : /url?username=hello&age=20
  - 메시지 바디 없이 URL의 쿼리 파라미터에 데이터를 포함해서 전달
  - 검색, 필터, 페이징 등에서 많이 사용하는 방식
- **POST** - HTML Form : content-type:application/x-www-form-urlencoded
  - 메시지 바디에 쿼리 파라미터 형식으로 전달
  - 회원 가입, 상품 주문, HTML Form 사용
- **HTTP message body**에 데이터를 직접 담아서 요청
  - HTTP API에서 주로 사용, JSON, XML, TEXT
- 데이터 형식은 주로 JSON 사용
  - POST, PUT, PATCH

### [📗 HTTP 요청 데이터 - GET 쿼리 파라미터](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HTTP%20%EC%9A%94%EC%B2%AD%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20GET%20%EC%BF%BC%EB%A6%AC%20%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-1)

서버에서는 HttpServletRequest 가 제공하는 다음 메서드를 통해 쿼리 파라미터를 편리하게 조회할 수 있다.

```java
String username = request.getParameter("username"); //단일 파라미터 조회
Enumeration<String> parameterNames = request.getParameterNames(); //파라미터 이름들 모두 조회
Map<String, String[]> parameterMap = request.getParameterMap(); //파라미터를 Map 으로 조회
String[] usernames = request.getParameterValues("username"); //복수 파라미터 조회
```

**[RequestParamServlet]**

```java
package hello.servlet.basic.request;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Enumeration;

/**
* 1. 파라미터 전송 기능
* http://localhost:8080/request-param?username=hello&age=20
* <p>
* 2. 동일한 파라미터 전송 가능
* http://localhost:8080/request-param?username=hello&username=kim&age=20
*/
@WebServlet(name = "requestParamServlet", urlPatterns = "/request-param")
public class RequestParamServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    resp) throws ServletException, IOException {

        System.out.println("[전체 파라미터 조회] - start");

        /*
        Enumeration<String> parameterNames = request.getParameterNames();
        while (parameterNames.hasMoreElements()) {
        String paramName = parameterNames.nextElement();
        System.out.println(paramName + "=" +
        request.getParameter(paramName));
        }
        */

        request.getParameterNames().asIterator()
        .forEachRemaining(paramName -> System.out.println(paramName +
        "=" + request.getParameter(paramName)));
        System.out.println("[전체 파라미터 조회] - end");
        System.out.println();

        System.out.println("[단일 파라미터 조회]");
        String username = request.getParameter("username");
        System.out.println("request.getParameter(username) = " + username);

        String age = request.getParameter("age");
        System.out.println("request.getParameter(age) = " + age);
        System.out.println();

        System.out.println("[이름이 같은 복수 파라미터 조회]");
        System.out.println("request.getParameterValues(username)");
        String[] usernames = request.getParameterValues("username");
        for (String name : usernames) {
	        System.out.println("username=" + name);
        }

	    resp.getWriter().write("ok");
    }
}
```

**결과**

```shell
[전체 파라미터 조회] - start
username=hello
age=20
[전체 파라미터 조회] - end

[단일 파라미터 조회]
request.getParameter(username) = hello
request.getParameter(age) = 20

[이름이 같은 복수 파라미터 조회]
request.getParameterValues(username)
username=hello
username=kim
```

### [📗 HTTP 요청 데이터 -  POST HTML Form](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HTTP%20%EC%9A%94%EC%B2%AD%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20%08%20POST%20HTML%20Form-1)

쿼리 파라미터 조회 메서드를 그대로 사용  
클라이언트(웹 브라우저) 입장에서는 두 방식에 차이가 있지만 서버 입장에서는 동일하므로

request.getParameter()로 편리하게 구분없이 조회 가능

> **참고**  
> content-type은 HTTP 메시지 바디의 데이터 형식을 지정한다. GET URL 쿼리 파라미터 형식으로 클라이언트에서 서버로 데이터를 전달할 때는 HTTP 메시지 바디를 사용하지 않기 때문에 content-type이 없다. POST HTML Form 형식으로 데이터를 전달하면 HTTP 메시지 바디에 해당 데이터를 포함해서 보내기 때문에 바디에 포함된 데이터가 어떤 형식인지 content-type을 꼭 지정해야 한다. 이렇게 폼으로 데이터를 전송하는 형식을 **application/x-www-form-urlencoded** 라 한다.

**[hello-form.html]**

```xml
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/request-param" method="post">
    username: <input type="text" name="username" />
    age: <input type="text" name="age" />
    <button type="submit">전송</button>
</form>
</body>
</html>
```

### [📗 HTTP 요청 데이터 -  API 메시지 바디](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HTTP%20%EC%9A%94%EC%B2%AD%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20%08%20API%20%EB%A9%94%EC%8B%9C%EC%A7%80%20%EB%B0%94%EB%94%94-1)

#### **단순 텍스트**

HTTP message body에 데이터를 직접 담아서 요청

- HTTP API에서 주로 사용 JSON, XML, TEXT
- 데이터 형식은 주로 JSON 사용
- POST, PUT, PATCH

**[RequestBodyStringServlet]**

```java
package hello.servlet.basic.request;

import org.springframework.util.StreamUtils;
import javax.servlet.ServletException;
import javax.servlet.ServletInputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

@WebServlet(name = "requestBodyStringServlet", urlPatterns = "/request-bodystring")
public class RequestBodyStringServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response)
    throws ServletException, IOException {

        ServletInputStream inputStream = request.getInputStream();
        String messageBody = StreamUtils.copyToString(inputStream,
        StandardCharsets.UTF_8);

        System.out.println("messageBody = " + messageBody);
        response.getWriter().write("ok");
    }
}
```

> > inputStream은 byte 코드를 반환한다. byte 코드를 우리가 읽을 수 있는 문자(String)로 보려면 문자표 (Charset)를 지정해주어야 한다. 여기서는 UTF_8 Charset을 지정해주었다.

#### **JSON**

**[HelloData] - JSON 형식으로 파싱할 수 있는 객체**

```java
package hello.servlet.basic;

import lombok.Getter;
import lombok.Setter;

@Getter @Setter
public class HelloData {
    private String username;
    private int age;
}
```

**[RequestBodyJsonServlet]**

```java
package hello.servlet.basic.request;

import com.fasterxml.jackson.databind.ObjectMapper;
import hello.servlet.basic.HelloData;
import org.springframework.util.StreamUtils;
import javax.servlet.ServletException;
import javax.servlet.ServletInputStream;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.nio.charset.StandardCharsets;

/**
* http://localhost:8080/request-body-json
*
* JSON 형식 전송
* content-type: application/json
* message body: {"username": "hello", "age": 20}
*
*/
@WebServlet(name = "requestBodyJsonServlet", urlPatterns = "/request-bodyjson")
public class RequestBodyJsonServlet extends HttpServlet {

	private ObjectMapper objectMapper = new ObjectMapper();

    @Override
	protected void service(HttpServletRequest request, HttpServletResponse response)
		throws ServletException, IOException {

        ServletInputStream inputStream = request.getInputStream();
        String messageBody = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);

        System.out.println("messageBody = " + messageBody);

        HelloData helloData = objectMapper.readValue(messageBody, HelloData.class);
        System.out.println("helloData.username = " + helloData.getUsername());
        System.out.println("helloData.age = " + helloData.getAge());

        response.getWriter().write("ok");
    }
}
```

**결과**

```shell
messageBody={"username": "hello", "age": 20}
data.username=hello
data.age=20
```

> 참고  
> JSON 결과를 파싱해서 사용할 수 있는 자바 객체로 변환하려면 Jackson, Gson 같은 JSON 변환 라이브러리를 추가해서 사용해야 한다. 스프링 부트로 Spring MVC를 선택하면 기본으로 Jackson 라이브러리( ObjectMapper )를 함께 제공한다. HTML form 데이터도 메시지 바디를 통해 전송되므로 직접 읽을 수 있다. 하지만 편리한 파리미터 조회 기능( request.getParameter(…) )을 이미 제공하기 때문에 파라미터 조회 기능을 사용하면 된다.

## [📕 HttpServletResponse](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%95%20%08HttpServletResponse-1)

### [📗 HttpServletResponse - 역할](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HttpServletResponse%20-%20%EC%97%AD%ED%95%A0-1)

HTTP 응답 메시지 생성

- HTTP 응답코드 지정
- 헤더 생성
- 바디 생성

편의 기능 제공 : Content-Type, 쿠키, Redirect

### [📗 HttpServletResponse - 기본 사용법](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20HttpServletResponse%20-%20%EA%B8%B0%EB%B3%B8%20%EC%82%AC%EC%9A%A9%EB%B2%95-1)

**[ResponseHeaderServlet]**

```java
package hello.servlet.basic.response;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

/**
* http://localhost:8080/response-header
*
*/
@WebServlet(name = "responseHeaderServlet", urlPatterns = "/response-header")
public class ResponseHeaderServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {

        //[status-line]
        response.setStatus(HttpServletResponse.SC_OK); //200

        //[response-headers]
        response.setHeader("Content-Type", "text/plain;charset=utf-8");
        response.setHeader("Cache-Control", "no-cache, no-store, mustrevalidate");
        response.setHeader("Pragma", "no-cache");
        response.setHeader("my-header","hello");

        //[Header 편의 메서드]
        content(response);
        cookie(response);
        redirect(response);

        //[message body]
        PrintWriter writer = response.getWriter();
        writer.println("ok");

    }
}
```

**[Content 편의 메서드]**

```java
private void content(HttpServletResponse response) {
    //Content-Type: text/plain;charset=utf-8
    //Content-Length: 2
    //response.setHeader("Content-Type", "text/plain;charset=utf-8");
    response.setContentType("text/plain");
    response.setCharacterEncoding("utf-8");
    //response.setContentLength(2); //(생략시 자동 생성)
}
```

**[쿠키 편의 메서드]**

```java
private void cookie(HttpServletResponse response) {
    //Set-Cookie: myCookie=good; Max-Age=600;
    //response.setHeader("Set-Cookie", "myCookie=good; Max-Age=600");

    Cookie cookie = new Cookie("myCookie", "good");
    cookie.setMaxAge(600); //600초
    response.addCookie(cookie);
}
```

**[redirect 편의 메서드]**

```java
private void redirect(HttpServletResponse response) throws IOException {
    //Status Code 302
    //Location: /basic/hello-form.html

    //response.setStatus(HttpServletResponse.SC_FOUND); //302
    //response.setHeader("Location", "/basic/hello-form.html");
    response.sendRedirect("/basic/hello-form.html");
}
```

## [📕 HTTP 응답 데이터](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%95%20%08HTTP%20%EC%9D%91%EB%8B%B5%20%EB%8D%B0%EC%9D%B4%ED%84%B0-1)

### [📗 HTTP 응답 데이터 - 단순 텍스트](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%08HTTP%20%EC%9D%91%EB%8B%B5%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20%EB%8B%A8%EC%88%9C%20%ED%85%8D%EC%8A%A4%ED%8A%B8-1)

writer.println("ok");

### [📗 HTTP 응답 데이터 - HTML](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%08HTTP%20%EC%9D%91%EB%8B%B5%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20%08HTML-1)

**[ResponseHtmlServlet]**

```java
package hello.servlet.basic.response;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "responseHtmlServlet", urlPatterns = "/response-html")
public class ResponseHtmlServlet extends HttpServlet {

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {

        //Content-Type: text/html;charset=utf-8
        response.setContentType("text/html");
        response.setCharacterEncoding("utf-8");

        PrintWriter writer = response.getWriter();
        writer.println("<html>");
        writer.println("<body>");
        writer.println(" <div>안녕?</div>");
        writer.println("</body>");
        writer.println("</html>");
    }
}
```

HTTP 응답으로 HTML을 반환할 때는 content-type을 text/html로 지정해야 한다.

### [📗 HTTP 응답 데이터 - API JSON](https://repeater2487.tistory.com/115?category=1116968#%F0%9F%93%97%20%08HTTP%20%EC%9D%91%EB%8B%B5%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20-%20%08API%20JSON-1)

**[ResponseJsonServlet]**

```java
package hello.servlet.basic.response;

import com.fasterxml.jackson.databind.ObjectMapper;
import hello.servlet.basic.HelloData;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
* http://localhost:8080/response-json
*
*/
@WebServlet(name = "responseJsonServlet", urlPatterns = "/response-json")
public class ResponseJsonServlet extends HttpServlet {

	private ObjectMapper objectMapper = new ObjectMapper();

    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {

        //Content-Type: application/json
        response.setHeader("content-type", "application/json");
        response.setCharacterEncoding("utf-8");

        HelloData data = new HelloData();
        data.setUsername("kim");
        data.setAge(20);

        //{"username":"kim","age":20}
        String result = objectMapper.writeValueAsString(data);
        response.getWriter().write(result);
    }
}
```

- HTTP 응답으로 JSON을 반환할 때는 content-type을 application/json 로 지정해야 한다.
- Jackson 라이브러리가 제공하는 objectMapper.writeValueAsString() 를 사용하면 객체를 JSON 문자로 변경할 수 있다.
