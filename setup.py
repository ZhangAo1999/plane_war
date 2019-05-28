from setuptools import setup


setup(
    name="plane_war",
    version="1.2.0",
    author="zh_ang_ao",
    author_email="804951563@qq.com",
    url="暂无",
    description="a game which you need to biu!biu!biu!",
    packages={"plane_war"},
    platforms='any',
    package_data={
        "plane_war": ['feiji/*', '../startGame.bat', 'ziti/*']
    }
)

