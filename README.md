## 📖 简介

一个CTF比赛初始化框架，预分类好每个题目，每题单独内置wp模板，并支持对wp和脚本一键设置题目名称，使脚本和文件不再乱飞

文件树：

```
ezCTFTemplate/
├── cookiecutter.json
└── {{cookiecutter.CTF_name}}/
    ├── AndOthers/
    │   ├── 1/
    │   │   ├── final.py
    │   │   ├── SetName.py
    │   │   ├── solve.py
    │   │   └── wp/
    |   |        ├── wp.md
    │   ├── 2/          (与 1/ 目录结构完全相同)
    │   ├── 3/          (与 1/ 目录结构完全相同)
    │   ├── 4/          (与 1/ 目录结构完全相同)
    │   ├── 5/          (与 1/ 目录结构完全相同)
    │   ├── 6/          (与 1/ 目录结构完全相同)
    │   ├── 7/          (与 1/ 目录结构完全相同)
    │   ├── 8/          (与 1/ 目录结构完全相同)
    │   └── 9/          (与 1/ 目录结构完全相同)
    ├── Crypto/    		（下面五类同上）
    ├── Misc/
    ├── Pwn/
    ├── Reverse/
    └── Web/

```



## 📦 运行教程

安装cookiecutter

```cmd
pip install cookiecutter
```

使用模板(会在命令行当前目录下生成模板)

```cmd
cookiecutter <your_path>/ezCTFTemplate
```

会提示输入{CTF名称}作为最上层文件夹名；



运行每个文件夹中的`SetName.py`，输入{CTF题目名}，会使当前文件夹以及所有下级文件即文件夹带上{CTF题目名_}前缀，以及wp.md文件的标题也会换成这个。
