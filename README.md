#### This is a track board for LogSeq issues.

Run: `GITHUB_ACCESS_TOKEN=<YOURTOKEN> python ranker/gh2md.py logseq/logseq logseq-issues.md --no-closed-prs --no-closed-issues`

Algorithm v 0.0.1:
```
(<num-of-comments> * 2 + <num-of-emoji>) * <last-response-decay>
```

#### Credits:
https://github.com/mattduck/gh2md
Adopt to LogSeq's Markdown format, with the info of interest.
