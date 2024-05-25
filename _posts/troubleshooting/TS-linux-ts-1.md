---
title: '[Linux]zsh: corrupt history file 해결'
categories:
  - Troubleshooting
date:
updated:
tags: 
  - Linux
---

<!--

<center>Kaggle Customer Score Dataset</center>

- Machine Learning



- Statistics , Math
- Data Engineering
- Programming
- EDA & Visualization
- Preprocessing


#신경망이란 무엇인가?

https://www.youtube.com/watch?v=aircAruvnKk


#참고

https://cinema4dr12.tistory.com/1016?category=515283

https://www.kdnuggets.com/2021/07/top-python-data-science-interview-questions.html
-->

---

```bash
$ cd ~                          



$ mv .zsh_history .zsh_history.1217



$ strings .zsh_history.1217 .zsh_history



$ fc -R .zsh_history
```


## References

- https://www.whatwant.com/entry/zsh-corrupt-history-file 

