# PyPI Domains Extractor

Это библиотека для извлечения доменов PyPI (pypi.org и test.pypi.org).
Создана в рамках выполнения домашнего задания по курсу "Культура разработки программного обеспечения с открытым исходным кодом".

## Установка

Вы можете установить этот пакет напрямую из TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ pypi-domains-extractor
```

## Использование

```python
from pypi_domains_extractor import getPypiDomains

domains = getPypiDomains()
print(domains)
```

## Разработка и автоматизация (Makefile)

Проект использует `Makefile` для автоматизации основных действий:

1. **`make install`** - Устанавливает виртуальное окружение `.venv` и все необходимые зависимости, включая `dev`-группу из `pyproject.toml`.
2. **`make lint`** - Проверка стиля кода с помощью `flake8`.
3. **`make typecheck`** - Статический анализ типов с помощью `mypy`.
4. **`make test`** - Запуск юнит-тестов с помощью `pytest`.
5. **`make check-requirements`** - Проверка зависимостей с помощью `deptry`.
6. **`make check`** - Запускает весь пайплайн проверок (lint -> typecheck -> check-requirements -> test).
7. **`make build`** - Сборка проекта (sdist и wheel) с помощью модуля `build`. Артефакты будут помещены в папку `dist/`.
8. **`make publish`** - Загрузка собранного пакета на TestPyPI (требует настройки токена).
9. **`make docs`** - Простая цель, указывающая на README (так как проект маленький).

Проект использует `pyproject.toml` в качестве точки входа для сборки и описания зависимостей.
