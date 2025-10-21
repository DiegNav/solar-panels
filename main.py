from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    if roof_width <= 0 or roof_height <= 0 or panel_width <= 0 or panel_height <= 0:
        return 0
    
    panel_area = (roof_width // panel_width) * (roof_height // panel_height)
    panel_area_inv = (roof_width // panel_height) * (roof_height // panel_width)

    max_panels = max(panel_area, panel_area_inv)


    for cut in range(1, roof_width):
        left = calculate_panels(panel_width, panel_height, cut, roof_height)
        right = calculate_panels(panel_width, panel_height, roof_width - cut, roof_height)
        max_panels = max(max_panels, left + right)

    for cut in range(1, roof_height):
        top = calculate_panels(panel_width, panel_height, roof_width, cut)
        bottom = calculate_panels(panel_width, panel_height, roof_width, roof_height - cut)
        max_panels = max(max_panels, top + bottom)

    return max_panels


def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()
