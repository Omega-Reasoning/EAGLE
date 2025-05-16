from setuptools import setup, find_packages

setup(
    name='eagle-llm',
    version='3.0.0',
    description='Accelerating LLMs by 3x with No Quality Loss',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author_email='yuhui.li@stu.pku.edu.cn',
    url='https://github.com/SafeAILab/EAGLE',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
)
