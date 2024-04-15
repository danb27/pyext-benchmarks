from data.constants import BIGRAM_REQUESTS, BIGRAMS_DIR
from python_implementation.funcs import bigrams


if __name__ == '__main__':
    for file, input_ in BIGRAM_REQUESTS.items():
        output = bigrams(**input_)
        # Write the output to the corresponding file in the outputs directory
        output_file = BIGRAMS_DIR / file
        output_file.write_text(str(output))
