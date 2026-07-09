# Phase 3 - Extraction Database Design

## Overview

The Extraction Database is the second layer of PlacementIQ.

Phase 2 stored interview experiences in a normalized raw format.

Phase 3 introduces an AI-powered knowledge layer that converts raw interview narratives into structured, queryable knowledge.

This database is **NOT** a replacement for the existing `interviews` table.

Instead, it sits on top of it and stores AI-extracted knowledge that will power:

- Search
- Analytics
- Pattern Detection
- Recommendation
- Future LangGraph Agents

---

# Design Goals

The extraction database is designed to:

- Preserve the original interview experience.
- Store structured knowledge separately.
- Support efficient retrieval.
- Support company comparisons.
- Support analytics.
- Support future multi-agent workflows.
- Minimize repeated LLM processing.
- Keep the schema extensible.

---

# Overall Architecture

```
                        Internito API
                              │
                              ▼
                        API Client
                              │
                              ▼
                     interviews.json
                              │
                              ▼
                     interviews (RAW)
                              │
                    LLM Extractor Agent
                              │
                              ▼
               structured_experiences
                              │
      ┌───────────────────────┼────────────────────────┐
      ▼                       ▼                        ▼
coding_questions      subject_questions       interview_rounds
      │                       │
      ▼                       ▼
 sql_questions           puzzles
      │
      ▼
hr_questions

```

The **interviews** table remains the immutable source of truth.

The **structured_experiences** table becomes the AI knowledge layer.

---

# Database Design Philosophy

The extraction database follows a **Hybrid Relational Model**.

Frequently queried information is stored relationally.

Less frequently queried metadata is stored as JSON.

This balances:

- Query performance
- Simplicity
- AI flexibility

---

# Table Relationships

```
interviews
      │
      │ 1 : 1
      ▼
structured_experiences
      │
      ├────────── coding_questions
      │
      ├────────── subject_questions
      │
      ├────────── sql_questions
      │
      ├────────── puzzles
      │
      ├────────── hr_questions
      │
      └────────── interview_rounds
```

---

# Table 1 : interviews

Status:

Existing Phase 2 table.

Purpose:

Stores normalized interview experiences.

Never modified by Phase 3.

Acts as the source of truth.

---

# Table 2 : structured_experiences

Purpose

Stores high-level structured knowledge extracted by the LLM.

Primary Key

```
id
```

Foreign Key

```
interview_id
```

Columns

| Column | Type | Description |
|---------|------|-------------|
| id | TEXT | Primary Key |
| interview_id | TEXT | FK → interviews.id |
| company | TEXT | Company Name |
| role | TEXT | Job Role |
| batch | TEXT | Batch |
| experience_type | TEXT | Internship / Placement |
| result | TEXT | Selected / Rejected / Unknown |
| overall_difficulty | TEXT | Easy / Medium / Hard |
| number_of_rounds | INTEGER | Total rounds |
| oa_platform | TEXT | HackerRank / CodeSignal / etc |
| summary | TEXT | AI generated summary |
| technologies | JSON | Mentioned technologies |
| keywords | JSON | Search keywords |
| tips | JSON | Candidate advice |
| mistakes | JSON | Candidate mistakes |
| resources | JSON | Learning resources |
| important_concepts | JSON | Extra concepts |
| projects_discussed | JSON | Resume projects discussed |
| schema_version | TEXT | Extraction schema version |
| model_used | TEXT | LLM used |
| processed_at | DATETIME | Extraction timestamp |

---

# Table 3 : coding_questions

Purpose

Stores every coding question individually.

Each question becomes searchable.

Primary Key

```
id
```

Foreign Key

```
structured_experience_id
```

Columns

| Column | Type |
|---------|------|
| id | TEXT |
| structured_experience_id | TEXT |
| title | TEXT |
| topic | TEXT |
| difficulty | TEXT |
| round | TEXT |
| platform | TEXT |
| tags | JSON |
| evidence | TEXT |

---

# Table 4 : subject_questions

Purpose

Stores Core CS questions.

Instead of four tables

