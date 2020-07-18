<template>
  <div class="dashboard-container">
    <div class="dashboard-text">name: {{ name }}</div>
    <h1>Please select device</h1>
    <el-divider />
    <el-row>
      <el-col :span="3">
        <el-card :body-style="{ padding: '0px' }">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <span>Device1</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button" @click="to_device(1)">click</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="3" :offset="2">
        <el-card :body-style="{ padding: '0px' }">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <span>Device2</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">click</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      <el-col :span="3" :offset="2">
        <el-card :body-style="{ padding: '0px' }">
          <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
          <div style="padding: 14px;">
            <span>Device3</span>
            <div class="bottom clearfix">
              <el-button type="text" class="button">click</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>

</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {
    to_device(id) {
      this.$router.push('/device/' + id)
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
  .button {
    padding: 0;
    float: right;
  }
  .image {
    width: 100% !important;
    display: block;
  }
  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  .clearfix:after {
      clear: both
  }
</style>
