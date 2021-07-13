package com.funny.cmaterialcolors.test.utils

import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import com.funny.cmaterialcolors.MaterialColors
import kotlin.reflect.KProperty

fun Color.inverse() = ColorUtils.inverseColor(this)

data class ColorBean(val name:String, val color: Color)

object ColorUtils {
    fun getAllColors(): List<ColorBean> {
        val colorClass = MaterialColors.Companion::class
        val colorList = colorClass.members
        return colorList.filter { it is KProperty }
            .map { ColorBean(it.name, it.call(MaterialColors) as Color) }
    }

    fun inverseColor(color:Color) = Color((0xFFFFFFFF-color.toArgb()) or 0xFF000000)
}

fun main() {
    val color = Color(0xFFFF0000)
    print(ColorUtils.inverseColor(color))
}