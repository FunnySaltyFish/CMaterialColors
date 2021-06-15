import re
import os

"""
    根据XML resource生成kotlin colors
    @copyright : FunnySaltyFish [github](https://github.com/FunnySaltyFish)
    @date : 2021/06/14 22:28:48
"""

text = """
    <color name="Red50">#fde0dc</color>
    <color name="Red100">#f9bdbb</color>
    <color name="Red200">#f69988</color>
    <color name="Red300">#f36c60</color>
    <color name="Red400">#e84e40</color>
    <color name="Red500">#e51c23</color>
    <color name="Red600">#dd191d</color>
    <color name="Red700">#d01716</color>
    <color name="Red800">#c41411</color>
    <color name="Red900">#b0120a</color>
    <color name="RedA100">#ff7997</color>
    <color name="RedA200">#ff5177</color>
    <color name="RedA400">#ff2d6f</color>
    <color name="RedA700">#e00032</color>
    <color name="Pink50">#fce4ec</color>
    <color name="Pink100">#f8bbd0</color>
    <color name="Pink200">#f48fb1</color>
    <color name="Pink300">#f06292</color>
    <color name="Pink400">#ec407a</color>
    <color name="Pink500">#e91e63</color>
    <color name="Pink600">#d81b60</color>
    <color name="Pink700">#c2185b</color>
    <color name="Pink800">#ad1457</color>
    <color name="Pink900">#880e4f</color>
    <color name="PinkA100">#ff80ab</color>
    <color name="PinkA200">#ff4081</color>
    <color name="PinkA400">#f50057</color>
    <color name="PinkA700">#c51162</color>
    <color name="Purple50">#f3e5f5</color>
    <color name="Purple100">#e1bee7</color>
    <color name="Purple200">#ce93d8</color>
    <color name="Purple300">#ba68c8</color>
    <color name="Purple400">#ab47bc</color>
    <color name="Purple500">#9c27b0</color>
    <color name="Purple600">#8e24aa</color>
    <color name="Purple700">#7b1fa2</color>
    <color name="Purple800">#6a1b9a</color>
    <color name="Purple900">#4a148c</color>
    <color name="PurpleA100">#ea80fc</color>
    <color name="PurpleA200">#e040fb</color>
    <color name="PurpleA400">#d500f9</color>
    <color name="PurpleA700">#aa00ff</color>
    <color name="Deep_Purple50">#ede7f6</color>
    <color name="Deep_Purple100">#d1c4e9</color>
    <color name="Deep_Purple200">#b39ddb</color>
    <color name="Deep_Purple300">#9575cd</color>
    <color name="Deep_Purple400">#7e57c2</color>
    <color name="Deep_Purple500">#673ab7</color>
    <color name="Deep_Purple600">#5e35b1</color>
    <color name="Deep_Purple700">#512da8</color>
    <color name="Deep_Purple800">#4527a0</color>
    <color name="Deep_Purple900">#311b92</color>
    <color name="Deep_PurpleA100">#b388ff</color>
    <color name="Deep_PurpleA200">#7c4dff</color>
    <color name="Deep_PurpleA400">#651fff</color>
    <color name="Deep_PurpleA700">#6200ea</color>
    <color name="Indigo50">#e8eaf6</color>
    <color name="Indigo100">#c5cae9</color>
    <color name="Indigo200">#9fa8da</color>
    <color name="Indigo300">#7986cb</color>
    <color name="Indigo400">#5c6bc0</color>
    <color name="Indigo500">#3f51b5</color>
    <color name="Indigo600">#3949ab</color>
    <color name="Indigo700">#303f9f</color>
    <color name="Indigo800">#283593</color>
    <color name="Indigo900">#1a237e</color>
    <color name="IndigoA100">#8c9eff</color>
    <color name="IndigoA200">#536dfe</color>
    <color name="IndigoA400">#3d5afe</color>
    <color name="IndigoA700">#304ffe</color>
    <color name="Blue50">#e7e9fd</color>
    <color name="Blue100">#d0d9ff</color>
    <color name="Blue200">#afbfff</color>
    <color name="Blue300">#91a7ff</color>
    <color name="Blue400">#738ffe</color>
    <color name="Blue500">#5677fc</color>
    <color name="Blue600">#4e6cef</color>
    <color name="Blue700">#455ede</color>
    <color name="Blue800">#3b50ce</color>
    <color name="Blue900">#2a36b1</color>
    <color name="BlueA100">#a6baff</color>
    <color name="BlueA200">#6889ff</color>
    <color name="BlueA400">#4d73ff</color>
    <color name="BlueA700">#4d69ff</color>
    <color name="Light_Blue50">#e1f5fe</color>
    <color name="Light_Blue100">#b3e5fc</color>
    <color name="Light_Blue200">#81d4fa</color>
    <color name="Light_Blue300">#4fc3f7</color>
    <color name="Light_Blue400">#29b6f6</color>
    <color name="Light_Blue500">#03a9f4</color>
    <color name="Light_Blue600">#039be5</color>
    <color name="Light_Blue700">#0288d1</color>
    <color name="Light_Blue800">#0277bd</color>
    <color name="Light_Blue900">#01579b</color>
    <color name="Light_BlueA100">#80d8ff</color>
    <color name="Light_BlueA200">#40c4ff</color>
    <color name="Light_BlueA400">#00b0ff</color>
    <color name="Light_BlueA700">#0091ea</color>
    <color name="Cyan50">#e0f7fa</color>
    <color name="Cyan100">#b2ebf2</color>
    <color name="Cyan200">#80deea</color>
    <color name="Cyan300">#4dd0e1</color>
    <color name="Cyan400">#26c6da</color>
    <color name="Cyan500">#00bcd4</color>
    <color name="Cyan600">#00acc1</color>
    <color name="Cyan700">#0097a7</color>
    <color name="Cyan800">#00838f</color>
    <color name="Cyan900">#006064</color>
    <color name="CyanA100">#84ffff</color>
    <color name="CyanA200">#18ffff</color>
    <color name="CyanA400">#00e5ff</color>
    <color name="CyanA700">#00b8d4</color>
    <color name="Teal50">#e0f2f1</color>
    <color name="Teal100">#b2dfdb</color>
    <color name="Teal200">#80cbc4</color>
    <color name="Teal300">#4db6ac</color>
    <color name="Teal400">#26a69a</color>
    <color name="Teal500">#009688</color>
    <color name="Teal600">#00897b</color>
    <color name="Teal700">#00796b</color>
    <color name="Teal800">#00695c</color>
    <color name="Teal900">#004d40</color>
    <color name="TealA100">#a7ffeb</color>
    <color name="TealA200">#64ffda</color>
    <color name="TealA400">#1de9b6</color>
    <color name="TealA700">#00bfa5</color>
    <color name="Green50">#d0f8ce</color>
    <color name="Green100">#a3e9a4</color>
    <color name="Green200">#72d572</color>
    <color name="Green300">#42bd41</color>
    <color name="Green400">#2baf2b</color>
    <color name="Green500">#259b24</color>
    <color name="Green600">#0a8f08</color>
    <color name="Green700">#0a7e07</color>
    <color name="Green800">#056f00</color>
    <color name="Green900">#0d5302</color>
    <color name="GreenA100">#a2f78d</color>
    <color name="GreenA200">#5af158</color>
    <color name="GreenA400">#14e715</color>
    <color name="GreenA700">#12c700</color>
    <color name="Light_Green50">#f1f8e9</color>
    <color name="Light_Green100">#dcedc8</color>
    <color name="Light_Green200">#c5e1a5</color>
    <color name="Light_Green300">#aed581</color>
    <color name="Light_Green400">#9ccc65</color>
    <color name="Light_Green500">#8bc34a</color>
    <color name="Light_Green600">#7cb342</color>
    <color name="Light_Green700">#689f38</color>
    <color name="Light_Green800">#558b2f</color>
    <color name="Light_Green900">#33691e</color>
    <color name="Light_GreenA100">#ccff90</color>
    <color name="Light_GreenA200">#b2ff59</color>
    <color name="Light_GreenA400">#76ff03</color>
    <color name="Light_GreenA700">#64dd17</color>
    <color name="Lime50">#f9fbe7</color>
    <color name="Lime100">#f0f4c3</color>
    <color name="Lime200">#e6ee9c</color>
    <color name="Lime300">#dce775</color>
    <color name="Lime400">#d4e157</color>
    <color name="Lime500">#cddc39</color>
    <color name="Lime600">#c0ca33</color>
    <color name="Lime700">#afb42b</color>
    <color name="Lime800">#9e9d24</color>
    <color name="Lime900">#827717</color>
    <color name="LimeA100">#f4ff81</color>
    <color name="LimeA200">#eeff41</color>
    <color name="LimeA400">#c6ff00</color>
    <color name="LimeA700">#aeea00</color>
    <color name="Yellow50">#fffde7</color>
    <color name="Yellow100">#fff9c4</color>
    <color name="Yellow200">#fff59d</color>
    <color name="Yellow300">#fff176</color>
    <color name="Yellow400">#ffee58</color>
    <color name="Yellow500">#ffeb3b</color>
    <color name="Yellow600">#fdd835</color>
    <color name="Yellow700">#fbc02d</color>
    <color name="Yellow800">#f9a825</color>
    <color name="Yellow900">#f57f17</color>
    <color name="YellowA100">#ffff8d</color>
    <color name="YellowA200">#ffff00</color>
    <color name="YellowA400">#ffea00</color>
    <color name="YellowA700">#ffd600</color>
    <color name="Amber50">#fff8e1</color>
    <color name="Amber100">#ffecb3</color>
    <color name="Amber200">#ffe082</color>
    <color name="Amber300">#ffd54f</color>
    <color name="Amber400">#ffca28</color>
    <color name="Amber500">#ffc107</color>
    <color name="Amber600">#ffb300</color>
    <color name="Amber700">#ffa000</color>
    <color name="Amber800">#ff8f00</color>
    <color name="Amber900">#ff6f00</color>
    <color name="AmberA100">#ffe57f</color>
    <color name="AmberA200">#ffd740</color>
    <color name="AmberA400">#ffc400</color>
    <color name="AmberA700">#ffab00</color>
    <color name="Orange50">#fff3e0</color>
    <color name="Orange100">#ffe0b2</color>
    <color name="Orange200">#ffcc80</color>
    <color name="Orange300">#ffb74d</color>
    <color name="Orange400">#ffa726</color>
    <color name="Orange500">#ff9800</color>
    <color name="Orange600">#fb8c00</color>
    <color name="Orange700">#f57c00</color>
    <color name="Orange800">#ef6c00</color>
    <color name="Orange900">#e65100</color>
    <color name="OrangeA100">#ffd180</color>
    <color name="OrangeA200">#ffab40</color>
    <color name="OrangeA400">#ff9100</color>
    <color name="OrangeA700">#ff6d00</color>
    <color name="Deep_Orange50">#fbe9e7</color>
    <color name="Deep_Orange100">#ffccbc</color>
    <color name="Deep_Orange200">#ffab91</color>
    <color name="Deep_Orange300">#ff8a65</color>
    <color name="Deep_Orange400">#ff7043</color>
    <color name="Deep_Orange500">#ff5722</color>
    <color name="Deep_Orange600">#f4511e</color>
    <color name="Deep_Orange700">#e64a19</color>
    <color name="Deep_Orange800">#d84315</color>
    <color name="Deep_Orange900">#bf360c</color>
    <color name="Deep_OrangeA100">#ff9e80</color>
    <color name="Deep_OrangeA200">#ff6e40</color>
    <color name="Deep_OrangeA400">#ff3d00</color>
    <color name="Deep_OrangeA700">#dd2c00</color>
    <color name="Brown50">#efebe9</color>
    <color name="Brown100">#d7ccc8</color>
    <color name="Brown200">#bcaaa4</color>
    <color name="Brown300">#a1887f</color>
    <color name="Brown400">#8d6e63</color>
    <color name="Brown500">#795548</color>
    <color name="Brown600">#6d4c41</color>
    <color name="Brown700">#5d4037</color>
    <color name="Brown800">#4e342e</color>
    <color name="Brown900">#3e2723</color>
    <color name="Grey50">#fafafa</color>
    <color name="Grey100">#f5f5f5</color>
    <color name="Grey200">#eeeeee</color>
    <color name="Grey300">#e0e0e0</color>
    <color name="Grey400">#bdbdbd</color>
    <color name="Grey500">#9e9e9e</color>
    <color name="Grey600">#757575</color>
    <color name="Grey700">#616161</color>
    <color name="Grey800">#424242</color>
    <color name="Grey900">#212121</color>
    <color name="Grey1000">#000000</color>
    <color name="Grey1000">#ffffff</color>
    <color name="Blue_Grey50">#eceff1</color>
    <color name="Blue_Grey100">#cfd8dc</color>
    <color name="Blue_Grey200">#b0bec5</color>
    <color name="Blue_Grey300">#90a4ae</color>
    <color name="Blue_Grey400">#78909c</color>
    <color name="Blue_Grey500">#607d8b</color>
    <color name="Blue_Grey600">#546e7a</color>
    <color name="Blue_Grey700">#455a64</color>
    <color name="Blue_Grey800">#37474f</color>
    <color name="Blue_Grey900">#263238</color>
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