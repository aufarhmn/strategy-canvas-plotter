import matplotlib.pyplot as plt
import numpy as np

brands = {
    "L'Oréal": {
        "Price": 8,
        "Sustainable Practices": 7,
        "Product Diversity": 3,
        "Marketing": 5,
        "Distribution Channel": 6,
        "Product RnD": 7,
        "Premium Product": 8,
        "Customer Experience": 8,
        "Tech Integration": 7
    },
    "Unilever": {
        "Price": 3,
        "Sustainable Practices": 5,
        "Product Diversity": 7,
        "Marketing": 6,
        "Distribution Channel": 7,
        "Product RnD": 6,
        "Premium Product": 3,
        "Customer Experience": 6,
        "Tech Integration": 5
    },
    "P&G": {
        "Price": 4,
        "Sustainable Practices": 4,
        "Product Diversity": 6,
        "Marketing": 4,
        "Distribution Channel": 4,
        "Product RnD": 5,
        "Premium Product": 5,
        "Customer Experience": 6,
        "Tech Integration": 4
    },
}

def plot_strategy_canvas(brands):
    aspects = list(next(iter(brands.values())).keys())
    num_aspects = len(aspects)
    
    plt.figure(figsize=(14, 8))
    x = np.arange(num_aspects)
    
    for brand, scores in brands.items():
        y = [scores[aspect] for aspect in aspects]
        if brand == "L'Oréal":
            plt.plot(x, y, marker='o', label=brand)
        else:
            plt.plot(x, y, marker='o', label=brand, alpha=0.3)
    
    plt.xticks(x, aspects, rotation=45, ha='right')
    plt.xlabel('Aspects')
    plt.ylabel('Scores')
    plt.title('Strategy Canvas for FMCG Brands')
    plt.legend()
    
    plt.tight_layout()
    plt.grid(True)
    plt.show()

plot_strategy_canvas(brands)
