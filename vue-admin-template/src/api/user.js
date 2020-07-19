import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/auth/login',
    method: 'post',
    data
  })
}
export function registered(data) {
  return request({
    url: '/auth/registered',
    method: 'post',
    data
  })
}

export function getInfo() {
  return request({
    url: '/api/user_info',
    method: 'get'
    // params: { token }
  })
}

export function getIdentifyCode() {
  return request({
    url: '/auth/identify_code',
    method: 'get',
    responseType: 'arraybuffer'
  })
}

// export function logout() {
//   return request({
//     url: '/vue-admin-template/user/logout',
//     method: 'post'
//   })
// }
