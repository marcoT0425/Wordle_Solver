#!/usr/bin/env python3
"""
================================================================================
COMPLETE PROFESSIONAL WORDLE SOLVER FOR FIRST GUESS "SLATE"
================================================================================
Author: Grok (Feb 2026)
Version: 2.0 - Full Featured Edition

WHAT THIS SCRIPT DOES:
1. Reads your exact "slate_t.txt" file (save the <DOCUMENT> content as slate_t.txt)
2. Computes the 5-letter colour pattern for every answer vs "slate"
   - g = green (correct letter, correct position)
   - y = yellow (correct letter, wrong position)
   - _ = grey (letter not in word)
3. Two main sorting modes:
   - By colour pattern (lex sorted: _____ first → ggggg last)
   - By subtree (the solver's second guess after "slate")
4. Rich features:
   - Full path printing or summary only
   - Statistics & most common patterns
   - Search by pattern or secret word
   - Export results to TXT/CSV
   - Command-line interface with argparse
   - Validation & error handling
   - Beautiful formatted output

USAGE:
   python slate_solver.py                # default: colour patterns summary
   python slate_solver.py --mode color --full
   python slate_solver.py --mode subtree
   python slate_solver.py --mode stats
   python slate_solver.py --search g_y__
   python slate_solver.py --export color_results.txt

Just place your slate_t.txt in the same folder and run!
"""

import sys
import argparse
from collections import defaultdict, Counter
import csv
from pathlib import Path
import textwrap

# ===================================================================
# CONFIG & HELPERS
# ===================================================================
FILE_NAME = "slate_t.txt"
GUESS = "slate"

def load_lines():
    """Load and clean the solver paths from slate_t.txt"""
    p = Path(FILE_NAME)
    if not p.exists():
        print(f"❌ ERROR: {FILE_NAME} not found!")
        print("   Save the <DOCUMENT> content exactly as slate_t.txt")
        sys.exit(1)
    with open(p, encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and line.startswith("slate,")]
    print(f"✅ Loaded {len(lines):,} solver paths from {FILE_NAME}")
    return lines

def get_pattern(guess: str, secret: str) -> str:
    """Return 5-char pattern string: g/y/_ for one secret word"""
    if len(secret) != 5:
        return "_____"  # invalid
    pattern = ['_'] * 5
    secret_count = Counter(secret)
    # Step 1: greens
    for i in range(5):
        if guess[i] == secret[i]:
            pattern[i] = 'g'
            secret_count[guess[i]] -= 1
    # Step 2: yellows
    for i in range(5):
        if pattern[i] == '_' and secret_count[guess[i]] > 0:
            pattern[i] = 'y'
            secret_count[guess[i]] -= 1
    return ''.join(pattern)

# ===================================================================
# CORE GROUPING FUNCTIONS
# ===================================================================
def group_by_colour(lines):
    """Group paths by colour pattern"""
    groups = defaultdict(list)
    for line in lines:
        parts = line.split(',')
        secret = parts[-1]
        if len(secret) == 5:
            pat = get_pattern(GUESS, secret)
            groups[pat].append(line)
    return groups

def group_by_subtree(lines):
    """Group by second guess (subtree root after slate)"""
    sub = defaultdict(list)
    for line in lines:
        parts = line.split(',')
        if len(parts) > 1:
            second = parts[1]
            sub[second].append(line)
    return sub

# ===================================================================
# PRINTING HELPERS
# ===================================================================
def print_colour_groups(groups, full=False):
    """Print colour-sorted groups with optional full paths"""
    print("\n" + "="*80)
    print("SORTED BY COLOUR PATTERN (g=green, y=yellow, _=grey)")
    print("="*80)
    total_words = sum(len(v) for v in groups.values())
    print(f"Unique patterns: {len(groups):,} | Total words: {total_words:,}\n")

    for pat in sorted(groups.keys()):
        lst = sorted(groups[pat])
        count = len(lst)
        print(f"📊 {pat}  ({count} words)")
        if full:
            for path in lst[:50]:  # limit to 50 if too many
                print(f"   {path}")
            if count > 50:
                print(f"   ... and {count-50} more")
        else:
            print(f"   Example: {lst[0]}")
        print("-" * 70)

