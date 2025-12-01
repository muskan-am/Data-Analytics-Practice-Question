from shapes import Cylinder, Cone, Cube, Cuboid, Sphere

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def cylinder_flow():
    r = get_number("Enter radius (r): ")
    h = get_number("Enter height (h): ")
    c = Cylinder(r, h)
    return c

def cone_flow():
    r = get_number("Enter radius (r): ")
    h = get_number("Enter height (h): ")
    return Cone(r, h)

def cube_flow():
    a = get_number("Enter side length (a): ")
    return Cube(a)

def cuboid_flow():
    l = get_number("Enter length (l): ")
    b = get_number("Enter breadth (b): ")
    h = get_number("Enter height (h): ")
    return Cuboid(l, b, h)

def sphere_flow():
    r = get_number("Enter radius (r): ")
    return Sphere(r)

def operation_menu(obj):
    while True:
        print("\nChoose operation:")
        print("1. Curved Surface Area (CSA / Lateral)")
        print("2. Total Surface Area (TSA)")
        print("3. Volume")
        print("4. Back to main menu")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            try:
                print("Result:", round(obj.csa(), 6))
            except Exception as e:
                print("Error computing CSA:", e)
        elif choice == '2':
            try:
                print("Result:", round(obj.tsa(), 6))
            except Exception as e:
                print("Error computing TSA:", e)
        elif choice == '3':
            try:
                print("Result:", round(obj.volume(), 6))
            except Exception as e:
                print("Error computing volume:", e)
        elif choice == '4':
            return
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\n--- Choose a shape ---")
        print("1. Cylinder")
        print("2. Cone")
        print("3. Cube")
        print("4. Cuboid")
        print("5. Sphere")
        print("6. Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            obj = cylinder_flow()
            operation_menu(obj)
        elif choice == '2':
            obj = cone_flow()
            operation_menu(obj)
        elif choice == '3':
            obj = cube_flow()
            operation_menu(obj)
        elif choice == '4':
            obj = cuboid_flow()
            operation_menu(obj)
        elif choice == '5':
            obj = sphere_flow()
            operation_menu(obj)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
