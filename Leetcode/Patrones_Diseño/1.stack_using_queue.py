"""
Implementación de una pila (Stack) usando solo una cola (deque).

Problema:
---------
Implementar una estructura de datos tipo pila (LIFO: Last In, First Out)
utilizando únicamente operaciones válidas de una cola (FIFO: First In, First Out).

La pila debe soportar los métodos:
- push(x): agrega el elemento x en la parte superior de la pila.
- pop(): elimina y retorna el elemento en la parte superior de la pila.
- top(): retorna el elemento en la parte superior sin eliminarlo.
- empty(): retorna True si la pila está vacía, False en caso contrario.

Restricciones:
--------------
- Solo se pueden usar operaciones de cola estándar:
  - agregar al final (append)
  - quitar desde el frente (popleft)
  - mirar el frente
  - comprobar si está vacía
- 1 <= x <= 9
- Se harán como máximo 100 llamadas a los métodos.
"""

from collections import deque

class MyStack:
    """Pila implementada utilizando una sola cola (deque)."""

    def __init__(self):
        """Inicializa la pila vacía."""
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Inserta un elemento en la pila.
        Después de insertarlo, rota la cola para que el nuevo
        elemento quede al frente (simulando el comportamiento LIFO).
        """
        self.q.append(x)
        # Rotar la cola n-1 veces
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Elimina y retorna el elemento que está en la parte superior de la pila.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Retorna el elemento en la parte superior sin eliminarlo.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Retorna True si la pila está vacía, False en caso contrario.
        """
        return not self.q


if __name__ == "__main__":
    # Casos de prueba rápidos
    stack = MyStack()
    print("¿Está vacía?", stack.empty())  # True
    stack.push(1)
    stack.push(2)
    print("Elemento arriba:", stack.top())  # 2
    print("Eliminado:", stack.pop())        # 2
    print("¿Está vacía?", stack.empty())    # False
