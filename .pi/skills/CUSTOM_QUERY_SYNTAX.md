---
name: custom-query-filter-syntax
description: Use this skill whenever the user asks to build, write, or embed a filter/query string in this codebase's custom query language (the one parsed by the ply-based tokenizer.py/parser.py with tokens EQUALS, AND, OR, NOT, LPAREN, RPAREN, WORD, NUMBER, NOT_EQUALS, DATE, GT, LT, GTE, LTE) — including when the goal is to construct a URL, API request, or "sysparm_query"-style parameter that carries this filter syntax. Trigger on requests like "filter where status is active and priority is greater than 3", "build a query string for this", "write the URL for this search", or any mention of AND/OR/NOT filters, field comparisons, or date-range filters that need to go into this system. Do NOT use for SQL, JSON filters, or any other query DSL — this is specifically for the `^` / `|` / `!` symbolic grammar defined by this project's lexer and parser.
---

# Custom Query Filter Syntax

This project parses filter strings with a hand-rolled `ply` lexer + parser (see
`tokenizer.py` and `parser.py`). The parser turns the compact symbolic syntax
below into a readable SQL-like string internally (e.g. `status=active` becomes
`status = 'active'`) — but **the string you write must use the compact
symbolic syntax**, not the SQL-like output.

Use this skill any time you need to hand-author or generate one of these
filter strings, including when it will be embedded as a query-string
parameter in a URL.

## Operator cheat sheet

| Meaning        | Symbol | Example                    |
|----------------|--------|----------------------------|
| AND            | `^`    | `status=active^priority>3` |
| OR             | `\|`   | `status=open\|status=pending` |
| NOT            | `!`    | `!(status=closed)`         |
| Equals         | `=`    | `status=active`            |
| Not equals     | `!=`   | `status!=closed`           |
| Greater than   | `>`    | `priority>3`               |
| Less than      | `<`    | `priority<8`               |
| Greater/equal  | `>=`   | `created>=2024-01-01`      |
| Less/equal     | `<=`   | `created<=2024-12-31`      |
| Group          | `( )`  | `(status=open\|status=pending)^owner=alice` |

There is **no implicit AND** — two terms next to each other must be joined
explicitly with `^`. There is no whitespace-as-separator between terms.

## Grammar rules (from parser.py)

A query is an `expression`, built from `term`s:

- `expression AND expression` → written as `expression^expression`
- `expression OR expression` → written as `expression|expression`
- `NOT expression` → written as `!expression`
- `(expression)` for grouping — parentheses may wrap a full expression or a
  single term
- A `term` is one comparison:
  - `field=value`
  - `field!=value`
  - `field>comparable`
  - `field<comparable`
  - `field>=comparable`
  - `field<=comparable`

**Precedence** (low → high): `AND`/`OR` (same level, left-associative) < `NOT`
(right-associative, binds tighter). Use parentheses whenever you mix AND and
OR, or whenever precedence isn't obvious — the parser will happily accept
ambiguous-looking input but you should still group explicitly for clarity and
correctness, e.g.:

```
(status=open|status=pending)^assigned_to=alice
```

not

```
status=open|status=pending^assigned_to=alice   # AND binds same as OR here — group it
```

## Fields

- A `field` is a bare `WORD` token (see below) and **must not contain a
  space** — the grammar raises a parsing error (`Field may not contain
  space.`) if it does. Use identifiers like `status`, `assigned_to`,
  `created_date`.
- Never quote a field.

## Values

Two kinds of value can appear on the right-hand side of `=` / `!=`:

1. **`WORD` (bare string)** — write it **unquoted**. The parser adds the
   quotes internally (`name=John` → `name = 'John'`). Do not write
   `name='John'` yourself.
   - `WORD` must start with a letter (`a-z`/`A-Z`).
   - After the first letter it may contain letters, digits, `_`, `-`, `:`,
     `.`, and internal spaces (so multi-word values like `name=John Smith`
     are valid).
   - It must **end** in a word character or `-` — it cannot end with a
     trailing space, `.`, or `:`. Avoid trailing whitespace before an
     operator/paren.
2. **`comparable`** — a `NUMBER` or a `DATE`:
   - `NUMBER`: optional leading `-`, digits, optional decimal part
     (`3`, `-4`, `3.5`). No commas, no scientific notation.
   - `DATE`: `YYYY-M-D` or `YYYY-MM-DD` (e.g. `2024-1-5` or `2024-01-05`).
     It's parsed with `dateutil` and normalized to ISO `YYYY-MM-DD`, and gets
     quoted in the output automatically — write it **unquoted**.

`>`, `<`, `>=`, `<=` only accept a `comparable` (`NUMBER` or `DATE`) on the
right-hand side — you cannot use them to compare against a bare string.
`=` and `!=` accept either a `WORD` or a `comparable`.

## Worked examples

| Intent | Query string |
|---|---|
| Active status | `status=active` |
| Not closed | `status!=closed` |
| Active AND high priority | `status=active^priority>3` |
| Open OR pending | `status=open\|status=pending` |
| Not closed, grouped | `!(status=closed)` |
| Date range | `created>=2024-01-01^created<=2024-12-31` |
| Mixed AND/OR, grouped | `(status=open\|status=pending)^assigned_to=alice` |
| Multi-word value | `name=John Smith^department=Customer Success` |
| Nested grouping | `(priority>3^status=open)\|(priority>=8^!status=closed)` |

## Embedding in a URL

When the finished filter string is placed inside an actual URL (e.g. as a
query-string parameter like `?filter=...`), percent-encode it as you would
any query value — encode characters such as space (` ` → `%20` or `+`),
`^`, `|`, `!`, `(`, `)`, `=`, `>`, `<` if the target consuming system requires
strict encoding. Build the raw filter string first using the rules above,
then URL-encode the whole string as the final step — don't try to encode and
apply grammar rules at the same time.

## Common mistakes to avoid

- Quoting values yourself (`status='active'`) — write `status=active`.
- Using a space or plain word next to another term without `^`/`|` — there's
  no implicit AND.
- Putting a space inside a `field` name.
- Comparing a string with `>`/`<`/`>=`/`<=` — only numbers and dates are
  allowed there.
- Leaving ambiguous AND/OR chains ungrouped — always parenthesize mixed
  AND/OR expressions.
- Malformed dates (e.g. missing parts) — always use `YYYY-M-D` or
  `YYYY-MM-DD`.