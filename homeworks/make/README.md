## Введение
Данный проект посвящен внедрению практик автоматизации и контроля качества кода в экосистему Python.
## 1. Работа с окружением (Stateless & Isolated)
В проекте реализован принцип **изолированного окружения**. Вместо ручной активации виртуальной среды (`source activate`), `Makefile` обращается к интерпретатору и бинарным файлам инструментов напрямую через путь `.venv/bin/`. Это гарантирует, что команды выполняются именно в контексте проекта, независимо от состояния системного Python.

### Создание окружения
Для создания окружения и установки в него всех инструментов используйте команду `make install`.

### Механика работы:

* Автоматическое создание: Если директория `.venv/` отсутствует, Make вызовет системный модуль venv для её инициализации.

* Установка зависимостей: После создания окружения Make использует локальный бинарный файл pip (.venv/bin/pip) для установки пакетов из requirements.txt.

* Связанность задач: Следующие таргеты имеют install в качестве зависимости. Это означает, что при попытке запустить любую проверку в "чистом" репозитории, Make сначала самостоятельно развернет окружение.
## 2. Управление зависимостями (By-Design)
Для обеспечения целостности проекта используется инструмент `deptry`. Он сопоставляет импорты в исходном коде (`src/`) с объявленными пакетами в `requirements.txt`.

### Демонстрация проверки:
Для проверки работоспособности в файл `src/service.py` были добавлены импорты библиотек, отсутствующих в конфигурации(код из задания).
**Лог ошибки при запуске `make check-requirements` до добавления библиотек в `requirements.txt`:**
```bash
src/service.py:2:8: DEP001 'numpy' imported but missing from the dependency definitions
src/service.py:3:8: DEP001 'fastapi' imported but missing from the dependency definitions
```
**Также инструмент выявляет лишние импорты:**
```bash
requirements.txt: DEP002 'deptry' defined as a dependency but not used in the codebase
requirements.txt: DEP002 'mypy' defined as a dependency but not used in the codebase
requirements.txt: DEP002 'flake8' defined as a dependency but not used in the codebase
```
Это подтверждает, что автоматизация успешно выявляет несоответствия между кодом и средой развертывания.

## 3. Статический анализ типов
Внедрение `mypy` позволяет отлавливать логические ошибки до этапа выполнения. В файле `src/calc.py` намеренно создана ситуация передачи несовместимых типов (строка вместо целого числа).

**Результат работы `make typecheck`:**
```bash
src/calc.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
```
Добавлен исправленный код `corrected_calc.py`, для проверки работы при правильном использовании

## 4. Контроль стиля (Linting)
Соблюдение стандарта **PEP 8** автоматизировано с помощью `flake8`. Это гарантирует единообразие кода во всей команде.

**Пример обнаруженных нарушений `make lint` (неиспользуемые импорты, лишние пробелы):**
```bash
src/app.py:1:1: F401 'requests' imported but unused
src/app.py:3:21: W292 no newline at end of file
src/calc.py:4:1: E305 expected 2 blank lines after class or function definition, found 1
src/calc.py:4:26: W292 no newline at end of file
src/example.py:1:9: E201 whitespace after '('
src/example.py:1:11: E231 missing whitespace after ','
src/example.py:1:13: E202 whitespace before ')'
src/example.py:2:2: E111 indentation is not a multiple of 4
src/example.py:2:12: W292 no newline at end of file
src/service.py:1:1: F401 'requests' imported but unused
src/service.py:3:1: F401 'fastapi' imported but unused
src/service.py:5:27: W292 no newline at end of file
```
Добавлен исправленный код `corrected_calc.py` и `corrected_example`
## 5. Цепочки зависимостей (Pipeline)
Ключевой особенностью решения является использование графа зависимостей Make. Создан составной target `check`, который объединяет все проверки в единый конвейер.

### Порядок запуска:
`check` → `lint` → `typecheck` → `check-requirements`

Если любой из этапов завершается с ошибкой (non-zero exit code), Make прерывает выполнение цепочки. При выполнении команды так и будет. Я оставил код с ошибками для проверки выполнения заданий.


