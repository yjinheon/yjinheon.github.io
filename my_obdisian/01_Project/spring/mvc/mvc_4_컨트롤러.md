## [📕 프론트 컨트롤러 패턴 소개](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%ED%94%84%EB%A1%A0%ED%8A%B8%20%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC%20%ED%8C%A8%ED%84%B4%20%EC%86%8C%EA%B0%9C-1)

#### **프론트 컨트롤러 도입 전**

![](https://blog.kakaocdn.net/dn/YUfO3/btsjpExprWU/OUNV1VP0GzKuLntcPjaagk/img.png)

**=> 공통 로직이 각각의 컨트롤러에 중복되어 존재**

#### **프론트 컨트롤러 도입 후**

![](https://blog.kakaocdn.net/dn/tK03C/btsjmvVjfYV/VIqCkvSAg0GAE1qONiSPa0/img.png)

**FrontController 패턴 특징**

- 프론트 컨트롤러 서블릿 하나로 클라이언트의 요청을 받음
- 프론트 컨트롤러가 요청에 맞는 컨트롤러를 찾아서 호출
- 공통 처리 가능
- 프론트 컨트롤러를 제외한 나머지 컨트롤러는 서블릿을 사용하지 않아도 됨

**=> 스프링 웹 MVC의 DispatcherServlet이 FrontController 패턴으로 구현되어 있음**

## [📕 프론트 컨트롤러 도입 - V1](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%ED%94%84%EB%A1%A0%ED%8A%B8%20%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC%20%EB%8F%84%EC%9E%85%20-%20V1-1)

### [📗 V1 구조](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20V1%20%EA%B5%AC%EC%A1%B0-1)

![](https://blog.kakaocdn.net/dn/BihPF/btsjmBgQKvJ/EBrBq9YVfKa1Tie8iaOLC0/img.png)

### [📗 ControllerV1](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20ControllerV1-1)

```java
package hello.servlet.web.frontcontroller.v1;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public interface ControllerV1 {
    void process(HttpServletRequest request, HttpServletResponse response) 
    	throws ServletException, IOException;
}
```

=> 각 컨트롤러는 이 인터페이스를 구현하고 프론트 컨트롤러는 이 인터페이스를 호출함으로써

구현과 관계없이 로직의 일관성을 가져갈 수 있다.

**[MemberFormControllerV1] - 회원 등록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v1.controller;

import hello.servlet.web.frontcontroller.v1.ControllerV1;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MemberFormControllerV1 implements ControllerV1 {
    
    @Override
    public void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String viewPath = "/WEB-INF/views/new-form.jsp";
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

**[MemberSaveControllerV1] - 회원 저장 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v1.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.v1.ControllerV1;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MemberSaveControllerV1 implements ControllerV1 {
    
	private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        String username = request.getParameter("username");
        int age = Integer.parseInt(request.getParameter("age"));
        
        Member member = new Member(username, age);
        memberRepository.save(member);
        
        request.setAttribute("member", member);
        
        String viewPath = "/WEB-INF/views/save-result.jsp";
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

**[MemberListControllerV1] - 회원 목록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v1.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.v1.ControllerV1;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

public class MemberListControllerV1 implements ControllerV1 {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public void process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Member> members = memberRepository.findAll();
        request.setAttribute("members", members);
        
        String viewPath = "/WEB-INF/views/members.jsp";
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

**[FrontControllerServletV1] - 프론트 컨트롤러 V1**

```java
package hello.servlet.web.frontcontroller.v1;

import hello.servlet.web.frontcontroller.v1.controller.MemberFormControllerV1;
import hello.servlet.web.frontcontroller.v1.controller.MemberListControllerV1;
import hello.servlet.web.frontcontroller.v1.controller.MemberSaveControllerV1;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@WebServlet(name = "frontControllerServletV1", urlPatterns = "/frontcontroller/v1/*")
public class FrontControllerServletV1 extends HttpServlet {
    
    private Map<String, ControllerV1> controllerMap = new HashMap<>();
    
    public FrontControllerServletV1() {
        controllerMap.put("/front-controller/v1/members/new-form", new MemberFormControllerV1());
        controllerMap.put("/front-controller/v1/members/save", new MemberSaveControllerV1());
        controllerMap.put("/front-controller/v1/members", new MemberListControllerV1());
    }
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        System.out.println("FrontControllerServletV1.service");
        String requestURI = request.getRequestURI();
        
        ControllerV1 controller = controllerMap.get(requestURI);
        if (controller == null) {
	        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        return;
        }
        
        controller.process(request, response);
    }
}
```

#### **프론트 컨트롤러 분석**

- **urlPatterns**
    - urlPatterns = "/front-controller/v1/*" : /front-controller/v1 를 포함한 하위 모든 요청은 이 서블릿에서 받아들인다.
    - 예) /front-controller/v1, /front-controller/v1/members, /front-controller/v1/members/new-form
- **ControllerMap**
    - key : 매핑 URL
    - value : 호출될 컨트롤러
- **Service()**
    - 먼저 requestURI 를 조회해서 실제 호출할 컨트롤러를 controllerMap 에서 찾는다.   
        만약 없다면 404(SC_NOT_FOUND) 상태 코드를 반환한다.
    - 컨트롤러를 찾고 controller.process(request, response); 을 호출해서 해당 컨트롤러를 실행한다.
- **JSP**  
    - JSP는 이전 MVC에서 사용했던 것을 그대로 사용한다.

## [📕 View 분리 - V2](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%08View%20%EB%B6%84%EB%A6%AC%20-%20V2-1)

### [📗 V1의 문제점](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20V1%EC%9D%98%20%EB%AC%B8%EC%A0%9C%EC%A0%90-1)

**=> 모든 컨트롤러에서 뷰로 이동하는 부분이 중복되어 깔금하지 않다.**

> String viewPath = "/WEB-INF/views/new-form.jsp";  
> RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);  
> dispatcher.forward(request, response);

이 문제를 해결하기 위하여 별도로 뷰를 처리하는 객체를 만든다.  
  

### [📗 V2 구조](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20V2%20%EA%B5%AC%EC%A1%B0-1)

![](https://blog.kakaocdn.net/dn/bfOtuV/btsjnIGN8xV/OBLVgGRqY2HV2IZeC2lGA1/img.png)

### [📗 ControllerV2](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20ControllerV2-1)

```java
package hello.servlet.web.frontcontroller.v2;

import hello.servlet.web.frontcontroller.MyView;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public interface ControllerV2 {
    
    MyView process(HttpServletRequest request, HttpServletResponse response) 
    	throws ServletException, IOException; // 컨트롤러가 뷰를 반환한다.
}
```

**[**MyView**]**

```java
package hello.servlet.web.frontcontroller;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MyView {
    
    private String viewPath;
    
    public MyView(String viewPath) {
	    this.viewPath = viewPath;
    }
    
    public void render(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
}
```

**[MemberFormControllerV2] - 회원 등록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v2.controller;

import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v2.ControllerV2;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MemberFormControllerV2 implements ControllerV2 {
    
    @Override
    public MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        return new MyView("/WEB-INF/views/new-form.jsp");
    }
}
```

- 각 컨트롤러는 복잡한 dispatcher.forward() 를 직접 생성해서 호출하지 않아도 된다. 
- 단순히 MyView 객체를 생성하고 거기에 뷰 이름만 넣고 반환하면 된다.
- ControllerV1 을 구현한 클래스와 ControllerV2 를 구현한 클래스를 비교해보면, 이 부분의 중복이 확실하게 제거된 것을 확인할 수 있다.

**[MemberSaveControllerV2] - 회원 저장 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v2.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;

import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v2.ControllerV2;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class MemberSaveControllerV2 implements ControllerV2 {
    
	private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        String username = request.getParameter("username");
        int age = Integer.parseInt(request.getParameter("age"));
        
        Member member = new Member(username, age);
        memberRepository.save(member);
        
        request.setAttribute("member", member);
        
        return new MyView("/WEB-INF/views/save-result.jsp");
    }
}
```

**[MemberListControllerV2] - 회원 목록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v2.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v2.ControllerV2;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

public class MemberListControllerV2 implements ControllerV2 {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public MyView process(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        List<Member> members = memberRepository.findAll();
        request.setAttribute("members", members);
        
        return new MyView("/WEB-INF/views/members.jsp");
    }
}
```

**[FrontControllerServletV2] - 프론트 컨트롤러 V2**

```java
package hello.servlet.web.frontcontroller.v2;

import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v2.controller.MemberFormControllerV2;
import hello.servlet.web.frontcontroller.v2.controller.MemberListControllerV2;
import hello.servlet.web.frontcontroller.v2.controller.MemberSaveControllerV2;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@WebServlet(name = "frontControllerServletV2", urlPatterns = "/frontcontroller/v2/*")
public class FrontControllerServletV2 extends HttpServlet {
    
    private Map<String, ControllerV2> controllerMap = new HashMap<>();
    
    public FrontControllerServletV2() {
        controllerMap.put("/front-controller/v2/members/new-form", new MemberFormControllerV2());
        controllerMap.put("/front-controller/v2/members/save", new MemberSaveControllerV2());
        controllerMap.put("/front-controller/v2/members", new MemberListControllerV2());
    }
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        String requestURI = request.getRequestURI();
        
        ControllerV2 controller = controllerMap.get(requestURI);
        if (controller == null) {
            response.setStatus(HttpServletResponse.SC_NOT_FOUND);
            return;
        }
        
        MyView view = controller.process(request, response);
        view.render(request, response);
    }
}
```

#### **프론트 컨트롤러 분석**

ControllerV2의 반환 타입이 MyView 이므로 프론트 컨트롤러는 컨트롤러의 호출 결과로 MyView 를 반환 받는다. 

그리고 view.render() 를 호출하면 forward 로직을 수행해서 JSP가 실행된다.

MyView.render()

```java
public void render(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
    dispatcher.forward(request, response);
}
```

프론트 컨트롤러의 도입으로 MyView 객체의 render() 를 호출하는 부분을 모두 일관되게 처리할 수 있다. 

각각의 컨트롤러는 MyView 객체를 생성만 해서 반환하면 된다.

## [📕 Model 추가 - V3](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%08Model%20%EC%B6%94%EA%B0%80%20-%20V3-1)

### [📗 V2의 문제점](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20V2%EC%9D%98%20%EB%AC%B8%EC%A0%9C%EC%A0%90-1)

- **서블릿 종속성 제거**  
    - 컨트롤러 입장에서 HttpServletRequest, HttpServletResponse은 필요하지 않다.
    - 요청 파라미터 정보는 자바의 Map으로 대신 넘기도록 하면 지금 구조에서는 컨트롤러가 서블릿 기술을 몰라도 동작할 수 있다.
    - request 객체를 Model로 사용하는 대신에 별도의 Model 객체를 만들어서 반환하면 된다. 이렇게 하면 구현 코드도 매우 단순해지고, 테스트 코드 작성이 쉽다.
- **뷰 이름 중복 제거**
    - 컨트롤러는 뷰의 논리 이름을 반환하고, 실제 물리 위치의 이름은 프론트 컨트롤러에서 처리하도록 단순화 하자.
    - 이렇게 해두면 향후 뷰의 폴더 위치가 함께 이동해도 프론트 컨트롤러만 고치면 된다.

### [📗 V3 구조](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20V3%20%EA%B5%AC%EC%A1%B0-1)

- 지금까지 컨트롤러에서 서블릿에 종속적인 HttpServletRequest를 사용했다.   
    그리고 Model도 request.setAttribute() 를 통해 데이터를 저장하고 뷰에 전달했다.
- 서블릿의 종속성을 제거하기 위해 Model을 직접 만들고, 추가로 View 이름까지 전달하는 객체를 만든다.   
    (이번 버전에서는 컨트롤러에서 HttpServletRequest를 사용할 수 없다.   
    따라서 직접 request.setAttribute() 를 호출할 수 도 없다. 따라서 Model이 별도로 필요하다.)

**[ModelView] - Model 객체**

```java
package hello.servlet.web.frontcontroller;

import java.util.HashMap;
import java.util.Map;

public class ModelView {
    private String viewName;
    private Map<String, Object> model = new HashMap<>();
    
    public ModelView(String viewName) {
	    this.viewName = viewName;
    }
    
    public String getViewName() {
    	return viewName;
    }
    
    public void setViewName(String viewName) {
	    this.viewName = viewName;
    }
    
    public Map<String, Object> getModel() {
    	return model;
    }
    
    public void setModel(Map<String, Object> model) {
	    this.model = model;
    }
}
```

뷰의 이름과 뷰를 렌더링할 때 필요한 model 객체를 가지고 있다. model은 단순히 map으로 되어 있으므로 컨트롤러에서 뷰에 필요한 데이터를 key, value로 넣어주면 된다.

### [📗 ControllerV3](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20ControllerV3-1)

```java
package hello.servlet.web.frontcontroller.v3;

import hello.servlet.web.frontcontroller.ModelView;
import java.util.Map;

public interface ControllerV3 {
	ModelView process(Map<String, String> paramMap);
}
```

- 이 컨트롤러는 서블릿 기술을 전혀 사용하지 않아 구현이 매우 단순해지고 테스트 코드 작성이 쉽다.
- HttpServletRequest가 제공하는 파라미터는 프론트 컨트롤러가 paramMap에 담아서 호출해주면 된다.   
    응답 결과로 뷰 이름과 뷰에 전달할 Model 데이터를 포함하는 ModelView 객체를 반환하면 된다.

**[MemberFormControllerV3] - 회원 등록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v3.controller;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v3.ControllerV3;
import java.util.Map;

public class MemberFormControllerV3 implements ControllerV3 {
    @Override
    public ModelView process(Map<String, String> paramMap) {
	    return new ModelView("new-form");
    }
}
```

ModelView 를 생성할 때 new-form 이라는 view의 논리적인 이름을 지정한다.   
실제 물리적인 이름은 프론트 컨트롤러에서 처리한다.

**[MemberSaveControllerV3] - 회원 저장 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v3.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v3.ControllerV3;
import java.util.Map;

public class MemberSaveControllerV3 implements ControllerV3 {
	private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public ModelView process(Map<String, String> paramMap) {
        String username = paramMap.get("username"); // paramMap에서 필요한 요청 파라미터 조회
        int age = Integer.parseInt(paramMap.get("age"));
        
        Member member = new Member(username, age);
        memberRepository.save(member);
        
        ModelView mv = new ModelView("save-result");
        mv.getModel().put("member", member); // 모델에 뷰에서 필요한 객체를 담고 반환
        return mv;
    }
}
```

**[MemberListControllerV3] - 회원 목록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v3.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v3.ControllerV3;
import java.util.List;
import java.util.Map;

public class MemberListControllerV3 implements ControllerV3 {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public ModelView process(Map<String, String> paramMap) {
        List<Member> members = memberRepository.findAll();
        
        ModelView mv = new ModelView("members");
        mv.getModel().put("members", members);
        
        return mv;
    }
}
```

**[FrontControllerServletV3] - 프론트 컨트롤러 V3**

```java
package hello.servlet.web.frontcontroller.v3;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v3.controller.MemberFormControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberListControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberSaveControllerV3;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@WebServlet(name = "frontControllerServletV3", urlPatterns = "/frontcontroller/v3/*")
public class FrontControllerServletV3 extends HttpServlet {
    private Map<String, ControllerV3> controllerMap = new HashMap<>();
    
    public FrontControllerServletV3() {
        controllerMap.put("/front-controller/v3/members/new-form", new MemberFormControllerV3());
        controllerMap.put("/front-controller/v3/members/save", new MemberSaveControllerV3());
        controllerMap.put("/front-controller/v3/members", new MemberListControllerV3());
    }
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        String requestURI = request.getRequestURI();
        
        ControllerV3 controller = controllerMap.get(requestURI);
        if (controller == null) {
	        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
        	return;
	    }

        Map<String, String> paramMap = createParamMap(request);
        ModelView mv = controller.process(paramMap);
        
        String viewName = mv.getViewName();
        MyView view = viewResolver(viewName);
        view.render(mv.getModel(), request, response);
    }
    
    // HttpServletRequest에서 파라미터 정보를 꺼내에 Map으로 변환한다.
    private Map<String, String> createParamMap(HttpServletRequest request) {
        Map<String, String> paramMap = new HashMap<>();
        request.getParameterNames().asIterator()
            .forEachRemaining(paramName -> paramMap.put(paramName, request.getParameter(paramName)));
        return paramMap;
    }
    
    // 컨트롤러가 반환한 논리 뷰 이름을 실제 물리 뷰 경로로 변경한다.
    private MyView viewResolver(String viewName) {
    	return new MyView("/WEB-INF/views/" + viewName + ".jsp");
    }
}
```

**[MyView] - V2에서 쓰인 클래스에 추가**

```java
package hello.servlet.web.frontcontroller;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.Map;

public class MyView {
    private String viewPath;
    
    public MyView(String viewPath) {
	    this.viewPath = viewPath;
    }
    
    public void render(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
    
    // v3에서 추가
    // 모델 정보를 함께 받는 새로운 render()를 정의
    public void render(Map<String, Object> model, HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        modelToRequestAttribute(model, request);
        RequestDispatcher dispatcher = request.getRequestDispatcher(viewPath);
        dispatcher.forward(request, response);
    }
    
    // 모델의 데이터를 꺼내어 request에 담아둔다.
    private void modelToRequestAttribute(Map<String, Object> model, HttpServletRequest request) {
	    model.forEach((key, value) -> request.setAttribute(key, value));
    }
}
```

## [📕 단순하고 실용적인 컨트롤러 - V4](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%08%EB%8B%A8%EC%88%9C%ED%95%98%EA%B3%A0%20%EC%8B%A4%EC%9A%A9%EC%A0%81%EC%9D%B8%20%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC%20-%20V4-1)

> 앞서 만든 v3 컨트롤러는 서블릿 종속성을 제거하고 뷰 경로의 중복을 제거하는 등, 잘 설계된 컨트롤러이다.  
> 그런데 실제 컨트롤러 인터페이스를 구현하는 개발자 입장에서 보면,  
> 항상 ModelView 객체를 생성하고 반환해야 하는 부분이 조금은 번거롭다.  
> 좋은 프레임워크는 아키텍처도 중요하지만, 그와 더불어 실제 개발하는 개발자가 단순하고 편리하게 사용할 수 있어야 한다.   
> 소위 실용성이 있어야 한다.

### [📗 V4 구조](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20V4%20%EA%B5%AC%EC%A1%B0-1)

![](https://blog.kakaocdn.net/dn/QgAtm/btsjnb97LoM/FzZm61v8HYXIFCplvJwQk1/img.png)

기본적인 구조는 V3와 같지만 컨트롤러가 ModelView를 반환하지 않고 ViewName만 반환한다.

### [📗 ControllerV4](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20ControllerV4-1)

```java
package hello.servlet.web.frontcontroller.v4;

import java.util.Map;

public interface ControllerV4 {
    
    /**
    * @param paramMap
    * @param model
    * @return viewName
    */
    String process(Map<String, String> paramMap, Map<String, Object> model);
}
```

**[MemberFormControllerV4] - 회원 등록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v4.controller;

import hello.servlet.web.frontcontroller.v4.ControllerV4;

import java.util.Map;

public class MemberFormControllerV4 implements ControllerV4 {
    
    @Override
    public String process(Map<String, String> paramMap, Map<String, Object> model) {
	    return "new-form"; // 뷰의 논리 이름만 반환하면 된다.
    }
}
```

**[MemberSaveControllerV4] - 회원 저장 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v4.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.v4.ControllerV4;

import java.util.Map;
public class MemberSaveControllerV4 implements ControllerV4 {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public String process(Map<String, String> paramMap, Map<String, Object> model) {
        String username = paramMap.get("username");
        int age = Integer.parseInt(paramMap.get("age"));
        
        Member member = new Member(username, age);
        memberRepository.save(member);
        
        model.put("member", member); // 모델이 파라미터로 전달되기 때문에 모델을 직접 생성하지 않아도 된다.
        
        return "save-result";
    }
}
```

**[MemberListControllerV4] - 회원 목록 컨트롤러**

```java
package hello.servlet.web.frontcontroller.v4.controller;

import hello.servlet.domain.member.Member;
import hello.servlet.domain.member.MemberRepository;
import hello.servlet.web.frontcontroller.v4.ControllerV4;

import java.util.List;
import java.util.Map;

public class MemberListControllerV4 implements ControllerV4 {
    
    private MemberRepository memberRepository = MemberRepository.getInstance();
    
    @Override
    public String process(Map<String, String> paramMap, Map<String, Object> model) {
        List<Member> members = memberRepository.findAll();
        model.put("members", members);
        
        return "members";
    }
}
```

**[FrontControllerServletV4] - 프론트 컨트롤러 V4**

```java
package hello.servlet.web.frontcontroller.v4;

import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v4.controller.MemberFormControllerV4;
import hello.servlet.web.frontcontroller.v4.controller.MemberListControllerV4;
import hello.servlet.web.frontcontroller.v4.controller.MemberSaveControllerV4;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@WebServlet(name = "frontControllerServletV4", urlPatterns = "/frontcontroller/v4/*")
public class FrontControllerServletV4 extends HttpServlet {
    
    private Map<String, ControllerV4> controllerMap = new HashMap<>();
    
    public FrontControllerServletV4() {
        controllerMap.put("/front-controller/v4/members/new-form", new MemberFormControllerV4());
        controllerMap.put("/front-controller/v4/members/save", new MemberSaveControllerV4());
        controllerMap.put("/front-controller/v4/members", new MemberListControllerV4());
    }
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse
    response) throws ServletException, IOException {
        String requestURI = request.getRequestURI();
        
        ControllerV4 controller = controllerMap.get(requestURI);
        if (controller == null) {
	        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
	        return;
    	}
        
        Map<String, String> paramMap = createParamMap(request);
        Map<String, Object> model = new HashMap<>(); //추가

        String viewName = controller.process(paramMap, model);

        MyView view = viewResolver(viewName);
        view.render(model, request, response);
    }
    
    private Map<String, String> createParamMap(HttpServletRequest request) {
    	Map<String, String> paramMap = new HashMap<>();
	    request.getParameterNames().asIterator()
            .forEachRemaining(paramName -> paramMap.put(paramName, request.getParameter(paramName)));
        return paramMap;
    }
    
    private MyView viewResolver(String viewName) {
    	return new MyView("/WEB-INF/views/" + viewName + ".jsp");
    }
}
```

#### **정리**

- 이번 버전의 컨트롤러는 매우 단순하고 실용적이다. 기존 구조에서 모델을 파라미터로 넘기고,   
    뷰의 논리 이름을 반환한다는 작은 아이디어를 적용했을 뿐인데,   
    컨트롤러를 구현하는 개발자 입장에서 보면 이제 군더더기 없는 코드를 작성할 수 있다.
- 또한 중요한 사실은 여기까지 한번에 온 것이 아니라는 점이다.   
    프레임워크가 점진적으로 발전하는 과정 속에서 이런 방법도 찾을 수 있었다.
- **프레임워크나 공통 기능이 수고로워야 사용하는 개발자가 편리해진다.**

## [📕 유연한 컨트롤러 - V5](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%08%EC%9C%A0%EC%97%B0%ED%95%9C%20%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC%20-%20V5-1)

### [📗 어댑터 패턴](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20%EC%96%B4%EB%8C%91%ED%84%B0%20%ED%8C%A8%ED%84%B4-1)

```java
public interface ControllerV3 {
    ModelView process(Map<String, String> paramMap);
}
```

```java
public interface ControllerV4 {
    String process(Map<String, String> paramMap, Map<String, Object> model);
}
```

지금까지 개발한 프론트 컨트롤러는 한가지 방식의 컨트롤러 인터페이스만 사용할 수 있다.   
ControllerV3, ControllerV4 는 완전히 다른 인터페이스이므로 호환이 불가능하다. 

**이럴 때 사용하는 것이 바로 어댑터이다.**  
  

### [📗 V5 구조](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%97%20%08V5%20%EA%B5%AC%EC%A1%B0-1)

![](https://blog.kakaocdn.net/dn/b6b6kF/btsjnH8YkuZ/i5kSyARMUl1UZXsDkQz10k/img.png)

**핸들러 어댑터**

- 중간에 어댑터 역할을 하는 어댑터가 추가되었는데 이름이 핸들러 어댑터이다.
- 여기서 어댑터 역할을 해주는 덕분에 다양한 종류의 컨트롤러를 호출할 수 있다

**핸들러**

- 컨트롤러의 이름을 더 넓은 범위인 핸들러로 변경했다. 
- 그 이유는 이제 어댑터가 있기 때문에 꼭 컨트롤러의 개념 뿐만 아니라   
    어떠한 것이든 해당하는 종류의 어댑터만 있으면 다 처리할 수 있기 때문이다.

**[MyHandlerAdapter]**

```java
package hello.servlet.web.frontcontroller.v5;

import hello.servlet.web.frontcontroller.ModelView;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public interface MyHandlerAdapter {
    
    boolean supports(Object handler);
    
    ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) throws ServletException, IOException;
}
```

boolean supports(Object handler)

- handler는 컨트롤러를 말한다.
- 어댑터가 해당 컨트롤러를 처리할 수 있는지 판단하는 메서드다.

ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler)

- 어댑터는 실제 컨트롤러를 호출하고, 그 결과로 ModelView를 반환해야 한다.
- 실제 컨트롤러가 ModelView를 반환하지 못하면, 어댑터가 ModelView를 직접 생성해서라도 반환해야 한다.
- 이전에는 프론트 컨트롤러가 실제 컨트롤러를 호출했지만 이제는 이 어댑터를 통해서 실제 컨트롤러가 호출된다.

**[ControllerV3HandlerAdapter]**

```java
package hello.servlet.web.frontcontroller.v5.adapter;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v3.ControllerV3;
import hello.servlet.web.frontcontroller.v5.MyHandlerAdapter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

public class ControllerV3HandlerAdapter implements MyHandlerAdapter {
    
    @Override
    public boolean supports(Object handler) {
	    return (handler instanceof ControllerV3);
    }
    
    @Override
    public ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        ControllerV3 controller = (ControllerV3) handler;
        Map<String, String> paramMap = createParamMap(request);
        
        ModelView mv = controller.process(paramMap);
        return mv;
    }
    
    private Map<String, String> createParamMap(HttpServletRequest request) {
        Map<String, String> paramMap = new HashMap<>();
        request.getParameterNames().asIterator()
            .forEachRemaining(paramName -> paramMap.put(paramName, request.getParameter(paramName)));
        return paramMap;
    }
}
```

**[FrontControllerServletV5]**

```java
package hello.servlet.web.frontcontroller.v5;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.MyView;
import hello.servlet.web.frontcontroller.v3.controller.MemberFormControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberListControllerV3;
import hello.servlet.web.frontcontroller.v3.controller.MemberSaveControllerV3;
import hello.servlet.web.frontcontroller.v5.adapter.ControllerV3HandlerAdapter;
import hello.servlet.web.frontcontroller.v5.adapter.ControllerV4HandlerAdapter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@WebServlet(name = "frontControllerServletV5", urlPatterns = "/frontcontroller/v5/*")
public class FrontControllerServletV5 extends HttpServlet {
    
    // ControllerV3, ControllerV4 같은 인터페이스 대신 아무 값이나 받을 수 있는 Object로 변경되었다.
    private final Map<String, Object> handlerMappingMap = new HashMap<>();
    private final List<MyHandlerAdapter> handlerAdapters = new ArrayList<>();
    
    // 생성자는 핸들러 매핑과 어댑터를 초기화한다.
    public FrontControllerServletV5() {
        initHandlerMappingMap();
        initHandlerAdapters();
    }
    
    private void initHandlerMappingMap() {
        handlerMappingMap.put("/front-controller/v5/v3/members/new-form", new MemberFormControllerV3());
        handlerMappingMap.put("/front-controller/v5/v3/members/save", new MemberSaveControllerV3());
        handlerMappingMap.put("/front-controller/v5/v3/members", new MemberListControllerV3());
    }
    
    private void initHandlerAdapters() {
	    handlerAdapters.add(new ControllerV3HandlerAdapter());
    }
    
    @Override
    protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        
        Object handler = getHandler(request);
        if (handler == null) {
	        response.setStatus(HttpServletResponse.SC_NOT_FOUND);
    	    return;
	    }
        
        MyHandlerAdapter adapter = getHandlerAdapter(handler);
        ModelView mv = adapter.handle(request, response, handler);
        
        MyView view = viewResolver(mv.getViewName());
        view.render(mv.getModel(), request, response);
    }
    
    // handlerMappingMap에서 URL에 매핑된 핸들러(컨트롤러) 객체를 찾아서 반환한다.
    private Object getHandler(HttpServletRequest request) {
        String requestURI = request.getRequestURI();
        return handlerMappingMap.get(requestURI);
    }
    
    // handler를 처리할 수 있는 어댑터를 adapter.supports(handler)를 통해 찾는다.
    private MyHandlerAdapter getHandlerAdapter(Object handler) {
        for (MyHandlerAdapter adapter : handlerAdapters) {
            if (adapter.supports(handler)) {
                return adapter;
            }
        }
        throw new IllegalArgumentException("handler adapter를 찾을 수 없습니다. handler=" + handler); 
    }
    
    private MyView viewResolver(String viewName) {
        return new MyView("/WEB-INF/views/" + viewName + ".jsp");
    }
}
```

**FrontControllerServeletV5에 ControllerV4 추가**

```java
private void initHandlerMappingMap() {
    handlerMappingMap.put("/front-controller/v5/v3/members/new-form", new MemberFormControllerV3());
    handlerMappingMap.put("/front-controller/v5/v3/members/save", new MemberSaveControllerV3());
    handlerMappingMap.put("/front-controller/v5/v3/members", new MemberListControllerV3());
    
    //V4 추가
    handlerMappingMap.put("/front-controller/v5/v4/members/new-form", new MemberFormControllerV4());
    handlerMappingMap.put("/front-controller/v5/v4/members/save", new MemberSaveControllerV4());
    handlerMappingMap.put("/front-controller/v5/v4/members", new MemberListControllerV4());
}

private void initHandlerAdapters() {
    handlerAdapters.add(new ControllerV3HandlerAdapter());
    handlerAdapters.add(new ControllerV4HandlerAdapter()); //V4 추가
}
```

**[ControllerV4HandlerAdapter]**

```java
package hello.servlet.web.frontcontroller.v5.adapter;

import hello.servlet.web.frontcontroller.ModelView;
import hello.servlet.web.frontcontroller.v4.ControllerV4;
import hello.servlet.web.frontcontroller.v5.MyHandlerAdapter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

public class ControllerV4HandlerAdapter implements MyHandlerAdapter {
    
    // handler가 ControllerV4인 경우에만 처리
    @Override
    public boolean supports(Object handler) {
	    return (handler instanceof ControllerV4);
    }
    
    @Override
    public ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        
        ControllerV4 controller = (ControllerV4) handler;
        
        Map<String, String> paramMap = createParamMap(request);
        Map<String, Object> model = new HashMap<>();
        
        String viewName = controller.process(paramMap, model);
        
        // ControllerV4는 뷰의 이름을 반환하지만 어댑터는 ModelView를 만들어서 반환
        ModelView mv = new ModelView(viewName);
        mv.setModel(model);
        
        return mv;
    }
    
    private Map<String, String> createParamMap(HttpServletRequest request) {
        Map<String, String> paramMap = new HashMap<>();
        request.getParameterNames().asIterator()
            .forEachRemaining(paramName -> paramMap.put(paramName, request.getParameter(paramName)));
        return paramMap;
    }
}
```

**어댑터와 ControllerV4**

```java
public interface ControllerV4 {
	String process(Map<String, String> paramMap, Map<String, Object> model);
}

public interface MyHandlerAdapter {
	ModelView handle(HttpServletRequest request, HttpServletResponse response, Object handler) throws ServletException, IOException;
}
```

## [📕 정리](https://repeater2487.tistory.com/117?category=1116968#%F0%9F%93%95%20%08%08%EC%A0%95%EB%A6%AC-1)

- **v1** **:** **프론트 컨트롤러를 도입** / 기존 구조를 최대한 유지하면서 프론트 컨트롤러를 도입
- **v2** **:** **View 분류** / 단순 반복 되는 뷰 로직 분리
- **v3: Model 추가** / 서블릿 종속성 제거 뷰 이름 중복 제거
- **v4: 단순하고 실용적인 컨트롤러** / v3와 거의 비슷 구현 입장에서 ModelView를 직접 생성해서 반환하지 않도록 편리한 인터페이스 제공
- **v5: 유연한 컨트롤러** / 어댑터 도입 어댑터를 추가해서 프레임워크를 유연하고 확장성 있게 설계

여기에 애노테이션을 사용해서 컨트롤러를 더 편리하게 발전시길 수도 있다. 만약 애노테이션을 사용해서 컨트롤러를 편리하게 사용할 수 있게 하려면 어떻게 해야할까? 바로 애노테이션을 지원하는 어댑터를 추가하면 된다! 다형성과 어댑터 덕분에 기존 구조를 유지하면서, 프레임워크의 기능을 확장할 수 있다.  
  
스프링 MVC 여기서 더 발전시키면 좋겠지만, 스프링 MVC의 핵심 구조를 파악하는데 필요한 부분은 모두 만들어보았다. 지금까지 작성한 코드는 스프링 MVC 프레임워크의 핵심 코드의 축약 버전이고, 구조도 거의 같다. 스프링 MVC에는 지금까지 우리가 학습한 내용과 거의 같은 구조를 가지고 있다.