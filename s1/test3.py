import math

def main():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
    except ValueError:
        print("Please enter a valid numeric value for the radius.")

if __name__ == "__main__":
    main()