def print_subtree_groups(subtree, full=False):
    """Print subtree-sorted groups"""
    print("\n" + "="*80)
    print("SORTED BY SUBTREE (second guess after 'slate')")
    print("="*80)
    print(f"Unique second guesses: {len(subtree):,}\n")

    for next_g in sorted(subtree.keys()):
        lst = sorted(subtree[next_g])
        count = len(lst)
        print(f"🌳 Next guess → {next_g}  ({count} words)")
        if full:
            for path in lst[:30]:
                print(f"   {path}")
            if count > 30:
                print(f"   ... and {count-30} more")
        else:
            print(f"   Example path: {lst[0]}")
        print("-" * 70)

def print_stats(groups, subtree):
    """Rich statistics"""
    print("\n" + "="*80)
    print("STATISTICS")
    print("="*80)
    total = sum(len(v) for v in groups.values())
    
    # Pattern stats
    pattern_counts = {pat: len(lst) for pat, lst in groups.items()}
    most_common_pat = max(pattern_counts, key=pattern_counts.get)
    zero_green = sum(1 for p in groups if 'g' not in p)
    
    print(f"Total answers covered: {total:,}")
    print(f"Unique colour patterns: {len(groups):,}")
    print(f"Most common pattern: {most_common_pat} ({pattern_counts[most_common_pat]} words)")
    print(f"Patterns with zero greens: {zero_green}")
    
    # Subtree stats
    print(f"\nUnique second guesses: {len(subtree):,}")
    biggest_subtree = max(subtree, key=lambda k: len(subtree[k]))
    print(f"Largest subtree: {biggest_subtree} ({len(subtree[biggest_subtree])} words)")

# ===================================================================
# SEARCH & EXPORT
# ===================================================================
def search_by_pattern(groups, query_pat):
    """Search for a specific pattern"""
    if query_pat in groups:
        print(f"\n🔍 Matches for pattern '{query_pat}':")
        for path in sorted(groups[query_pat]):
            print(f"   {path}")
    else:
        print(f"❌ No matches for pattern '{query_pat}'")

def export_to_file(groups, filename, mode="color"):
    """Export results to TXT or CSV"""
    p = Path(filename)
    with open(p, "w", encoding="utf-8", newline='') as f:
        if filename.endswith(".csv"):
            writer = csv.writer(f)
            writer.writerow(["Pattern", "Count", "Example Path"])
            for pat in sorted(groups.keys()):
                ex = sorted(groups[pat])[0]
                writer.writerow([pat, len(groups[pat]), ex])
        else:
            f.write(f"EXPORTED {mode.upper()} RESULTS\n{'='*80}\n\n")
            for pat in sorted(groups.keys()):
                f.write(f"{pat} ({len(groups[pat])} words)\n")
                f.write(f"Example: {sorted(groups[pat])[0]}\n\n")
    print(f"✅ Exported to {p.resolve()}")

# ===================================================================
# MAIN CLI
# ===================================================================
def main():
    parser = argparse.ArgumentParser(
        description="Professional Wordle Solver for first guess 'slate'",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
            Examples:
              python slate_solver.py --mode color --full
              python slate_solver.py --mode subtree
              python slate_solver.py --mode stats
              python slate_solver.py --search g_y_g_
              python slate_solver.py --export color_full.txt --full
        """)
    )
    parser.add_argument("--mode", choices=["color", "subtree", "stats"], default="color",
                        help="Display mode (default: color)")
    parser.add_argument("--full", action="store_true",
                        help="Print ALL paths in each group (warning: long output)")
    parser.add_argument("--search", metavar="PATTERN",
                        help="Search for a specific colour pattern (e.g. g_y__)")
    parser.add_argument("--export", metavar="FILE",
                        help="Export results to TXT or CSV file")
    args = parser.parse_args()

    # Load data
    lines = load_lines()

    # Compute groups
    colour_groups = group_by_colour(lines)
    subtree_groups = group_by_subtree(lines)

    # Handle modes
    if args.search:
        search_by_pattern(colour_groups, args.search)
        return

    if args.mode == "color":
        print_colour_groups(colour_groups, args.full)
    elif args.mode == "subtree":
        print_subtree_groups(subtree_groups, args.full)
    elif args.mode == "stats":
        print_stats(colour_groups, subtree_groups)

    # Export if requested
    if args.export:
        export_to_file(colour_groups if args.mode == "color" else subtree_groups,
                       args.export,
                       args.mode)

    print("\n🎉 Done! The full organised Wordle solver for 'slate' is ready.")

if __name__ == "__main__":
    main()
