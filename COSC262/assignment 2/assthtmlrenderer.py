"""A program to display the output of the line_edits function in an
   html table.
   Written for COSC262 DP Assignment 
   Richard Lobb February 2020.
"""

import os
import re
from html import escape
import webbrowser
import sys
from collections import deque

DEFAULT_CSS = """
table {font-size: 100%; border-collapse: collapse}
td, th  {border: 1px solid LightGrey; padding: 2px; }
td del {background-color: #FFBB00; text-decoration: none;}
"""


class HtmlTable:
    """A table to be rendered in HTML."""

    def __init__(self, column_headers):
        """The column headers is a list of strings. Its length determines the
        number of columns in the table"""
        self.headers = column_headers
        self.num_cols = len(column_headers)
        self._html = ""
        self._html += (
            "<tr>" + "".join(f"<th>{hdr}</th>" for hdr in column_headers) + "</tr>\n"
        )

    def add_row(self, values, column_styles=None):
        """Given a list of strings ('values'), the length of which must match
        the length of the list of column headers when the table was created,
        add one row to the table. column_styles is an optional list of
        strings for setting the style attributes of the row's <td>
        elements. If given, its length must match the number of columns.

        For example
           add_row(["this", "that"], ["background-color:yellow", ""])

        would add a table row containing the values 'this' and 'that' with the
        first column having a background-color of yellow. An empty style
        string is ignored.
        String values are html-escaped (i.e. characters like '&' and '<' get
        converted to HTML-entities). Then, as a special feature for this
        assignment, any sequence of characters wrapped in double square
        brackets is instead wrapped in HTML <del> elements; these are by
        default rendered with a purple background by the HTML renderer.
        Then any newline characters are converted to <br>.
        Finally the resulting string is wrapped in a <pre> element.
        """

        def td_element(value, style, i_column):
            value = escape(value)  # HTML escaping
            value = re.sub(
                r"\[\[(..*?)\]\]",
                r"<del>\1</del>",
                value,
                flags=re.DOTALL + re.MULTILINE,
            )
            value = value.replace("\n", "<br>")
            style_string = f' style="{style}"' if style else ""
            td = f"<td{style_string}><pre>{value}</pre></td>"
            return td

        if column_styles is None:
            column_styles = ["" for i in range(self.num_cols)]
        tds = [td_element(values[i], column_styles[i], i) for i in range(self.num_cols)]
        row = f"<tr>{''.join(tds)}</tr>\n"
        self._html += row

    def html(self):
        return "<table>\n" + self._html + "</table>\n"


class HtmlRenderer:
    """A class to help with displaying HTML for COSC262 Assignment 1, 2020.
    Once constructed"""

    def __init__(self, css=DEFAULT_CSS):
        """Initialise self to contain the given html string"""
        self.html = ""
        self.css = css

    def add_html(self, html):
        """Concatenate the given html to the end of the current html string"""
        self.html += html

    def render(self):
        """Display the current html in a browser window"""
        html = f"""<html><head><style>{self.css}</style></head><body>{self.html}</body></html>"""
        path = os.path.abspath("temp.html")
        with open(path, "w") as f:
            f.write(html)
        webbrowser.open("file://" + path)


def edit_table(operations):
    """Construct an HtmlTable to display the given sequence of operations, as
    returned by the line_edits function.
    """
    table = HtmlTable(["Previous", "Current"])
    grey = "background-color:LightGrey"
    for op, left, right in operations:
        if op == "C":
            table.add_row([left, right])
        elif op == "D":
            table.add_row([left, right], ["background-color:#BBBBFF", grey])
        elif op == "S":
            bg = "background-color:#FFFF99"
            table.add_row([left, right], [bg, bg])
        else:
            table.add_row([left, right], [grey, "background-color:#ABEBC6"])
    return table


# ************************************************************************
#
# Your line_edits function and any support functions goes here.


