package com.funny.cmaterialcolors.test

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.Card
import androidx.compose.material.MaterialTheme
import androidx.compose.material.Surface
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import com.funny.cmaterialcolors.MaterialColors
import com.funny.cmaterialcolors.test.ui.theme.CMaterialColorsTheme
import com.funny.cmaterialcolors.test.utils.ColorBean
import com.funny.cmaterialcolors.test.utils.ColorUtils
import com.funny.cmaterialcolors.test.utils.inverse

class MainActivity : ComponentActivity() {
    val TAG = "MainActivity"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val colorList = ColorUtils.getAllColors()
        setContent {
            CMaterialColorsTheme {
                // A surface container using the 'background' color from the theme
                Surface(color = MaterialTheme.colors.background) {
                    ColorList(colorBeanList = colorList)
                }
            }
        }
    }
}


@Composable
fun ColorItem(
    colorBean : ColorBean
){
    Card(
        elevation = 4.dp,
        shape = RoundedCornerShape(2.dp),
    ) {
        Box(modifier = Modifier
            .height(48.dp)
            .fillMaxWidth()
            .background(colorBean.color),contentAlignment = Alignment.CenterStart){
            Text(text = colorBean.name, modifier = Modifier.padding(4.dp),color = colorBean.color.inverse())
        }
    }

}

@Composable
fun ColorList(colorBeanList : List<ColorBean>){
    LazyColumn(
        modifier = Modifier.fillMaxWidth(),
        contentPadding = PaddingValues(horizontal = 4.dp,vertical = 8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        itemsIndexed(colorBeanList){ _,bean ->
            ColorItem(colorBean = bean)
        }
    }
}

@Preview(showBackground = true)
@Composable
fun DefaultPreview() {
    CMaterialColorsTheme {
        //ColorItem(color = MaterialColors.BlueA200)
        val allColors = arrayListOf<ColorBean>()
        allColors.add(ColorBean("Red400",MaterialColors.Red400))
        allColors.add(ColorBean("Red600",MaterialColors.Red600))
        //print(allColors)
        ColorList(colorBeanList = allColors)
    }
}