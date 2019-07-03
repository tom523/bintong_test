<template>
  <div class="app-container">
    <el-col>
      <div id="saved" style="width: 80%; margin-left: auto; margin-right: 0px; margin-top: 60px">
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
import { getSavedNum } from '@/api/table'

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
      listLoading: true
    }
  },
  created() {
    // this.fetchData()
  },
  mounted() {
    this.initData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getSavedNum().then(response => {
        this.list = response.results
        this.listLoading = false
      })
    },
    initData() {
      this.listLoading = true
      getSavedNum().then(response => {
        this.list = response.results
        d3.select('#saved')
          .selectAll("div")
          .data(response.results.map(item => { return item.val}))
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
#saved div {
  display: inline-block;
  background: #4285F4;
  width: 20px;
  margin-right: 3px;
}
</style>
