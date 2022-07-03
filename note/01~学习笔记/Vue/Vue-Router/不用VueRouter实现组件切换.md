# 方式1：使用v-show或v-if

```vue
<template>
  <div id="app">
    <button @click="x = 1">页面1</button>
    <button @click="x = 2">页面2</button>
    <button @click="x = 3">页面3</button>
    <button @click="x = 4">页面4</button>
    <button @click="x = 5">页面5</button>
    <hr />

    <!-- 展示 PageX 组件 -->
    <Page1 v-show="x == 1" />
    <Page2 v-show="x == 2" />
    <Page3 v-show="x == 3" />
    <Page4 v-show="x == 4" />
    <Page5 v-show="x == 5" />
  </div>
</template>

<script>
import Page1 from "@/views/Page1.vue";
import Page2 from "@/views/Page2.vue";
import Page3 from "@/views/Page3.vue";
import Page4 from "@/views/Page4.vue";
import Page5 from "@/views/Page5.vue";
  
export default {
  components: { Page1, Page2, Page3, Page4, Page5 },
  data() {
    return {
      x: "",
    };
  },
};
</script>
```

# 方式2：使用动态组件 component

```vue
<template>
  <div id="app">
    <button @click="showPage = 'Page1'">页面1</button>
    <button @click="showPage = 'Page2'">页面2</button>
    <button @click="showPage = 'Page3'">页面3</button>
    <button @click="showPage = 'Page4'">页面4</button>
    <button @click="showPage = 'Page5'">页面5</button>
    <hr />
    <component :is="showPage" />
  </div>
</template>

<script>
import Page1 from "@/views/Page1.vue";
import Page2 from "@/views/Page2.vue";
import Page3 from "@/views/Page3.vue";
import Page4 from "@/views/Page4.vue";
import Page5 from "@/views/Page5.vue";

export default {
  components: { Page1, Page2, Page3, Page4, Page5 },
  data() {
    return {
      showPage: "",
    };
  },
};
</script>
```

