---
modified: 2024-01-01T08:55:54+09:00
created: 2024-01-05T20:10
updated: 2024-07-11T09:28
---

## TODAY

```tasks
not done  
created before tomorrow
```


## This Week
```tasks

not done
due before in a week
```


## INBOX

```tasks
not done
tags include #inbox
```

## Courses

- online courses progress tracker

```tasks
not done
tags include #oc
```


## TODO
```tasks  
not done  
short mode  
```

## IN_PROGRESS
```tasks  
status.type is IN_PROGRESS
```



## TEST

```dataview
table
tags , alias as description
where contains(status,"todo") or contains(status,"in_progress") 
SORT file.path ASCENDING
```
