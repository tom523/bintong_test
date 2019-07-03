import request from '@/utils/request'

export function getRandomNum(params) {
  return request({
    url: '/real-time-num/random_nums/',
    method: 'get',
    params
  })
}

export function saveRandomNum(data) {
  return request({
    url: '/saved-num/batch_saved/',
    method: 'post',
    data
  })
}

export function getSavedNum(params) {
  return request({
    url: '/saved-num/',
    method: 'get',
    params
  })
}
