# 模块简介 #

“base\_report\_cn”模块是基于 [Gábor Dukai](http://exploringopenerp.blogspot.com/2009/04/new-module-basereportunicode.html) 编写的 base\_report\_unicode 模块修改而来，自带了开源的文泉驿正黑体和 AR PL SungtiL GB 宋体。该模块的使用非常简单，直接导入这个模块，不需要任何的 hack，OpenERP 现存的报表即可直接支持中文。当然了，内置报表的现存的文字仍然是英文的，本模块只是提供中文支持，让中文别显示成方框。

# 安装 #

  1. 请[单击此处](http://openerp-community-addons.googlecode.com/files/base_report_cn.zip)下载 base\_report\_cn.zip 压缩包。
  1. 将其解压到 `openerp-server/bin/addons/` 下
  1. 在 OpenERP 中更新模块列表并安装 base\_report\_cn 模块。
  1. Enjoy it!

# 提示 #

如果您是 Windows 用户的话可以把 Windows 系统自带的 SimSun.ttc 和 SimHei.ttf 分别改名为 SimSun.ttf 和 SimHei.ttf 复制到 base\_report\_cn/fonts 目录中即可替换本模块自带的开源字体。