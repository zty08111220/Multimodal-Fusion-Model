# 实验五：多模态情感分析

## 项目概述

本项目旨在使用文本与图像多模态融合模型进行情感分析，并将其结果与消融实验结果对比分析。

## 文件结构

```
|-- 多模态融合模型.ipynb                   # 多模态融合模型得出测试结果的实验代码
|-- 文本模型，图像模型和多模态融合模型.ipynb   # 文本模型、图像模型和多模态融合模型的对比实验代码
|-- check.py                             # 检查txt数据的编码格式
|-- train.txt                            # 训练数据，包含每个样本的GUID和标签
|-- test_without_label.txt               # 测试数据，包含待预测的样本GUID
|-- results.txt                          # 测试结果，包含待预测的样本GUID和标签
|-- multimodal_loss_curve.png            # 多模态模型训练和验证损失曲线图
|-- total_loss_curve.png                 # 文本模型、图像模型和多模态融合模型训练和验证损失曲线图
|-- text_losses.txt                      # 文本模型的训练和验证损失记录
|-- image_losses.txt                     # 图像模型的训练和验证损失记录
|-- multimodal_losses.txt                # 多模态模型的训练和验证损失记录
|-- requirements.txt                     # 项目依赖的 Python 库列表
|-- README.md                            # 项目说明文件，包含项目概述、文件结构和使用说明
|-- batch_size和模型复杂程度.txt           # 关于批量大小和模型复杂度的实验记录
|-- 学习率.txt                           # 关于学习率的实验记录
|-- 报告.pdf                             # 项目报告，包含模型设计、结果分析和bug
```

## 安装和使用说明

1. 安装所需的库`pip install -r requirements.txt`。
2. 运行 `多模态融合模型.ipynb`  获得测试结果、多模态融合模型权重文件、多模态模型训练和验证损失曲线图。
3. 运行`文本模型，图像模型和多模态融合模型.ipynb`获得文本模型、图像模型和多模态融合模型训练和验证损失曲线图。
1. 参考 `报告.pdf` 了解模型设计，不同超参数或不同模型的结果分析。

## 联系我们

如果您有任何问题或建议，请通过以下方式联系我们：

- 电话：18221516950
- 邮件：zty20221220@126.com

## 致谢

感谢所有为开源社区做出贡献的开发者！