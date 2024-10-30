In UTF-8 encoding:

Each character can be represented by 1 to 4 bytes.
The encoding follows specific patterns depending on the number of bytes:
1-byte (ASCII): 0xxxxxxx
2-byte: 110xxxxx 10xxxxxx
3-byte: 1110xxxx 10xxxxxx 10xxxxxx
4-byte: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Each 10xxxxxx byte indicates a continuation byte. The leading bits of the first byte (e.g., 110 for 2 bytes) determine the total byte count for that character.

Checklist
Mask and Check each byte:
Use bitwise operations to extract the first few bits of each byte and verify patterns.
Determine byte sequence length:
The first byte indicates how many bytes the character occupies.
Validate Continuation Bytes:
Ensure subsequent bytes begin with 10.
Iterate and Validate Entire Data:
Loop through data list, skipping over validated continuation bytes.
