import random
from pathlib import Path

random.seed(42)

EXAMPLES_DIR = Path(__file__).parent
TEXTS_DIR = EXAMPLES_DIR / "texts"
BIGRAMS_DIR = EXAMPLES_DIR / "bigrams"

BIGRAM_REQUESTS = {
    file.name: {"text": file.read_text()} for file in TEXTS_DIR.glob("*.txt")
}
BIGRAM_OUTPUTS = {file.name: file.read_text() for file in BIGRAMS_DIR.glob("*.txt")}

TWO_SUM_REQUESTS = {}
TWO_SUM_RESPONSES = {}


def solution_is_valid(solution, nums, target) -> bool:
    if not solution:
        return False
    i, j = solution
    return nums[i] + nums[j] == target


for idx in range(100):
    nums = [random.randint(0, 1000) for _ in range(100)]
    target = sum(nums[-2:])
    TWO_SUM_REQUESTS[idx] = {"nums": nums, "target": target}
    TWO_SUM_RESPONSES[idx] = solution_is_valid
