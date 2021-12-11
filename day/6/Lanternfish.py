class Lanternfish:
    """
    Lanternfish is a fish from the challenge of the advent of code.
    """
    def __init__(self, time: int):
        """Lanternfish is a fish from the challenge of the advent of code.
        >>> lanternfish = Lanternfish(8)
        >>> print(lanternfish.time)
        8
        >>> lanternfish.time = 2
        >>> print(lanternfish.time)
        2
        """
        self.time = time

    def pass_a_day(self):
        """
        >>> lanternfish = Lanternfish(8)
        >>> print(lanternfish.time)
        8
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> lanternfish.pass_a_day()
        >>> print(lanternfish.time)
        0
        >>> lanternfish.pass_a_day()
        Lanternfish(8)
        >>> print(lanternfish.time)
        6
        """
        self.time -= 1
        if self.time == -1:
            self.time = 6
            return Lanternfish(8)
        return None
    
    def __str__(self) -> str:
        return f'f({self.time})'
    
    def __repr__(self) -> str:
        return f'Lanternfish({self.time})'

if __name__ == "__main__":
    import doctest
    doctest.testmod()