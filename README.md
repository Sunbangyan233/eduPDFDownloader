# eduPDFDownloader
一个用来下载某个网站上的教材PDF的工具

## 如何使用？
1. 右键PDF页面，打开“查看框架源代码”
   ![image](https://github.com/user-attachments/assets/128b0319-8a1e-4f8b-8726-4187f60f01e6)
2. 复制最上面的一串链接（带不带view:source 都可以）
   ![image](https://github.com/user-attachments/assets/05a933ca-ca4e-4eed-aadf-7c8d0b257d60)
3. 打开项目网页，粘贴并解析
   ![image](https://github.com/user-attachments/assets/65aeefcb-5dd6-47b2-a025-c87a1232057d)
4. 复制好文件名（在原来的网页），在新打开的页面点击右上角，粘贴文件名保存
   ![image](https://github.com/user-attachments/assets/74a65eb8-ee9d-4dba-b0b3-b9cb158ba6d7)
完成~

## QA

- 下载速度太慢？
- 建议[下载exe](https://app.sunimg.top/PDF.js/app.exe)，运行后将解析跳转到的 ` https://pdf.sunimg.top/ ` 替换为 `http://127.0.0.1:5000/`
- 下载报401/403？
- 下载器报错401的话，建议用网页版浏览器保存。浏览器报错403的话，请检查链接有无缺失。其他可能暂时没遇到
