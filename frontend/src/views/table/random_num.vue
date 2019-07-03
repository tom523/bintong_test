<template>
  <div class="app-container">
    <el-button style="margin-left: 80%; width: 10%" type="primary" @click="doSave">保存</el-button>
    <el-col>
      <div id="mydiv" style="width: 80%; margin-left: auto; margin-right: 0px; margin-top: 60px">
      </div>
<!--     <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      style="width: 80%; margin-left: auto; margin-right: auto; margin-top: 20px"
    >
      <el-table-column align="center" label="ID" width="95">
        <template slot-scope="scope">
          {{ scope.$index }}
        </template>
      </el-table-column>
      <el-table-column label="value">
        <template slot-scope="scope">
          {{ scope.row.val }}
        </template>
      </el-table-column>
    </el-table> -->
    </el-col>
  </div>
</template>

<script>
import { getRandomNum, saveRandomNum } from '@/api/table'
import { Message } from 'element-ui'

export default {
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      listLoading: false
    }
  },
  // created() {
  //   this.fetchData()
  // },
  mounted() {
    this.fetchData()
  },
  methods: {
    doSave(row) {
      saveRandomNum(this.list).then(response => {
        Message({
          type: 'success',
          message: '保存成功'
        })
      })
    },
    fetchData() {
      this.initData()
      const that = this
      setInterval(function () {
        that.refreshData()
      }, 10000)
    },
    refreshData() {
      this.listLoading = true
      getRandomNum().then(response => {
        this.list = response
        d3.select('#mydiv')
          .selectAll("div")
          .data(response.map(item => { return item.val}))
          .style("height", (d)=> d*500 + "px")
        // this.listLoading = false
      })
    },
    initData() {
      this.listLoading = true
      getRandomNum().then(response => {
        this.list = response
        d3.select('#mydiv')
          .selectAll("div")
          .data(response.map(item => { return item.val}))
          .enter()
          .append("div")
          .style("height", (d)=> d*500 + "px")
        // this.listLoading = false
      })
    }
  }
}
</script>

<style>
#mydiv div {
  display: inline-block;
  background: #4285F4;
  width: 60px;
  margin-right: 3px;
}
</style>
