.PHONY: compile-rust compile-cython update-ground-truth benchmark-all clean clean-cython clean-outputs

BASE_DIR = $(shell pwd)
PYTHON = ${BASE_DIR}/.venv/bin/python

all: setup compile benchmark clean
setup: update-ground-truth
compile: compile-rust compile-cython
clean: clean-cython clean-rust clean-outputs

compile-cython:
	@echo "Compiling Cython code..."
	@{ \
  		cd src/cython_implementation && \
		$(PYTHON) setup.py build_ext --inplace; \
	} > /dev/null

compile-rust:
	@echo "Compiling Rust code..."
	@{ \
  		set -e && \
		cd src/rust_implementation && \
		$(PYTHON) -m maturin build --release && \
		$(PYTHON) -m pip install target/wheels/rust_implementation*.whl; \
	} > /dev/null

update-ground-truth:
	@echo "Updating benchmarks..."
	@cd src && $(PYTHON) update_ground_truth.py

benchmark:
	@echo "Running all benchmarks..."
	@cd src && $(PYTHON) benchmark_all.py

clean-cython:
	@echo "Cleaning up Cython build files..."
	@rm -rf src/cython_implementation/*.so src/cython_implementation/*.c src/cython_implementation/build/

clean-rust:
	@echo "Cleaning up Rust build files..."
	@rm -rf src/rust_implementation/target/ src/rust_implementation/Cargo.lock
	@$(PYTHON) -m pip uninstall -y rust_implementation

clean-outputs:
	@echo "Cleaning up output files..."
	@rm -rf src/data/outputs/*.txt
