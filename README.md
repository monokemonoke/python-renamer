# Renamer

これは, 同じパターンのファイル名を置換する作業を行うPythonのcliツールです.

## Install

```bash
$ python setup.py develop
```

## How to use

```bash
$ tree
.
├── fuga.txt
└── hoge.txt
$ renamer "*.txt" .txt .md
$ tree
.
├── fuga.md
└── hoge.md
```
