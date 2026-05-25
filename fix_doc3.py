import re

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 2.5 section - remove comment markers and clean up
content = content.replace(
    '***Здесь не должно быть пунктов, текст надо оформить в параграфы***',
    ''
)

content = content.replace(
    '***Это техническая информация, это не источник данных, источник данных описан выше. Это результат преобразований.***',
    ''
)

content = content.replace(
    '***Необходимо описание: что такое теплый день, я об этом уже писала, вижу, что описан в разделе выше, верно?***',
    ''
)

content = content.replace(
    '***Все то же самое, что и для графиков выше.***',
    ''
)

content = content.replace(
    '***При чем здесь слово "интерпретация" должен быть логичный связный текст, с абзацами, как в книге, а не стиль бюлютени, где просто перечилсяются факты***',
    ''
)

content = content.replace(
    '***Опять же это должен быть подраздел 2.5***',
    ''
)

content = content.replace(
    '***Вопрос к файлу такой же: нельзя ссылаться на файла на github.***',
    ''
)

content = content.replace(
    '***Чрезвычайная пожароопасность где\-то участвует в анализе?***',
    ''
)

content = content.replace(
    '***Уже писала про графики выше.***',
    ''
)

content = content.replace(
    '***Должен быть литературный текст, самостоятельные параграфы и абзацы.***',
    ''
)

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'w', encoding='utf-8') as f:
    f.write(content)
    
print('Done')