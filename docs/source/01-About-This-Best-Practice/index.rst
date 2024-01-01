About This Best Practice
==============================================================================
我个人同时维护着 10 多个垂直领域的 Alfred Workflow. 在这个过程中我发明了几个方便我开发的 Python 库:

- `afwf <https://github.com/MacHu-GWU/afwf-project>`_: 一个帮助我开发 Alfred Workflow 的业务逻辑代码的框架.
- `afwf_ops <https://github.com/MacHu-GWU/afwf_ops-project>`_: 一个帮助我维护 Alfred Workflow 的库, 提供了很多便利的自动化脚本.

我的 Alfred Workflow 都是基于这两个库开发的. 在这个过程中我形成了一套代码规范, 代码库目录结构, 开发流程, 测试, 发布流程等一整套的最佳实践. 该方法经过了大型项目的考验, 在非常复杂的项目中依然工作良好. 于是我用这套最佳实践创建了 ``afwf_example`` 这个 Alfred Workflow. 它本身是以 Demo 为目的, 不包含具体的实际用途, 但是展示了 Alfred Workflow 的各种常见的 Use Case 应该怎样去实现. 并且我以这个代码库为基础, 创建了 `cookiecutter-afwf <https://github.com/MacHu-GWU/cookiecutter-afwf>`_ 模版, 使得以后我需要开发新的 Alfred Workflow, 我只需要简单的输入一个新的项目名字, 就会用模版创建一个包含了所有最佳实践的代码库了. 大大缩短了项目周期. 这也是我为什么能用很少的时间但能同时维护 10 多个 Alfred Workflow 的秘密武器.
