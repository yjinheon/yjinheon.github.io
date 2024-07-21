---
title: "[Neovim]NeoVim Keybinding"
date: 
tags: 
categories:
  - - Tools
    - Neovim
updated: 2024-07-21T10:38
modified: 2023-12-29T09:48:45+09:00
draft: true
created: 2024-06-07T07:02
---

## Intro

간단한 파이썬 코딩을 할 경우에는 주로 Neovim을 사용하고 있다. Neovim은
플러그인을 이것저것 설치하면서 자신만의 IDE를 만들 수 있다는 장점이 있지만 나는
아직 그런 커스텀에 익숙하지 않아서 `Nvchad` 라는 Neovim 기반 유사 IDE 플러그인을
깔고 거기에 필요한 플러그인을 추가하는 방식으로 사용하고 있다.

이 글에서는 내가 주로 사용하는 Nvim 키 바인딩을 정리하고 업데이트 할 예정이다.

## 자주 사용하는 단축키

- `:sp` : 현재 파일을 가로로 분할
- `:vsp` : 현재 파일을 세로로 분할
- `<leader> + b` : 새 버퍼 생성
- `<leader> + x` : 현재 버퍼 닫기
- `<leader> + ch `: 치트시트 확인
- `<leader> + fm` : 현재 파일에 black, prettier 등의 formatter 적용
- `<leader> + ff` : 현재 프로젝트 범위에서 파일 탐색. fzf 적용
- `:Vista ` :  파일 스트럭쳐 확인
- `<leader> + h` : 가로 터미널 열기


### 필요한 기능

- 열편집 (sublimetext같은거)
- 다중 편집 


## Reference

- https://github.com/folke/which-key.nvim
- https://github.com/nvim-neo-tree/neo-tree.nvim file structure 확인
- https://github.com/liuchengxu/vista.vim
- https://learnbyexample.github.io/tips/vim-tip-14/
