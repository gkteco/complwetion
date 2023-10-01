from setuptools import setup, find_packages

setup(
    name="complwetion",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        'attrs==23.1.0',
        'beautifulsoup4==4.12.2',
        'bs4==0.0.1',
        'huggingface-hub==0.17.3',
        'numpy==1.24.4',
        'openai==0.28.1',
        'packaging==23.1',
        'Pillow==10.0.1',
        'pinecone-client==2.2.4',
        'regex==2023.8.8',
        'requests==2.31.0',
        'sentence-transformers==2.2.2',
        'tokenizers==0.13.3',
        'torch==2.0.1',
        'tqdm==4.66.1',
        'transformers==4.33.3',
        'typing_extensions==4.8.0',
        'urllib3==2.0.5',
    ],
    author="Gianni Crivello",
    author_email="gianni.crivello@techolution.com",
    description="Small helper library to build chat applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gkteco/complwetion/tree/master",
    classifiers=[
        # Choose from: https://pypi.org/classifiers/
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning"
    ],
)
