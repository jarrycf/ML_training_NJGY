import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5001,
    open: false, //自动打开
    base: "./ ", //生产环境路径
    host:'0.0.0.0',
    proxy: {
      '/api': 'http://hjh.nat300.top',
    }
    }


})
