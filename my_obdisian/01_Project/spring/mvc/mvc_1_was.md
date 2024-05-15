---
modified: 2023-12-31T08:26:07+09:00
---

## [📕 웹 서버, 웹 애플리케이션 서버](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%95%20%EC%9B%B9%20%EC%84%9C%EB%B2%84%2C%20%EC%9B%B9%20%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%20%EC%84%9C%EB%B2%84-1)

### [📗 웹 - HTTP 기반](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%9B%B9%20-%20HTTP%20%EA%B8%B0%EB%B0%98-1)

- HTTP 메시지로 HTML, TEXT, 이미지, 음성, 영상, JSON, XML 등등 모든 형태의 데이터를 전송할 수 있다.

### [📗 웹 서버(Web Server)](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%9B%B9%20%EC%84%9C%EB%B2%84(Web%20Server)-1)

- HTTP 기반으로 동작하고 정적 리소스를 제공하며 기타 부가 기능을 가진다.
- 정적 리소스: HTML, CSS, JS, 이미지, 영상
- ex. Nginx, Apache

### [📗 웹 애플리케이션 서버(WAS - Web Application Server)](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%9B%B9%20%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98%20%EC%84%9C%EB%B2%84(WAS%20-%20Web%20Application%20Server)-1)

- HTTP 기반으로 동작하고 웹 서버의 기능을 포함한다.
- 프로그램 코드를 실행하여 애플리케이션 로직을 수행한다.
    - 동적 HTML, HTTP API(JSON)
    - 서블릿, JSP, 스프링 MVC
- ex. Tomcat, Jetty, Undertow

### [📗 Web Server vs WAS](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20Web%20Server%20vs%20WAS-1)

- 웹 서버는 정적 리소스(파일), WAS는 애플리케이션 로직으로 일반적으로 분류하지만 사실 둘의 용어도 경계도 모호하다.
- Java의 경우 서블릿 컨테이너 기능을 제공하면 WAS라고 한다.
- WAS는 애플리케이션 코드를 실행하는 데에 특화되어 있다.

### [📗 웹 시스템 구성](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%9B%B9%20%EC%8B%9C%EC%8A%A4%ED%85%9C%20%EA%B5%AC%EC%84%B1-1)

#### **1. WAS, DB**

