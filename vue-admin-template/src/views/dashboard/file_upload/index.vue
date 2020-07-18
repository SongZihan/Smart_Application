<template>
  <div>
    <p>this is file upload page</p>
    <p>device id is {{ this.$route.params.id }}</p>
    <el-upload
      ref="upload"
      class="upload-demo"
      drag
      action=""
      :http-request="uploadFile"
      multiple
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      :auto-upload="false"
    >
      <i class="el-icon-upload" />
      <div class="el-upload__text">Drag file there or <em>click to select file</em></div>
      <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
      <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">Upload</el-button>
    </el-upload>
  </div>

</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
      fileList: []
    }
  },
  methods: {
    uploadFile(item) {
      const file = item.file
      if (file.name) {
        // 文件处理代码
        // 用正则匹配文件类型进行自动归档，对文件名进行处理后发送到服务器
      }
      console.log(item)
      console.log('ready to upload ')
      console.log(this.fileList)
      // https://blog.csdn.net/fcku_88/article/details/103852857
    },
    submitUpload() {
      this.$refs.upload.submit()
    },
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    }
  }
}
</script>

<style scoped>

</style>
