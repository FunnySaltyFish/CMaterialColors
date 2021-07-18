## introduction

|[中文](README_CN.md)|

**CMaterialColors** is a library that contains all **MaterialColors** you need in **Jetpack Compose projects.**

## Usage

### Get the library

You can choose one of these ways to get it.

- Simply copy the file which locates at  [lib/src/main/java/com/funny/cmaterialcolors/CMaterialColors.kt](/lib/src/main/java/com/funny/cmaterialcolors/CMaterialColors.kt) to your own project , and then modify the package name
- <del>Add maven source ` maven { url "https://jitpack.io" }` in your project's `build.gradle` and dependencies `implementation "com.github.FunnySaltyFish:CMaterialColors:1.0.0"` in your module's `build.gradle `</del>

<small>There should be the second way , and it is more convenient than copying the file. However, I have tried a lot of times to upload the library to jitpack.io , but all failed to build in the end. I would really appreciate it if you could help me fix the bug!!!</small>

<small>The failure building log is as below:</small>[output](https://jitpack.io/com/github/FunnySaltyFish/CMaterialColors/1.0.19/build.log)



### Use it in kotlin code

```kotlin
import com.funnty.cmaterialcolors.MaterialColors

/*...*/

Surface(color = MaterialColors.Red200) {
    Text(text = "FunnySaltyFish", modifier = Modifier.padding(4.dp),color = MaterialColors.PurpleA700)
    /*Anything like this*/
}
```

That's it!



## What's More

### How I write the library?

Actually, all of the codes are generated by a python script as below:

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

To get the full code, check the file [generate_code_by_xml.py](generate_code_by_xml.py)



### About the example

To check all supported colors , you can download the `demo.apk`. It uses reflection to show all the colors.



![screen_1.png](https://raw.githubusercontent.com/FunnySaltyFish/CMaterialColors/master/screen_1.png)





