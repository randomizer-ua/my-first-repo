# Лабораторна робота №4
# Варіант №18

class ArtificialXmasTree:
    def __init__(self, manufacturer="Chinese Bing-Sing Company",
        height=175,
        price=45,
        material="Plastic and Polyethylene",
        weight=7,
        longevity="MINIMUM: 2.5 years; MAXIMUM: 5 years."
        ):
        
        self.__manufacturer = manufacturer
        self.__height = height
        self.__price = price
        self.__material = material
        self.weight = weight
        self.longevity = longevity

    def get_manufacturer(self):
        return self.__manufacturer

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def get_material(self):
        return self.__material

    def __str__(self):
        return (f"Manufacturer: {self.__manufacturer}; "
                f"Height: {self.__height} cm; "
                f"Price: {self.__price} USD; "
                f"Material: {self.__material}; "
                f"Weight: {self.weight} kg; "
                f"Longevity: {self.longevity}."
                )

    def __repr__(self):
        return (f"ArtificialXmasTree("
                f"manufacturer={self.__manufacturer!r}, "
                f"height={self.__height!r}, "
                f"price={self.__price!r}, "
                f"material={self.__material!r}, "
                f"weight={self.weight!r}, "
                f"longevity={self.longevity!r})"
                )

    def __del__(self):
        print("Artificial Xmas Tree has been destroyed.")

def main():
    art_tree1 = ArtificialXmasTree()

    art_tree2 = ArtificialXmasTree(
        "Xi Zhinping",
        160,
        999,
        "Communism",
        10,
        "SUPER Quality product. MINIMUM: 69 years; MAXIMUM: 100 years."
    )

    art_tree3 = ArtificialXmasTree(
        "Ukrainian Christmas Trees",
        220,
        120,
        "PVC and PE",
        12,
        "7 years."
    )

    for tree in (art_tree1, art_tree2, art_tree3):
        print(tree)
        print(repr(tree))

        print("Manufacturer:", tree.get_manufacturer())
        print("Height:", tree.get_height())
        print("Price:", tree.get_price(), "$")
        print("Material:", tree.get_material())
        print("Weight:", tree.weight)
        print("Longevity:", tree.longevity)
        print(tree.weight)
        print()

main()