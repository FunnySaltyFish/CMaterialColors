## 简介

**CMaterialColors**帮助您在**Jetpack Compose**项目中轻松使用**MaterialColors**

## 用法

### 引入库

你可以选择下面的任意一种方式引入本库

- 将位于[lib/src/main/java/com/funny/cmaterialcolors/CMaterialColors.kt](/lib/src/main/java/com/funny/cmaterialcolors/CMaterialColors.kt) 的文件拷贝到您的项目中，按需修改包名即可
- <del>在项目级别的`build.gradle`中添加Maven仓库 ` maven { url "https://jitpack.io" }` 并在模块级别的`build.gradle` 中添加依赖`implementation "com.github.FunnySaltyFish:CMaterialColors:1.0.0"` </del>

<small>理论上应该是有第二种方法的。但是，由于我多次尝试将其上传到jitpack.io均以失败告终，所以暂且不可以使用。如果你能帮我修复一下这个bug，我将感激不尽！！！</small>

<small>构建失败的log如下所示</small>：[log](https://jitpack.io/com/github/FunnySaltyFish/CMaterialColors/1.0.19/build.log)



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
