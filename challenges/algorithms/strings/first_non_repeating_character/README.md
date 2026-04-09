# 🧩 First Non-Repeating Character

**🌐 Plataforma:** CodeWars  
**⚡ Dificultad:** Medium  
**📂 Categoría:** algorithms › strings  
**⏱️ Tiempo de resolución:** ~20 min  

---

## 📋 Problema

Dada una cadena de texto, encontrar el primer carácter que no se repite y retornarlo. Si todos los caracteres se repiten, retornar una cadena vacía `""`. La búsqueda es case-insensitive, pero el retorno conserva el case original.

---

## 🔢 Ejemplos

| Input | Output |
|-------|--------|
| `"stress"` | `"t"` |
| `"sTreSS"` | `"t"` |
| `"aabbcc"` | `""` |
| `"a"` | `"a"` |

---

## 🧠 Enfoque

El problema se reduce a contar frecuencias de cada carácter y luego hacer una segunda pasada para encontrar el primero con frecuencia 1. Usé un diccionario de conteos construido con comprensión de diccionario, iterando sobre la cadena en minúsculas para manejar el case-insensitive. Luego filtré los únicos y tomé el primero.

El truco está en mantener el **orden de aparición** al retornar: por eso se itera sobre `s` original (no sobre el diccionario).

---

## 💡 Mi solución

```python
def first_non_repeating_character(s: str) -> str:
    s_lower = s.lower()

    dict_count = {char: s_lower.count(char) for char in s_lower}

    unique_chars = [char for char in s if dict_count[char.lower()] == 1]

    return unique_chars[0] if unique_chars else ""
```

### 📊 Complejidad

|            | Complejidad |
|------------|-------------|
| ⏱️ Tiempo  | O(n²) — `str.count()` recorre la cadena completa por cada carácter |
| 🗂️ Espacio | O(k) — donde k es el número de caracteres únicos |

---

## 🤖 Solución con feedback IA

El cuello de botella es usar `str.count()` dentro de la comprensión: por cada carácter recorre toda la cadena, resultando en O(n²). La solución óptima construye el conteo en una sola pasada con `Counter`.

```python
from collections import Counter

def first_non_repeating_character(s: str) -> str:
    counts = Counter(s.lower())
    return next((char for char in s if counts[char.lower()] == 1), "")
```

### 📊 Complejidad

|            | Complejidad |
|------------|-------------|
| ⏱️ Tiempo  | O(n) — una pasada para contar, una para encontrar |
| 🗂️ Espacio | O(k) — donde k es el número de caracteres únicos |

---

## 🏷️ Conceptos clave

`hash map` `frequency counting` `string traversal` `case-insensitive`

---

## 📚 Para profundizar

- [collections.Counter — documentación oficial](https://docs.python.org/3/library/collections.html#collections.Counter)
- [Generators y next() en Python](https://docs.python.org/3/glossary.html#term-generator)
- LeetCode 387 — First Unique Character in a String

---

## ✍️ Lecciones aprendidas

- `str.count()` dentro de una comprensión genera O(n²). `Counter` resuelve lo mismo en O(n).
- `next()` con valor por defecto es más idiomático que construir una lista completa para tomar solo el primer elemento.