(DBMS / OS / CN / OOP)

one table is used.

Columns

| Column | Type |
|---------|------|
| id | TEXT |
| structured_experience_id | TEXT |
| subject | TEXT |
| question | TEXT |
| round | TEXT |
| evidence | TEXT |

Allowed Subject Values

- DBMS
- OS
- CN
- OOP
- Aptitude
- System Design

---

# Table 5 : sql_questions

Purpose

Stores SQL interview questions.

Columns

| Column | Type |
|---------|------|
| id | TEXT |
| structured_experience_id | TEXT |
| question | TEXT |
| round | TEXT |
| evidence | TEXT |

---

# Table 6 : puzzles

Purpose

Stores logical puzzles asked during interviews.

Columns

| Column | Type |
|---------|------|
| id | TEXT |
| structured_experience_id | TEXT |
| title | TEXT |
| difficulty | TEXT |
| round | TEXT |
| evidence | TEXT |

Examples

- 25 Horses
- 100 Prisoners
- Bridge Crossing
- Poison Bottles

---

# Table 7 : hr_questions

Purpose

Stores HR and behavioural questions.

Columns

| Column | Type |
|---------|------|
| id | TEXT |
| structured_experience_id | TEXT |
| question | TEXT |
| type | TEXT |
| evidence | TEXT |

Allowed Types

- HR
- Behavioural
- Resume

---

# Table 8 : interview_rounds

Purpose

Stores complete interview flow.

Columns

| Column | Type |
|---------|------|
| id | TEXT |
| structured_experience_id | TEXT |
| round_number | INTEGER |
| round_name | TEXT |
| round_type | TEXT |
| duration | TEXT |
| difficulty | TEXT |
| summary | TEXT |

---

# Why Some Fields Use JSON

The following fields remain JSON because they are usually retrieved together rather than searched individually.

- technologies
- keywords
- tips
- mistakes
- resources
- important_concepts
- projects_discussed
- tags

Benefits

- Simpler schema
- Flexible storage
- Easier future schema evolution

---

# Indexing Strategy

Indexes should be created on frequently queried columns.

structured_experiences

- company
- role
- batch
- experience_type
- overall_difficulty

coding_questions

- topic
- title
- difficulty

subject_questions

- subject

sql_questions

- question

puzzles

- title

hr_questions

- type

These indexes optimize future retrieval and analytics.

---

# Why Evidence Is Stored

Every extracted entity stores evidence.

Example

```
Question:

LRU Cache

Evidence:

"The interviewer asked me to implement an LRU Cache using HashMap and Doubly Linked List."
```

Benefits

- Explainable AI
- Source citation
- Hallucination reduction
- Trustworthy answers

---

# Future Agent Compatibility

The extraction database is designed specifically for future LangGraph agents.

## Search Agent

Reads

- coding_questions
- subject_questions
- hr_questions
- puzzles
- keywords

Returns

Relevant interview knowledge.

---

## Pattern Agent

Reads

- coding_questions
- subject_questions
- interview_rounds
- overall_difficulty
- technologies

Finds

- common topics
- repeated questions
- company patterns

---

## Analytics Agent

Reads

- difficulty
- rounds
- topics
- results

Computes

- frequency
- distributions
- trends
- statistics

---

## Recommendation Agent

Reads

- coding_questions
- subject_questions
- tips
- resources
- mistakes

Generates

Personalized preparation roadmap.

---

## Answer Agent

Coordinates all other agents.

Produces the final natural language answer.

If required,

it can retrieve the original interview from the `interviews` table for additional context.

---

# Design Principles

The extraction database follows the following software engineering principles.

- Separation of Concerns
- Single Responsibility Principle
- Hybrid Relational Design
- Explainable AI
- Source Preservation
- Extensibility
- AI-first Retrieval
- Multi-Agent Compatibility

---

# Summary

The extraction database transforms PlacementIQ from a data collection system into a structured knowledge system.

The raw interview remains unchanged.

The AI layer builds structured knowledge on top of it.

Future agents interact primarily with the structured database while using the raw interview only when additional context or evidence is required.