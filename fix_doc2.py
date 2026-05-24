import re

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the section header comment
content = content.replace(
    '### **2.4. Описательные характеристики климатических параметров весеннего периода по годам (2008–2023 гг.)\n\n***Этот раздел должен быть перед описание LC-кривых***',
    '### **2.4. Описательные характеристики климатических параметров весеннего периода по годам (2008–2023 гг.)**'
)

# Remove other comment markers in section 2.4
content = content.replace('#### ***Таблица 2.1.', '#### Таблица 2.1.')
content = content.replace('#### ***Таблица 2.2.', '#### Таблица 2.2.')
content = content.replace('#### ***Таблица 2.3.', '#### Таблица 2.3.')
content = content.replace('#### ***Таблица 2.4.', '#### Таблица 2.4.')

with open('Diploma/ВКР_ФИНАЛ_RED.md', 'w', encoding='utf-8') as f:
    f.write(content)
    
print('Done')