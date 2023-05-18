BASE = r"""Export of Github issues for [{repo_name}]({repo_url}).{datestring}

{issues}
"""
ISSUE = r"""- [[GitHub/{number}]] [link]({url})
    - tags:: {labels}
      IssueRank:: {issue_rank_score}
    - {title}
    - {issue_rank_comment}
	- [[GitHub/User/{author}]][link]({author_url}) opened issue at {date}
"""

COMMENT = ""

ISSUE_FILE_FOOTNOTE = ""
