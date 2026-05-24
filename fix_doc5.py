import re

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Chapter 4
content = content.replace(
    '**Где приведены эти вычисления? Они должны быть выделены в отдельную главу.**',
    ''
)

content = content.replace(
    '***Должны быть ссылки на нормативные акты, откуда взят именно такое реагирование МЧС. Объяснение, почему именно такие меры?***',
    ''
)

content = content.replace(
    '***То же самое.***',
    ''
)

content = content.replace(
    '***Не научная формулировка.***',
    ''
)

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'w', encoding='utf-8') as f:
    f.write(content)
    
print('Done')