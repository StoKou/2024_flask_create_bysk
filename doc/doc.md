# 创新实践文档
<center>小组成员：时扣、陈亮亮

</center>


## 一、前端框架
### Vue3

* Vue.js 3 是一种流行的前端 JavaScript 框架，用于构建交互式的用户界面。它是 Vue.js 框架的最新版本，与之前的版本相比，它引入了许多新的特性和改进，旨在提供更好的性能、可维护性和开发体验。具体体现在以下几个方面
1. 更好的性能：Vue.js 3 引入了优化的响应式系统，通过新的 Proxy API 实现了更快的响应式数据绑定，达到了比之前版本更高的性能水平。此外，Vue.js 3 还对编译器进行了优化，生成更高效的渲染函数，提高了整体的渲染速度。
2. 更好的可维护性：Vue.js 3 对组件的组织和复用提供了更多的选项和灵活性。通过 Composition API，开发者可以使用函数式的方式编写组件逻辑，使代码更易理解、测试和维护。此外，Vue.js 3 也提供了更好的 TypeScript 支持，让开发者可以更安全地使用类型检查。
3. 更好的开发体验：Vue.js 3 改进了开发者工具和调试能力，使开发过程更流畅。它支持同时渲染多个根元素，可以更好地适应组件化的开发模式。另外，Vue.js 3 还提供了更多的内置指令和组件，减少了开发者需要编写的重复代码。

总的来说，Vue.js 3 提供了更好的性能、可维护性和开发体验，使开发者能够更高效地构建现代化的 Web 应用程序。无论是初学者还是有经验的开发者，都可以从 Vue.js 3 的特性中受益，并且享受到构建优质用户界面的乐趣。

### Vite

Vite 意在提供开箱即用的配置，同时它的 插件 API 和 JavaScript API 带来了高度的可扩展性，并有完整的类型支持。

## 二、后端框架

### Flask
* Flask 是一种轻量级的 Python Web 框架，用于构建灵活且易于扩展的 Web 应用程序。它被设计为简单而优雅，具有最小的核心依赖项和一个模块化的设计，使开发者可以根据自己的需求选择适合的扩展和工具。Flask 提供了简洁的 API，易于学习和使用。它使用装饰器来定义路由，可以通过编写函数来处理不同的 URL 请求。同时，Flask 也提供了强大的扩展机制，可以方便地集成第三方库和插件，例如数据库访问、身份验证、表单处理、文件上传等功能。
Flask 的优点包括：
1. 简单灵活：Flask 的设计理念是保持简单和灵活，没有过多的约束和规定。开发者可以根据自己的喜好和需求选择扩展和工具，以实现最佳的灵活性和自定义性。
2. Pythonic：Flask 在设计上借鉴了 Python 的哲学，采用了简洁优雅的语法和风格，使开发者可以用更少的代码实现相同的功能。
3. 易扩展：Flask 提供了丰富的扩展机制，开发者可以方便地集成各种功能扩展和第三方库，以满足不同应用的需求。
4. 功能丰富：尽管 Flask 是一个轻量级框架，但它仍然提供了许多有用的功能，如请求处理、模板引擎、会话管理、静态文件服务等，使开发者能够快速构建出功能完备的 Web 应用程序。

总的来说，Flask 是一个简单、灵活和易于扩展的 Python Web 框架。它适用于各种规模的项目，无论是构建简单的原型应用还是开发复杂的生产级应用，Flask 都能提供一个可靠而高效的开发环境。

