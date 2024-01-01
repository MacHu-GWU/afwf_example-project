Development Guide
==============================================================================


Automation Scripts
------------------------------------------------------------------------------
一个 Python Alfred Workflow 项目本质上是一个 Python 项目. 我有一个命令行工具 `pyproject_ops <https://github.com/MacHu-GWU/pyproject_ops-project>`_ 能自动化 Python 项目工作流中那些常用的步骤. 简单来说, 当你拿到你个新的项目后, 你需要依次运行以下命令:

Create Virtual Environment

.. code-block:: bash

    pyops venv-create

Resolve Dependencies (Yes, we use `poetry <https://python-poetry.org/>`_ to ensure deterministic dependency resolution)

.. code-block:: bash

    pyops poetry-lock

Install All Dependencies

.. code-block:: bash

    pyops install-all

Run Unit Test

.. code-block:: bash

    pyops cov

除此之外, 还有两个跟 Alfred 相关的自动化脚本也很重要.

Build workflow, 当你完成你的本地 Git repo 代码库开发后, 这个脚本能将代码部署到 ``Alfred.preferences`` 中 (实装).

.. code-block:: bash

    python ./bin/s01_build_workflow.py

Refresh Code, 这个脚本跟上一个脚本类似, 只不过跳过了安装依赖的步骤, 速度更快. 常用于你只进行了非常小的修改后快速进行热更新.

.. code-block:: bash

    python ./bin/s02_refresh_code.py


Path to Alfred Workflow
------------------------------------------------------------------------------
你的 Alfred Workflow 的所有文件都是保存在一个特定目录下的. Alfred 有一个默认的目录, 但你也可以自定义这个目录. 如果你参照上一篇文档, 使用 ``cookiecutter-afwf`` 工具自动化创建了你的代码库, 你应该在创建的代码库的时候就填写了这个目录的路径. 但是如果你要手动修改这个路径, 你可以在 ``./bin/automation/ops.py`` 文件中进行修改.


The Workflow Entry Point - main.py
------------------------------------------------------------------------------
在项目的根目录下有一个 `main.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/main.py>`_ 文件. 这个文件是 Alfred Workflow 的入口脚本. , 也是 Alfred Workflow 的主要逻辑. 请跳转到文件的内容查看注释了解它的功能.


The Workflow Source Code
------------------------------------------------------------------------------
在项目的根目录下有一个 `afwf_example <https://github.com/MacHu-GWU/afwf_example-project/tree/main/afwf_example>`_ 目录. 这个目录就是你的 Alfred Workflow 的源码了. 其中 `workflow.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/workflow.py>`_ 模块定义了 Workflow 的对象实例. 并且将所有需要用到的 ``Handler`` 都注册了. 而 `handlers <https://github.com/MacHu-GWU/afwf_example-project/tree/main/afwf_example/handlers>`_ 子模块则包含了所有的 handlers 的实现. 我建议查看所有示例 handlers 的源码来了解如何编写常见的 handler 逻辑.

- `error.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/error.py>`_: 故意抛出异常, 用于测试异常处理逻辑.
- `memorize_cache.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/memorize_cache.py>`_: 一个带磁盘缓存的记忆函数.
- `open_file.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/open_file.py>`_: 可以用来选择并打开文件.
- `open_url.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/open_url.py>`_: 可以用来选择并在浏览器中打开网页.
- `read_file.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/read_file.py>`_: 对文件的内容进行读取.
- `write_file.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/write_file.py>`_: 对文件的内容进行写入.
- `set_settings.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/set_settings.py>`_: 对数据库进行写入.
- `view_settings.py <https://github.com/MacHu-GWU/afwf_example-project/blob/main/afwf_example/handlers/view_settings.py>`_: 对数据库进行读取.
