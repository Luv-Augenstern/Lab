# Base class Figure
class Figure:
    def __init__(self, a: float, b: float, c: float):
        # Store the dimensions as instance attributes
        self.a = a  # Dimension a (length)
        self.b = b  # Dimension b (width)
        self.c = c  # Dimension c (height)

    def volume(self) -> float:
        """Method 1: Calculate volume V = a * b * c"""
        # Calculate and return the volume using the formula
        return self.a * self.b * self.c


# Figure with internal cavity
class FigureWithCavity(Figure):
    def __init__(self, a: float, b: float, c: float, d: float):
        # Call the parent class constructor to initialize a, b, c
        super().__init__(a, b, c)
        # Unique:wall thickness-d
        self.d = d  # Wall thickness

    def volume(self) -> float:
        """Method 2: Calculate volume excluding the cavity (V - (a-d)*(b-d)*(c-d))"""
        # Calculate outer volume using parent class method
        outer_vol = super().volume()

        # Calculate inner dimensions after subtracting wall thickness
        inner_a = self.a - self.d
        inner_b = self.b - self.d
        inner_c = self.c - self.d

        # Check if inner dimensions are valid (positive)
        if inner_a <= 0 or inner_b <= 0 or inner_c <= 0:
            # If any inner dimension is zero or negative, cavity volume is zero
            inner_vol = 0
        else:
            # Calculate inner cavity volume
            inner_vol = inner_a * inner_b * inner_c

        # Return the volume of the material (outer minus inner)
        return outer_vol - inner_vol


# Array of figures
class FigureArray(Figure):
    def __init__(self, a: float, b: float, c: float, n: int):
        # Call the parent class constructor to initialize a, b, c
        super().__init__(a, b, c)
        # Unique:number of figures
        self.n = n  # Count of identical figures in the array

    def total_volume(self) -> float:
        # Calculate volume of one figure and multiply by count
        return super().volume() * self.n


# Main execution block for testing
if __name__ == "__main__":
    # Test the base class
    fig1 = Figure(2, 3, 4)
    print(f"Volume of figure: {fig1.volume()}")

    # Test the FigureWithCavity class
    fig2 = FigureWithCavity(10, 10, 10, 2)
    print(f"Volume of body with cavity: {fig2.volume()}")

    # Test the FigureArray class
    fig3 = FigureArray(1, 2, 3, 5)
    print(f"Total volume of figure array: {fig3.total_volume()}")

    # Demonstrate polymorphism with a list of different figure types
    figures = [fig1, fig2, fig3]
    for fig in figures:
        if isinstance(fig, FigureArray):
            print(f"Figure array: {fig.total_volume()}")
        elif isinstance(fig, FigureWithCavity):
            print(f"Body with cavity: {fig.volume()}")
        else:
            print(f"Simple figure: {fig.volume()}")