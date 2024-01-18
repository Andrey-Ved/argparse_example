# Argparse example 
\
Simple example command-line interface via [argparse](https://docs.python.org/3/library/argparse.html)

## Installation

- Clone this repo and cd into it;
- Create a venv (virtual environment): python3.10 -m venv venv;
- source venv/bin/activate && pip install -r requirements.txt;
  
## Demonstration

```bash
$ python.exe -m argparse_demo --h
```  
```bash
$ python.exe -m argparse_demo --ip
```
```bash
$ python.exe -m argparse_demo --ram
```
```bash
$ python.exe -m argparse_demo --cpu --int 56
```  

## Error demo

```bash
$ python.exe -m argparse_demo --cpu --int 56.1
```
```bash
$ python.exe -m argparse_demo --cpu True --int 56
```

## Test

```bash
$ pytest -v -l -s  
```