![](https://blog.kakaocdn.net/dn/bNNXtT/btsius6EOIv/Kvvqn1377Xx7akoCn86K5K/img.png)

WAS와 DB만으로 시스템을 구성할 수는 있지만 다음과 같은 단점을 가지고 있다.

- WAS가 너무 많은 역할을 담당하여 서버가 과부하될 수 있다.
- 가장 비싼 애플리케이션 로직이 정적 리소스 때문에 수행하기 어려울 수 있다.
- WAS에 장애가 생기면 오류 화면도 노출되지 않는다.

#### **2. WEB, WAS, DB**

![](https://blog.kakaocdn.net/dn/bWrXc8/btsiuMDJYo2/kJbHJoicKjS6Og76LnlAX0/img.png)

위와 같은 문제점 때문에 웹 서버를 따로 두어 정적 리소스를 처리하게 한다. 애플리케이션 로직 같은 동적인 처리가 필요하면 WAS에 요청을 위임하고 WAS는 중요한 애플리케이션 로직의 처리만을 맡는다. 이러한 구조는 다음과 같은 장점을 가진다.

- 정적 리소스가 많이 사용되면 웹 서버를 증설하고, 애플리케이션 리소스가 많이 사용되면 WAS를 증설하는 등 효율적인 리소스 관리가 가능하다.
- 애플리케이션 로직이 동작하는 WAS는 잘 죽지만 정적 리소스만 제공하는 웹 서버는 잘 죽지 않기 때문에 WAS나 DB 장애시 웹 서버가 오류 화면을 제공할 수 있다.

## [📕 서블릿](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%95%20%EC%84%9C%EB%B8%94%EB%A6%BF-1)

### [📗 서블릿(Servlet) 이란?](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B8%94%EB%A6%BF(Servlet)%20%EC%9D%B4%EB%9E%80%3F-1)

> **클라이언트의 요청을 처리하고, 그 결과를 반환하는 Servlet 클래스의 구현 규칙을 지킨 자바 웹 프로그래밍 기술**

![](https://blog.kakaocdn.net/dn/bYUsjF/btsiwkNv62C/KKkbRwh2GGTTrmB3sTjwv0/img.png)

클라이언트가 웹 페이지에서 전송 버튼을 누를 경우 위와 같이 웹 브라우저가 요청 HTTP 메시지를 생성한다.

![](https://blog.kakaocdn.net/dn/bfS9aW/btsisZ4TXnc/7FqLlMi7DNpqytOFCGIbTK/img.png)

웹 애플리케이션 서버를 직접 구현할 경우 왼쪽의 로직을 전부 구현해야 하지만 서블릿을 지원하는 WAS를 사용할 경우 개발자는 의미있는 비즈니스 로직만 구현하면 된다.

### [📗 서블릿(Servlet) 특징](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B8%94%EB%A6%BF(Servlet)%20%ED%8A%B9%EC%A7%95-1)

```java
@WebServlet(name = "helloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {
	
	@Override
	protected void service(HttpServletRequest request, HttpServletResponse response) {
		//애플리케이션 로직
	}
}
```

- urlPatterns의 URL이 호출되면 서블릿 코드가 실행된다.
- HTTP 요청 정보를 편리하게 사용할 수 있는 HttpServletRequest
- HTTP 응답 정보를 편리하게 제공할 수 있는 HttpServletResponse
- 개발자는 HTTP 스펙을 매우 편리하게 사용할 수 있다. (물론 HTTP 관련 지식은 있어야 한다)

### [📗 HTTP 요청, 응답 흐름](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20HTTP%20%EC%9A%94%EC%B2%AD%2C%20%EC%9D%91%EB%8B%B5%20%ED%9D%90%EB%A6%84-1)

![](https://blog.kakaocdn.net/dn/s0BSJ/btsiu1Oc8XN/EDjdJpobOWmIobC9Z8djG0/img.png)

1. HTTP 요청시 WAS는 Request, Response 객체를 새로 만들어서 서블릿 객체 호출
2. 개발자는 Request 객체에서 HTTP 요청 정보를 편리하게 꺼내서 사용
3. 개발자는 Response 객체에 HTTP 응답 정보를 편리하게 입력
4. WAS는 Response 객체에 담겨있는 내용으로 HTTP 응답 정보를 생성

### [📗 서블릿 컨테이너](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B8%94%EB%A6%BF%20%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88-1)

- 톰캣처럼 서블릿을 지원하는 WAS를 서블릿 컨테이너라고 한다.
- 서블릿 컨테이너는 서블릿 객체를 생성, 초기화, 호출, 종료하는 생명주기를 관리한다.
- 서블릿 객체는 싱글톤으로 관리된다.
    - 고객의 요청이 올 때 마다 계속 객체를 생성하는 것은 비효율적이므로 최초 로딩 시점에 서블릿 객체를 미리 만들어두고 재활용한다. 따라서 모든 고객 요청은 동일한 서블릿 객체 인스턴스에 접근한다.
    - 공유 변수 사용 주의. ex. 로그인할 때 다른 사람의 계정에 접속
    - 서블릿 컨테이너 종료시 함께 종료
- JSP도 서블릿으로 변환 되어서 사용
- 동시 요청을 위한 멀티 쓰레드 처리를 지원한다.

## [📕 동시 요청 - 멀티 쓰레드](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%95%20%EB%8F%99%EC%8B%9C%20%EC%9A%94%EC%B2%AD%20-%20%EB%A9%80%ED%8B%B0%20%EC%93%B0%EB%A0%88%EB%93%9C-1)

### [📗 쓰레드](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%93%B0%EB%A0%88%EB%93%9C-1)

![](https://blog.kakaocdn.net/dn/uuoFH/btsiuAi0Oy3/UwE6p4ezBSlLTDA09GVIWk/img.png)

- 쓰레드는 애플리케이션 코드를 실행하는 것으로 서블릿 객체를 호출
- 자바 main 메서드를 처음 실행하면 main이라는 이름의 쓰레드가 실행됨
- 쓰레드는 한 번에 하나의 코드 라인만 실행하므로 동시 처리가 필요할 경우 쓰레드를 추가로 생성해야 함

![](https://blog.kakaocdn.net/dn/cMcbmT/btsivgLopJS/kSHinEF9aTknSkcohUKenK/img.png)

DB 작업 등으로 인하여 요청의 처리가 지연될 경우 새로운 쓰레드를 생성하는 것으로 새로운 요청을 처리할 수 있음

**요청마다 쓰레드를 생성한다면?**

**장점**

- 동시 요청을 처리할 수 있음
- 리소스(CPU, 메모리)가 허용할 때까지 처리 가능하므로 리소스 최대 활용
- 하나의 쓰레드가 지연되어도 나머지 쓰레드는 정상 동작

**단점**

- 쓰레드의 생성 비용은 매우 비싸므로 고객의 요청이 올 때마다 쓰레드를 생성하면 응답 속도가 늦어짐
- 컨텍스트 스위칭 비용이 발생
- 쓰레드 생성에 제한이 없어 고객 요청이 너무 많이 오면 서버가 죽을 수 있음

### [📗 쓰레드 풀](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%C2%A0%EC%93%B0%EB%A0%88%EB%93%9C%20%ED%92%80-1)

> **요청마다 쓰레드 생성하는 방식의 단점 보완**

![](https://blog.kakaocdn.net/dn/zONW9/btsiuKFYEE7/OSO5fXwk2RWqu6T1PW4rN0/img.png)

![](https://blog.kakaocdn.net/dn/beXhDE/btsiu02RDHs/BeCkQJY9wx70512BjHM4yK/img.png)

- **특징**
    - 필요한 쓰레드를 쓰레드 풀에 보관하고 관리
    - 쓰레드 풀에서 생성 가능한 쓰레드의 최대치를 관리. 톰캣은 최대 200개가 기본
- **사용**
    - 쓰레드가 필요할 경우 쓰레드 풀에서 이미 생성된 쓰레드를 사용
    - 사용을 종료하면 쓰레드 풀에 해당 쓰레드를 반납
    - 쓰레드가 모두 사용 중이어서 쓰레드 풀에 쓰레드가 없을 경우 거절하거나 특정 숫자만큼 대기할 수 있음
- **장점**
    - 쓰레드가 미리 생성되어 있으므로 쓰레드를 생성하고 종료하는 CPU 비용이 절약되고 응답 시간 향상
    - 생성 가능한 쓰레드의 최대치를 정하여 너무 많은 요청이 들어와도 기존 요청을 안전하게 처리 가능
- **실무 팁**
    - 최대 쓰레드 수는 WAS의 주요 튜닝 포인트
    - 너무 낮으면 서버 리소스는 여유롭지만 클라이언트는 금방 응답 지연을 겪게 됨
    - 너무 높으면 서버가 다운될 위험성이 커짐
- **쓰레드 풀의 적정 숫자**
    - 애플리케이션 로직의 복잡도, CPU, 메모리, I/O 리소스 상황에 따라 천차만별
    - 최대한 실제 서비스와 유사하게 성능 테스트를 시도하는 것이 좋음 (Apache AB, JMETER, nGrinder)

### [📗 WAS의 멀티 쓰레드 지원](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20WAS%EC%9D%98%20%EB%A9%80%ED%8B%B0%20%EC%93%B0%EB%A0%88%EB%93%9C%20%EC%A7%80%EC%9B%90-1)

- 멀티 쓰레드에 대한 부분은 WAS가 처리
- 개발자가 멀티 쓰레드 관련 코드를 고려하지 않아도 됨
- 마치 싱글 쓰레드 프로그래밍을 하듯이 편리하게 소스 코드를 개발
- 멀티 쓰레드 환경이므로 싱글톤 객체(서블릿, 스프링 빈)는 주의해서 사용

## [📕 HTML, HTTP API, CSR, SSR](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%95%20HTML%2C%C2%A0HTTP%C2%A0API%2C%C2%A0CSR%2C%C2%A0SSR-1)

### [📗 정적 리소스 (Static Resource)](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%A0%95%EC%A0%81%C2%A0%EB%A6%AC%EC%86%8C%EC%8A%A4%C2%A0(Static%C2%A0Resource)-1)

고정된 HTML 파일, CSS, JS, 이미지, 영상 등을 주로 웹 브라우저로 제공

![](https://blog.kakaocdn.net/dn/nVTcl/btsiFONLnDh/kl06rM7To3kRVTMbKpkPWK/img.png)

### [📗 HTML 페이지](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20HTML%C2%A0%ED%8E%98%EC%9D%B4%EC%A7%80-1)

동적으로 필요한 HTML 파일을 생성해서 웹 브라우저에 전달하고 웹 브라우저는 HTML을 해석

![](https://blog.kakaocdn.net/dn/mZeQH/btsizdHmCaL/ls8tTaU9L1QCSNxVsmnsyk/img.png)

### [📗 HTML API](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%C2%A0HTML%20API-1)

![](https://blog.kakaocdn.net/dn/catdaO/btsiFDFuohA/Xpllg8ATiuFpdcf0OrykcK/img.png)

- HTML이 아닌 JSON 등의 데이터를 전달
- 다양한 시스템에서 호출

![](https://blog.kakaocdn.net/dn/byiA9a/btsiBLjvjqz/jKSxwLWngF31JpOBILFBD0/img.png)

- API를 통해서는 데이터만 주고 받고 UI가 필요할 경우 클라이언트에서 별도로 처리함
- UI 클라이언트 접점
    - 앱 클라이언트 (iPhone, Android, PC)
    - 웹 브라우저에서 Javascript를 통한 HTTP API 호출
    - React, Vue.js 같은 웹 클라이언트
- 서버 to 서버
    - 주문 서버  => 결제 서버
    - 기업간 데이터 통신

### [📗 서버 사이드 렌더링(SSR)](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%20%EC%84%9C%EB%B2%84%20%EC%82%AC%EC%9D%B4%EB%93%9C%20%EB%A0%8C%EB%8D%94%EB%A7%81(SSR)-1)

![](https://blog.kakaocdn.net/dn/bGea6t/btsitzLZV9M/6Xj0yDySkAjnEbEYYtFI4K/img.png)

- HTML 최종 결과를 서버에서 만들어서 웹 브라우저에 전달
- 주로 정적인 화면에 사용
- 관련 기술 : JSP, Thymeleaf

### [📗 클라이언트 사이드 렌더링(CSR)](https://repeater2487.tistory.com/114?category=1116968#%F0%9F%93%97%C2%A0%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8%20%EC%82%AC%EC%9D%B4%EB%93%9C%20%EB%A0%8C%EB%8D%94%EB%A7%81(CSR)-1)

![](https://blog.kakaocdn.net/dn/Du77g/btsis0v3bCX/id8BAFyIY1VdkvFWhGNPP0/img.png)

- HTML 결과를 Javascript로 웹 브라우저에서 동적으로 생성
- 주로 동적인 화면에 사용, 웹 환경을 마치 앱처럼 필요한 부분마다 변경할 수 있음
- 관련 기술 : React, Vue.js