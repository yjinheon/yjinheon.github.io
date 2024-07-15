### instance 접속 후 할 것

root 계정설정

root 비밀번호 생성하기

1. ubuntu 계정(w. private key)으로 ec2 접속 

2. sudo passwd root 입력

3. 아래와 같이 비밀번호 입력, 비밀번호 재확인 과정을 거쳐 root 비밀번호를 설정 할 수 있다. 

ubuntu@ip-172-31-3-41:~$ sudo passwd root
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully

 

ubuntu 계정 비밀번호 생성하기

1. ubuntu 계정(w. private key)으로 ec2 접속

2. sudo su - 입력

3. passwd ubuntu 입력

4. 아래와 같이 비밀번호 입력, 비밀번호 재확인 과정을 거쳐 ubuntu 비밀번호를 설정 할 수 있다. 

ubuntu@ip-172-31-3-41:~$ sudo  su -
root@ip-172-31-3-41:~# passwd ubuntu
Enter new UNIX password:
Retype new UNIX password:

