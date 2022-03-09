import pytest


# pytest_addoption 可以让用户注册一个自定义的命令行参数，方便用户将数据传递给 pytest
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", 
        default="None", 
        type=list,# 类型可以int，str，float，list 等类型，如果不指定类型的话，pytest会把接受到的参数值都默认为 str 类型
        # choices= ['python', 'java', 'c++'],#
        help="将自定义命令行参数 ’--cmdopt' 添加到 pytest 配置中"
    )

# 从配置对象中读取自定义参数的值
@pytest.fixture(scope="session") # scope 有session、module、class、function
def cmdopt(request):
    return request.config.getoption("--cmdopt")
# 然后任何 fixture 或测试用例都可以调用 cmdopt 来获得设备信息
 
# 将自定义参数的值打印出来
@pytest.fixture(autouse=True)
def fix_1(cmdopt):
    print('\n --cmdopt的值：',cmdopt)
 
if __name__ == '__main__':
    # 使用参数
    pytest.main(['-s', '--cmdopt=98k'])
    
    
'''
    命令行执行:pytest test24-sys-argv.py --cmdopt=abcd
'''