def line_edits_og_without_cache(s1, s2, na=None, nb=None):
    """
    Edit distance algorithm - bottom-up algorithm given in the lecture notes, where "Alignment" corresponds to "Copied"
    s1: previous version
    s2: current version
    returns a list of 3 element tuples (operation, left_line, right_line)
    operation: 'C', 'S', 'D' or 'I' for Copied, Substituted, Deleted and Inserted, respectively
    left_line, right_line: the contents of the left and right table cells
    left_line will be the empty string for 'I' operations and
    right_line will be empty for 'D' operations
    substitution > deletion > insertion
    """
    if na is None:
        na = len(s1)
        nb = len(s2)
    if na == 0 or nb == 0:
        return max(na, nb)
    elif s1[na - 1] == s2[nb - 1]:  # Do last chars match?
        return line_edits(s1, s2, na - 1, nb - 1)  # Yes - this is the align/copy case
    else:  # Last chars dont match
        # Must delete last a, insert last b or replace a with last b
        delete_cost = 1 + line_edits(s1, s2, na - 1, nb)
        insert_cost = 1 + line_edits(s1, s2, na, nb - 1)
        replace_cost = 1 + line_edits(s1, s2, na - 1, nb - 1)
        return min(delete_cost, insert_cost, replace_cost)


# This is my attempt at this problem
def line_edits_first_try(s1, s2):
    """
    Edit distance algorithm - bottom-up algorithm given in the lecture notes, where "Alignment" corresponds to "Copied"
    s1: previous version
    s2: current version
    returns a list of 3 element tuples (operation, left_line, right_line)
    operation: 'C', 'S', 'D' or 'I' for Copied, Substituted, Deleted and Inserted, respectively
    left_line, right_line: the contents of the left and right table cells
    left_line will be the empty string for 'I' operations and
    right_line will be empty for 'D' operations
    substitution > deletion > insertion
    """
    na = len(s1)
    nb = len(s2)

    cache = [[0] * (nb + 1) for _ in range(na + 1)]

    for i in range(1, na + 1):
        for j in range(1, nb + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] == cache[i - 1][j - 1] + 1
            else:
                # Must delete last a, insert last b or replace a with last b
                cache[i][j] = (
                    # Delete cost        insert cost      replace cost
                    min(cache[i - 1][j], cache[i][j - 1], cache[i - 1][j - 1])
                    + 1
                )

    i, j = na, nb
    tuples = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            tuples.append(("C", s1[i - 1], s1))
            i -= 1
            j -= 1
        elif cache[i - 1][j - 1] > cache[i - 1][j] > cache[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return tuples


def lcs(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)

    # Create a 2D array to store lengths of longest common subsequence.
    cache = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]

    # Fill the cache using the bottom-up approach
    for i in range(1, s1_length + 1):
        for j in range(1, s2_length + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    # Reconstruct the LCS from the cache
    i, j = s1_length, s2_length
    lcs_str = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif cache[i - 1][j] > cache[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_str))


from collections import deque


def longest_common_subsequence(s1, s2):
    """
    Find the longest common subsequence between s1 and s2.
    Returns the LCS as a deque.
    """
    s1_length = len(s1)
    s2_length = len(s2)

    # Create a 2D array to store lengths of longest common subsequence.
    cache = [[0] * (s2_length + 1) for _ in range(s1_length + 1)]

    # Fill the cache using the bottom-up approach
    for i in range(1, s1_length + 1):
        for j in range(1, s2_length + 1):
            if s1[i - 1] == s2[j - 1]:
                cache[i][j] = cache[i - 1][j - 1] + 1
            else:
                cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])

    # Reconstruct the LCS from the cache
    i, j = s1_length, s2_length
    lcs_str = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str.append(s1[i - 1])
            i -= 1
            j -= 1
        elif cache[i - 1][j] > cache[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_str))


def highlight_differences(s, lcs):
    """
    Highlight characters in s that are not part of lcs.
    """
    highlighted = []
    lcs = deque(lcs)  # Create a copy of lcs to modify
    for c in s:
        if lcs and lcs[0] == c:
            lcs.popleft()
            highlighted.append(c)
        else:
            highlighted.append(f"[[{c}]]")
    return "".join(highlighted)


