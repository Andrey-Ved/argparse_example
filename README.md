# Argparse example 
  
## Installation

- Clone this repo and cd into it;
- Create a venv (virtual environment): python3.10 -m venv venv;
- source venv/bin/activate && pip install -r requirements.txt;
  
## Demonstration

```bash
$ python.exe -m argparse_demo --h
```  
```bash
$ python.exe -m argparse_demo --ram True
```  
```bash
$ python.exe -m argparse_demo --ip 1
```
```bash
$ python.exe -m argparse_demo --cpu 1 --int 56
```  

## Error demo

```bash
$ python.exe -m argparse_demo --cpu 1 --int 56.1
```

## Test

```bash
$ pytest -v -l -s  
```
