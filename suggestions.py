def get_suggestion(pattern):

    if pattern == "criticism":

        return """
Communication pattern detected: Criticism

Description:
This often happens when frustration is expressed as a general statement about the other person's character.

Suggestion:
Try focusing on the specific situation instead of general statements.

Example:
Instead of "You never listen", try
"I felt unheard in that moment and wanted to explain why."
"""

    elif pattern == "defensive_response":

        return """
Communication pattern detected: Defensive response

Description:
This occurs when someone reacts to perceived blame by rejecting responsibility or counter-accusing.

Suggestion:
Acknowledge part of the concern before explaining your perspective.

Example:
"I understand why that felt frustrating. My intention was different, but I see how it came across."
"""

    elif pattern == "repair_attempt":

        return """
Communication pattern detected: Repair attempt

Description:
This is an effort to calm the interaction and restore understanding.

Suggestion:
Continue acknowledging feelings and keeping the conversation constructive.
"""

    else:

        return """
Communication pattern unclear.

Suggestion:
Try describing the situation with more details.
"""