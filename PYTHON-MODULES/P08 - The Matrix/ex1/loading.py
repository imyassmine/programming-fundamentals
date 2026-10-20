#!/usr/bin/env python3


import importlib


def check_dependency(module_name: str, description: str) -> bool:
    try:
        module = importlib.import_module(module_name)
        print(
            f"[OK] {module_name} ({module.__version__}) "
            f"- {description} ready"
            )
        return True
    except ImportError:
        print(f"[KO] {module_name} is not installed")
        return False


def generate_matrix_data(np):
    return np.random.rand(1000)


def analyze_data(pd, data):
    df = pd.DataFrame(data, columns=["value"])
    return df["value"].mean()


def create_visualization(plt, data):
    plt.hist(data)
    plt.savefig("matrix_analysis.png")


def compare_dependency_managers():
    print("\n--- pip vs Poetry ---")
    print(
        "pip: uses requirements.txt, no automatic lock file"
        " manual venv management"
        )
    print(
        "Poetry: uses pyproject.toml, generates poetry.lock,"
        " manages venv automatically"
          )


def main() -> None:
    print("Checking dependencies:")
    numpy_ok = check_dependency("numpy", "Numerical computation")
    pandas_ok = check_dependency("pandas", "Data manipulation")
    matplotlib_ok = check_dependency("matplotlib", "Visualization")
    if numpy_ok:
        np = importlib.import_module("numpy")
        data = generate_matrix_data(np)
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    if numpy_ok and pandas_ok:
        pd = importlib.import_module("pandas")
        mean = analyze_data(pd, data)
        print(f"Mean: {mean}")
    print("Generating visualization...")
    if numpy_ok and matplotlib_ok:
        plt = importlib.import_module("matplotlib.pyplot")
        create_visualization(plt, data)
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    compare_dependency_managers()


if __name__ == "__main__":
    main()