## 三、项目结构
### 1.目录结构
- **frontend/**
  - **public/**
    - `index.html`         // 入口 HTML 文件
    - `favicon.ico`         // 图标
    - **css/**               // 样式文件
    - **js/**                // 静态脚本
  - **src/**
    - **assets/**             // 静态资源（图片、字体等）
    - **components/**         // UI 组件
    - **views/**              // 页面组件（Vue/React/Angular 组件）
    - **router/**             // 路由配置
    - **store/**              // 状态管理（如 Vuex）
    - **utils/**              // 工具函数
    - `App.vue`               // 主应用组件
    - `main.js`               // 应用入口文件（Vue CLI）
  - `package.json`           // 项目依赖及脚本配置
  - `vite.config.js`         // Vite 配置文件（或者 webpack.config.js）
  - `.babelrc`               // Babel 配置文件
  - `tsconfig.json`          // TypeScript 配置文件（如果使用 TypeScript）
- **backend/**
  - **app/**
    - **controllers/**        // 控制器
    - **models/**             // 数据模型（ORM 模型）
    - **services/**           // 业务逻辑层
    - **routers/**            // 路由配置
    - **middlewares/**        // 中间件
  - **config/**                // 项目配置文件
  - **static/**                // 静态文件（如果有的话）
  - **tests/**                 // 测试文件
  - `requirements.txt`       // Python 依赖文件（如果是 Flask）
  - `server.py`              // 后端启动文件（Flask/Django）
  - `.env`                   // 环境变量配置文件
  - `.gitignore`             // Git 忽略文件
  - `Dockerfile`             // Docker 配置文件（如果有）
  - ...
- `README.md`                  // 项目说明文件

### 2.功能
#### 可视化

1. 数据处理
![alt text](image-2.png)
处理后的结果

2. 展示方式
前端展示
后端

#### 接口设计


## 四、数据集
### 1.SEED数据集
### 简介：
* 上海交通大学情绪脑电图数据集（SEED）是由BCMI实验室提供的脑电图数据集集合，该实验室由Bao-Liang Lu教授和Wei-Long Zheng教授领导。
### 名词解释：

| 缩写         | 名词解释                             |
|--------------|--------------------------------------|
| DASM         | 微分不对称，用于描述信号的不对称特性 |
| ASM          | 不对称，通常用来描述信号的对称性缺失 |
| DCAU         | 微分因果性特征，分析信号的因果关系  |
| PSD          | 提取功率谱密度，用于分析信号的频率特性 |
| RASM         | 有理不对称，涉及数学处理的不对称性  |
| LDS         | 移动平均方式，用于处理噪声  |
|ExtractedFeatures|未经处理的数据集|
|Preprocessed_EEG|经过预处理后的数据集|

### 数据集处理（展示）





### 数据集结构

- **SEED**
  - **ExtractedFeatures**
    - `1_20131027.mat` 
    - ...
  - **Preprocessed_EEG**
    - `1_20131027.mat` 
    - ...  
  - `channel-order.xlsx`
  - `seed-stimulation.xlsx` 
  - `subject-id-gender-seed.txt`

### 数据集截图

<div style="display: flex; justify-content: space-around;">
  <img src="image.png" alt="Image 1" style="width: 280px; height: 500px;">
  <img src="image-1.png" alt="Image 2" style="width: 280px; height: 500px;">
  
</div>

## 四、模型
### 1、SVM（不完全失败案例）

### 2、CNN
![alt text](image-3.png)
上面是SEED经过预处理后并且合并之后的数据
![alt text](image-4.png)
读取这些数据，按照62*200进行切分，不足200的部分舍去
![alt text](image-5.png)
针对其中一个样例，切分的结果如上（47001/200=235.005，向下取整，取235）
![alt text](image-6.png)
最终的预测标签的个数是3，因此对于每一个输入数据，经过处理，输出的最终矩阵格数就是（1 *3），因此训练的时候构造的训练label也是（1 *3）
规定了输入格式为（62 *200），输出格式为（1 *3），处理完所有的数据后，后面要对数据进行划分，划分训练集和测试集
![alt text](image-7.png)
![alt text](image-8.png)
训练集：测试集=0.8：0.2，上面是划分后的数据格式
```python
train_feature, train_label, test_feature, test_label = subject_independent_data_split(feature_vector_dict, label_dict,
                                                                                      {'2', '6', '9'})
```
我们选取了2，6，9这三个作为最后的测试，其他全部作为训练数据
之后需要使用pytorch训练，因此使用Dataset转化数据
![alt text](image-9.png)
我们选择的batch_size=24，因此122184/24=5091，因此一次需要5091次训练，这就算一个epoch
之后就是进行正常的训练，由于使用Dataset数据格式，最终得到的数据格式如下
![alt text](image-10.png)
（batch_size,1，62，200）
![alt text](image-11.png)
一个batch是24个，因此label也是（1*24）

#### 开始写后端导入模型代码
![alt text](image-12.png)
这是处理之后的test_feature 
![alt text](image-13.png)
这是最终的结果，对于每一个（1 *62 *200）的输入，最终都通过模型预测出了一个（1 *3）的result，然后我们取max，得到每个batch_size的输入的结果，由于一次性输入了15个片段，并且片段都进行的打乱，所以如果需要分离的话，需要重新进行每个片段的特征块的数量计算，然后重新划分，这样和我们最终要的效果不同，所以我打算把每个片段全部重新提取出来，然后每一个观看影响的结果作为一个单独的输入，这样就比较合理了
![alt text](image-14.png)
一共有45个数据，每个有15个表， 因此一共有675份数据
完成CNN模型
![alt text](image-15.png)
其中也遇到了一些问题，我的模型训练是在cuda下进行了，训练了大概有5个小时的样子，但是由于默认安装的pytorch不支持cuda，因此在后端加载模型的时候会出现错误，由于这个问题有两个解决方案：
1.在新的环境中安装能够使用cuda的pytroch版本和依赖包
2.使用训练模型时所使用的环境
出于时间考虑吧，我选择了第二种方案，最终也解决了问题，但是明显第一种会更好，因为有可能会造成环境污染，不过在我的记忆中，想要装一个使用cuda的torch和依赖包，也不是一件很简单的事情，当然是可以熟能生巧的
