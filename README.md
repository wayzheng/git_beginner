# git使用教程

## 目录

* [git简介](#git简介)

* [git安装与配置](#git安装与配置)

* [git基础操作和使用](#git基础操作和使用)

## git简介

> Git是一个分布式版本控制系统，用于高效地管理和跟踪文件的更改。它由Linux内核的创始人Linus Torvalds开发，旨在处理从小型到大型项目的所有内容，具有高效、灵活和强大的特点。

* 通过使用git可以对文件进行跟踪，对版本进行控制和管理，同时可以通过软件操作来对软件版本和项目进行跟踪和控制

## git安装和配置

1. git安装
    * 通过直接在官网下载相关的文件来进行安装和使用
    * git官方网站 [git官方网站](https://git-scm.com/)
    * 下载完成之后，一直点击next之后就是可以了，注意要将git添加到环境变量中
    > 环境变量是操作系统用来存储系统范围内的配置信息的一种机制，他们可以影响运行中的进程的行为，环境变量用于配置系统路径，用户信息，系统设置等，环境变量是一个动态命名值，可以影响运行中的进程或者程序中的行为，他们通常是以键值对的形式来出现的。
2. git基础配置
    * 通过安装好git之后，在终端中运行，`git --version`如果显示结果是如下所示的结果就是表示的就是安装的是没有问题的
    * ![alt text](image.png)
    * 之后就是可以进行配置，首先，对于一个文件追踪的功能软件，对文件修改的人的身份是必须要给出的，通过使用
        1. `git config --权限 user.name = "用户名称"`
        2. `git config --权限 user.email = "用户的邮箱"`
    * 对于使用github的用户来说，如果需要使用ssh来进行配置，就是需要来获取私钥，获取私钥的方式就是可以通过使用以下的方式来进行获取
        1. 首先打开终端窗口，然后运行`ssh-keygen -t rsa -b 4096 -C "你的邮箱账号"`，之后直接点击enter键使用默认的位置，通常就是~/.ssh/id_rsa，并选择是否设置密码短语
        2. 生成秘钥对之后，可以通过使用以下命令来查看私钥，`cat ~/.ssh/id_rsa`
        3. 可以通过以下命令来查看私钥`cat ~/.ssh/id_rsa.pub`
    * 之后就是可以通过在github中添加ssh来使用ssh来对仓库来进行操作
    > SSH（Secure Shell）是一种加密网络协议，用于在不安全的网络中安全地操作网络服务。SSH通过使用加密技术来确保数据传输的机密性和完整性，常用于远程登录系统和执行命令。

    ### 使用SSH(同上，但是更加规整)

    1. **生成SSH密钥对**：
        ```sh
        ssh-keygen -t rsa -b 4096 -C "你的邮箱账号"
        ```
        这将生成一个新的SSH密钥对，并提示你输入文件保存位置和密码短语。

    2. **添加SSH密钥到SSH代理**：
        ```sh
        eval "$(ssh-agent -s)"
        ssh-add ~/.ssh/id_rsa
        ```

    3. **将公钥添加到GitHub**：
        - 复制公钥内容：
            ```sh
            cat ~/.ssh/id_rsa.pub
            ```
        - 登录GitHub，进入“Settings” -> “SSH and GPG keys” -> “New SSH key”，粘贴公钥内容并保存。

    4. **测试SSH连接**：
        ```sh
        ssh -T git@github.com
        ```
        如果配置正确，你会看到类似于“Hi username! You've successfully authenticated...”的消息。

    通过以上步骤，你就可以使用SSH来安全地与GitHub仓库进行交互了。

## git基础操作和使用

1. 基础操作 
    * 查看git版本 通过使用`git --version`
    * 