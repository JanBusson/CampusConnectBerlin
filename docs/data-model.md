---
title: Data Model
parent: Technical Docs
nav_order: 3
---

[Kaan Baskaya]
{: .label }

# Data model
{: .no_toc }

Our web application focuses on enabling friendships between students by using personality based matching. The core functionalities are: user registration, login, storing personality test results, swiping other users, and matches when both users like each other.

The following database tables support these functions: `user`, `university`, `personality_result`, `swipe`, and `match`.

Below is the breakdown of the relevant attributes, their types, and constraints.

# Table for Users

<details open markdown="block">
<summary>- User/</summary>
<pre>
  "user_id"       INTEGER PRIMARY KEY,
  "uni_id"        INTEGER,
  "name"          TEXT NOT NULL,
  "email"         TEXT UNIQUE NOT NULL,
  "password"      TEXT NOT NULL,
  "age"           INTEGER,
  "created_at"    DATE DEFAULT CURRENT_DATE,
  FOREIGN KEY ("uni_id") REFERENCES university("uni_id")
</pre>
</details>

# Table for Universities

<details open markdown="block">
<summary>- University/</summary>
<pre>
  "uni_id"        INTEGER PRIMARY KEY,
  "name"          TEXT NOT NULL,
  "short_name"    TEXT,
  "location"      TEXT
</pre>
</details>

# Table for Personality Test Results

<details open markdown="block">
<summary>- Personality_Result/</summary>
<pre>
  "result_id"     INTEGER PRIMARY KEY,
  "user_id"       INTEGER,
  "vec_ei"        FLOAT,
  "vec_sn"        FLOAT,
  "vec_tf"        FLOAT,
  "vec_jp"        FLOAT,
  "mbti_type"     TEXT,
  "completed_at"  DATE,
  FOREIGN KEY ("user_id") REFERENCES user("user_id")
</pre>
</details>

# Table for Swipes

<details open markdown="block">
<summary>- Swipe/</summary>
<pre>
  "swipe_id"        INTEGER PRIMARY KEY,
  "swiper_id"       INTEGER,
  "swiped_id"       INTEGER,
  "swipe_type"      TEXT,  -- "like" or "dislike"
  "swiped_at"       DATE,
  "match_generated" BOOLEAN DEFAULT FALSE,
  FOREIGN KEY ("swiper_id") REFERENCES user("user_id"),
  FOREIGN KEY ("swiped_id") REFERENCES user("user_id")
</pre>
</details>

# Table for Matches

<details open markdown="block">
<summary>- Match/</summary>
<pre>
  "match_id"      INTEGER PRIMARY KEY,
  "user1_id"      INTEGER,
  "user2_id"      INTEGER,
  "compatibility" FLOAT,
  "status"        TEXT,  -- e.g., "active", "expired"
  "matched_at"    DATE,
  FOREIGN KEY ("user1_id") REFERENCES user("user_id"),
  FOREIGN KEY ("user2_id") REFERENCES user("user_id")
</pre>
</details>

**Constraints:**

Most fields use `NOT NULL` where appropriate to ensure data integrity. Foreign keys are used to enforce relationships between users and universities, test results, swipes, and matches.
