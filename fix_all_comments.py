import re

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all remaining *** markers and their content
# These are comment markers that should be removed
lines = content.split('\n')
filtered_lines = []
for line in lines:
    # Skip lines that are single-row comments (*** text ***)
    if line.strip().startswith('***') and line.strip().endswith('***'):
        continue
    # Skip lines that start with *** but have more content
    if line.strip().startswith('***') or '***' in line:
        # Remove *** markers but keep the content
        line = line.replace('***', '')
    filtered_lines.append(line)

content = '\n'.join(filtered_lines)

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
with open('Diploma/ВКР_ФИНАЛ_RED.md', 'r', encoding='utf-8') as f:
    check = f.read()
    count = check.count('***')
    print(f'Remaining *** markers: {count}')