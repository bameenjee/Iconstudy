<template>
  <App>
    <div class="contents">
      <div v-if="resultNumber">주사위를 굴려 {{Number(resultNumber)+1}} 나왔습니다.</div>
      <button @click="rollDice">주사위 굴리기</button>
    </div>
  </App>
</template>

<script>
import App from "../layouts/App";
import IconService from "icon-sdk-js";

const httpProvider = new IconService.HttpProvider(
  "https://bicon.net.solidwallet.io/api/v3"
);
const iconService = new IconService(httpProvider);
export default {
  name: "home",
  data() {
    return {
      resultNumber: 0
    };
  },
  components: {
    App
  },
  methods: {
    rollDice() {
      const call = new IconService.IconBuilder.CallBuilder()
        .to("cxf196bc1c4b8df9649408aa0f0b516520561ae00c")
        .method("diceRoll")
        .params({ data: Math.random().toString() })
        .build();
      iconService.call(call).execute().then(resultNumber => this.resultNumber = resultNumber );
    }
  }
};
</script>

<style lang="scss" scoped>
.contents {
  margin: 0 auto;
  width: 300px;
  button {
    width: 100px;
    height: 50px;
  }
}
</style>