def line_edits(s1, s2):
    """
    Edit distance algorithm - bottom-up algorithm given in the lecture notes,
    where "Alignment" corresponds to "Copied"
    s1: previous version
    s2: current version
    returns a list of 3 element tuples (operation, left_line, right_line)
    operation: 'C', 'S', 'D' or 'I' for Copied, Substituted, Deleted and
    Inserted, respectively
    left_line, right_line: the contents of the left and right table cells
    left_line will be the empty string for 'I' operations and
    right_line will be empty for 'D' operations
    substitution > deletion > insertion
    """
    # Split into lists of lines
    lines1 = s1.splitlines()
    lines2 = s2.splitlines()

    # Compute the edit distance using dynamic programming
    m = len(lines1)
    n = len(lines2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if lines1[i - 1] == lines2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    operations = []
    while m > 0 or n > 0:
        if m > 0 and n > 0 and lines1[m - 1] == lines2[n - 1]:
            operations.insert(0, ("C", lines1[m - 1], lines2[n - 1]))
            m -= 1
            n -= 1
        elif m > 0 and n > 0 and dp[m][n] == dp[m - 1][n - 1] + 1:
            lcs = longest_common_subsequence(lines1[m - 1], lines2[n - 1])
            left_highlighted = highlight_differences(lines1[m - 1], lcs)
            right_highlighted = highlight_differences(lines2[n - 1], lcs)
            operations.insert(0, ("S", left_highlighted, right_highlighted))
            m -= 1
            n -= 1
        elif m > 0 and dp[m][n] == dp[m - 1][n] + 1:
            operations.insert(0, ("D", lines1[m - 1], ""))
            m -= 1
        else:
            operations.insert(0, ("I", "", lines2[n - 1]))
            n -= 1

    return operations


# Example usage:
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)


# Example usage
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
# for row in table:
#     print(row)


# Example usage
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
# print(table)
# for row in table:
#     print(row)

# Example usage
s1 = "Line1\nLine3\nLine5\n"
s2 = "Twaddle\nLine5\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)


# Example usage
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
# table = line_edits(s1, s2)
# for row in table:
#     print(row)

# ************************************************************************


def main(s1, s2):
    renderer = HtmlRenderer()
    renderer.add_html("<h1>Show Differences (COSC262 2020)</h1>")
    operations = line_edits(s1, s2)
    table = edit_table(operations)
    renderer.add_html(table.html())
    renderer.render()


# Two example strings s1 and s2, follow.
# These are the same ones used in the assignment spec.

s1 = r"""# ============== DELETEs =====================
# TODO: add docstrings
@app.route('/queue/<hostname>', methods=['DELETE'])
def delete(hostname):
    try:
        data = json.loads(request.get_data())
        mac_address = data['macAddress']
    except:
        abort(400, 'Missing or invalid user data')
    status = queue.dequeue(hostname, macAddress)
    return ('', status)


@app.route('/queue', methods=['DELETE'])
def empty_queue():
    if request.remote_addr.upper() != TUTOR_MACHINE.upper():
        abort(403, "Not authorised")
    else:
        queue.clear_queue()
        response = jsonify({"message": "Queue emptied"})
        response.status_code = 204
        return response
"""

s2 = r'''# ============== DELETEs =====================
@app.route('/queue/<hostname>', methods=['DELETE'])
def delete(hostname):
    """Handle delete request from the given host"""
    try:
        data = json.loads(request.get_data())
        mac_address = data['mac_address']
    except:
        abort(400, 'Missing or invalid user data')
    status = queue.dequeue(hostname, mac_address)
    return ('', status)


@app.route('/queue', methods=['DELETE'])
def clear_queue():
    """Clear the queue. Valid only if coming from tutor machine"""
    if request.remote_addr.upper() != TUTOR_MACHINE.upper():
        abort(403, "Only the tutor machine can clear the queue")
    else:
        queue.clear_queue()
        response = jsonify({"message": "Queue cleared"})
        response.status_code = 204
        return response
'''

# main(s1, s2)
