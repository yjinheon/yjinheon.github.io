---
created: 2024-07-26T09:55
updated: 2024-07-30T17:11
---

- [ ] #status/pending 리눅스 디스크 용량 확인 관련

참조

- https://uzihoon.com/post/831cf540-adf4-11ea-b011-b113e86828fc
- https://inpa.tistory.com/entry/LINUX-%F0%9F%93%9A-%EB%94%94%EC%8A%A4%ED%81%AC-%EB%AA%85%EB%A0%B9%EC%96%B4-%EC%A0%95%EB%A6%AC-df-du-%EC%9A%A9%EB%9F%89-%EA%B5%AC%ED%95%98%EA%B8%B0

- [ ] #status/pending /dev/null @>&1 의미
      https://jybaek.tistory.com/115

## Vue js 개발 스타일

### Options API

---

**_Concept_**

- **[Vue] OptionsAPI** : data,method,mounted 등과 같은 객체를 이용하여 컴포넌트 로직을 정의하는 방식. 옵션으로 정의된 속성은 컴포넌트 인스탄스를 가리키는 함수 내부의 this에 노출된다.
- **[Vue]data** : data 메서드는 해당 컴포넌트에서 사용될 state 즉 데이터들을 관리하는 곳이다. data 에서 반환된 속성들은 반응적인 상태가 되어 this 에 노출된다.
- **[Vue]methods** : methods은 속성 값을 변경하고 업데이트 할 수 있는 함수이며 템플릿 내에서 이벤트 핸들러로 바인딩 가능. methods에서 반환된 함수들은 this에 노출됨
- **[Vue]LifeCycleI Hook** : 컴포넌트 생명주기의 여러 단계에서 호출

---

### Composition API

---

**_Concept_**

- **[Vue] CompositionAPI** : import해서 가져온 Vue.js 의 내장된 API 함수들을 사용하여 컴포넌트를 정의하는 방식. SFC에서 컴포넌트는 일반적으로 script setup 과 함께 사용

- **[Vue]ref, reactive** : 컴포지션 API에서 반응성 있는 데이터를 만들어줄 경우, ref 혹은 reactive 키워드를 통하여 변수를 선언해준다.

- **[Vue]CompositionAPI methods** : methods 객체를 선언할 필요가 없기 때문에 함수를 그냥 만들어서 사용하면 된다.

---

---

**_Concept_**

- **[Vue] 컴포넌트 생성** : 각각의 Vue 컴포넌트 인스턴스는 생성될 때 일련의 초기화 과정을 거친다.
- **[Vue] Created** : 템플릿 및 Virtual DOM이 마운팅 혹은 렌더링 되기 전에 실행되며 , 데이터와 이벤트가 활성화되어 접근할 수 있다. 기본적으로 컴포넌트가 생성된 직후에 접근할 수 있는 라이프사이클 훅. 데이터와 관련되어 있다
- **[Vue] Mounted** : 컴포넌트가 초기 렌더링 DOM 노드 생성이 완료된 후 코드 실행. template 부분의 html요소가 모두 렌더링 된 이후에 접근이 가능하다 기본적으로 화면 요소를 제어 하는 UI컨트롤과와 관련되어 있다,
- **[Vue] Updated** : 컴포넌트 데이터가 변경되어 DOM이 렌더링 된 후 실행. Property 변경, 데이터 변경, 이벤트 처리 등이 가능.

---
