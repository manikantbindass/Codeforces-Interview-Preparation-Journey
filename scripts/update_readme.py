#!/usr/bin/env python3
"""
update_readme.py
Auto-update README.md stats (problem counts, difficulty badges)
and maintain progress tracker.

Usage: python scripts/update_readme.py
"""

import os
import re
import glob
import sys
from pathlib import Path
from datetime import datetime


def get_repo_root():
    """Get repository root directory."""
    script_dir = Path(__file__).parent
    return script_dir.parent


def count_problems(repo_root):
    """Count problem files by difficulty."""
    counts = {"easy": 0, "medium": 0, "hard": 0}
    for difficulty in counts:
        pattern = str(repo_root / "problems" / difficulty / "*.md")
        files = glob.glob(pattern)
        counts[difficulty] = len(files)
    counts["total"] = sum(counts.values())
    return counts


def get_problem_tags(repo_root):
    """Extract tags from all problem files."""
    tag_counts = {}
    for difficulty in ["easy", "medium", "hard"]:
        pattern = str(repo_root / "problems" / difficulty / "*.md")
        for filepath in glob.glob(pattern):
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            # Extract tags from the metadata line
            tag_match = re.search(r"\*\*Tags:\*\*\s*(.+)", content)
            if tag_match:
                tags_raw = tag_match.group(1)
                tags = re.findall(r"`([^`]+)`", tags_raw)
                for tag in tags:
                    tag = tag.strip()
                    if tag:
                        tag_counts[tag] = tag_counts.get(tag, 0) + 1
    return tag_counts


def update_readme_badges(repo_root, counts):
    """Update badge counts in README.md."""
    readme_path = repo_root / "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update problem count badges
    replacements = {
        r"(Problems_Solved-)\d+(-blue)": rf"\g<1>{counts['total']}\2",
        r"(Easy-)\d+(-success)": rf"\g<1>{counts['easy']}\2",
        r"(Medium-)\d+(-orange)": rf"\g<1>{counts['medium']}\2",
        r"(Hard-)\d+(-red)": rf"\g<1>{counts['hard']}\2",
    }

    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)

    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return True


def update_tracker(repo_root, counts):
    """Update progress tracker stats."""
    tracker_path = repo_root / "progress" / "tracker.md"
    if not tracker_path.exists():
        return False

    with open(tracker_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Update overall stats table
    content = re.sub(
        r"(\| Total Solved \| )\d+( \|)",
        rf"\g<1>{counts['total']}\2",
        content,
    )
    content = re.sub(
        r"^(\| Easy \| )\d+( \|)$",
        rf"\g<1>{counts['easy']}\2",
        content,
        flags=re.MULTILINE,
    )
    content = re.sub(
        r"^(\| Medium \| )\d+( \|)$",
        rf"\g<1>{counts['medium']}\2",
        content,
        flags=re.MULTILINE,
    )
    content = re.sub(
        r"^(\| Hard \| )\d+( \|)$",
        rf"\g<1>{counts['hard']}\2",
        content,
        flags=re.MULTILINE,
    )

    with open(tracker_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    return True


def update_tag_table(repo_root, tag_counts):
    """Update tags table in README with actual counts."""
    readme_path = repo_root / "README.md"
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Map common tag names to table entries
    tag_emoji_map = {
        "math": "🔢 Math",
        "arrays": "📦 Arrays",
        "implementation": "🔧 Implementation",
        "strings": "🔤 Strings",
        "sorting": "📊 Sorting",
        "trees": "🌲 Trees",
        "graphs": "🗺️ Graphs",
        "dp": "🧮 DP",
        "binary-search": "🔍 Binary Search",
        "sliding-window": "🪟 Sliding Window",
        "linked-lists": "🔗 Linked Lists",
        "stacks": "📚 Stacks/Queues",
        "queues": "📚 Stacks/Queues",
        "greedy": "🎒 Greedy",
        "backtracking": "🔙 Backtracking",
        "bit-manipulation": "🧩 Bit Manipulation",
        "game-theory": "♟️ Game Theory",
        "brute-force": "📦 Arrays",  # Group with arrays
    }

    grouped_counts = {}
    for tag, count in tag_counts.items():
        tag_lower = tag.lower().strip()
        if tag_lower in tag_emoji_map:
            emoji_name = tag_emoji_map[tag_lower]
            grouped_counts[emoji_name] = grouped_counts.get(emoji_name, 0) + count

    for emoji_name in set(tag_emoji_map.values()):
        count = grouped_counts.get(emoji_name, 0)
        status = "🟢 In Progress" if count > 0 else "🔴 Not Started"
        content = re.sub(
            rf"^\| {re.escape(emoji_name)} \| \d+ \| .+ \|$",
            f"| {emoji_name} | {count} | {status} |",
            content,
            flags=re.MULTILINE,
        )

    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    repo_root = get_repo_root()
    print("Updating repository statistics...\n")

    # Count problems
    counts = count_problems(repo_root)
    print(f"  Total: {counts['total']}")
    print(f"  Easy:  {counts['easy']}")
    print(f"  Medium: {counts['medium']}")
    print(f"  Hard:  {counts['hard']}")

    # Get tags
    tag_counts = get_problem_tags(repo_root)
    if tag_counts:
        print(f"\nTags found: {', '.join(tag_counts.keys())}")

    # Update README badges
    if update_readme_badges(repo_root, counts):
        print("\nREADME.md badges updated")

    # Update tag table
    if tag_counts:
        update_tag_table(repo_root, tag_counts)
        print("README.md tag table updated")

    # Update tracker
    if update_tracker(repo_root, counts):
        print("progress/tracker.md updated")

    print("\nAll stats updated successfully!")


if __name__ == "__main__":
    main()
