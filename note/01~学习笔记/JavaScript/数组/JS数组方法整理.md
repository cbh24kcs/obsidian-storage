#数组
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
	* `Array.of ( );` 
		* 将一组参数转换为数组实例。可用于替代 `Array.prototype.slice.call(arguments)`

 ## 检测数组
- `Array.isArray ( );`

## 迭代器
- ### Array原型检索数组内容方法  #原型 
    - `keys ( );` 返回数组 *==索引==* 的迭代器
        - `values ( );` 返回数组 *==元素==* 的迭代器
        - `entries ( );` 返回 *==索引/元素==* 的迭代器

## 方法整理
- ### 复制及填充
	- `fill ([element], [start_选填], [end_选填]);`  从索引`start`至`end`批量填充/覆盖元素`element`
	- `copyWithin ([index], [start_选填], [end_选填]);`  从索引`start`至`end`进行 *==浅复制==*，并将结果填充至指定索引位置`index`
- ### 转换
	- `value of ( );`
	- `toString ( );`
	-  `alert ( );` 期待字符串，结果同 `toString ( )`
	- `toLocaleString ( )`
	- `join ( )` 修改数组分隔符
- ### 栈/队列
	- `push ( );` 数组末尾添加元素
	- `pop ( );` 数组末尾删除元素
	- `shift ( );` 数组开头删除元素
	- `unshift ( );` 数组开头添加元素
     *==【TIPS 1】==* 以上方法删除元素返回被删除项，添加元素返回数组长度
     *==【TIPS 2】==* 性能比较： `push/pop` 方法运行的比较快，而 `shift/unshift` 比较慢
- ### 排序
	- `reverse ( );` 反向排序
	- `soft ( );` 
		- 按照升序排列
		- 会在每一项上调用 `string ( )` 转型函数，转换为字符串比较。 *==（数值可能不按数值升序排列）==*
		- 可以接收一个比较函数，判断哪个值应该放在前面
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
- ### 副本操作
	- `concat ([parameter1], [parameter2]...)` 创建新数组，并将参数 `parameter` 插入新数组末尾
	- `slice ([start], [end_选填])` 
		- 将所有从索引 `start` 到 `end(不含)` 位置的数组项复制到新的数组副本中
	- `splice ([start], [deleteNumber], [element]);`
		- 从指定索引 `start` 处开始，删除指定个数 `deleteNumber` 元素,插入若干元素 `element`
		- 返回 *==被删除元素组成的数组==*
		- 支持负值索引，从末尾计算
- ### 搜索
	- `indexof ([element], [start]);` 从数组开头开始，找到则返回元素位置，没找到返回-1
	- `lastindexof ([element], [start];` 从数组末尾开始，找到则返回元素位置，没找到返回-1
	- `includes ([element], [start]);`  返回布尔值 *==ES7新增==*
		- `includes` 能找到NaN，但是 `indexOf` 找不到NaN
		- `includes` 内部使用了 `Number.isNaN` 对 `NaN` 进行了匹配
	- `find ([回调], [回调的this]);` 返回第一个匹配的元素 #回调 
	- `findindex ([回调], [回调的this]);` 返回找第一个匹配元素的索引 #回调
- ### 迭代 #回调 
	- `every ( );` 对每一项运行函数，如果每一项都返回 `true`，则该方法返回 `true`
	- `filter ( );` 对每一项运行函数，将结果为 `true` 的项组成数组后返回
	- `foreach ( );` 对每一项运行函数，没有返回值
	- `map ( );` 对每一项运行函数，返回由每次函数调用结果构成的数组
	- `some ( );` 对每一项运行函数，如果有一项返回 `true` ,则返回 `true`
- ### 归约 #回调 
	- `reduce ([prev], [cur], [index], [array])；` 
		- `prev` :上一个归并值;  `cur`:当前项; `index` :当前项索引; `array` :数组本身;
		- 每调用一次函数，结果返回给上一个归并值用以下次调用，最后一个归并值即为最终结果；
	- `reduceRight ([prev], [cur], [index], [array])；`
		- 同 `reduce ( )` ,但方向相反，`reduceRight ( )`从数组末尾开始遍历。