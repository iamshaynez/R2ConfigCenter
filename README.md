# R2ConfigCenter

这是一个基于 Cloudfare R2 的配置中心简易实现，用来实现文件级别的配置文件存储，远程读取。理论上 AWS S3 通用。

# 如何配置

在 Cloudflare 中建立对应的 R2 Bucket，并创建对应权限的 Token 即可。环境变量或构造函数中，配置如下信息。

```
CF_R2_REGION=
CF_R2_ACCOUNT_ID=
CF_R2_ACCESS_KEY_ID=
CF_R2_SECRET_ACCESS_KEY=
CF_R2_BUCKET_NAME=
```

安装 pip

```
pip install git+https://github.com/iamshaynez/R2ConfigCenter.git
```

使用

```python
from ConfigCenter import R2Config
config = R2Config() # 环境变量以有，则无需传入构造函数
config.read_json('file.json')
config.read_text('file.txt')
```