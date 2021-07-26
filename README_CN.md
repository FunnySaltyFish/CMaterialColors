[![Version](https://jitpack.io/v/FunnySaltyFish/CMaterialColors.svg)](https://jitpack.io/#FunnySaltyFish/CMaterialColors)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## 简介

**CMaterialColors**帮助您在**Jetpack Compose**项目中轻松使用**MaterialColors**

## 用法

### 引入库

你可以选择下面的任意一种方式引入本库

- 将位于[lib/src/main/java/com/funny/cmaterialcolors/CMaterialColors.kt](/lib/src/main/java/com/funny/cmaterialcolors/CMaterialColors.kt) 的文件拷贝到您的项目中，按需修改包名即可
- 在项目级别的`build.gradle`中添加Maven仓库 ` maven { url "https://jitpack.io" }` 并在模块级别的`build.gradle` 中添加依赖`implementation 'com.github.FunnySaltyFish:CMaterialColors:1.0.21` 

<small>如果你好奇为什么第一个版本号会是1.0.21，我可以告诉你，因为之前的所有版本提交到Jitpack.io都构建失败了！得益于互相抄袭的博主们，这个库硬是到这个版本号才构建成功</small>

<small>如果你对整个发布过程感兴趣，可以参阅</small>：[blog](https://funnysaltyfish.github.io/2021/07/26/jitpack-build-error-solve/)



### 在kotlin代码中使用

```kotlin
import com.funnty.cmaterialcolors.MaterialColors

/*...*/

Surface(color = MaterialColors.Red200) {
    Text(text = "FunnySaltyFish", modifier = Modifier.padding(4.dp),color = MaterialColors.PurpleA700)
    /*像这样写颜色就好*/
}
```

对，就是这么简单！



### 其他

这个库的所有颜色不是手打的，它是通过下面的代码生成的：

```python
import re
import os

"""
    generate kotlin colors
    @copyright : FunnySaltyFish [github](https://github.com/FunnySaltyFish)
    @date : 2021/06/14 22:28:48
"""

text = """
    <color name="Red50">#fde0dc</color>
    <color name="Red100">#f9bdbb</color>
    ...
"""


def generate_colors(xml:str):
    """ generate kotlin code by using android resources xml file
        @params xml source xml file 
    """
    pattern_color = re.compile(r"<color name=\"(.+)\">(.+)</color>")
    find_colors = re.findall(pattern=pattern_color,string=xml) #find all colors by re module
    result_code = ""
    for (name,color) in find_colors:
        name = name.replace("_","") #replace redundant symbol "_" 
        color = color.replace("#","0xff")
        color = color.upper() #change the color into a stander format 
        result_code += f"@Stable\nval {name} = Color({color})\n" #generate the kotlin code
    return result_code

if __name__ == "__main__":
    code = generate_colors(text)
    file_path = "./code/code.txt"
    if not os.path.exists(file_path): #create folder if that dose not exist
        os.makedirs(os.path.dirname(file_path))
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(code)
```

你可以在[这里](generate_code_by_xml.py)查看此脚本完整代码



### 举个栗子

要查看所有受支持的颜色，你可以下载`demo.apk`. 它使用反射罗列了该库包含的所有颜色。



![screen_1.png](https://raw.githubusercontent.com/FunnySaltyFish/CMaterialColors/master/screen_1.png)
