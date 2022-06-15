# 快速总结

# 声明数组
- <b><font color = orange>空数组</font></b>
    - *let arr = new Array ( );
    - *let arr = [ ];    <font color = grey>字面量创建</font>
- <b><font color = orange>指定length</font></b>
    - *let arr = Array (3);*   <font color = yellow>数组的length属性非只读，可以通过修改length从末尾增加/删除元素</font>
- <b><font color = orange>指定数组元素</font></b>
     - *let arr = [1, 2, 3, 4];*    <font color = grey>如为单个数字参数则可能同指定length的创建方式</font>
- <b><font color = orange>ES6新增创建数组的静态方法</font></b>
    - *Array.from ( <font color = grey size = 2>类数组对象</font>, <font color =grey size = 2>映射函数参数 [可选]</font>, <font color = grey size =2>指定映射函数中this的值 [可选]</font>);  
         - 将类数组结构转换为数组实例，<font color = yellow>重写的this值在箭头函数中不适用</font>
    - *Array.of ( );  
         - 将一组参数转换为数组实例。可用于替代*Array.prototype.slice.call(arguments)

# 检测数组
- *Array.isArray ( )

# 迭代器
- <b><font color = orange>Array原型检索数组内容方法</font></b> #原型 
     - *keys ( );*       <font color = grey>返回数组索引的迭代器</font>
     - *values ( );*    <font color = grey>返回数组元素的迭代器</font>
     - *entries ( );*   <font color = grey>返回索引/值对应的迭代器 </font>

# 方法整理
- <b><font color = orange>复制及填充</font></b>
    - *fill  ( <font color = grey size = 2>需填充元素</font>, <font color =grey size = 2>开始填充索引位置 [可选]</font>, <font color = grey size =2>结束填充索引位置 [可选]</font>);*   指定元素填充
    - *copyWithin ( <font color = grey size = 2>插入位置</font>, <font color =grey size = 2>开始复制索引位置 [可选]</font>, <font color = grey size =2>结束复制索引位置 [可选]</font>);*  批量进行浅复制，并将结果填充至指定位置。
- <b><font color = orange>转换</font></b>












## 转换方法

