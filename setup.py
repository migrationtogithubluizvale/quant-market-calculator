from setuptools import setup, find_packages

setup(
    name="financial_interpolations",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "scipy",  # Adicione scipy como uma dependência
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
