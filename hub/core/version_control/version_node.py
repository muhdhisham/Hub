from datetime import datetime
from typing import List, Optional


class VersionNode:
    def __init__(self, branch: str, commit_id: Optional[str] = None):
        self.commit_id = commit_id
        self.branch = branch
        self.children: List["VersionNode"] = []
        self.parent: Optional["VersionNode"] = None
        self.commit_message = None
        self.commit_time = None
        self.commit_user_name = None

    def add_child(self, node: "VersionNode"):
        """Adds a child to the node, used for branching."""
        node.parent = self
        self.children.append(node)

    def add_successor(self, node: "VersionNode", message: Optional[str] = None):
        """Adds a successor (a type of child) to the node, used for commits."""
        node.parent = self
        self.children.append(node)
        self.commit_message = message
        user_name = "public"  # TODO: fetch username
        self.commit_user_name = "None" if user_name == "public" else user_name
        self.commit_time = datetime.now()

    def __repr__(self) -> str:
        return f'commit {self.commit_id} ({self.branch}) \nAuthor: {self.commit_user_name}\nCommit Time:  {str(self.commit_time)[:-7]}\nMessage: "{self.commit_message}"'

    __str__ = __repr__