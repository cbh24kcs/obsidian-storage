## 快速总结

## 声明数组
- ### 空数组
     - `let arr = new Array ( );`
     - `let arr = [ ];` 字面量创建
- ### 指定length
     - `let arr = Array (3);` 数组的length属性非只读，可以通过修改length从末尾增加/删除元素
- ### 指定数组元素
     - `let arr = [1, 2, 3, 4];` 如为单个数字参数则可能同指定length的创建方式
- ### ES6新增创建数组的静态方法
     - `Array.from (类数组对象, 映射函数参数【可选】, 指定映射函数中this的值【可选】);`
          - 将类数组结构转换为数组实例，*==重写的this值在箭头函数中不适用==*
     -  `Array.of ( );`  
          - 将一组参数转换为数组实例。可用于替代`Array.prototype.slice.call(arguments)`

 ## 检测数组
- `Array.isArray ( );`

## 迭代器
- ### Array原型检索数组内容方法  #原型 
    - `keys ( );` 返回数组 *==索引==* 的迭代器
    - `values ( );` 返回数组 *==元素==* 的迭代器
    - `entries ( );` 返回 *==索引/元素==* 的迭代器

## 方法整理
- ### 复制及填充
    - `fill (需填充元素, 开始填充索引位置 [可选], 结束填充索引位置 [可选]);`  
    - `copyWithin (插入位置, 开始复制索引位置 [可选], 结束复制索引位置 [可选]);`  批量进行 *==浅复制==*，并将结果填充至指定位置。

- ### 转换
     - `value of ( );`
     - `toString ( );`
     - `alert ( );` 期待字符串，结果同`toString ( )`
     - `toLocaleString ( )`
     - `join ( )` 修改数组分隔符

- ### 栈/队列
     - `push ( );` 数组末尾添加元素
     - `pop ( );` 数组末尾删除元素
     - `shift ( );` 数组开头删除元素
     - `unshift ( );` 数组开头添加元素
       *==【TIPS 1】==* 以上方法删除元素返回被删除项，添加元素返回数组长度
       *==【TIPS 2】==* 性能比较：`push/pop` 方法运行的比较快，而 `shift/unshift` 比较慢

- ### 排序
     - `reverse ( );` 反向排序
     - `soft ( );` 
          - 按照升序排列
          - 会在每一项上调用`string ( )`转型函数。转换为字符串比较。*==（数值可能不按数值升序排列）==*
          - 可以接收一个比较函数，判断哪个值应该放在前面```
          - *==数组原地排序，不进行复制
    ```jsx
    function compare (value1, value2) {
       if (value1 < value2) {
         return 1;
       } else if {value1 > value2) {
         return -1
       } else {
        return 0;
    }
    }
    
    let values = [0,1,5,10,15]
    values.sort (compare);
    alert (values); // 结果为0,1,5,10,15 调整compare函数也可做降序排列
    ```
- ### 子数组
    -  `concat (arg1, arg2...)` 创建副本数组，并将参数插入 *==副本末尾==

- ###