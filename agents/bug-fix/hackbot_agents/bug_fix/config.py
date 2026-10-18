# Tools that can modify the source repo — blocked under dry-run.
SOURCE_WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}

# Bugzilla MCP tool names as exposed to the agent (mcp__<server>__<tool>).
BUGZILLA_READ_TOOLS = [
    "mcp__bugzilla__search_bugs",
    "mcp__bugzilla__get_bugs",
    "mcp__bugzilla__get_bug_comments",
    "mcp__bugzilla__get_bug_attachments",
    "mcp__bugzilla__download_attachment",
]

# GitHub MCP tool names as exposed to the agent (mcp__<server>__<tool>).
GITHUB_READ_TOOLS = [
    "mcp__github__get_issue",
    "mcp__github__get_issue_comments",
    "mcp__github__get_pull_request",
    "mcp__github__get_pull_request_files",
]

# Phabricator MCP tool names as exposed to the agent (mcp__<server>__<tool>).
PHABRICATOR_READ_TOOLS = [
    "mcp__phabricator__get_revision",
    "mcp__phabricator__get_revision_comments",
    "mcp__phabricator__get_revision_diff",
]

# Action types that the agent may record in any bug-fix workflow.
BUG_FIX_ACTIONS = [
    "bugzilla.update_bug",
    "bugzilla.add_comment",
    "bugzilla.add_attachment",
    "bugzilla.create_bug",
    "try_server.push",
    "phabricator.submit_patch",
    "phabricator.update_patch",
    "phabricator.add_comment",
    "github.submit_pr",
    "github.update_pr",
    "github.add_comment",
]

# Firefox build/test tools.
FIREFOX_TOOLS = [
    "mcp__firefox__evaluate_testcase",
    "mcp__firefox__build_firefox",
    "mcp__firefox__evaluate_js_shell",
    "mcp__firefox__bootstrap_firefox",
]

def get_read_tools(platform):
    if platform == "github":
        return GITHUB_READ_TOOLS
    elif platform == "phabricator":
        return PHABRICATOR_READ_TOOLS
    elif platform == "bugzilla":
        return BUGZILLA_READ_TOOLS
    return []
