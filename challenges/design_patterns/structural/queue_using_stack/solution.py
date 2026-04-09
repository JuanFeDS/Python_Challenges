"""
Implementación de una cola (Queue) usando solo pilas (stacks).

Problema:
---------
Implementar una estructura de datos tipo cola (FIFO: First In, First Out)
utilizando únicamente operaciones válidas de una pila (LIFO: Last In, First Out).

La cola debe soportar los métodos:
- push(x): agrega el elemento x al final de la cola.
- pop(): elimina y retorna el elemento al frente de la cola.
- peek(): retorna el elemento al frente sin eliminarlo.
- empty(): retorna True si la cola está vacía, False en caso contrario.

Restricciones:
--------------
- Solo se pueden usar operaciones estándar de una pila:
  - agregar al final (append)
  - quitar desde el final (pop)
  - mirar el último elemento
  - comprobar si está vacía
- 1 <= x <= 9
- Se harán como máximo 100 llamadas a los métodos.
"""

class MyQueue:
    """Cola implementada utilizando dos pilas (listas en Python)."""

    def __init__(self):
        """Inicializa la cola vacía."""
        # stack_in = pila donde entran los elementos
        # stack_out = pila desde donde salen los elementos
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        Inserta un elemento al final de la cola.
        Operación sencilla: siempre se hace en stack_in.
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        Elimina y retorna el elemento que está al frente de la cola.
        Si stack_out está vacío, se transfieren todos los elementos
        desde stack_in a stack_out (invirtiendo el orden).
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

    def peek(self) -> int:
        """
        Retorna el elemento al frente de la cola sin eliminarlo.
        Aplica la misma lógica de transferencia que pop().
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        """
        Retorna True si la cola está vacía, False en caso contrario.
        La cola está vacía solo si ambas pilas lo están.
        """
        return not self.stack_in and not self.stack_out


if __name__ == "__main__":
    # Casos de prueba rápidos
    queue = MyQueue()
    print("¿Está vacía?", queue.empty())  # True
    queue.push(1)
    queue.push(2)
    print("Frente:", queue.peek())        # 1
    print("Eliminado:", queue.pop())      # 1
    print("¿Está vacía?", queue.empty())  # False
    print("Eliminado:", queue.pop())      # 2
    print("¿Está vacía?", queue.empty())  # True
