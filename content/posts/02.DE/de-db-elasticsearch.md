---
title: "[DB]ElasticSearch"
draft: true
date: 2023-07-21T06:52:55.000Z
categories:
  - Data Engineering
tags:
  - elasticsearch
  - database
created: 2024-06-28T16:02
updated: 2024-07-20T20:50
tag:
---

## 개요

## 특성

- nosql json 기반 data store
- Restful API 기반 쿼리
- data sourcess : logs, metrics, app id

## Comparison RDBMS

DB <-> Indexes/Indices
Tables <-> Pattererns/Types
Rows <-> Documents
Columnns <-> Fields

## ELK Stack

### beats

### logstash

- opensource server side processing pipeline
- input/transform(formatting)/stash it somewhere
- somewhere is elastic search

### kibana

- ui dashboard
- widgets/visualizations
