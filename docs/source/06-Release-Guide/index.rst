Release Guide
==============================================================================


Summary
------------------------------------------------------------------------------
我们希望能将开发好的 Workflow 发布出去供大家下载. 并且希望安装的过程尽可能的简单. 作为 Workflow 的开发者, 我们希望简化发布新版本的流程.


Solution
------------------------------------------------------------------------------
1. 首先运行一次 ``pyops cov`` 命令执行代码覆盖率单元测试, 确保 90% 以上的覆盖率. 不然你自己都说服不了自己你的 Workflow 会不会有严重的 Bug.
2. 然后运行一次 ``python ./bin/s01_build_workflow.py`` 命令从源代码构建 Alfred Workflow. 保证你即将发布的 Workflow 的代码跟你的代码库中一致.
3. 在 Alfred 中输入 ``?Workflow`` 进入 Alfred Workflow 菜单.
4. 找到你的 Workflow, 点击右键呼出菜单, 然后点击 ``Export`` 进入导出页面.
5. 给你的 Workflow 加上一些 Metadata. 例如:
    - Bundle Id: 可以是 ``${GitHubUserName}-${ProjectName}`` 的格式
    - Version: 用 Semantic Version 的方式命名. 从 ``0.1.1`` 开始
6. 导出后将文件重命名为这种格式: ``${ProjectName}-${SemanticVersion}-${OS}_${PlatForm}.alfredworkflow``, 例如: ``afwf_example-0.1.1-macosx_arm64.alfredworkflow``. 这个导出的文件就会包括 Workflow Diagram Definition 文件 ``info.plist`` 以及 Python 依赖和源码.
7. 在 GitHub Repo 中的 Release 菜单里点击 ``Draft a new release``. 然后设置 Tag 为你的 Semantic Version, Release Title 也是一样. 然后在将你刚才创建的 ``.alfredworkflow`` 文件拖曳到 ``Attach binaries by dropping them here or selecting them.`` 区域上传.
8. 至此你的用户可以在 Release 中点击 ``.alfredworkflow`` 文件下载然后双击安装你的 Workflow 了.

.. note::

    有些 Python 依赖除了纯 Python 代码以外还含有编译后的 binary 文件. 例如 ``*.so``. 如果你的依赖中用到了这些文件, 那么用户安装后是无法运行的. 因为 Mac 会检查 App 的来源, 而对于编译后的 binary 文件 Mac 是无法判断是否有害的, 所以 Mac 会禁止你运行. 这时用户就需要从源码构建了. 具体步骤如下:

    1. 从 Release 下载 ``${ProjectName}-${SemanticVersion}-${OS}_${PlatForm}.alfredworkflow`` 文件, 并双击安装. 但不要运行. 然后右键点击 Open in Finder 找到这个 Workflow 的路径, 后面有用.
    2. 要 Clone 仓库到本地, 然后修改 ``bin/automation/ops.py`` 中 ``dir_workflow = ...`` 这一行代码, 把你的 Workflow 路径填写进去.
    3. 然后按顺序执行以下命令:

    .. code-block:: bash

        # create python virtualenv
        pyops venv-create

        # install all dependencies
        pyops install-all

        # activate virtualenv
        source .venv/bin/activate

        # build workflow
        python bin/s01_build_wf.py

    我知道这样对于最终用户来说比较麻烦, 不是所有的用户都有 Python 知识. 我准备在今后的版本中加入自动化构建的功能, 使得用户能一键进行安装.
