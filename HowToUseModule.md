# 如何使用我们提供的模块 #

  1. 首先将本项目的代码 checkout 到一个目录中
  1. 'nix' 家族：使用 ln -s 命令把 '/addons/' 链接到 OpenERP Server 项目的 '/bin/addons/' 下
  1. Windows 家族：使用 junction.exe 工具把 '/addons/' 链接到 OpenERP Server 项目的 '/bin/addons/' 下
  1. 重新启动 OpenERP Server 并更新模块列表