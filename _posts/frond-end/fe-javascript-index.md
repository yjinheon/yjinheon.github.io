---
title: "자바스크립트 코드스니펫"
date: 
tags:
  - [Link, javascript]
categories:
  - [FrontEnd]
updated:
---


### spread operator - 배열

`...` 을 사용하여 배열을 복사하거나 합칠 수 있다.

```js

let arr1 =['one','two','three'];
let arr2 =['four','five','six'];

const arr3 = [...arr1, ...arr2];

console.log(arr3); // ["one", "twi", "three", "four", "five", "six"]

const [a,b,c,...rest] = arr1;

console.log(a); // one
console.log(b); // two
console.log(c); // three
console.log(rest); // 배열의 나머지 값이 없으면 빈 배열이 출력

```

### spread operator - 객체

```js

let obj1 = {one:1, two:2, other:3};
let obj2 = {four:4, five:5, other:6};

const combined = {
  ...obj1,
  ...obj2,
};

console.log(combined); // {one: 1, two: 2, other: 6, four: 4, five: 5}

let {other ...rest} = combined;

console.log(rest); // {one: 1, two: 2, four: 4, five: 5}

```

### destructuring

```javascript

// 핵심은 배열을 나누는 것

const userNameData = ['John', 'Doe']
const [firstName, lastName] = userNameData; // destructuring array

console.log(firstName)
console.log(lastName)

```

### String 

```javascript
let string = 'Hello';
let string2 = 'Jinheon';

let greetings = `${string} ${string2}`;

console.log(greetings);

let product = {
    name : 'Milk',
    price : 1.99,
}

// templete string

let message = `The price of ${product.name} is ${product.price}`;
let multiline = `This is
a multiline
string`;

console.log(message);
console.log(multiline);
```