-   valueOf ( ）返回**数组本身**。
-   toString ( ) 返回由数组中**每个数值的等效字符串拼接而成的一个逗号分隔的字符串**。
-   alert ( ) 期待字符串，结果等同toString ( )。
-   toLocaleString ( ) 为了得到最终的字符串，会调用数组每个值的 toLocaleString ( ) 方法。
-   如需**改变分隔符**，需要使用 join ( ) 的方法。**如果不给join ( ) 传入任何参数，或者传入undefined，则仍然使用逗号作为分隔符。**

## 栈方法

栈是一种**后进先出**（LIFO, Last-In-First-Out）的**数据结构**，也就是一种限制插入和删除项的结构。也就是最近添加的项先被删除。数据项的插入（称为推入，push）和删除（称为弹出，pop）旨在栈的一个地方发生，即栈顶。**ECMAScript数组提供了push ( ) 和 pop ( ) 方法，以实现类似栈的行为。**

-   push ( )
    
    -   接收任意变量的参数，**并将它们添加到数组末尾，返回数组的最新长度。**
-   pop ( )
    
    -   用于删除数组的最后一项，同时减少数组的length值，**返回被删除项。**
    
    ```jsx
    let a = ["1", "2"]
    let item = colors.pop (); // 取得最后一项
    alert (item); // 2
    ```
    

## 队列方法

队列在列表末尾添加数据，但从列表开头添加数据。

模拟队列，从数组开头处理数据，采用shift ( ) 以及unshift ( )方法

-   shift ( )
    -   **删除数组第一项并返回删除项，数组长度减1**
-   unshift ( )
    -   与shift相反，**在数组开头添加任意多个值，然后返回新的数组长度。用法等同push。**

## 排序方法

-   reverse ( )
    
    -   将数组元素反向排列
-   soft ( )
    
    -   按照升序重新排列，最小值在前面，最大值在后面。
    -   **会在每一项上调用string ( ) 转型函数。转换为字符串比较。（数值排序可能出现问题）**
    -   sort ( ) 方法可以接收一个比较函数。用于判断哪个值应该排在前面。
    
    ```jsx
    let values = [0, 1, 5, 10, 15]
    values.sort ();
    alert (values); // 结果为0,1,10,15,5 因为转换为字符串比较，所以不符合数值升序排列规则
    ```
    
    ```jsx
    function compare (value1, value2) {
       if (value1 < value2) {
         return -1;
      } else if {value1 > value2) {
      } else {
        return 0;
      }
    }
    
    let values = [0,1,5,10,15]
    values.sort (compare);
    alert (values); // 结果为0,1,5,10,15 调整compare函数也可做降序排列
    ```
    
    ```jsx
    let values = [0, 1, 5, 10, 15];
    values.sort ((a, b) => a < b ? 1 : a >b ? -1 : 0);
    alert (values); // 结果为15,10,5,1,0 箭头函数简化写法
    ```
    

**reverse ( ) 和 soft ( ) 都返回调用它们的数组的引用**

## 操作方法

-   concat ( )
    -   创建原有数组副本，将新参数添加到副本末尾
-   slice ( )
    -   用于创建一个包含原有数组中一个或多个元素的新数组。
    -   **slice ( ) 方法不会影响原始数组**
-   **splice ( )**
    -   主要目的是在数组中间插入元素
    -   **删除**：splice (第一个要删除元素的位置，要删除元素的数量)
    -   **插入**：splice (开始位置，要删除的元素数量，插入的元素）
    -   **替换**：同插入
    -   该方法**返回包含从数组中删除的元素的数组**

## 搜索和位置方法

-   **严格相等**搜索办法**（===比较）**
    -   index （ ）
        -   从数组第一项向后查找，返回查找元素位置，如果没找到则返回-1
    -   lastindexof ( )
        -   从数组末尾向前查找，返回查找元素位置，如果没找到则返回-1
    -   includes （ ）**【ECMAScript 7新增】**
        -   从数组第一项向后查找，返回布尔值
-   断言函数（**接收3个参数：元素、索引、数组本身**）
    -   find ( )
        
        从数组最小索引开始，**返回第一个匹配元素，找到匹配后不再继续搜索**
        
    -   findindex ( )
        
        从数组最小索引开始，**返回第一个匹配元素的索引，找到匹配后不在继续搜索**
        

## 迭代方法

以下每个方法接收两个参数，传给每个方法的函数接收3个参数：**数组元素、元素索引、数组本身**。**这些方法不改变调用它们的数组**。

-   every ( )
    
    对每一项都运行传入的函数，**如果每一项都返回true，则该方法返回true。**
    
-   filter ( )
    
    对数组每一项都运行传入的函数，**函数组成true的项会组成数组后返回。**
    
-   forEach ( )
    
    对数组每一项都运行传入的函数，**没有返回值。**
    
-   map ( )
    
    对数组每一项都运行传入的函数，**返回由每次函数调用的结果构成的数组。**
    
-   some ( )
    
    对数组每一项都运行传入的函数，**如果有一项返回true，则这个方法返回true。**
    

## 归并方法

以下两个方法都会迭代函数所有项目，并构建一个最终返回值。

-   reduce ( ) **【从前向后遍历】**
    
    ```jsx
    let values = [1, 2, 3, 4, 5]
    let sum = values.reduce((prev, cur, index, array) => prev +cur);
    alert (sum); // 15
    ```
    
-   reduceright ( ) **【从后向前遍历】**










**数组方法**

-   **遍历**
    
    -   **arr.forEach(回调, 回调的this)**
        -   已删除或者未初始化的项将被跳过（例如在稀疏数组上）
        -   除了抛出异常以外，没有办法中止或跳出 `forEach()` 循环。如果你需要中止或跳出循环，`forEach()` 方法不是应当使用的工具。
-   **队列方法**
    
    -   **push(...items)**：在末端添加一个元素
        
    -   **pop()**：从末端取出一个元素
        
    -   **unshift(...items)**：在数组的首端添加元素
        
    -   **shift()**：取出队列首端的一个元素，整个队列往前移
        
    -   注：添加操作会返回添加的索引，删除操作会返回删除的元素
        
    -   **性能比较：**`push/pop` 方法运行的比较快，而 `shift/unshift` 比较慢
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc23cbed-6dec-4942-8a2e-1ce1772d2834/Untitled.png)
        
-   **子数组**：
    
    -   **arr.slice([start], [end])**
        -   将所有从索引 `start` 到 `end`（不包括 `end`）的数组项复制到一个**新的数组**
        -   `start` 和 `end` 都可以是负数，在这种情况下，从末尾计算索引
-   **拼接**：
    
    -   **arr.concat(arg1, arg2...)**
        -   创建一个新数组，其中包含来自于其他数组和其他项的值
-   **先删除后添加**：
    
    -   **arr.splice(开始操作的位置, 要删除的个数, 后面的都是要插入的元素...)**
        -   从索引 `start` 开始修改 `arr`，删除 `deleteCount` 个元素
        -   并在当前位置插入 `elem1, ..., elemN`
        -   最后返回已**被删除元素的数组**
        -   注：在这里和其他数组方法中，负向索引都是被允许的。它们从数组末尾计算位置
-   **查找**
    
    -   **arr.indexOf(要查找的元素, 开始查找的位置)**
    -   **arr.lastIndexOf(要查找的元素, 开始查找的位置)**
    -   **arr.includes(要查找的元素, 开始查找的位置) 【ES7】**
        -   includes能找到NaN，但是indexOf找不到NaN
        -   includes内部使用了`Number.isNaN`对`NaN`进行了匹配
    -   **arr.find(回调, 回调的this)**
        -   回调函数的参数：**当前元素,当前索引,数组本身**（其他有回调函数的基本也是这个样子）
        -   thisArg：回调内部使用的this（有了箭头函数之后一般也不用了）
    -   **_arr_.findIndex(回调, 回调的this)**
    -   **新的数组 = arr.filter(回调, 回调的this)**
-   **转换**
    
    -   **填充**
        -   **arr.fill(填充值, 起始, 终止)** 填充指定值，返回修改后的数组
    -   **映射**
        -   **新的数组 = arr.map(回调, 回调的this)**
    -   **排序**
        -   **arr.sort(比较函数(第一个元素, 第二个元素))**
            -   比较函数返回值 < 0，则第一个元素在前面，>0则第二个元素在前面
            -   比较函数必须总是对相同的输入返回相同的比较结果，否则排序的结果将是不确定的。
            -   排序后的数组。请注意，数组已原地排序，并且不进行复制！
    -   **翻转**
        -   **arr.reverse()** 颠倒数组中元素的位置，改变了数组，并返回该数组的引用
    -   **合并**
        -   **arr.join(分隔符=',')**
    -   **打平**
        -   **新的数组 = arr.flat(深度) 【ES10】**
            -   可以传参数，参数为降维的次数
            -   如果传的是一个无限大的数字，那么就实现了多维数组(无论几维)降为一维数组
        -   **新的数组 = arr.flatMap(回调, 回调的this) 【ES10】**
            -   相当于 map + flat
            -   一个新的数组，其中每个元素都是回调函数的结果，并且结构深度 `depth` 值为1
    -   **归约**
        -   **reduce(function(累计器, 当前值, 当前索引, 原数组), 初始值)**
            -   回调函数的返回值会被分配给下一次调用回调时候的累计器
            -   结束时，累计器中的值就是结果值
        -   **reduceRight(function(累计器, 当前值, 当前索引, 原数组), 初始值)**
            -   与reduce相同，不过执行的顺序是从右到左
    -   **拷贝**
        -   **arr.copyWithin(target, start, end)**
            -   将从位置 `start` 到 `end` 的所有元素复制到 **自身** 的 `target` 位置（覆盖现有元素）
-   **判断**
    
    -   **arr.some(回调, 回调的this)**
        -   数组中有至少一个元素通过回调函数的测试就会返回**`true`**
        -   所有元素都没有通过回调函数的测试返回值才会为`false`
    -   **arr.every(回调, 回调的this)**
        -   如果回调函数的每一次返回都为true，返回 true ，否则返回 false
    -   **Array.isArray(要判断的东西)**
        -   判断是不是数组
        -   数组是基于对象的，不构成单独的语言类型
        -   所以 `typeof` 不能帮助从数组中区分出普通对象