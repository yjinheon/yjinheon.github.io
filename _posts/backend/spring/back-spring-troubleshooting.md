---
title: '[Spring]트러블슈팅'
categories:
  - [backend,Spring]
tags:
    - Spring
    - troubleshooting
date:
updated:
---

### @Buiilder 초기화 필드 적용


- @Builder는 클래스를 빌더 패턴으로 생성할 수 있게 만드는 Annotation
- 필드에서 초기화된 상태는  @Builder 에서 무시된다.
- 초기화를   @Builder로 하던가 따로 @Builder.Default 를 필드에 명시해준다.


```
@Builder.Default  
@Column(name = "delete_yn")  
private Boolean deleteYn = false;  
public void delete()     {  
    this.deleteYn = true;  
}

```