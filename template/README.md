# Work Package Template and Acceptance Rules

This folder is the reference template for a delivery work package. It illustrates the
required layout. The template itself is reference material and is not a delivered package.

## Required layout

A delivered work package lives at:

    contributions/<contributor-handle>/<package-name>/

Every package directory must contain the following files:

| Path | Requirement |
| --- | --- |
| `README.md` | Required documentation. Must be non-empty and must contain only English text. |
| `NOTES.md` | Required documentation. Must be non-empty and must contain only English text. |
| `CHANGELOG.md` | Optional documentation. May be absent. If present and non-empty it must contain only English text. An empty CHANGELOG.md is acceptable. |
| `verification/run_checks.py` | Mandatory automation script. Must exist at exactly this relative path. |
| `metadata.json` | Mandatory package metadata. Must exist at exactly this relative path. |

## Detailed acceptance rules

1. A documentation file is considered non-empty only when it contains at least one
   non-whitespace character. A whitespace-only file counts as empty.
2. "English text only" means that every character in the documentation file must be
   part of the ASCII character set (code points U+0000 through U+007F). Any non-ASCII
   character - including CJK characters, Cyrillic, accented letters, curly quotes or
   em dashes - violates the rule.
3. The content of `verification/run_checks.py` and `metadata.json` is never inspected.
   For these files only existence is checked. Comments, language or formatting inside
   them do not affect acceptance.
4. The optional `CHANGELOG.md` rule applies only when the file is present and non-empty.
   An absent file or an empty file passes.

## Acceptance decision

A package is **complete** only when every applicable rule above passes. If any single
rule fails, the package is **in progress**.
